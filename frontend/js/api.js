const BASE = "http://localhost:8000";
export async function uploadImage(file) {
  const body = new FormData();
  body.append("file", file);
  const res = await fetch(`${BASE}/ocr`, { method: "POST", body });
  if (!res.ok) throw new Error(await res.text());
  return res.json();
}
