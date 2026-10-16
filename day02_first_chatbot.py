
while True:
    message = input("You: ").strip().lower()

    if message == "hello":
        print("Bot: Hi! Nice to meet you.")
    elif message == "how are you":
        print("Bot: I'm doing great! Thanks for asking.")
    elif message == "good morning":
        print("Bot: Good morning! Have a great day.")
    elif message == "what is your name":
        print("Bot: I'm MiniBot, your first AI project!")
    elif message == "thank you":
        print("Bot: You're welcome!")
    elif message == "bye":
        print("Bot: Goodbye! See you again.")
        break
    else:
        print("Bot: Sorry, I don't understand.")
