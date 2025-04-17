import smtplib
from email.message import EmailMessage
from twilio.rest import Client
from datetime import datetime
import pytz
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ---- Email Setup ----
EMAIL_ADDRESS = "gkc1764@gmail.com"  # Your email address
EMAIL_PASSWORD = "dgjx fllm zjgq bjxj"  # You'll need to generate an App Password from Google Account settings
TEST_EMAIL_RECIPIENT = "gkc1764@gmail.com"  # Updated recipient email

# ---- Twilio Setup ----
TWILIO_SID = os.getenv('TWILIO_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE = os.getenv('TWILIO_PHONE')
RECIPIENT_PHONE = "+919350475758"  # Your phone number with country code

def format_amount(amount):
    """Format amount in Indian currency format"""
    amount_str = f"{amount:,.2f}"
    parts = amount_str.split('.')
    parts[0] = parts[0].replace(',', '_')  # Temporary replacement
    parts[0] = parts[0][::-1].replace('_', ',', 2)[::-1]  # Indian number system
    parts[0] = parts[0].replace('_', ',')  # Restore other commas
    return f"₹{parts[0]}.{parts[1]}"

def send_email_alert(transaction):
    msg = EmailMessage()
    msg['Subject'] = 'Fraud Alert: Suspicious Transaction Detected'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS

    content = f"""
    Fraud Alert!
    
    A suspicious transaction has been detected:
    
    Amount: ₹{transaction['amount']}
    Location: {transaction['location']}
    Time: {transaction['timestamp']}
    
    Please review this transaction immediately.
    """
    
    msg.set_content(content)
    
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        print("Email alert sent successfully!")
    except Exception as e:
        print(f"Failed to send email alert: {e}")

def send_sms_alert(transaction):
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    
    message = f"""
    Fraud Alert!
    Amount: ₹{transaction['amount']}
    Location: {transaction['location']}
    Time: {transaction['timestamp']}
    """
    
    try:
        message = client.messages.create(
            body=message,
            from_=TWILIO_PHONE,
            to=RECIPIENT_PHONE
        )
        print(f"SMS alert sent successfully! SID: {message.sid}")
    except Exception as e:
        print(f"Failed to send SMS alert: {e}")

def send_alert(transaction):
    if transaction['is_fraud']:
        send_email_alert(transaction)
        send_sms_alert(transaction)

# Test function
def test_alerts():
    ist = pytz.timezone('Asia/Kolkata')
    current_time = datetime.now(ist)
    
    test_transaction = {
        "user_email": TEST_EMAIL_RECIPIENT,
        "amount": 245999.99,  # ₹2,45,999.99
        "location": "New Delhi, India",
        "timestamp": current_time.strftime("%Y-%m-%d %I:%M:%S %p IST"),
        "currency": "INR",
        "is_fraud": True
    }
    
    print("Testing email alert...")
    send_email_alert(test_transaction)
    
    print("\nTesting SMS alert...")
    send_sms_alert(test_transaction)

if __name__ == "__main__":
    test_alerts()
