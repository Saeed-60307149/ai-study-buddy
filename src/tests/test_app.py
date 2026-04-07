import pytest
import mongomock
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

@pytest.fixture
def client(monkeypatch):
    monkeypatch.setenv('MONGO_URI', 'mongodb://localhost:27017/')
    import mongomock
    monkeypatch.setattr('pymongo.MongoClient', mongomock.MongoClient)
    import app as flask_app
    flask_app.app.config['TESTING'] = True
    with flask_app.app.test_client() as c:
        yield c

def test_health_returns_200(client):
    r = client.get('/health')
    assert r.status_code == 200

def test_health_returns_ok_status(client):
    r = client.get('/health')
    assert r.get_json()['status'] == 'ok'

def test_home_returns_200(client):
    r = client.get('/')
    assert r.status_code == 200

def test_summarize_with_notes_returns_200(client):
    r = client.post('/api/summarize',
        json={'notes': 'some study notes here'})
    assert r.status_code == 200

def test_summarize_returns_summary_key(client):
    r = client.post('/api/summarize', json={'notes': 'notes'})
    assert 'summary' in r.get_json()

def test_summarize_with_no_notes_returns_400(client):
    r = client.post('/api/summarize', json={})
    assert r.status_code == 400

def test_quiz_with_notes_returns_200(client):
    r = client.post('/api/quiz', json={'notes': 'some notes'})
    assert r.status_code == 200

def test_quiz_returns_questions_key(client):
    r = client.post('/api/quiz', json={'notes': 'notes'})
    assert 'questions' in r.get_json()

def test_quiz_with_no_notes_returns_400(client):
    r = client.post('/api/quiz', json={})
    assert r.status_code == 400

def test_sessions_get_returns_200(client):
    r = client.get('/api/sessions')
    assert r.status_code == 200

def test_sessions_get_returns_sessions_key(client):
    r = client.get('/api/sessions')
    assert 'sessions' in r.get_json()

def test_sessions_post_saves_session(client):
    r = client.post('/api/sessions',
        json={'notes': 'test', 'type': 'summary', 'result': 'ok'})
    assert r.status_code == 200
    assert 'message' in r.get_json()
