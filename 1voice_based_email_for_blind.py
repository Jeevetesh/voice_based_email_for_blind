import speech_recognition as sr
import smtplib
# import pyaudio
# import platform
# import sys
from bs4 import BeautifulSoup
import email
import imaplib
from gtts import gTTS
import pyglet
import os, time
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


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
if __name__ == "__main__":
    



    def speak(text):
        tts = gTTS(text, lang='en')
        ttsname=("name.mp3") #Example: path -> C:\Users\dell\Desktop> just change with your desktop directory. Don't use my directory.
        tts.save(ttsname)
        
        music = pyglet.media.load(ttsname, streaming = False)
        music.play()

        time.sleep(music.duration)
        os.remove(ttsname)


    #fetch project name
    speak("Project: Voice based Email for blind")


    #login from os
    login = os.getlogin
    print ("You are logging from : "+login())

    #choices
    print ("1. composed a mail.")
    speak("option 1. composed a mail.")


    print ("2. Check your inbox")
    speak("option 2. Check your inbox")


    #this is for input choices
    speak("Your choice")


    #voice recognition part
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            # r.adjust_for_ambient_noise(source, duration=0.
            print ("Your choice:") 

            audio=r.listen(source)
            
            text=r.recognize_google(audio)
            text = text.lower()
            print("Did you say "+text)

    except sr.UnknownValueError  :
        print("unknown error occurred")
        
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e)) 



    #choices details
    if text == '1' or text == 'One' or text == 'one' or text == "option one" or text=="option 1":
        r = sr.Recognizer() #recognize
        try:
            with sr.Microphone() as source:
                print("Your message :")
                speak("Your message :")
                audio=r.listen(source)
                msg=r.recognize_google(audio)
                msg = text.lower()
                speak("ok done!")
                print("Your message :"+str(msg))
                speak("Your message:"+str(msg))

                speak("victim id ")
                print("victim id :")
                test=r.listen(source)
                Vic_id=r.recognize_google(test)
                Vic_id = Vic_id.lower()
                Vic_id = Vic_id.replace(" ", "")
                speak("ok done! victim id: "+str(Vic_id))
                print("ok done! victim id: "+str(Vic_id))
            
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio.")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))    

        mail = smtplib.SMTP('smtp.gmail.com',587)    #host and port area
        mail.ehlo()  #Hostname to send for this command defaults to the FQDN of the local host.
        mail.starttls() #security connection
        mail.login('jeeveteshbhanot163@gmail.com','yabpqdujuhyxwhxc') #login part     
        mail.sendmail('jeeveteshbhanot163@gmail.com',Vic_id,msg) #send part
        print ("Congrates! Your mail has send. ")
            
        speak("Congrates! Your mail has send. ")

        mail.close()   
        
    elif text == '2' or text == 'tu' or text == 'two' or text == 'Tu' or text == 'to' or text == 'To' or text == "option two" or "option 2" :
        mail = imaplib.IMAP4_SSL('imap.gmail.com',993) #this is host and port area.... ssl security
        unm = ('jeeveteshbhanot163@gmail.com')  #username
        psw = ('yabpqdujuhyxwhxc')  #password
        mail.login(unm,psw)  #login
        stat, total = mail.select('Inbox')  #total number of mails in inbox
        print ("Number of mails in your inbox :"+str(total))
        speak("Total mails are :"+ str(total))
        
        #unseen mails
        unseen = mail.search(None, 'UnSeen') # unseen count
        print ("Number of UnSeen mails :"+str(unseen))
        speak("Your Unseen mail :"+str(unseen))


        #search mails
        result, data = mail.uid('search',None, "ALL")
        inbox_item_list = data[0].split()
        new = inbox_item_list[-1]
        old = inbox_item_list[0]
        result2, email_data = mail.uid('fetch', new, '(RFC822)') #fetch
        raw_email = email_data[0][1].decode("utf-8") #decode
        email_message = email.message_from_string(raw_email)
        print ("From: "+email_message['From'])
        print ("Subject: "+str(email_message['Subject']))
        speak("From: "+email_message['From']+" And Your subject: "+str(email_message['Subject']))


        #Body part of mails
        stat, total1 = mail.select('Inbox')
        stat, data1 = mail.fetch(total1[0], "(UID BODY[TEXT])")
        msg = data1[0][1]
        soup = BeautifulSoup(msg, "html.parser")
        txt = soup.get_text()
        print ("Body :"+txt)
        speak("Body: "+txt)

        mail.close()
        mail.logout()

    else:
        speak("unknow error : Choice not satisfy ")
MyApp().run()
    
