import './globals.css';
import { ReactNode } from 'react';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import Navbar from '../components/Navbar';

const queryClient = new QueryClient();

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-gray-50">
        <QueryClientProvider client={queryClient}>
          <Navbar />
          <main className="p-4 max-w-5xl mx-auto">{children}</main>
        </QueryClientProvider>
      </body>
    </html>
  );
}
