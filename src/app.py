from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Study Assistant Running"

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(debug=True)