import React, { useState } from "react";
import "../styles/NewBusinessForm.css";
import ReactMarkdown from "react-markdown";

const NewBusinessForm = () => {
  const [form, setForm] = useState({
    name: "",
    area: "",
    seating_capacity: "",
    uses_gas: false,
    serves_meat: false,
    offers_delivery: false,
    serves_alcohol: false,
  });

  const [requirements, setRequirements] = useState<any[]>([]);
  const [reportText, setReportText] = useState(""); // New: AI report text
  const [downloadLink, setDownloadLink] = useState(""); // New: download URL
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value, type, checked } = e.target;
    setForm((prev) => ({
      ...prev,
      [name]: type === "checkbox" ? checked : value,
    }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError("");
    setRequirements([]);
    setReportText("");
    setDownloadLink("");

    try {
      const response = await fetch("http://localhost:5000/api/business", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          ...form,
          area: Number(form.area),
          seating_capacity: Number(form.seating_capacity),
        }),
      });

      if (!response.ok) {
        throw new Error("Server responded with an error.");
      }

      const data = await response.json();

      if (data.message) {
        setError(data.message);
      }

      if (data.requirements) {
        setRequirements(data.requirements);
      }

      if (data.report) {
        setReportText(data.report);
      }

      if (data.download_url) {
        setDownloadLink(data.download_url);
      }

    } catch (err) {
      console.error("Submission error:", err);
      setError("An error occurred while submitting the form.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="form-container">
      <h2>Create New Business</h2>

      <div className="form-group">
        <label htmlFor="name">Enter the business name</label>
        <input
          id="name"
          name="name"
          value={form.name}
          onChange={handleChange}
          required
        />

        <label htmlFor="area">Business area (in square meters)</label>
        <input
          id="area"
          name="area"
          type="number"
          value={form.area}
          onChange={handleChange}
          required
        />

        <label htmlFor="seating_capacity">Seating capacity</label>
        <input
          id="seating_capacity"
          name="seating_capacity"
          type="number"
          value={form.seating_capacity}
          onChange={handleChange}
          required
        />
      </div>

      <div className="features-group">
        <p className="features-title">Select Business Features:</p>
        <div className="feature-options">
          <button
            type="button"
            className={form.uses_gas ? "feature active" : "feature"}
            onClick={() => setForm((prev) => ({ ...prev, uses_gas: !prev.uses_gas }))}
          >
            Uses Gas
          </button>

          <button
            type="button"
            className={form.serves_meat ? "feature active" : "feature"}
            onClick={() => setForm((prev) => ({ ...prev, serves_meat: !prev.serves_meat }))}
          >
            Serves Meat
          </button>

          <button
            type="button"
            className={form.offers_delivery ? "feature active" : "feature"}
            onClick={() => setForm((prev) => ({ ...prev, offers_delivery: !prev.offers_delivery }))}
          >
            Delivery
          </button>

          <button
            type="button"
            className={form.serves_alcohol ? "feature active" : "feature"}
            onClick={() => setForm((prev) => ({ ...prev, serves_alcohol: !prev.serves_alcohol }))}
          >
            Alcohol
          </button>
        </div>
      </div>

      <button type="submit" disabled={loading}>
        {loading ? "Submitting..." : "Submit"}
      </button>

      {error && <p className="error">{error}</p>}

      {requirements.length > 0 && (
        <div className="requirements">
          <h3>Matched Requirements</h3>
          <ul>
            {requirements.map((req) => (
              <li key={req.id}>
                <strong>{req.title}</strong>: {req.description}
              </li>
            ))}
          </ul>
        </div>
      )}

      {reportText && (
        <div className="report-section">
          <h3>AI Business Report</h3>
          
         <ReactMarkdown components={{
            div: ({node, ...props}) => <div className="markdown-body" {...props} />
          }}>{reportText}</ReactMarkdown>

          {downloadLink && (
            <a href={`http://localhost:5000${downloadLink}`} download target="_blank" rel="noopener noreferrer">
              <button className="download-btn">Download Report</button>
            </a>
          )}
        </div>
      )}
    </form>
  );
};

export default NewBusinessForm;
