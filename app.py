from flask import Flask, request, render_template
import openai
import os

# 🔐 REPLACE this with your actual key or use environment variable
openai.api_key = os.environ.get("OPENAI_API_KEY")

app = Flask(__name__)

def chatbot_response(message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message}
            ],
            temperature=0.7,
            max_tokens=300
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Sorry, something went wrong: {str(e)}"

@app.route("/", methods=["GET", "POST"])
def home():
    response = ""
    if request.method == "POST":
        user_input = request.form["message"]
        response = chatbot_response(user_input)
    return render_template("index.html", response=response)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
