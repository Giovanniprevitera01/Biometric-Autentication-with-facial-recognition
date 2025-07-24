import React, { useState } from 'react';
import './App.css';

function App() {
  const [message, setMessage] = useState('');

  const handleTest = async () => {
    try {
      const response = await fetch('http://localhost:5000/test');
      const data = await response.json();
      setMessage(data.message);
    } catch (error) {
      setMessage('Errore nella connessione al backend.');
    }
  };

  return (
    <div className="App">
      <h1>Face Recognition Dashboard</h1>
      <button onClick={handleTest}>Test Connessione Backend</button>
      <p>{message}</p>
    </div>
  );
}

export default App;
