from flask import Flask, request, render_template, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key
api_key = "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"
openai.api_key = api_key

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate_sayri", methods=["POST"])
def generate_sayri():
    try:
        prompt = request.form.get("prompt")
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=50,
            n=1,
        )
        generated_sayri = response.choices[0].text.strip()
        return jsonify/({"generated_sayri": generated_sayri})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
