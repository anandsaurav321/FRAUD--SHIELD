import firebase_admin
from firebase_admin import credentials, firestore
from faker import Faker
import random
import time
from datetime import datetime
from alerts import send_sms_alert, send_email_alert  # We'll create this next
import pytz  # For timezone handling

# Initialize Firebase Admin
cred = credentials.Certificate("serviceAccountKey.json")  # Download this from Firebase project settings
firebase_admin.initialize_app(cred)
db = firestore.client()

fake = Faker()
ist = pytz.timezone('Asia/Kolkata')  # Indian Standard Time

def generate_transaction():
    # Convert to IST
    current_time = datetime.now(ist)
    
    return {
        "user_email": fake.email(),
        "amount": round(random.uniform(1000, 500000), 2),  # Amount in INR (₹1000 to ₹500000)
        "location": fake.city() + ", India",  # Indian cities
        "timestamp": current_time.strftime("%Y-%m-%d %I:%M:%S %p IST"),
        "currency": "INR",
        "is_fraud": random.choices([False, True], weights=[85, 15])[0]  # 15% fraud
    }

def push_transaction():
    transaction = generate_transaction()
    doc_ref = db.collection("transactions").document()
    doc_ref.set(transaction)
    print("Transaction sent:", transaction)

    if transaction["is_fraud"]:
        send_sms_alert(transaction)
        send_email_alert(transaction)

if __name__ == "__main__":
    print("Starting transaction stream...")
    while True:
        push_transaction()
        time.sleep(random.randint(3, 6))  # Every 3–6 seconds
