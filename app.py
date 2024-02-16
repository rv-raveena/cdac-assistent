from flask import Flask, render_template, request, jsonify
from autocorrect import Speller  # Import the autocorrect library

app = Flask(__name__)

# Assuming you have a chatbot function in chat.py
from chat import chatbot

# Initialize the Speller from autocorrect
spell = Speller()

@app.route("/")
def hello():
    return render_template('chat.html')

@app.route("/ask", methods=['POST'])
def ask():
    message = str(request.form['messageText'])

    # Use autocorrect for spelling correction in the message
    corrected_message = spell(message)

    # Use the corrected message in the chatbot function
    bot_response = chatbot(corrected_message)

    return jsonify({'status': 'OK', 'answer': bot_response})

@app.route("/search", methods=['POST'])
def search():
    query_text = str(request.form['queryText'])

    # Use autocorrect for spelling correction in the query
    corrected_query = spell(query_text)

    return jsonify({'status': 'OK', 'corrected_query': corrected_query})

if __name__ == "__main__":
    app.run(debug=True)
