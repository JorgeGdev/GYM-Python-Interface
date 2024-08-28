import sqlite3
import random


conn = sqlite3.connect("gym_database.db")
cursor = conn.cursor()


first_names = ["John", "Jane", "Alex", "Chris", "Katie", "David", "Laura", "Michael", "Emma", "Daniel", "Sophia", "James", "Olivia", "Benjamin", "Isabella", "Liam", "Mia", "Noah", "Charlotte", "Ethan", "Amelia", "Lucas", "Ava", "Mason", "Harper"]
last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson", "Clark", "Rodriguez", "Lewis", "Lee", "Walker"]


membership_types = ["Basic", "Regular", "Premium"]
membership_durations = ["3 Months", "6 Months", "12 Months", "24 Months"]
payment_frequencies = ["Weekly", "Monthly"]


def generate_phone_number():
    return f"555-{random.randint(1000, 9999)}"


def generate_address():
    streets = ["Main St", "High St", "Maple Ave", "Oak St", "Pine St", "Cedar St", "Elm St", "Washington St", "Lake St", "Hill St"]
    return f"{random.randint(1, 999)} {random.choice(streets)}"


for _ in range(43):  
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    address = generate_address()
    mobile = generate_phone_number()
    membership_type = random.choice(membership_types)
    membership_duration = random.choice(membership_durations)
    direct_debit = random.choice([0, 1])
    extra_1 = random.choice([0, 1])
    extra_2 = random.choice([0, 1])
    extra_3 = random.choice([0, 1])
    extra_4 = random.choice([0, 1])
    payment_frequency = random.choice(payment_frequencies)

    cursor.execute('''INSERT INTO Memberships (First_Name, Last_Name, Address, Mobile, Membership_Type, Membership_Duration, Direct_Debit, Extra_1, Extra_2, Extra_3, Extra_4, Payment_Frequency)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   (first_name, last_name, address, mobile, membership_type, membership_duration, direct_debit, extra_1, extra_2, extra_3, extra_4, payment_frequency))


conn.commit()
conn.close()
