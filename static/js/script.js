console.log("AI Study Assistant JS loaded");

// ===== SUMMARIZE PAGE =====
const summarizeBtn = document.getElementById('summarizeBtn');
if (summarizeBtn) {
    summarizeBtn.addEventListener('click', async function () {
        const notes = document.getElementById('notesInput').value.trim();
        const errorMsg = document.getElementById('errorMsg');
        const loading = document.getElementById('loading');
        const resultCard = document.getElementById('resultCard');
        const summaryResult = document.getElementById('summaryResult');

        if (!notes) {
            errorMsg.textContent = 'Please paste your notes first.';
            return;
        }

        errorMsg.textContent = '';
        loading.style.display = 'block';
        resultCard.style.display = 'none';

        try {
            const response = await fetch('/api/summarize', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ notes: notes })
            });
            const data = await response.json();
            loading.style.display = 'none';
            summaryResult.textContent = data.summary;
            resultCard.style.display = 'block';
        } catch (error) {
            loading.style.display = 'none';
            errorMsg.textContent = 'Something went wrong. Please try again.';
        }
    });
}

// ===== QUIZ PAGE =====
const quizBtn = document.getElementById('quizBtn');
if (quizBtn) {
    quizBtn.addEventListener('click', async function () {
        const notes = document.getElementById('notesInput').value.trim();
        const errorMsg = document.getElementById('errorMsg');
        const loading = document.getElementById('loading');
        const resultCard = document.getElementById('resultCard');
        const quizResult = document.getElementById('quizResult');

        if (!notes) {
            errorMsg.textContent = 'Please paste your notes first.';
            return;
        }

        errorMsg.textContent = '';
        loading.style.display = 'block';
        resultCard.style.display = 'none';

        try {
            const response = await fetch('/api/quiz', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ notes: notes })
            });
            const data = await response.json();
            loading.style.display = 'none';

            if (data.questions && data.questions.length > 0) {
                quizResult.innerHTML = data.questions.map((q, i) =>
                    `<div class="session-item"><strong>Q${i+1}:</strong> ${q}</div>`
                ).join('');
            } else {
                quizResult.textContent = 'No questions generated. Try with more detailed notes.';
            }
            resultCard.style.display = 'block';
        } catch (error) {
            loading.style.display = 'none';
            errorMsg.textContent = 'Something went wrong. Please try again.';
        }
    });
}

// ===== DASHBOARD — VIEW SESSIONS =====
const viewSessionsBtn = document.getElementById('viewSessionsBtn');
if (viewSessionsBtn) {
    viewSessionsBtn.addEventListener('click', async function (e) {
        e.preventDefault();
        const sessionsContainer = document.getElementById('sessionsContainer');
        const sessionsList = document.getElementById('sessionsList');

        try {
            const response = await fetch('/api/sessions');
            const data = await response.json();

            if (data.sessions.length === 0) {
                sessionsList.innerHTML = '<p>No sessions saved yet.</p>';
            } else {
                sessionsList.innerHTML = data.sessions.map(s =>
                    `<div class="session-item">
                        <strong>${s.type.toUpperCase()}</strong> — ${s.created_at}<br>
                        <small>${s.notes.substring(0, 100)}...</small>
                    </div>`
                ).join('');
            }
            sessionsContainer.style.display = 'block';
        } catch (error) {
            sessionsList.innerHTML = '<p>Could not load sessions.</p>';
            sessionsContainer.style.display = 'block';
        }
    });
}
