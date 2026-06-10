print("=== RMIT Student Assistant Chatbot ===")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hello! Welcome to RMIT Student Assistant.")
    
    elif "study" in user:
        print("Bot: Create a study schedule and revise regularly.")

    elif "exam" in user:
        print("Bot: Practice past papers and revise key concepts.")

    elif "assignment" in user:
        print("Bot: Start early and break the work into smaller tasks.")

    elif "internship" in user:
        print("Bot: Build projects, maintain GitHub, and apply through Seek and LinkedIn.")

    elif user == "bye":
        print("Bot: Goodbye! Have a great day.")
        break

    else:
        print("Bot: Sorry, I don't understand that question.")
