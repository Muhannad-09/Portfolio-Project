import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:5000/api/v1/books",
});

export const getBooks = async (query = "") => {
  const res = await API.get("/", { params: { q: query } });
  return res.data;
};
