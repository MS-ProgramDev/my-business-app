import React, { useState } from "react";
import "../styles/NewBusinessForm.css";

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

  const [requirements, setRequirements] = useState([]);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value, type, checked } = e.target;
    setForm((prev) => ({
      ...prev,
      [name]: type === "checkbox" ? checked : value,
    }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const response = await fetch("http://localhost:5000/api/business", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        ...form,
        area: Number(form.area),
        seating_capacity: Number(form.seating_capacity),
      }),
    });

    const data = await response.json();
    setRequirements(data.requirements);
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

        <label htmlFor="area">What is the business area (in square meters)?</label>
        <input
          id="area"
          name="area"
          type="number"
          value={form.area}
          onChange={handleChange}
          required
        />

        <label htmlFor="seating_capacity">How many seating places are available?</label>
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
      onClick={() => setForm(prev => ({ ...prev, uses_gas: !prev.uses_gas }))}
    >
      Uses Gas
    </button>

    <button
      type="button"
      className={form.serves_meat ? "feature active" : "feature"}
      onClick={() => setForm(prev => ({ ...prev, serves_meat: !prev.serves_meat }))}
    >
      Serves Meat
    </button>

    <button
      type="button"
      className={form.offers_delivery ? "feature active" : "feature"}
      onClick={() => setForm(prev => ({ ...prev, offers_delivery: !prev.offers_delivery }))}
    >
      Delivery
    </button>

    <button
      type="button"
      className={form.serves_alcohol ? "feature active" : "feature"}
      onClick={() => setForm(prev => ({ ...prev, serves_alcohol: !prev.serves_alcohol }))}
    >
      Alcohol
    </button>
  </div>
</div>


      <button type="submit">Submit</button>

      {requirements.length > 0 && (
        <div className="requirements">
          <h3>Matched Requirements</h3>
          <ul>
            {requirements.map((req: any) => (
              <li key={req.id}>
                <strong>{req.title}</strong>: {req.description}
              </li>
            ))}
          </ul>
        </div>
      )}
    </form>
  );
};

export default NewBusinessForm;
