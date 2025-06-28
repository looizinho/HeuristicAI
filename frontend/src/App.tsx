import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import SnapshotsList from './SnapshotsList';

function Home() {
  return (
    <div>
      <h1>Bem-vindo à Home</h1>
      <p><Link to="/snapshots">Ver Snapshots</Link></p>
    </div>
  );
}

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/snapshots" element={<SnapshotsList />} />
      </Routes>
    </Router>
  );
}

export default App;
