import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def generate_business_report(requirements):
    """
    Sends business requirements to Groq API and returns a structured, concise compliance report
    based on official Israeli regulation form 4.2A (restaurant category).
    """

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    system_prompt = (
        "You are a regulatory compliance expert for Israeli businesses.\n"
        "You specialize in generating structured, actionable reports based on official regulations "
        "for food-related businesses in Israel.\n\n"

        "Your only source of truth is the official Israeli specification:\n"
        "'מפרט אחיד פריט 4.2 א׳ – בית אוכל / מסעדה (כולל משלוח ושתייה לשימוש במקום)'\n"
        "This document is available at:\n"
        "https://www.gov.il/BlobFolder/generalpage/uniform-spec-04-02a/he/18-07-2022_4.2A.pdf\n\n"

        "Instructions:\n"
        "For each requirement I give you, return a well-structured, clean **Markdown** section. "
        "Do NOT use bullet points or decorative symbols like •. Each field should be clearly labeled and bolded, "
        "and its value should appear on a new line underneath. Keep the format strictly consistent.\n\n"

        "The structure should be:\n"
        "### [Requirement Title]\n\n"
        "**Name:**\n"
        "[Short name of the requirement]\n\n"
        "**What it is and why it's needed:**\n"
        "[Short explanation in simple English]\n\n"
        "**Steps to comply:**\n"
        "1. Step one\n"
        "2. Step two\n"
        "(Maximum 5 steps)\n\n"
        "**Estimated cost (in NIS):**\n"
        "[Approximate range, or 'Not specified']\n\n"
        "**Estimated time to complete:**\n"
        "[Example: '1–3 weeks', or 'Not specified']\n\n"
        "**Responsible authority:**\n"
        "[Official body or ministry]\n\n"
        "**Priority level:**\n"
        "High / Medium / Low\n\n"
        "**Useful links:**\n"
        "Each link must include a short explanation of what the business owner should do with it, "
        "such as 'Use this to submit your application', or 'Download this form to register'.\n"
        "Example:\n"
        "https://www.gov.il/... – Use this site to submit the gas approval request.\n"
        "https://www.gov.il/... – Download this form to apply for a sanitation permit.\n\n"

        "If a field is unknown or not mentioned in the PDF, write: 'Not specified'.\n"
        "Be concise and factual. Use friendly, readable English suitable for business owners."
    )

    user_prompt = "Please generate the compliance details for the following:\n\n"
    for req in requirements:
        user_prompt += f"- {req['title']}: {req['description']}\n"

    payload = {
        "model": "meta-llama/llama-4-scout-17b-16e-instruct",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.1,
        "max_tokens": 2000
    }

    print("📤 Sending to Groq:")
    print(json.dumps(payload, indent=2, ensure_ascii=False))

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        report = response.json()["choices"][0]["message"]["content"]

        return report
    else:
        raise Exception(f"Groq API Error: {response.status_code} {response.text}")
