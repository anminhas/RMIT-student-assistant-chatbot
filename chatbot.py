print("🤖 RMIT Student Assistant Chatbot")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user in ["hello", "hi", "hey"]:
        print("Bot: Hello! How can I help you today?")

    elif "study" in user:
        print("Bot: Create a study schedule and revise consistently.")

    elif "exam" in user:
        print("Bot: Practice past papers and focus on key concepts.")

    elif "assignment" in user:
        print("Bot: Start early and break large tasks into smaller steps.")

    elif "internship" in user:
        print("Bot: Build projects, maintain GitHub, and apply through LinkedIn, Seek, and GradConnection.")

    elif "rmit" in user:
        print("Bot: RMIT University is known for industry-focused learning and strong technology programs.")

    elif "ai" in user:
        print("Bot: AI stands for Artificial Intelligence. Learning Python and Machine Learning is a great start.")

    elif "software engineering" in user:
        print("Bot: Software Engineering focuses on designing, building, testing, and maintaining software systems.")

    elif "github" in user:
        print("Bot: GitHub helps you store code, collaborate on projects, and showcase your work to employers.")

    elif user == "bye":
        print("Bot: Goodbye! Good luck with your studies and career.")
        break

    else:
        print("Bot: Sorry, I don't understand that question.")
