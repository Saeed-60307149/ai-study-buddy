# 📚 AI Study Assistant

> An AI-powered web application that helps students study smarter by summarizing notes and generating quiz questions using Google Gemini.

---

## 📖 Description

AI Study Assistant is a Flask-based web application built for students who want to study more efficiently. Users can paste their study notes and instantly receive AI-generated summaries and quiz questions powered by the Google Gemini API. Study sessions are saved to a MongoDB database so users can review their progress over time.

---

## ✨ Features

| Feature | AI-Powered |
|---|---|
| Paste or upload study notes | ❌ |
| AI-generated note summary | ✅ Gemini API |
| AI-generated quiz questions | ✅ Gemini API |
| Save and view past study sessions | ❌ |
| Health check endpoint | ❌ |

---

## 🛠️ Tech Stack

| Layer | Technology | Justification |
|---|---|---|
| Backend | Python + Flask | Lightweight, easy to structure REST APIs |
| AI / LLM | Google Gemini API | Provided by instructor, strong summarization |
| Database | MongoDB Atlas | Free tier, flexible document storage |
| Frontend | HTML + CSS + JS | Simple, fast, no framework overhead |
| CI/CD | GitHub Actions | Course standard, integrates natively with GitHub |
| Deployment | Render.com | Free tier, supports Docker, easy deploy hooks |
| Containerization | Docker | Ensures consistent environment across machines |

---

## 👥 Team Members

| Name | Student ID | Role | Ownership |
|---|---|---|---|
| Hamad Almansouri | 60302091 | Backend & Database | Flask API routes, MongoDB integration |
| Abdulrahman Al-Mutawah | 60102286 | AI & Testing | Gemini integration, prompt design, unit tests |
| Saeed Abdullah Dar | 60307149 | Frontend & DevOps | UI templates, GitHub Actions CI/CD, Render deployment |

---

## 📁 Project Structure
```
ai-study-assistant/
│
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── Dockerfile              # Container configuration
├── .env.example            # Environment variable template
├── .gitignore              # Git ignore rules
│
├── templates/              # HTML templates (Jinja2)
│   ├── base.html           # Base layout template
│   ├── index.html          # Homepage
│   ├── login.html          # Login page
│   └── dashboard.html      # Dashboard page
│
├── static/
│   ├── css/
│   │   └── style.css       # Main stylesheet
│   └── js/
│       └── script.js       # Frontend JavaScript
│
└── .github/
    └── workflows/
        └── ci.yml          # GitHub Actions CI pipeline
```

---

## ⚙️ Local Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/HBS-oc/ai-study-assistant.git
cd ai-study-assistant
```

### 2. Create Virtual Environment
```bash
python -m venv venv
```

Activate it:

- Windows:
```bash
venv\Scripts\activate
```
- Mac/Linux:
```bash
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
```bash
cp .env.example .env
```

Open `.env` and fill in your values:
```
FLASK_ENV=development
FLASK_DEBUG=1
SECRET_KEY=your-secret-key-here
GEMINI_API_KEY=your-gemini-api-key-here
MONGO_URI=your-mongodb-connection-string-here
```

### 5. Run the Application
```bash
python app.py
```

### 6. Open in Browser
```
http://127.0.0.1:5000/
```

### 7. Verify Health Endpoint
```
http://127.0.0.1:5000/health
```

Expected response:
```json
{"status": "ok"}
```

---

## 🐳 Run with Docker

### Build the Image
```bash
docker build -t ai-study-assistant .
```

### Run the Container
```bash
docker run -p 5000:5000 --env-file .env ai-study-assistant
```

### Open in Browser
```
http://localhost:5000/
```

---

## 🔀 Branch Strategy
```
main          → production-ready code only
develop       → integration branch
feature/name  → one branch per feature or task
fix/issue-N   → bug fixes
```

All work is done via feature branches and pull requests.
No direct commits to main or develop.

---

## 📅 Timeline

| Milestone | Due Date | Goals |
|---|---|---|
| Foundation | April 2, 2026 | Repo setup, proposal, app skeleton, Docker, CI |
| Core Development | April 4, 2026 | All features, AI integration, unit tests, CI green |
| Deployment & Presentation | April 6, 2026 | CD pipeline, live URL, presentation ready |

---

## 🌐 Live URL

> 🔗 To be updated after deployment

---

## 📝 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Homepage |
| GET | `/health` | Health check |
| GET | `/api/test-db` | Test database connection |
| POST | `/api/summarize` | Generate AI summary from notes |
| POST | `/api/quiz` | Generate quiz questions from notes |
| GET | `/api/sessions` | Get all past study sessions |
| POST | `/api/sessions` | Save a new study session |