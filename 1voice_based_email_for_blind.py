import os
import time
import smtplib
import email
import imaplib
from bs4 import BeautifulSoup
import pyglet
from gtts import gTTS
import speech_recognition as sr
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import pyaudio

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")
        label = Label(text="Welcome to my app!")
        button = Button(text="Click me", on_release=self.button_clicked)
        layout.add_widget(label)
        layout.add_widget(button)
        return layout

    def button_clicked(self, *args):
        # Your code to handle the button click event goes here
        pass

def speak(text):
    tts = gTTS(text, lang='en')
    ttsname = "name.mp3"
    tts.save(ttsname)

    music = pyglet.media.load(ttsname, streaming=False)
    music.play()

    time.sleep(music.duration)
    os.remove(ttsname)

if __name__ == "__main__":
    # Fetch project name
    speak("Project: Voice based Email for blind")

    # Login from os
    login = os.getlogin()
    print("You are logging from: " + login)

    # Choices
    print("1. Compose a mail.")
    speak("Option 1. Compose a mail.")

    print("2. Check your inbox")
    speak("Option 2. Check your inbox")

    # This is for input choices
    speak("Your choice")

    # Voice recognition part
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Your choice:")
            audio = r.listen(source)
            text = r.recognize_google(audio).lower()
            print("Did you say " + text)
    except sr.UnknownValueError:
        print("Unknown error occurred")
        text = None
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        text = None

    # Choices details
    if text in ['1', 'one', 'option one', 'option 1']:
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Your message:")
                speak("Your message:")
                audio = r.listen(source)
                msg = r.recognize_google(audio).lower()
                speak("ok done!")
                print("Your message: " + msg)
                speak("Your message: " + msg)

                speak("victim id")
                print("victim id:")
                test = r.listen(source)
                Vic_id = r.recognize_google(test).lower().replace(" ", "")
                speak("ok done! victim id: " + Vic_id)
                print("ok done! victim id: " + Vic_id)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio.")
            Vic_id = None
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            Vic_id = None

        if Vic_id and msg:
            try:
                mail = smtplib.SMTP('smtp.gmail.com', 587)  # host and port area
                mail.ehlo()  # Hostname to send for this command defaults to the FQDN of the local host.
                mail.starttls()  # Security connection
                mail.login('jeeveteshbhanot163@gmail.com', 'pkvjhuaaybdoptzj')  # Login part
                mail.sendmail('jeeveteshbhanot163@gmail.com', Vic_id, msg)  # Send part
                print("Congrats! Your mail has been sent.")
                speak("Congrats! Your mail has been sent.")
                mail.close()
            except Exception as e:
                print(f"An error occurred while sending the email: {e}")
        else:
            speak("Failed to get victim id or message.")

    elif text in ['2', 'two', 'option two', 'option 2']:
        try:
            mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)  # This is host and port area.... SSL security
            unm = 'jeeveteshbhanot163@gmail.com'  # Username
            psw = 'yabpqdujuhyxwhxc'  # Password
            mail.login(unm, psw)  # Login
            stat, total = mail.select('Inbox')  # Total number of mails in inbox
            print("Number of mails in your inbox: " + str(total[0]))
            speak("Total mails are: " + str(total[0]))

            # Unseen mails
            unseen = mail.search(None, 'UnSeen')  # Unseen count
            unseen_count = len(unseen[1][0].split())
            print("Number of UnSeen mails: " + str(unseen_count))
            speak("Your Unseen mail: " + str(unseen_count))

            # Search mails
            result, data = mail.uid('search', None, "ALL")
            inbox_item_list = data[0].split()
            new = inbox_item_list[-1]
            old = inbox_item_list[0]
            result2, email_data = mail.uid('fetch', new, '(RFC822)')  # Fetch
            raw_email = email_data[0][1].decode("utf-8")  # Decode
            email_message = email.message_from_string(raw_email)
            print("From: " + email_message['From'])
            print("Subject: " + str(email_message['Subject']))
            speak("From: " + email_message['From'] + " And Your subject: " + str(email_message['Subject']))

            # Body part of mails
            stat, total1 = mail.select('Inbox')
            stat, data1 = mail.fetch(total1[0], "(UID BODY[TEXT])")
            msg = data1[0][1]
            soup = BeautifulSoup(msg, "html.parser")
            txt = soup.get_text()
            print("Body: " + txt)
            speak("Body: " + txt)

            mail.close()
            mail.logout()
        except Exception as e:
            print(f"An error occurred while accessing the inbox: {e}")

    else:
        speak("Unknown error: Choice not satisfied")

    MyApp().run()
