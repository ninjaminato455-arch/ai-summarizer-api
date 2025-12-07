from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "API résumé en ligne !"

@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.get_json() or {}
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "Aucun texte fourni."}), 400

    # Résumé ultra-simple (première phrase)
    sentences = [s.strip() for s in text.split(".") if s.strip()]
    summary = sentences[0] + "." if sentences else text

    return jsonify({"summary": summary})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
