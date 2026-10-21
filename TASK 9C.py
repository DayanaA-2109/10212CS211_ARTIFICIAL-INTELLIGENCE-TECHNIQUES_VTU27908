import re

support_data = {
    "order": "You can track your order using the tracking "
             "link in your order confirmation message.",
    "product": "Product specifications are available on the "
               "respective product details page.",
    "return": "You can request a return through the Orders "
              "section, subject to the return policy.",
    "refund": "Refunds are processed after the returned item "
              "is verified, according to the refund policy."
}

def preprocess(text):
    text = text.lower().strip()
    return re.sub(r"[^a-z0-9\s]", "", text)

def chatbot(query):
    query = preprocess(query)

    if any(word in query for word in
           ["order", "track", "tracking", "delivery"]):
        intent = "order"
    elif any(word in query for word in
             ["product", "specification", "features", "details"]):
        intent = "product"
    elif any(word in query for word in
             ["return", "replace", "replacement"]):
        intent = "return"
    elif any(word in query for word in
             ["refund", "money back", "reimbursement"]):
        intent = "refund"
    else:
        return "Sorry, I could not understand your query."

    return support_data[intent]

print("E-Commerce Customer Support Chatbot")
print("Type 'exit' to stop.")

while True:
    user_input = input("You: ")

    if user_input.lower().strip() == "exit":
        print("Chatbot: Thank you for contacting support!")
        break

    print("Chatbot:", chatbot(user_input))
