import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'


function App() {
  const [messages, setMessages] = useState([
    { role: "assistant", text: "👋 Hello, I’m Crash. How can I help?" }
  ]);
  const [input, setInput] = useState("");

  const sendMessage = () => {
    if (!input.trim()) return; // ignore empty

    // Add user message
    const newMessage = { role: "user", text: input };
    setMessages([...messages, newMessage]);

    // Clear input
    setInput("");
  };

  return (
    <div style={{ 
      height: "100vh", 
      display: "flex", 
      flexDirection: "column", 
      justifyContent: "space-between", 
      backgroundColor: "#1e1e1e", 
      color: "white", 
      padding: "20px" 
    }}>
      {/* Chat messages area */}
      <div id="chat-window" style={{ flex: 1, overflowY: "auto", marginBottom: "10px" }}>
        {messages.map((msg, i) => (
          <p 
            key={i} 
            style={{ 
              textAlign: msg.role === "user" ? "right" : "left",
              backgroundColor: msg.role === "user" ? "#007bff" : "#333",
              padding: "8px 12px",
              borderRadius: "8px",
              display: "inline-block",
              maxWidth: "70%",
              marginBottom: "8px"
            }}
          >
            {msg.text}
          </p>
        ))}
      </div>

      {/* Input area */}
      <div style={{ display: "flex" }}>
        <input 
          type="text" 
          placeholder="Type your message..." 
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && sendMessage()}
          style={{ flex: 1, padding: "10px", borderRadius: "8px", border: "none" }} 
        />
        <button 
          onClick={sendMessage}
          style={{ marginLeft: "10px", padding: "10px 20px", borderRadius: "8px", border: "none", backgroundColor: "#007bff", color: "white" }}
        >
          Send
        </button>
      </div>
    </div>
  );
}

export default App;


