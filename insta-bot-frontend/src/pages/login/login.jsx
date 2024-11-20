import React, { useState } from "react";
import axios from "axios";

function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async () => {
    try {
      const response = await axios.post("http://127.0.0.1:8000/api/configs/", {
        username,
        password,
        target_hashtags: "example",
      });
      alert("Bot created with ID: " + response.data.id);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="container flex items-center justify-center h-[100dvh]">
      <div className="flex flex-col items-center gap-5 bg-white p-16 rounded-2xl shadow-md">
        <h1 className="text-2xl font-semibold">Instagram Bot</h1>
        <input
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          className="border-2 px-3 py-2 rounded-2xl min-w-52 w-64 text-lg"
        />
        <input
          placeholder="Password"
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className="border-2 px-3 py-2 rounded-2xl min-w-52 w-64"
        />
        <button 
            onClick={handleLogin}
            className="bg-orange-500 w-fit text-white p-3 rounded-full text-xl"
        >
            Create Bot
        </button>
      </div>
    </div>
  );
}

export default Login;
