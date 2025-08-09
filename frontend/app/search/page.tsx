'use client';
import { useState } from 'react';
import { useMutation } from '@tanstack/react-query';
import api from '../../lib/api';
import ArticleList from '../../components/ArticleList';

export default function SearchPage() {
  const [q, setQ] = useState('');
  const { mutate, data } = useMutation({
    mutationFn: async () => (await api.post('/search', { query: q })).data,
  });
  return (
    <div>
      <h1 className="text-2xl mb-4">Search</h1>
      <div className="flex gap-2 mb-4">
        <input className="border p-2 flex-1" value={q} onChange={(e) => setQ(e.target.value)} />
        <button className="bg-blue-500 text-white px-4" onClick={() => mutate()}>Go</button>
      </div>
      {data && <ArticleList articles={data} />}
    </div>
  );
}
