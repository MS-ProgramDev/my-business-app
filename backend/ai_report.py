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

    # -------- SYSTEM PROMPT (English, Israeli context) ----------
    system_prompt = (
        "You are an expert advisor for business licensing **in Israel**. "
        "Base every answer on the official Israeli regulatory framework, especially "
        "Form 4.2A (Ministry of Interior).  Your report must be in clear English, "
        "structured in Markdown (### section headers). For **each requirement**:\n"
        "• Explain what it is and why it matters.\n"
        "• List concrete steps to comply (links, documents, fees in NIS if known).\n"
        "• Name the responsible Israeli authority (e.g., Ministry of Health, Fire & Rescue).\n"
        "• State priority/urgency (High / Medium / Low).\n"
        "Organize the report by category (Health, Fire Safety, Accessibility, etc.)."
    )

    # -------- USER PROMPT -----------
    user_prompt = "Here is the list of applicable business requirements:\n\n"
    for req in requirements:
        user_prompt += f"- {req['title']}: {req['description']}\n"

    # -------- REQUEST BODY ----------
    body = {
        "model": "meta-llama/llama-4-scout-17b-16e-instruct",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.6,
        "max_tokens": 2000
    }

    # ---------- DEBUG ----------
    print("📤 Sending to Groq:")
    print(json.dumps(body, indent=2, ensure_ascii=False))

    response = requests.post(url, headers=headers, json=body)

    if response.status_code == 200:
        report = response.json()["choices"][0]["message"]["content"]

        # ---------- SAVE TO FILE ----------
        with open("reports/business_compliance_report.txt", "w", encoding="utf-8") as f:
            f.write(report)

        """
            os.makedirs("reports", exist_ok=True)
    file_id = str(uuid.uuid4())
    filename = f"{file_id}.md"        
    filepath = os.path.join("reports", filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(report)
         return report, f"/api/reports/{filename}"
        """

        return report
    else:
        raise Exception(f"Groq API Error: {response.status_code} {response.text}")
