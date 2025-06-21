export function showResult(res) {
  document.getElementById("annotated").src = `http://localhost:8000${res.annotated_url}`;
  document.getElementById("fullText").textContent = res.text;
}
