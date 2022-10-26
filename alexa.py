import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import wolframalpha # to calculate strings into formula
import os
from threading import Thread
import webbrowser 

def save_news():
    from newsapi import NewsApiClient
    newsapi = NewsApiClient(api_key='d57ef920ca1947a5baa8b4a2218de6d6')
    top_headlines = newsapi.get_top_headlines(sources='google-news-in',language='en')
    title = top_headlines['articles'][0]['title']
    des = top_headlines['articles'][0]['description']
    url = top_headlines['articles'][0]['url']
    f = open('log','w')
    f.write(title+'\n'+des+"/\/||\//end||||"+url)
    f.close()

t = Thread(target=save_news)
t.start()

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
isSpoken = True


def talk(text):
    engine.say(text)
    engine.runAndWait()


def takecommand():
    command=''

    try:
        with sr.Microphone() as source:
            print("")
            
            print(' What Yoy Want Me TO Do....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command

def runalexa():
    global isSpoken
    command1 = takecommand()
    print(command1)
    if 'what is '  in command1 or 'who is'in command1:
       isSpoken = True
       talk('I found This On Wikipedia')
       person = command1.replace('what is', '')
       info = wikipedia.summary(person, 1)
       print(info)
       talk(info)
       return
    elif 'what' in command1:
        isSpoken = True
        webb = command1.replace('what', '')
        print('what ' + webb)
        talk('what ' + webb)
        pywhatkit.search(webb)
        return

    elif 'play' in command1:
        isSpoken = True
        webb = command1.replace('play', '')
        print('playing ' + webb)
        talk('playing ' + webb)
        pywhatkit.playonyt(webb)
        return


    elif 'time' in command1:
        isSpoken = True
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('Current time is ' + time)
        talk('Current time is ' + time)
        return

    elif 'news' in command1:
        isSpoken = True
        try:
            with open('log') as f:
                text = f.read().split("/\/||\//end||||")
                webbrowser.open(text[1])
                talk(text[0])
                return
        except:
            pass
  
    elif 'date' in command1:
        isSpoken = True
        date_object = datetime.date.today()
        print(date_object)
        talk(date_object)
        return
    elif 'are you single' in command1:
        isSpoken = True
        print('I am in a relationship with Thanuish')
        talk('I am in a relationship with Thanuish')
        return
    elif "open word" in command1:
        isSpoken = True
        print("Opening Microsoft Word")
        talk("Opening Microsoft Word")
        os.startfile( "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\Word 2013.lnk")
        return
    elif "open excel" in command1:
        isSpoken = True
        print("Opening Microsoft Excel")
        talk("Opening Microsoft Excel")
        os.startfile( "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\Excel 2013.lnk")
        return
    elif "open google" in command1:
        isSpoken = True
        print("Opening google")
        talk("Opening google")
        os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")        
        return
    elif "open telegram" in command1:
        isSpoken = True
        print("Opening Telegram")
        talk("Opening Telegram")
        os.startfile( "I:\Telegram Desktop\Telegram.exe")
        return
   
    elif 'joke' in command1:
        isSpoken = True
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())
        return
    elif 'search' in command1:
        isSpoken = True
        web=pywhatkit.search(web)
        print("Searching...")
        return
    elif  "define yourself" in command1:
        isSpoken = True
        print ( 'Hello, I am Person. Your personal Assistant.  I am here to make your life easier. You can command me to perform  various tasks such as calculating sums or opening applications etcetra')

        talk( 'Hello, I am Person. Your personal Assistant.  I am here to make your life easier. You can command me to perform  various tasks such as calculating sums or opening applications etcetra')
        return
    elif "calculator" in command1.lower():
        isSpoken = True
        print("Select operation.")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")

        while True:
            choice = input("Enter choice(1/2/3/4): ")
            if choice in ('1', '2', '3', '4'):
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

            if choice == '1':
                print(num1, "+", num2, "=", (num1+num2))

            elif choice == '2':
                print(num1, "-", num2, "=", (num1-num2))

            elif choice == '3':
                print(num1, "*", num2, "=", (num1*num2))

            elif choice == '4':
                print(num1, "/", num2, "=", (num1/num2))
            next_calculation = input("Let's do next calculation? (yes/no): ")
            if next_calculation == "no":break
        return
   
    if 'exit' in command1 or 'bye' in command1:
        exit(0)

    
            
           
 
    else:
       # print('Please say the command again.')
        talk('Please say the command again.')

def wakeComment():
    command=''

    try:
        with sr.Microphone() as source:
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            
    except Exception as e:
        print(e)
        pass
    return command
 

while True:
    comment = ''
    if(isSpoken):
        comment = wakeComment()
        print(comment)
    if ('alexa' in comment or not isSpoken):
        talk('What can i do for you!')
        isSpoken = False
        runalexa()
        
