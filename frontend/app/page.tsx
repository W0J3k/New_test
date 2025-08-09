'use client';
import { useQuery } from '@tanstack/react-query';
import { getArticles } from '../lib/api';
import ArticleList from '../components/ArticleList';

export default function Page() {
  const { data } = useQuery({ queryKey: ['articles'], queryFn: getArticles });
  return (
    <div>
      <h1 className="text-2xl mb-4">Latest Articles</h1>
      {data ? <ArticleList articles={data} /> : 'Loading...'}
    </div>
  );
}
