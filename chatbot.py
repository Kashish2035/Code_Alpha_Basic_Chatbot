import datetime

def chatbot_reply(user_input):
    user_input = user_input.lower()

    # -------------------------
    # 1. Greetings
    # -------------------------
    if user_input in ["hello", "hi", "hey", "hii", "hello!"]:
        return "Hello! How can I assist you today?"

    # -------------------------
    # 2. Asking chatbot's name
    # -------------------------
    elif user_input in ["what is your name", "who are you"]:
        return "I'm your friendly rule-based chatbot!"

    # -------------------------
       # 3. Asking chatbot's age
    # -------------------------
    elif user_input in ["how old are you", "your age"]:
        return "I don’t have an age, but I'm always learning!"

    # -------------------------
    # 4. Gratitude replies
    # -------------------------
    elif user_input in ["thank you", "thanks", "thanks!"]:
        return "You're welcome! 😊"

    # -------------------------
    # 5. Emotional responses
    # -------------------------
    elif user_input in ["i am sad", "i am upset", "feeling sad"]:
        return "I'm really sorry to hear that. I'm here for you. ❤️"

    elif user_input in ["i am happy", "feeling good", "i am excited"]:
        return "That's awesome! Keep spreading positivity! 😄"

    # -------------------------
    # 6. Asking about the user's day
    # -------------------------
    elif user_input in ["how was your day", "how are you doing"]:
        return "I'm doing great! How about you?"

    # -------------------------
    # 7. Simple jokes
    # -------------------------
    elif user_input in ["tell me a joke", "joke"]:
        return "Why don’t programmers like nature? Too many bugs! 😂"

    elif user_input == "another joke":
        return "What do computers eat for a snack? Microchips! 😄"

    # -------------------------
    # 8. Weather-type response
    # -------------------------
    elif user_input in ["what is the weather", "weather"]:
        return "I can't check actual weather, but I hope it's a bright and beautiful day!"

    # -------------------------
    # 9. Date & Time
    # -------------------------
    elif user_input in ["what is the time", "time"]:
        return f"The current time is: {datetime.datetime.now().strftime('%I:%M %p')}"

    elif user_input in ["what is today's date", "date"]:
        return f"Today's date is: {datetime.date.today()}"

    # -------------------------
    # 10. Simple Math
    # -------------------------
    elif user_input.startswith("calculate"):
        try:
            expression = user_input.replace("calculate", "").strip()
            answer = eval(expression)
            return f"The answer is {answer}"
        except:
            return "Hmm, I couldn't calculate that. Try something simple like: calculate 5+3"

    # -------------------------
    # 11. About food, hobbies, places
    # -------------------------
    elif user_input in ["what is your favourite food", "favorite food"]:
        return "I don't eat, but I heard pizza is awesome! 🍕"

    elif user_input in ["what are your hobbies", "your hobbies"]:
        return "I enjoy chatting and helping you out!"

    elif user_input in ["where are you from"]:
        return "I live inside your computer! 😄"

    # -------------------------
    # 12. Asking for help
    # -------------------------
    elif user_input in ["help", "what can you do"]:
        return ("I can chat with you, tell jokes, calculate simple math, "
                "give date & time, and respond to basic questions!")

    # -------------------------
    # 13. Goodbye messages
    # -------------------------
    elif user_input in ["bye", "goodbye", "see you"]:
        return "Goodbye! Take care and see you soon!"

    # -------------------------
    # 14. Improved fallback message
    # -------------------------
    else:
        return "Hmm, I didn't quite understand that. Could you rephrase it?"

# -------------------------
# Main Chat Loop
# -------------------------
print("Chatbot: Hello! Type 'bye' to exit the chat.")

while True:
    user = input("You: ")
    response = chatbot_reply(user)
    print("Chatbot:", response)

    if user.lower() in ["bye", "goodbye", "see you"]:
        break
