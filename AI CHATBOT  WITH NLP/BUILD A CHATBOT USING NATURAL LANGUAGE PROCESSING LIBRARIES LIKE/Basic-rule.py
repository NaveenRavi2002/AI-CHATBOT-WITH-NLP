import nltk
from nltk.chat.util import Chat, reflections

# Pairs of patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you?"]
    ],
    [
        r"what is your name ?",
        ["My name is ChatBot.", "I'm ChatBot."]
    ],
    [
        r"how are you ?",
        ["I'm fine, thank you!", "Doing well, how about you?"]
    ],
    [
        r"sorry (.*)",
        ["No problem", "Don't worry about it"]
    ],
    [
        r"quit",
        ["Bye-bye! Take care.", "Goodbye!"]
    ],
    [
        r"(.*) help (.*)",
        ["I can help you. What do you need?"]
    ],
    [
        r"(.*) your name ?",
        ["I'm ChatBot, your assistant."]
    ],
    [
        r"(.*) weather (.*)",
        ["I'm not sure about the weather, but you can check a weather website."]
    ],
    [
        r"(.*)",
        ["Sorry, I don't understand that.", "Can you say that differently?"]
    ]
]

def chatbot():
    print("Hi, I'm ChatBot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
