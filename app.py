from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime
import os

load_dotenv()

app = Flask(__name__)

client = MongoClient(os.getenv('MONGO_URI'))
db = client['study_assistant']


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/health')
def health():
    return jsonify({'status': 'ok'})


@app.route('/api/test-db')
def test_db():
    try:
        client.admin.command('ping')
        return jsonify({'status': 'connected', 'db': 'ok'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route('/api/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    notes = data.get('notes', '')
    if not notes:
        return jsonify({'error': 'No notes provided'}), 400
    return jsonify({'summary': 'Summary coming soon - AI not connected yet'})


@app.route('/api/quiz', methods=['POST'])
def quiz():
    data = request.get_json()
    notes = data.get('notes', '')
    if not notes:
        return jsonify({'error': 'No notes provided'}), 400
    return jsonify({'questions': []})


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
    app.run(debug=True)