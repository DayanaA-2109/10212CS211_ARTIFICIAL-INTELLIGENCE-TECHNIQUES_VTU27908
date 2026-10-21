# Student Information System

studies_in = {
    "Ravi": "CSE",
    "Priya": "ECE",
    "Arun": "IT",
    "Meena": "AIML"
}

student = input("Enter student name: ").strip().title()

if student in studies_in:
    print(student, "studies in", studies_in[student])
else:
    print("Student not found in knowledge base.")
