import spacy

# Load the SpaCy English model
nlp = spacy.load('en_core_web_sm')

# Define FAQs (questions and answers)
faq_data = {
    "What is your return policy?": "Our return policy allows returns within 30 days of purchase.",
    "How can I track my order?": "You can track your order using the tracking link sent to your email.",
    "Do you offer international shipping?": "Yes, we offer international shipping to most countries.",
    "What payment methods do you accept?": "We accept Visa, MasterCard, PayPal, and other major payment methods.",
    "How do I contact customer service?": "You can contact customer service at support@company.com or call us at 123-456-7890."
}

def preprocess(text):
    """Preprocess the user input to convert it into a SpaCy document object."""
    return nlp(text.lower())

def find_best_match(user_input, faq_data):
    """Find the best matching FAQ question using simple similarity."""
    user_doc = preprocess(user_input)
    
    best_match = None
    highest_similarity = 0
    
    # Iterate through all FAQs and calculate similarity
    for question, answer in faq_data.items():
        question_doc = preprocess(question)
        similarity = user_doc.similarity(question_doc)
        
        if similarity > highest_similarity:
            highest_similarity = similarity
            best_match = question
    
    return best_match, highest_similarity

def chatbot():
    print("Welcome to the FAQ chatbot. Ask me anything!")
    
    while True:
        user_input = input("\nYou: ")
        
        # Exit condition
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye!")
            break
        
        # Find the best matching FAQ question
        best_match, similarity = find_best_match(user_input, faq_data)
        
        # If a good match is found, provide the answer
        if similarity > 0.7:  # Threshold for matching
            print(f"Chatbot: {faq_data[best_match]}")
        else:
            print("Chatbot: I'm sorry, I don't understand the question. Please ask something else.")
            
if __name__ == "__main__":
    chatbot()
