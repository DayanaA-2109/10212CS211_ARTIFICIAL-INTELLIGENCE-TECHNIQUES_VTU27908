# Library Knowledge Base

written_by = {
    "Python Basics": "John",
    "Ai Fundamentals": "David",
    "Data Science": "Anita",
    "Machine Learning": "Robert"
}

book = input("Enter book title: ").strip().title()

if book in written_by:
    print(book, "was written by", written_by[book])
else:
    print("Book not found in knowledge base.")
