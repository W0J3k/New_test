import axios from 'axios';

const api = axios.create({ baseURL: process.env.NEXT_PUBLIC_API_URL });

export async function getArticles() {
  const res = await api.get('/articles');
  return res.data;
}

export async function getArticle(id: string) {
  const res = await api.get(`/articles/${id}`);
  return res.data;
}

export default api;
