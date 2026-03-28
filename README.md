# 🚀 RSVP Speed Reader (Single-Chapter Clean Pipeline)

A high-speed reading application that displays text using the **RSVP (Rapid Serial Visual Presentation)** method, optimized for **clean, text-based PDFs (one chapter per file)**.

---

# 🧠 Project Overview

This project was built to solve a real limitation:

> ❌ Traditional PDF parsing (especially scanned books) leads to broken text, OCR errors, and unreliable chapter detection.

Instead of fighting noisy data, this system follows a **clean-input-first engineering approach**:

> ✅ Convert book → split into chapters → use clean PDFs → extract text directly → display via RSVP

---

# 🔥 Core Idea

Instead of:

```
PDF → OCR → Regex → Guess structure ❌
```

We use:

```
Clean Chapter PDF → Direct Text Extraction → Word Stream → RSVP Display ✅
```

---

# ⚙️ How the System Works

## 🧩 Backend (Python + Flask)

1. Accepts a **single chapter PDF upload**
2. Uses **PyMuPDF (fitz)** to extract text directly:

   ```python
   page.get_text()
   ```
3. Converts text into:

   * words
   * punctuation tokens
4. Sends word array to frontend via API

---

## 🌐 Frontend (HTML + JavaScript)

1. Uploads PDF to backend
2. Receives word list
3. Displays one word at a time:

   * center-aligned
   * **ORP (Optimal Recognition Point)** highlighted
4. Controls:

   * Start / Pause / Restart
   * Speed slider (100–1000 WPM)
   * Spacebar toggle

---

# 🧠 Why This Approach Works

## ❌ Problems with Previous Approaches

* OCR introduces errors:

  * `No One’s Crazy → N ine’ razy`
* Structure is lost:

  * headings collapse into plain text
* Regex-based chapter detection fails

---

## ✅ Advantages of This System

* Uses **real text (no OCR)**
* No structure guessing required
* Each file = one chapter → simplifies logic
* Fast and reliable
* Scalable for future upgrades

---

# 📁 Project Structure

```
speed_read/
│
├── backend/
│   └── app.py
│
├── frontend/
│   └── index.html
```

---

# 🛠️ Installation Guide

## 🔧 1. Clone the Repository

```bash
git clone <your-repo-url>
cd speed_read
```

---

## 🐍 2. Install Python Dependencies

```bash
pip install flask flask-cors pymupdf
```

---

## 🌐 3. No Frontend Dependencies

Frontend runs using Python’s built-in server.

---

# ▶️ Running the Application

## 1️⃣ Start Backend

```bash
cd backend
python app.py
```

---

## 2️⃣ Start Frontend

```bash
cd frontend
python -m http.server 8000
```

---

## 3️⃣ Open in Browser

```
http://localhost:8000
```

---

# 📖 Usage Instructions

1. Prepare your input:

   * Convert book → split into chapters
   * Ensure PDFs contain **only text (no images)**

2. Upload a chapter PDF

3. Click **Start** or press **Spacebar**

4. Adjust speed using slider (100–1000 WPM)

5. Pause anytime using Spacebar or Pause button

---

# 🎯 Features

* ⚡ High-speed RSVP reading (100–1000 WPM)
* 🎯 ORP-based word highlighting
* ⏯️ Play / Pause / Restart controls
* ⌨️ Spacebar toggle
* 🧼 Clean text processing (no OCR noise)
* 📄 Works with any text-based PDF

---

# ⚠️ Important Notes

* This system assumes:

  > Each PDF contains **one chapter only**

* Scanned/image PDFs will NOT work properly

* If needed:

  * Convert PDF → DOCX → clean → export as PDF again

---

# 🚀 Future Improvements

* 📚 Multi-chapter navigation (auto next file)
* 🧠 Adaptive reading speed (AI pacing)
* 📊 Reading analytics (WPM tracking, retention)
* 📂 Chapter library system
* 🎯 Smart pause logic (based on punctuation)

---

# 🧠 Key Engineering Insight

> **Fix the data, not the logic.**

Instead of building complex OCR + NLP pipelines, we simplified the problem by:

* improving input quality
* reducing ambiguity
* removing unnecessary computation

---

# 👨‍💻 Author

Built as a performance-focused reading tool combining:

* backend text processing
* frontend visualization
* human cognition principles (RSVP)

---

# ⭐ Final Thought

This is not just a reader.

It’s a demonstration of:

> **How simplifying the problem space leads to better systems than over-engineering solutions.**
