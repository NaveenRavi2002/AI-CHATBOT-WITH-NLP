import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import nltk
nltk.download('punkt')

# Training data - inputs and their corresponding intent labels
training_data = [
    ("Hello", "greeting"),
    ("Hi there", "greeting"),
    ("Hey", "greeting"),
    ("How are you?", "greeting"),
    ("What is your name?", "name"),
    ("Who are you?", "name"),
    ("Tell me your name", "name"),
    ("Bye", "bye"),
    ("Goodbye", "bye"),
    ("See you later", "bye"),
    ("Help me", "help"),
    ("Can you assist me?", "help"),
    ("I need help", "help"),
    ("What is the weather like?", "weather"),
    ("Tell me about the weather", "weather"),
]

# Responses for each intent
responses = {
    "greeting": ["Hello!", "Hi there!", "Hey!"],
    "name": ["I'm ChatBot.", "They call me ChatBot."],
    "bye": ["Goodbye!", "See you later!"],
    "help": ["How can I help you?", "What do you need assistance with?"],
    "weather": ["Sorry, I can't check the weather yet.", "Try looking outside!"],
    "default": ["Sorry, I don't understand.", "Can you rephrase?"]
}

# Prepare data
X_train = [item[0].lower() for item in training_data]
y_train = [item[1] for item in training_data]

# Vectorizer and classifier
vectorizer = CountVectorizer()
X_train_vectors = vectorizer.fit_transform(X_train)

classifier = LogisticRegression()
classifier.fit(X_train_vectors, y_train)

def predict_intent(text):
    text_vector = vectorizer.transform([text.lower()])
    intent = classifier.predict(text_vector)[0]
    return intent

def get_response(intent):
    if intent in responses:
        return random.choice(responses[intent])
    else:
        return random.choice(responses["default"])

def chatbot():
    print("Hi! I'm a simple ML chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("ChatBot: Goodbye!")
            break
        intent = predict_intent(user_input)
        reply = get_response(intent)
        print("ChatBot:", reply)

if __name__ == "__main__":
    chatbot()
