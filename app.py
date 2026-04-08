from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime
import google.generativeai as genai
import os

load_dotenv()

app = Flask(__name__)

# ---- DATABASE SETUP ----
mongo_uri = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/')
client = MongoClient(mongo_uri)
db = client['study_assistant']

# ---- GEMINI SETUP ----
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-2.0-flash')


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
        response = model.generate_content(prompt)
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
        Generate 5 quiz questions based on the following 
        study notes. For each question provide the answer.
        
        Format your response exactly like this for each question:
        Q: [question here]
        A: [answer here]

        Notes:
        {notes}
        """
        response = model.generate_content(prompt)
        raw = response.text.strip()
        questions = []
        blocks = raw.split('\n\n')
        for block in blocks:
            lines = block.strip().split('\n')
            if len(lines) >= 2:
                q = lines[0].replace('Q:', '').strip()
                a = lines[1].replace('A:', '').strip()
                if q and a:
                    questions.append({'question': q, 'answer': a})
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