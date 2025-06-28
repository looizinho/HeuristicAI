import React, { useEffect, useState } from 'react';

interface Snapshot {
  _id: string;
  name: string;
  timestamp: number;
  columns: number;
  layers: number;
  clips: number;
}

const SnapshotsList: React.FC = () => {
  const [snapshots, setSnapshots] = useState<Snapshot[]>([]);

  useEffect(() => {
    fetch('http://localhost:3000/snapshots')
      .then(res => res.json())
      .then(data => {
        const sorted = [...data].sort((a, b) => b.timestamp - a.timestamp);
        setSnapshots(sorted);
      })
      .catch(err => console.error(err));
  }, []);

  if (snapshots.length === 0) {
    return <div>Carregando snapshots...</div>;
  }

  const [latest, ...others] = snapshots;

  return (
    <div>
      <h2>Snapshot Mais Recente</h2>
      <h2>Snapshot Mais Recente</h2>
      <div>
        <strong>{latest.name}</strong><br />
        Data: {new Date(latest.timestamp * 1000).toLocaleString()}<br />
        Colunas: {latest.composition.columns ? latest.composition.columns.length : 0}<br />
        Layers: {latest.composition.layers ? latest.composition.layers.length : 0}<br />
        Clips: {latest.composition.clips ? latest.composition.clips.length : 0}
      </div>

      <h3>Outros Snapshots</h3>
      <ul>
        {others.map(snapshot => (
          <li key={snapshot._id}>
            {snapshot.name} - {new Date(snapshot.timestamp * 1000).toLocaleString()}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default SnapshotsList;
