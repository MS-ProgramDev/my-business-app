import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def generate_business_report(requirements):
    """
    Sends business requirements to Groq API and returns a detailed, business-friendly compliance report.
    """
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    system_prompt = (
        "You are a business compliance assistant. "
        "Your job is to translate regulatory requirements into clear, step-by-step business reports. "
        "For each requirement, explain:\n"
        "- What it is and why it's needed\n"
        "- Steps to comply (including links, documents, cost if known)\n"
        "- Priority level and urgency\n"
        "- Organize the report clearly by category and use friendly language"
    )

    user_prompt = "Here is the list of business requirements:\n\n"
    for req in requirements:
        user_prompt += f"- {req['title']}: {req['description']}\n"

    body = {
        "model": "meta-llama/llama-4-scout-17b-16e-instruct",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.6,
        "max_tokens": 2000
    }
    print("📤 Sending to Groq:")
    print(json.dumps(body, indent=2, ensure_ascii=False))

    response = requests.post(url, headers=headers, json=body)

    if response.status_code == 200:
        report = response.json()["choices"][0]["message"]["content"]

        # Save report to file
        with open("business_compliance_report.txt", "w", encoding="utf-8") as f:
            f.write(report)

        return report
    else:
        raise Exception(f"Groq API Error: {response.status_code} {response.text}")
