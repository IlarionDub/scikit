
from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

SAVE_FILE = "saved_text.txt"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/text", methods=["GET", "POST"])
def api_text():
    # Повернути збережений текст
    if request.method == "GET":
        if os.path.exists(SAVE_FILE):
            with open(SAVE_FILE, "r", encoding="utf-8") as f:
                text = f.read()
        else:
            text = ""
        return jsonify({"text": text})

    # Зберегти новий текст
    data = request.get_json() or {}
    text = data.get("text", "")

    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        f.write(text)

    return jsonify({"status": "ok"})


if __name__ == "__main__":
    # Локальний запуск
    app.run(host="0.0.0.0", port=5000, debug=True)