import { useState } from "react";
import { useAuth } from "../context/AuthContext";

export default function LoginForm() {
  const { login } = useAuth();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState(null);

  async function handleSubmit(e) {
    e.preventDefault();
    try {
      await login(username, password);
    } catch {
      setError("Invalid username or password.");
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <h2>Sign in</h2>
      {error && <p style={{ color: "red" }}>{error}</p>}
      <input
        placeholder="Username"
        value={username}
        onChange={e => setUsername(e.target.value)}
      />
      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={e => setPassword(e.target.value)}
      />
      <button type="submit">Login</button>
    </form>
  )
}
