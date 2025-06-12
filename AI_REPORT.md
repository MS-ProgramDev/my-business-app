
# AI Prompts and Use

## 🔧 Prompt Engineering Process

### Prompt 1 – Initial Version (Low Quality)
```
You are a business compliance assistant. For each requirement explain:
- what it is
- steps to comply
- costs
- urgency
```
🧠 Result: very generic, no local context, no reference to Israeli law.

---

### Prompt 2 – Improved (Medium Quality)
```
You are a regulatory advisor for Israeli businesses. Explain compliance steps for restaurants in Israel based on document 4.2A.
```
⚙️ Result: Some improvement, but lacked proper formatting and link explanations.

---

### Prompt 3 – Final Version (High Quality)
```
You are a regulatory compliance expert for Israeli businesses.

Your only source of truth is the official Israeli specification:
"מפרט אחיד פריט 4.2 א׳ – בית אוכל / מסעדה (כולל משלוח ושתייה לשימוש במקום)"
https://www.gov.il/BlobFolder/generalpage/uniform-spec-04-02a/he/18-07-2022_4.2A.pdf

Instructions:
- Return Markdown
- Bold field names (e.g., **Name:**)
- Each field on new line
- Include links with explanations for their purpose
```

📈 Result: Highly relevant, organized, accurate output.

---

## 🛠️ AI Tool Used

**Groq API** with model: `meta-llama/llama-4-scout-17b-16e-instruct`

## ⚠️ Considerations

- Groq used instead of OpenAI to avoid paid usage
- Prompt temperature was reduced to `0.1` for accuracy
