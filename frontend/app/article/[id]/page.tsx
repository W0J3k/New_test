'use client';
import { useQuery } from '@tanstack/react-query';
import { getArticle } from '../../../lib/api';

export default function ArticlePage({ params }: { params: { id: string } }) {
  const { data } = useQuery({
    queryKey: ['article', params.id],
    queryFn: () => getArticle(params.id),
  });
  if (!data) return <div>Loading...</div>;
  return (
    <div>
      <h1 className="text-2xl mb-4">{data.title}</h1>
      <article className="prose">{data.content}</article>
    </div>
  );
}
