import spacy

# Load the medium English model with word vectors
nlp = spacy.load("en_core_web_md")

# FAQ knowledge base: list of (question, answer) tuples
faq_knowledge_base = [
    ("What is your name?", "I am a spaCy chatbot."),
    ("How are you?", "I'm doing well, thank you! How can I help you?"),
    ("What can you do?", "I can answer your questions based on my knowledge base."),
    ("Tell me about AI.", "Artificial Intelligence is the simulation of human intelligence in machines."),
    ("What is NLP?", "NLP stands for Natural Language Processing, a field of AI."),
    ("Who created you?", "I was created by a Python developer using spaCy."),
    ("Goodbye", "Goodbye! Have a great day."),
]

def find_best_answer(user_question, kb=faq_knowledge_base, threshold=0.7):
    user_doc = nlp(user_question)
    best_answer = "Sorry, I don't understand your question."
    max_similarity = 0.0
    
    for question, answer in kb:
        question_doc = nlp(question)
        similarity = user_doc.similarity(question_doc)
        if similarity > max_similarity and similarity > threshold:
            max_similarity = similarity
            best_answer = answer
    return best_answer

def chatbot():
    print("Hi! Ask me anything. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("ChatBot: Goodbye!")
            break
        answer = find_best_answer(user_input)
        print("ChatBot:", answer)

if __name__ == "__main__":
    chatbot()
