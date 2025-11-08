import React from "react";
import { useState } from "react";
import { predictSentiment } from "../services/api";

export default function SentimentForm() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = await predictSentiment(text);
    setResult(data.sentiment);
  };

  return (
    <div>
      <h2>Sentiment Analyzer</h2>
      <form onSubmit={handleSubmit}>
        <textarea
          rows="4"
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Type something..."
        />
        <br />
        <button type="submit">Analyze</button>
      </form>
      {result && <p>Predicted Sentiment: <b>{result}</b></p>}
    </div>
  );
}
