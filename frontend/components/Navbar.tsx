'use client';
import Link from 'next/link';

export default function Navbar() {
  return (
    <nav className="bg-white shadow mb-4">
      <div className="max-w-5xl mx-auto p-4 flex gap-4">
        <Link href="/">Dashboard</Link>
        <Link href="/search">Search</Link>
        <Link href="/sources">Sources</Link>
      </div>
    </nav>
  );
}
