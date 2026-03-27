from flask import Flask, request, jsonify
from flask_cors import CORS
import fitz
import re

app = Flask(__name__)
CORS(app)

# ==============================
# EXTRACT WORDS FROM PDF
# ==============================
def extract_words(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")

    full_text = ""

    for page in doc:
        full_text += page.get_text()

    # Convert text into words + punctuation
    words = re.findall(r"\w+|[^\w\s]", full_text)

    return words


# ==============================
# API ROUTE
# ==============================
@app.route("/upload", methods=["POST"])
def upload_pdf():
    try:
        if "file" not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        file = request.files["file"]

        words = extract_words(file)

        print("📄 Total words:", len(words))

        return jsonify(words)

    except Exception as e:
        print("❌ ERROR:", str(e))
        return jsonify({"error": str(e)}), 500


# ==============================
# RUN SERVER
# ==============================
if __name__ == "__main__":
    print("🚀 Server running (single chapter mode)...")
    app.run(debug=True)