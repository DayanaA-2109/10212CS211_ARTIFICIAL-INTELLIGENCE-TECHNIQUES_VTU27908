# Hospital Information System

specializes_in = {
    "Dr Ravi": "Cardiology",
    "Dr Priya": "Neurology",
    "Dr Kumar": "Cardiology",
    "Dr Meena": "Pediatrics"
}

specialization = input(
    "Enter medical specialization: "
).strip().title()

found = False

for doctor, field in specializes_in.items():
    if field.lower() == specialization.lower():
        print(doctor, "specializes in", field)
        found = True

if not found:
    print("No doctor found for this specialization.")
