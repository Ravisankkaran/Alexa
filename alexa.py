import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import wolframalpha # to calculate strings into formula
import os


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
    command1 = takecommand()
    print(command1)
    if 'what is '  in command1 or 'who is'in command1:
       isSpoken = True
       talk('I found This On Wikipedia')
       person = command1.replace('what is', '')
       info = wikipedia.summary(person, 1)
       print(info)
       talk(info)
    elif 'what' in command1:
        isSpoken = True
        webb = command1.replace('what', '')
        print('what ' + webb)
        talk('what ' + webb)
        pywhatkit.search(webb)

    elif 'play' in command1:
        isSpoken = True
        webb = command1.replace('play', '')
        print('playing ' + webb)
        talk('playing ' + webb)
        pywhatkit.playonyt(webb)


    elif 'time' in command1:
        isSpoken = True
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('Current time is ' + time)
        talk('Current time is ' + time)
  
    elif 'date' in command1:
        isSpoken = True
        date_object = datetime.date.today()
        print(date_object)
        talk(date_object)
    elif 'are you single' in command1:
        isSpoken = True
        print('I am in a relationship with Thanuish')
        talk('I am in a relationship with Thanuish')
    elif "open word" in command1:
        isSpoken = True
        print("Opening Microsoft Word")
        talk("Opening Microsoft Word")
        os.startfile( "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\Word 2013.lnk")
    elif "open excel" in command1:
        isSpoken = True
        print("Opening Microsoft Excel")
        talk("Opening Microsoft Excel")
        os.startfile( "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\Excel 2013.lnk")
    elif "open google" in command1:
        isSpoken = True
        print("Opening google")
        talk("Opening google")
        os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")        
    elif "open telegram" in command1:
        isSpoken = True
        print("Opening Telegram")
        talk("Opening Telegram")
        os.startfile( "I:\Telegram Desktop\Telegram.exe")
   
    elif 'joke' in command1:
        isSpoken = True
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())
    elif 'search' in command1:
        isSpoken = True
        web=pywhatkit.search(web)
        print("Searching...")
    elif  "define yourself" in command1:
        isSpoken = True
        print ( 'Hello, I am Person. Your personal Assistant.  I am here to make your life easier. You can command me to perform  various tasks such as calculating sums or opening applications etcetra')

        talk( 'Hello, I am Person. Your personal Assistant.  I am here to make your life easier. You can command me to perform  various tasks such as calculating sums or opening applications etcetra')
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
    if(isSpoken):
        comment = wakeComment()
        print(comment)
    if ('alexa' in comment or not isSpoken):
        talk('What can i do for you!')
        runalexa()
        isSpoken = False
