import Link from 'next/link';

interface Article {
  id: number;
  title: string;
}

export default function ArticleList({ articles }: { articles: Article[] }) {
  return (
    <ul className="space-y-2">
      {articles.map((a) => (
        <li key={a.id} className="p-2 bg-white shadow">
          <Link href={`/article/${a.id}`}>{a.title}</Link>
        </li>
      ))}
    </ul>
  );
}
