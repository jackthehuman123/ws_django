import { useState } from "react";
import { useAuth } from "../context/AuthContext";

export default function InputBar({ onSend, disabled }) {
  const [text, setText] = useState("");

  function handleKeyDown(e) {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      if (text.trim() && !disabled) {
        onSend(text.trim());
        setText("");
      }
    }
  }

  return (
    <div style={{ display: "flex", gap: "8px", padding: "8px" }}>
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        onKeyDown={handleKeyDown}
        disabled={disabled}
        placeholder={
          disabled ? "Reconnecting..." : "Type a message (Enter to send)"
        }
        rows={2}
        style={{ flex: 1, resize: "none" }}
      ></textarea>
    </div>
  );
}
