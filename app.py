from flask import Flask, render_template, request
from chatbot_logic import get_response  # Import the chatbot logic

app = Flask(__name__)

@app.route('/')
def home():
    """Render the chatbot home page."""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Process the user input and return the chatbot's response."""
    user_input = request.form['message']
    response = get_response(user_input)
    return response

if __name__ == "__main__":
    app.run(debug=True)
