from flask import Flask, request, render_template
import os

app = Flask(__name__)

def chatbot_response(message):
    message = message.lower()
    if "hello" in message or "hi" in message:
        return "Hello! How can I assist you today?"
    elif "weather" in message:
        return "I heard the weather is nice today!"
    elif "how are you" in message:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif "bye" in message or "goodbye" in message:
        return "Goodbye! Have a nice day!"
    else:
        return "I'm sorry, I didn't understand that. Could you please rephrase?"

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
