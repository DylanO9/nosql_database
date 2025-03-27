import React, { useState } from "react";
import { setKeyValue, getKeyValue } from "./api";
import "./App.css"; // Import the CSS file

const App = () => {
  const [key, setKey] = useState("");
  const [value, setValue] = useState("");
  const [retrievedValue, setRetrievedValue] = useState("");
  const [error, setError] = useState("");

  const handleSet = async () => {
    if (!key || !value) {
      setError("Both key and value are required.");
      return;
    }
    const response = await setKeyValue(key, value);
    setError(response.message || "");
  };

  const handleGet = async () => {
    if (!key) {
      setError("Key is required.");
      return;
    }
    const response = await getKeyValue(key);
    setRetrievedValue(response.value || "Value not found");
    setError("");
  };

  return (
    <div className="app-container">
      <h1>Distributed NoSQL Database</h1>

      <div className="form-container">
        <h3>Store Key-Value Pair</h3>
        <input
          type="text"
          placeholder="Key"
          value={key}
          onChange={(e) => setKey(e.target.value)}
          className="input-field"
        />
        <input
          type="text"
          placeholder="Value"
          value={value}
          onChange={(e) => setValue(e.target.value)}
          className="input-field"
        />
        <button onClick={handleSet} className="button">
          Set Value
        </button>
      </div>

      <div className="form-container">
        <h3>Retrieve Value</h3>
        <input
          type="text"
          placeholder="Key"
          value={key}
          onChange={(e) => setKey(e.target.value)}
          className="input-field"
        />
        <button onClick={handleGet} className="button">
          Get Value
        </button>
      </div>

      {error && <p className="error-message">{error}</p>}
      {retrievedValue && <p className="retrieved-value">Retrieved Value: {retrievedValue}</p>}
    </div>
  );
};

export default App;
