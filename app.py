from flask import Flask, request, render_template
import os
import nltk
from nltk.tokenize import word_tokenize

nltk.data.path.append(os.path.join(os.path.dirname(__file__), "nltk_data"))


app = Flask(__name__)

# --- NEW SMART NLP-BASED RESPONSE LOGIC ---
def chatbot_response(message):
    message = message.lower()
    tokens = word_tokenize(message)

    if any(word in tokens for word in ["hello", "hi", "hey", "greetings"]):
        return "Hello! How can I assist you today?"
    elif "weather" in tokens:
        return "Sure! I heard the weather is nice today!"
    elif "time" in tokens:
        from datetime import datetime
        return f"The current time is {datetime.now().strftime('%H:%M')}."
    elif "joke" in tokens:
        return "Why don't scientists trust atoms? Because they make up everything!"
    elif any(word in tokens for word in ["bye", "goodbye", "see you"]):
        return "Goodbye! Have a nice day!"
    elif any(word in tokens for word in ["how", "are", "you"]):
        return "I'm just a bot, but I'm doing great! How about you?"
    else:
        return "I'm not sure I understand. Could you please rephrase?"

# --- ROUTING ---
@app.route("/", methods=["GET", "POST"])
def home():
    response = ""
    if request.method == "POST":
        user_input = request.form["message"]
        response = chatbot_response(user_input)
    return render_template("index.html", response=response)

# --- HOST SETTINGS FOR RENDER ---
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
