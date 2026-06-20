responses = {
    "hello": "Hi! Nice to meet you.",
    "how are you": "I am fine. Thank you!",
    "what is ai": "AI stands for Artificial Intelligence.",
    "python": "Python is a popular programming language.",
    "machine learning": "Machine Learning allows computers to learn from data."
}

print("🤖 AI Chatbot")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user == "bye":
        print("Bot: Goodbye!")
        break

    print("Bot:", responses.get(user, "Sorry, I don't understand."))