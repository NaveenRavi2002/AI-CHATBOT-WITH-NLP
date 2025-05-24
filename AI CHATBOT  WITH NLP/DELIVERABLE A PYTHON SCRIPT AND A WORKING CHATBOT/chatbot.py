import spacy

def load_nlp_model():
    print("Loading spaCy model (this may take a moment)...")
    return spacy.load("en_core_web_md")

# Knowledge base with questions and answers
FAQ_KNOWLEDGE_BASE = [
    ("What is your name?", "I am a spaCy chatbot."),
    ("How are you?", "I'm doing well, thank you! How can I help you?"),
    ("What can you do?", "I can answer your questions based on my knowledge base."),
    ("Tell me about AI.", "Artificial Intelligence is the simulation of human intelligence in machines."),
    ("What is NLP?", "NLP stands for Natural Language Processing, a field of AI."),
    ("Who created you?", "I was created by a Python developer using spaCy."),
    ("Goodbye", "Goodbye! Have a great day."),
]

def find_best_answer(user_question, nlp, kb=FAQ_KNOWLEDGE_BASE, threshold=0.7):
    user_doc = nlp(user_question)
    best_answer = "Sorry, I don't understand your question."
    max_similarity = 0.0

    for question, answer in kb:
        question_doc = nlp(question)
        similarity = user_doc.similarity(question_doc)
        # print(f"Debug similarity between '{user_question}' and '{question}': {similarity:.2f}")  # Uncomment to debug
        if similarity > max_similarity and similarity > threshold:
            max_similarity = similarity
            best_answer = answer
    return best_answer

def chatbot():
    nlp = load_nlp_model()
    print("Hi! Ask me anything. Type 'exit' or 'quit' to stop.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("ChatBot: Goodbye!")
            break
        answer = find_best_answer(user_input, nlp)
        print("ChatBot:", answer)

if __name__ == "__main__":
    chatbot()
