from flask import Flask, request, jsonify
from flask_cors import CORS
from db import SessionLocal
from models import BusinessProfile
from logic import get_matching_requirements
app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return {"message": "Flask is working!"}

@app.route("/api/business", methods=["POST"])
def create_business():
    data = request.get_json()
    session = SessionLocal()

    business = BusinessProfile(**data)
    session.add(business)
    session.commit()

    result = get_matching_requirements(business, session)

    session.close()
    return jsonify({"requirements": result})

if __name__ == "__main__":
    app.run(debug=True)
