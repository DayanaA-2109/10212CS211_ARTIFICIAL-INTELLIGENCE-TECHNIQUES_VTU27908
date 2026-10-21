import re

university_data = {
    "admission": "Admissions are based on eligibility criteria and the university admission process.",
    "fees": "Fee details are available on the official university website.",
    "exams": "Examination timetables are published on the university student portal.",
    "scholarship": "Scholarships are available for eligible students based on university rules."
}

def preprocess(text):
    text = text.lower().strip()
    return re.sub(r"[^a-z0-9\s]", "", text)

def chatbot(query):
    query = preprocess(query)

    if any(word in query for word in ["admission", "admissions", "join"]):
        intent = "admission"
    elif any(word in query for word in ["fee", "fees", "payment"]):
        intent = "fees"
    elif any(word in query for word in ["exam", "exams", "timetable"]):
        intent = "exams"
    elif any(word in query for word in ["scholarship", "scholarships"]):
        intent = "scholarship"
    else:
        return "Sorry, I could not understand your query."

    return university_data[intent]

print("University Enquiry Chatbot")
print("Type 'exit' to stop.")

while True:
    user_input = input("You: ")

    if user_input.lower().strip() == "exit":
        print("Chatbot: Thank you!")
        break

    print("Chatbot:", chatbot(user_input))
