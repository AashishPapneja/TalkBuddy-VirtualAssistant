wishMe()
    
    while True:
        query = takeCommand().lower()
        
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
                speak("Do you want to add any more tasks to your todo list?")
                response = takeCommand().lower()
                if('yes' or 'more' or 'one' or '1' or 'sure') in response:
                    continue
                else:
                    break

        
        #-----------Setting alarms and timers.------
        
        #---------Responding to simple greetings like "hello" or "hi".--------
        elif('hi'  in query or 'hello' in query):
            speak("Hello there, it's great to hear from you! How can I assist you today?")
            
        #--------Providing weather updates based on location.-----------
        
                
        elif('stop') in query:
            continue;          
        elif ('quit') in query:
            exit()