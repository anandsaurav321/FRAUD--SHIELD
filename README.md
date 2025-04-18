# FraudShield - Real-time Fraud Detection System

FraudShield is a comprehensive fraud detection system that monitors transactions in real-time and sends alerts when suspicious activities are detected. The system uses a combination of email and SMS notifications to ensure timely awareness of potential fraudulent transactions.

## Features

- Real-time transaction monitoring
- Automatic fraud detection
- Instant email alerts
- SMS notifications via Twilio
- Firebase integration for data storage
- Modern web interface for monitoring
- Transaction history tracking

## Tech Stack

- **Backend**: Python
- **Frontend**: HTML, CSS, JavaScript
- **Database**: Firebase Firestore
- **Authentication**: Firebase Authentication
- **Notifications**: 
  - Email (SMTP)
  - SMS (Twilio)

## Prerequisites

- Python 3.x
- Firebase account
- Twilio account
- Gmail account (for email notifications)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/FraudShield.git
cd FraudShield
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
source .venv/bin/activate  # On Unix/MacOS
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure Firebase:
   - Download your Firebase service account key
   - Rename it to `serviceAccountKey.json`
   - Place it in the project root directory

5. Configure Email Settings:
   - Update the email credentials in `alerts.py`
   - Use Gmail App Password for secure authentication

6. Configure Twilio:
   - Update Twilio credentials in `alerts.py`
   - Add your phone number for SMS notifications

## Usage

1. Start the transaction generator:
```bash
python generator.py
```

2. Start the web server:
```bash
python -m http.server 8000
```

3. Access the web interface:
   - Open your browser
   - Navigate to `http://localhost:8000`
   - Use the dashboard to monitor transactions

## Project Structure

```
FraudShield/
├── alerts.py           # Alert handling and notifications
├── generator.py        # Transaction generation
├── serviceAccountKey.json  # Firebase credentials
├── requirements.txt    # Python dependencies
├── js/                 # JavaScript files
│   ├── auth.js        # Authentication handling
│   └── firebase.js    # Firebase configuration
├── images/            # Project images
└── *.html             # Web interface files
```

## Security Considerations

- Never commit `serviceAccountKey.json` to version control
- Use environment variables for sensitive credentials
- Keep your Gmail App Password secure
- Protect your Twilio credentials

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Firebase for real-time database
- Twilio for SMS notifications
- Faker for generating test data #   F R A U D - - S H I E L D  
 