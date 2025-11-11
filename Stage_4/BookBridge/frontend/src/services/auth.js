import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:5000/api/v1/auth",
});

// LOGIN
export const loginUser = async (data) => {
  try {
    const res = await API.post("/login", data);
    const { token, user } = res.data;

    // Save token so we can use it later for protected routes
    localStorage.setItem("token", token);
    localStorage.setItem("user", JSON.stringify(user));

    alert(`Welcome back, ${user.username}!`);
    return res.data;
  } catch (err) {
    console.error(err);
    alert("Login failed! Please check your username and password.");
    throw err;
  }
};

// REGISTER
export const registerUser = async (data) => {
  try {
    const res = await API.post("/register", data);
    alert("Account created successfully!");
    return res.data;
  } catch (err) {
    console.error(err);
    alert("Registration failed! Try again.");
    throw err;
  }
};

// LOGOUT (optional but nice)
export const logoutUser = () => {
  localStorage.removeItem("token");
  localStorage.removeItem("user");
  alert("You have been logged out.");
};
