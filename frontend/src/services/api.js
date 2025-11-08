import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:8000",
});

export const predictSentiment = async (text) => {
  const response = await API.post("/predict/", { text });
  return response.data;
};
