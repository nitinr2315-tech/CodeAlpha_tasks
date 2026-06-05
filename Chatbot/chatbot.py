# ==========================================
# BASIC CHATBOT - RULE BASED CHATBOT
# ==========================================

# Predefined responses stored in a dictionary
responses = {
    "hello": "👋 Hi!",
    "hi": "😊 Hello there!",
    "how are you": "😄 I'm fine, thanks!",
    "what is your name": "🤖 My name is BasicBot.",
    "who made you": "👨‍💻 I was created using Python.",
    "thank you": "🙏 You're welcome!",
    "bye": "👋 Goodbye! Have a great day!",
}

# Function to get chatbot response
def get_response(user_input):
    user_input = user_input.lower().strip()

    # Exact match responses
    if user_input in responses:
        return responses[user_input]

    # Keyword matching
    elif "joke" in user_input:
        return "😂 Why do programmers prefer dark mode? Because light attracts bugs!"

    elif "python" in user_input:
        return "🐍 Python is a powerful and beginner-friendly programming language."

    elif "help" in user_input:
        return "💡 You can ask me things like: hello, how are you, joke, python, bye."

    elif user_input == "":
        return "⚠️ Please type something."

    else:
        return "🤔 Sorry, I don't understand that."

# Function to run chatbot
def run_chatbot():
    print("=" * 50)
    print("🤖 BASIC CHATBOT")
    print("Type 'bye', 'quit', or 'exit' to stop.")
    print("=" * 50)

    while True:
        user_input = input("\nYou: ")

        # Exit conditions
        if user_input.lower().strip() in ["bye", "quit", "exit"]:
            print("Bot: 👋 Goodbye! Have a great day!")
            break

        response = get_response(user_input)
        print("Bot:", response)

# Start chatbot
if __name__ == "__main__":
    run_chatbot()