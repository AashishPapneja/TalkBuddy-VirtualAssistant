import tkinter
import tkinter.messagebox
import customtkinter
from PIL import ImageTk, Image
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random 
import time #for sleep function

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

purple = "#8a2be2"


engine = pyttsx3.init('sapi5') #microsoft speech api
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)

commandtext = ""

def modifyCommandText(newtxt):
    currtext = scrollableLeftContent.cget("text")
    # print(text)
    # newtxt = "Modify karaya baabe da"
    global commandtext
    commandtext =  currtext +  "\n" + newtxt 
    # commandtext.append(currtext)
    
    scrollableLeftContent.configure(text = commandtext)




def speak(audio):
    '''Converts text to speech'''
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    '''Wishes user according to time'''
    # currtext = scrollableLeftContent.cget("text")
    
    
    # # print(text)
    # newtxt = "Modify karaya baabe da"
    # global commandtext
    # commandtext = newtxt + commandtext + "\n" + currtext 
    # # commandtext.append(currtext)
    
    # scrollableLeftContent.configure(text = commandtext)
    
    # txt = "modify karaya"
    # modifyCommandText(txt)
    
    hour = int(datetime.datetime.now().hour)
    if(hour>=6 and hour<12):
        speak("Good Morning !")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good evening")
   
    speak("This is ModiJi. How can i assist you today?")


def takeCommand():
    '''Convert user speech to text'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:  
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to , content):
    server = smtplib.SMPT('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password-here')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()
    
    
def tellJoke():
    '''Tells joke'''
    with open ("assets/jokes.txt", "r") as f:
        jokes_list = f.readlines()
        rand_num = random.randint(0, 39)
        joke = jokes_list[rand_num]
        return joke

def addToDoList(task):
    '''Add task in ToDoList'''
    with open ("assets/toDoList.txt", "a") as f:
        f.write(task)
        f.write("\n")
        


def button_callback():
    print("button clicked")
    
def query():
    query = takeCommand().lower()
    
    modifyCommandText(query)
     
    #Logic for executing tasks based on query
    
    #-------------Wikepedia search-----------
    if'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace('wikipedia',"")
        results = wikipedia.summary(query, sentences = 2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
        
    #----------Open a website in browser-----------
    # elif 'open stackoverflow' in query:
    #     webbrowser.open("stackoverflow.com")
    # elif 'open youtube' in query:
    #     webbrowser.open("youtube.com")
    # elif 'open google' in query:
    #     webbrowser.open("google.com")
    
    #-----------------Coded self------------------
    elif 'open' in query:
        lst = query.split(" ")
        ind1 = lst.index("open")
        
        
        if(ind1+1<len(lst)):
            website = lst[ind1+1]
            print(website)
            webbrowser.open(f"{website}.com")
            
    #-----------------Play Music------------------
    elif 'play music' in query or 'play song' in query:
        music_dir = 'C:\\Music'
        songs = os.listdir(music_dir)
        # print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))
        
    
    #------------------Tell Time-------------------
    elif 'the time' in query or 'time now' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time now is {strTime}")
    
    
    #------------------Open IDE-------------------
    elif 'open code' in query or 'open vs code' in query:
        codePath = r"C:\Users\Dell\AppData\Local\Programs\Microsoft VS Code\Code.exe"
        os.startfile(codePath)
        
        
    #-------------------Open Spotify--------------
    elif ('open spotify') in query:
        appPath = r"C:\Users\Dell\OneDrive\Desktop\Spotify.lnk"
        os.startfile((appPath))
    
    
    #------------------Send an Email----------------
    #-----------inactive for now(Require permission)---------------
    elif 'email to' in query or 'send an email' in query or 'send email' in query:
        try: 
            speak("Whom you want to send email to")
            receiver = takeCommand()
            mailTo = "xyz@gmail.com"  #dummy if mail not found
            
            #find the mailaddress of the receiver
            with open ("emails.txt", "r") as f:
                email_entires = f.read().splitlines()
                for email_entry in email_entires:
                    name = email_entry.split(" ")[0]
                    email_address = email_entry.split(" ")[1]
                    if(name==receiver):
                        mailTo = email_address
            
            speak("What should i say through the mail?")
            content = takeCommand()
            sendEmail(mailTo, content)
            speak("Email sent!")
        except exception as e:
            print(e)
            speak("Sorry, I am unable to send the emaiL. Please try again")
            
            
            
    #--------------Tell A joke------------
    elif'joke' in query or'laugh' in query:
        speak("Arzz kiyaa hai")
        joke = tellJoke()
            
        question = joke.split("?")[0]
        ans = joke.split("?")[1]
            
            
        print(question)
        speak(question)
        
        time.sleep(1.5) #pause
        
        print(ans)
        speak(ans)
        speak("Ha ha ha ha!")
        
    #--------------ToDo list------------
    elif ('add to do' in query) or ('add work' in query) or ('add task' in query) or ('add todo' in query) or ('add list' in query) or ('new task' in query) or ('record task' in query) or ('a task' in query) or ('add to list' in query):
        
        
#strings = ['play music', 'play song', 'start playlist']
#query = 'play some music please'

#if any(s in query for s in strings):
    # Do something
    
    
        speak("inside this list")
        while(True):
            speak("What task you want to add to your todo list?")
            task = takeCommand()
            print(task)
            addToDoList(task)
            
            #further tasks add?
            # speak("Do you want to add any more tasks to your todo list?")
            # response = takeCommand().lower()
            # if('yes' or 'more' or 'one' or '1' or 'sure') in response:
            #     continue
            # else:
            #     break

    
    #-----------Setting alarms and timers.------
    
    #---------Responding to simple greetings like "hello" or "hi".--------
    elif('hi'  in query or 'hello' in query):
        speak("Hello there, it's great to hear from you! How can I assist you today?")
        
    #--------Providing weather updates based on location.-----------
    
            
    elif('stop') in query:
        # continue;      
        pass    
    elif ('quit') in query:
        exit()
    
    
    
def assist():
    wishMe()
    query()
    
    # while True:
        
        
            
        



#---root---
app = customtkinter.CTk()

app.title("Virtual assistant")
app.geometry("1100x600")
#-------------

#--------label---------
label = customtkinter.CTkLabel(app, text="Virtual Assistant", fg_color="transparent",  width=150 , height= 50, font=("Arial", 30))
label.pack(padx=20, pady = 20)
#-------------

#main frame
main_frame = customtkinter.CTkFrame(master=app)
main_frame.pack(pady=20, padx=60, fill="both", expand=True)



# left frame
left_frame = customtkinter.CTkFrame(main_frame)
left_frame.pack(side="left", padx=20, pady=20, fill="both", expand=True)

#label of frame
labelleft = customtkinter.CTkLabel(left_frame, text="Command Window", fg_color="transparent",  width=50 , height= 20, font=("Arial", 15))
labelleft.pack(padx=10, pady = 10)

#childScrollabeFrame
leftchild_frame = customtkinter.CTkScrollableFrame(left_frame)
leftchild_frame.pack(side="left", padx=20, pady=20, fill="both", expand=True)

#label of scrollableFrame
scrollableLeftContent = customtkinter.CTkLabel(leftchild_frame, text = "hello world", fg_color="transparent",  width=50 , height= 20, font=("Arial", 15))
print("checking error")
scrollableLeftContent.pack(padx=10, pady = 10)



# right frame
right_frame = customtkinter.CTkFrame(main_frame, bg_color = "black")
right_frame.pack(side="left", padx=20, pady=20, fill="both", expand=True)

#label of right frame
labelright = customtkinter.CTkLabel(right_frame, text="Output Window", fg_color="transparent",  width=50 , height= 20, font=("Arial", 15))
labelright.pack(padx=10, pady = 10)

#childScrollabeFrame
leftchild_frame = customtkinter.CTkScrollableFrame(right_frame)
leftchild_frame.pack(side="left", padx=20, pady=20, fill="both", expand=True)



# Load the microphone image
mic_image = Image.open("assets/microphone2.png")
mic_image = mic_image.resize((40, 40))  # Resize the image as needed
mic_icon = ImageTk.PhotoImage(mic_image)

# Create the circular button
mic_button = customtkinter.CTkButton(app, image=mic_icon, text = "give command", command=assist)
mic_button.pack(padx=20, pady=20)

#--------button-----
# button = customtkinter.CTkButton(app, text="my button", command=button_callback)
# button.pack(padx=20, pady=20)
#------------------



app.mainloop()