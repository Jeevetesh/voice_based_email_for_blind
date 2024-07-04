
# Voice_Based_Email_System_For_Blind

## Application for the Visually Impaired

## Overview
This project is a voice-based email application designed specifically for visually impaired users. The application utilizes speech recognition and text-to-speech technologies to provide a hands-free email experience, allowing users to compose and check emails using voice commands.
## Features
Voice Commands: Users can navigate the application using voice commands, making it accessible for those with visual impairments.
Compose Emails: Dictate your email message and specify the recipient email address through voice commands.
Check Inbox: Listen to the number of unread emails and the details of the latest emails, including the sender and the subject.
Text-to-Speech: The application reads out prompts, options, and email contents to the user, ensuring a seamless interaction without needing to look at the screen.

## Documentation
### Installation

Prerequisites
Before installing the application, make sure you have the following prerequisites:

* Python 3.6 or higher
* Required Python packages: You can install these using the provided requirements.txt file.

#### Steps to Install
1. Clone the Repository:
```bash
git clone https://github.com/yourusername/voice-based-email-app.git
```
2. Navigate to the Project Directory:
```bash
cd voice-based-email-app
```
3. Install the Required Packages: 
```bash
pip install -r requirements.txt
```
### Configuration
Before running the application, you need to configure your email credentials. Open the vbes.py file and update the following lines with your email credentials:
```bash
# Replace with your email and app-specific password
mail.login('your_email@gmail.com', 'your_app_password')  # Login part
```
### Usage
1. Run the Application:
```bash
python vbes.py
```
2. Follow the Voice Prompts:
* The application will greet you and present options to either compose a new email or check your inbox.
* Speak your choice (e.g., "one" for composing an email, "two" for checking your inbox).
#### Composing an Email
* Step 1: After selecting the option to compose an email, the application will prompt you to dictate your message.
* Step 2: Next, you will be prompted to provide the recipient's email address. Speak the email address clearly.
* Step 3: The application will confirm the message and recipient, then send the email.
#### Checking Your Inbox
* Step 1: After selecting the option to check your inbox, the application will tell you the number of unread emails.
* Step 2: It will read out the details of the latest emails, including the sender and the subject.
* Step 3: The body of the email will also be read aloud if you choose to hear it.
### Troubleshooting
#### If you encounter issues, consider the following:
* Audio Input/Output: Ensure your microphone and speakers are working properly.
* Email Credentials: Double-check your email credentials and app-specific password.
* Python Dependencies: Make sure all required Python packages are installed correctly.
* Network Connection: Ensure you have an active internet connection.
### Contributing
We welcome contributions! If you have suggestions for improvements or find any issues, please submit a pull request or open an issue in the repository.

