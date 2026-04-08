# 📚 AI Study Assistant

> An AI-powered web application that helps students study smarter by summarizing notes and generating quiz questions using Google Gemini.

---

## 📖 Description

AI Study Assistant is a Flask-based web application built for students who want to study more efficiently. Users can paste their study notes and instantly receive AI-generated summaries and quiz questions powered by the Google Gemini API. Study sessions are saved to a MongoDB database so users can review their progress over time.

---

## 🌐 Live URL

> 🔗 [https://ai-study-buddy-latest-4114.onrender.com](https://ai-study-buddy-latest-4114.onrender.com)

---

## ✨ Features

| Feature | AI-Powered |
|---|---|
| Paste study notes | ❌ |
| AI-generated note summary | ✅ Gemini API |
| AI-generated quiz questions | ✅ Gemini API |
| Save and view past study sessions | ❌ |
| Dedicated sessions history page | ❌ |
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
| Image Registry | Docker Hub | Stores built images for deployment |

---

## 👥 Team Members

| Name | Student ID | Role | Ownership |
|---|---|---|---|
| Hamad Almansouri | 60302091 | Backend & Database | Flask API routes, MongoDB integration |
| Abdulrahman Al-Mutawah | 60102286 | AI & Testing | Gemini integration, prompt design, unit tests |
| Saeed Abdullah Dar | 60307149 | Frontend & DevOps | UI templates, GitHub Actions CI/CD, Render deployment |

---

## 🏗️ Architecture

```
Push to main
→ GitHub Actions CI runs:
   - Linter (flake8)
   - Unit tests (pytest — 12 tests)
   - Docker image build
   - Smoke test (/health endpoint)
→ CI passes
→ CD runs:
   - Builds and pushes image to Docker Hub
     (cipher974/ai-study-buddy:latest)
   - Triggers Render deploy hook
→ Render pulls latest image and deploys
→ Live URL updates automatically
```

---

## 📁 Project Structure

```
ai-study-buddy/
│
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── Dockerfile              # Container configuration
├── .env.example            # Environment variable template
├── .gitignore              # Git ignore rules
│
├── templates/              # HTML templates (Jinja2)
│   ├── base.html           # Base layout with navbar
│   ├── index.html          # Homepage
│   ├── dashboard.html      # Dashboard page
│   ├── summarize.html      # AI summarize page
│   ├── quiz.html           # AI quiz page
│   └── sessions.html       # Past sessions page
│
├── static/
│   ├── css/
│   │   └── style.css       # Cyberpunk dark theme stylesheet
│   └── js/
│       └── script.js       # Frontend JavaScript
│
├── tests/
│   ├── __init__.py
│   └── test_app.py         # Unit tests (12 tests)
│
└── .github/
    └── workflows/
        └── ci.yml          # GitHub Actions CI/CD pipeline
```

---

## ⚙️ Local Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/HBS-oc/ai-study-buddy.git
cd ai-study-buddy
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
GEMINI_API_KEY=your-gemini-api-key-here
MONGODB_URI=your-mongodb-connection-string-here
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
docker build -t ai-study-buddy .
```

### Run the Container

```bash
docker run -p 5000:5000 --env-file .env ai-study-buddy
```

### Open in Browser

```
http://localhost:5000/
```

---

## 🧪 Run Tests

```bash
pip install pytest mongomock
pytest tests/ -v
```

Expected: 12 tests passing

---

## 🔀 Branch Strategy

```
main          → production-ready code only
feature/name  → one branch per feature or task
fix/issue-N   → bug fixes
docs/name     → documentation updates
chore/name    → DevOps and configuration tasks
```

All work is done via feature branches and pull requests.
No direct commits to main.

---

## 📅 Timeline

| Milestone | Due Date | Goals |
|---|---|---|
| Foundation | April 2, 2026 | Repo setup, proposal, app skeleton, Docker, CI |
| Core Development | April 4, 2026 | All features, AI integration, unit tests, CI green |
| Deployment & Presentation | April 6, 2026 | CD pipeline, live URL, presentation ready |

---

## 📝 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Homepage |
| GET | `/dashboard` | Dashboard page |
| GET | `/summarize` | Summarize page |
| GET | `/quiz` | Quiz page |
| GET | `/sessions` | Sessions history page |
| GET | `/health` | Health check |
| GET | `/api/test-db` | Test database connection |
| POST | `/api/summarize` | Generate AI summary from notes |
| POST | `/api/quiz` | Generate quiz questions from notes |
| GET | `/api/sessions` | Get all past study sessions |
| POST | `/api/sessions` | Save a new study session |