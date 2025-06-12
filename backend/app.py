import os
import uuid
from flask import Flask, request, jsonify
from flask_cors import CORS
from db import SessionLocal
from models import BusinessProfile
from logic import get_matching_requirements
import requests
from ai_report import generate_business_report
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
CORS(app)

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

        return jsonify({
            "report": report,
        }), 200

    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500

    finally:
        session.close()


if __name__ == "__main__":
    app.run(debug=True)
