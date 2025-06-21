import { uploadImage } from "./api.js";
import { showResult } from "./ui.js";

document.getElementById("runBtn").onclick = async () => {
  const file = document.getElementById("fileInput").files[0];
  if (!file) return alert("画像を選択してください");
  try {
    const res = await uploadImage(file);
    showResult(res);
  } catch (e) {
    alert("OCR 失敗: " + e.message);
  }
};
