from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime
from google import genai
import os

load_dotenv()

app = Flask(__name__)

# ---- DATABASE SETUP ----
mongo_uri = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/')
client = MongoClient(mongo_uri)
db = client['study_assistant']

# ---- GEMINI SETUP ----
genai_client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))


# ---- PAGE ROUTES ----
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/summarize')
def summarize_page():
    return render_template('summarize.html')


@app.route('/quiz')
def quiz_page():
    return render_template('quiz.html')


# ---- HEALTH CHECK ----
@app.route('/health')
def health():
    return jsonify({'status': 'ok'})


# ---- DATABASE TEST ----
@app.route('/api/test-db')
def test_db():
    try:
        client.admin.command('ping')
        return jsonify({'status': 'connected', 'db': 'ok'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


# ---- SUMMARIZE ROUTE ----
@app.route('/api/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    notes = data.get('notes', '')
    if not notes:
        return jsonify({'error': 'No notes provided'}), 400
    try:
        prompt = f"""You are a study assistant.
Summarize the following study notes in a clear,
concise and easy to understand way.
Use bullet points where appropriate.

Notes:
{notes}
"""
        response = genai_client.models.generate_content(
            model='gemini-2.0-flash',
            contents=prompt
        )
        return jsonify({'summary': response.text})
    except Exception as e:
        return jsonify({'error': f'AI service error: {str(e)}'}), 500


# ---- QUIZ ROUTE ----
@app.route('/api/quiz', methods=['POST'])
def quiz():
    data = request.get_json()
    notes = data.get('notes', '')
    if not notes:
        return jsonify({'error': 'No notes provided'}), 400
    try:
        prompt = f"""You are a study assistant.
Generate exactly 5 quiz questions based on the following
study notes. For each question provide the answer.

You MUST use exactly this format with no extra text:
Q: question here
A: answer here

Q: question here
A: answer here

Notes:
{notes}
"""
        response = genai_client.models.generate_content(
            model='gemini-2.0-flash',
            contents=prompt
        )
        raw = response.text.strip()
        questions = []
        lines = raw.split('\n')
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if line.startswith('Q:'):
                q = line[2:].strip()
                a = ''
                if i + 1 < len(lines) and lines[i + 1].strip().startswith('A:'):
                    a = lines[i + 1].strip()[2:].strip()
                    i += 1
                if q:
                    questions.append({'question': q, 'answer': a})
            i += 1
        return jsonify({'questions': questions})
    except Exception as e:
        return jsonify({'error': f'AI service error: {str(e)}'}), 500


# ---- SESSIONS ROUTES ----
@app.route('/api/sessions', methods=['GET'])
def get_sessions():
    sessions = list(db.sessions.find({}, {'_id': 0}))
    return jsonify({'sessions': sessions})


@app.route('/api/sessions', methods=['POST'])
def save_session():
    data = request.get_json()
    session = {
        'notes': data.get('notes', ''),
        'type': data.get('type', 'summary'),
        'result': data.get('result', ''),
        'created_at': datetime.utcnow().isoformat()
    }
    db.sessions.insert_one(session)
    return jsonify({'message': 'Session saved successfully'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
