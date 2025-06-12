# My Business App 🇮🇱📄

This is a smart assistant for restaurants in Israel, helping business owners understand their legal licensing obligations based on official specification **4.2A**.  
The system matches business characteristics to regulatory requirements and uses AI (via Groq) to generate clear, personalized compliance reports in English.

## 🏗️ Architecture

- **Frontend:** React (Port 3000)
- **Backend:** Python Flask (Port 5000)
- **Database:** PostgreSQL (Port 5432)
- **AI Integration:** Groq LLM (`llama-4-scout-17b`)

## 📦 Project Structure

```
my-business-app/
├── backend/
│   ├── app.py
│   ├── db.py
│   ├── models.py
│   ├── logic.py
│   ├── ai_report.py
│   ├── seed.py
│   └── requirements.txt
├── src/
│   └── React app with form and result renderer
└── .env.example  (example with env var names)
```


## 🧪 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/MS-ProgramDev/my-business-app.git
```

### 2. Backend Setup

#### a. Environment variables (`backend/.env`)
```ini
GROQ_API_KEY=your-groq-key
DB_USER=your-db-username
DB_PASS=your-db-password
```

#### b. Create database schema

```bash
python backend/init_db.py
```

#### c. Seed initial regulatory requirements

```bash
python backend/seed.py
```

#### d. Install dependencies and run the server

```bash
cd backend
pip install -r requirements.txt
python app.py
```

---

### 3. Frontend Setup

```bash
cd frontend
npm install
npm start
```

## 🧠 AI Integration (Groq)

- Model: `llama-4-scout-17b-16e-instruct`
- Temperature: 0.1 (for factual precision)
- Prompts are designed to produce structured, markdown-formatted regulatory reports per requirement.
- Prompt includes link to the official Israeli regulation PDF (spec 4.2A) and instructs the model to extract only relevant fields.

---

## 🧪 API Documentation

### POST `/api/business`
Submits business data and returns AI-generated compliance report.

**Request JSON**
```json
{
  "name": "Nice Work",
  "area": 441,
  "seating_capacity": 88,
  "uses_gas": true,
  "serves_meat": true,
  "offers_delivery": true,
  "serves_alcohol": true
}
```

**Response JSON**
```json
{
  "report": "### Gas System Approval\n\n**Name:** Gas System Approval ..."
}
```

---

## 📦 Data Model

- `BusinessProfile`: name, area, seating_capacity, uses_gas, serves_meat, offers_delivery, serves_alcohol
- `Requirement`: title, description, action, priority
- `RequirementCondition`: field_name, operator, value → used for matching

---

## 📊 Development Log

- First time integrating with an LLM API (Groq)
- Initially received vague output; improved results by crafting precise system prompt and lowering temperature
- Realized prompt engineering and temperature control are critical to output quality
- Decided to avoid OpenAI due to cost concerns and kept Groq as the free alternative

---

## 🚀 Future Improvements

- Add report download button (PDF/Markdown)
- Save user reports per business
- Admin panel to manage regulatory requirements
- Add more conditions and broader categories

---

## 🧪 Tools Used

- **AI**: Groq LLM API (`llama-4-scout-17b`)
- **Editor**: VSCode, Pycharm
- **Languages**: Python, TypeScript
- **Frontend**: React + CSS
- **Backend**: Flask
- **DB**: PostgreSQL

---

## 📷 Screenshots

![alt text](../image.png) ![alt text](../image-1.png) ![alt text](../image-2.png) ![alt text](../image-3.png) ![alt text](../image-4.png)
---

## 🤖 Prompt Example

```text
You are a regulatory compliance expert for Israeli businesses...
Each requirement should include:
- Name:
- What it is and why it's needed:
- Steps to comply:
- Estimated cost...
...
```

---

## ✅ Submission Notes

- Everything runs locally (no Docker)
- .env file not uploaded (see template above)
- Sensitive values stored securely
- The app meets all core functional and technical requirements

---

## 🏁 To Run End-to-End

1. Setup backend `.env`, DB, and `python seed.py`
2. Start backend on port 5000
3. Start frontend on port 3000
4. Enter data via form → Get report

[def]: ../image.png
[def2]: ../image-4.png
