'use client';
import { useState } from 'react';
import api from '../../lib/api';

export default function SourcesPage() {
  const [url, setUrl] = useState('');
  const [type, setType] = useState('rss');

  const addSource = async () => {
    await api.post('/sources', { type, name: url, url });
    setUrl('');
  };

  return (
    <div>
      <h1 className="text-2xl mb-4">Sources</h1>
      <div className="flex gap-2 mb-4">
        <select value={type} onChange={(e) => setType(e.target.value)} className="border p-2">
          <option value="rss">RSS</option>
          <option value="reddit">Reddit</option>
          <option value="telegram">Telegram</option>
        </select>
        <input
          className="border p-2 flex-1"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          placeholder="URL or identifier"
        />
        <button className="bg-green-600 text-white px-4" onClick={addSource}>
          Add
        </button>
      </div>
    </div>
  );
}
