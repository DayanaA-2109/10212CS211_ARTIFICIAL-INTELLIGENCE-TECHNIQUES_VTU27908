import re

healthcare_data = {
    "departments": "Our hospital has Cardiology, Neurology, "
                   "Orthopedics, Pediatrics and General Medicine departments.",
    "timings": "Consultation timings are generally from "
               "9 AM to 5 PM. Please confirm with the hospital.",
    "appointment": "Appointments can be booked through the "
                   "hospital website or registration desk.",
    "emergency": "For a medical emergency, contact local "
                 "emergency services or visit the nearest emergency department."
}

def preprocess(text):
    text = text.lower().strip()
    return re.sub(r"[^a-z0-9\s]", "", text)

def chatbot(query):
    query = preprocess(query)

    if any(word in query for word in
           ["department", "departments", "specialist", "doctor"]):
        intent = "departments"
    elif any(word in query for word in
             ["timing", "timings", "hours", "open"]):
        intent = "timings"
    elif any(word in query for word in
             ["appointment", "book", "booking"]):
        intent = "appointment"
    elif any(word in query for word in
             ["emergency", "urgent"]):
        intent = "emergency"
    else:
        return "Sorry, I could not understand your query."

    return healthcare_data[intent]

print("Healthcare Information Chatbot")
print("Type 'exit' to stop.")

while True:
    user_input = input("You: ")

    if user_input.lower().strip() == "exit":
        print("Chatbot: Thank you!")
        break

    print("Chatbot:", chatbot(user_input))
