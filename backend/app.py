import os
import uuid

from flask import Flask, request, jsonify
from flask_cors import CORS
from db import SessionLocal
from models import BusinessProfile
from logic import get_matching_requirements
import requests
from ai_report import generate_business_report

"""
# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
"""
app = Flask(__name__)
CORS(app)

"""
@app.route("/ask-groq", methods=["POST"])
def ask_groq():
    user_question = request.json.get("question")

    if not user_question:
        return jsonify({"error": "Missing question"}), 400

    url = "https://api.groq.com/openai/v1/chat/completions"

    payload = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_question}
        ],
        "temperature": 0.7
    }

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        answer = response.json()["choices"][0]["message"]["content"]
        return jsonify({"answer": answer})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

"""
@app.route("/")
def hello():
    return {"message": "Flask is working!"}

@app.route("/api/business", methods=["POST"])
def create_business():
    data = request.get_json()
    session = SessionLocal()

    try:
        business = BusinessProfile(**data)
        session.add(business)
        session.commit()

        requirements = get_matching_requirements(business, session)

        if not requirements:
            return jsonify({"message": "No requirements found for the given business."}), 200

        report = generate_business_report(requirements)

        file_id = str(uuid.uuid4())
        filename = f"{file_id}.txt"
        filepath = os.path.join("reports", filename)
        os.makedirs("reports", exist_ok=True)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(report)

        download_url = f"/api/reports/{filename}"

        return jsonify({
            "report": report,
            "download_url": download_url
        }), 200

    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500

    finally:
        session.close()
"""
@app.route("/api/business", methods=["POST"])
def create_business():
    data = request.get_json()
    session = SessionLocal()

    business = BusinessProfile(**data)
    session.add(business)
    session.commit()

    requirements = get_matching_requirements(business, session)
    session.close()
    if not requirements:
        return jsonify{"message": "No requirements found for the given business."}

    report = generate_business_report(requirements)
    return jsonify{"report": report}

"""

from flask import send_from_directory

@app.route("/api/reports/<filename>", methods=["GET"])
def download_report(filename):
    return send_from_directory("reports", filename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
