import nltk
import spacy
from nltk.chat.util import Chat, reflections

# Download necessary NLTK datasets
nltk.download('punkt')
nltk.download('wordnet')

# Initialize spaCy NLP model (English)
nlp = spacy.load('en_core_web_sm')

# Define chatbot conversation rules with NLTK
pairs = [
    ['hi|hello|hey', ['Hello! How can I assist you today?']],
    ['what is your name?', ['I am your customer support assistant.']],
    ['(.*) problem (.*)', ['I can help with technical support. What seems to be the issue?']],
    ['(.*) refund (.*)', ['I can assist you with a refund request. What is your order number?']],
    ['(.*) payment (.*)', ['Please clarify the payment issue you are facing, and I will help.']],
    ['(.*) shipping (.*)', ['You can track your order on our website. Would you like the tracking link?']],
    ['bye', ['Goodbye! Feel free to contact us again if you need any further assistance.']]
]

# NLTK Chat instance for basic responses
chatbot = Chat(pairs, reflections)

def get_response(user_input):
    """Process user input and return a response using both NLTK and spaCy."""
    if any(greeting in user_input.lower() for greeting in ['hi', 'hello', 'hey']):
        return chatbot.respond(user_input)

    doc = nlp(user_input)  # Process the input with spaCy

    if 'help' in user_input.lower():
        return "How can I assist you with your issue?"
    elif 'problem' in user_input.lower():
        return "I see you are facing an issue. Could you describe it in more detail?"
    elif 'refund' in user_input.lower():
        return "Please provide your order number, and I will process your refund request."
    elif 'payment' in user_input.lower():
        return "Let me help you with your payment issue. Could you provide more details?"
    elif 'shipping' in user_input.lower():
        return "I can assist you with tracking your shipment. Do you need a tracking link?"

    # Default fallback response if no matching pattern is found
    return "I'm not sure how to help with that. Can you please provide more details?"
