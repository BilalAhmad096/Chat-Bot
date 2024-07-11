def project():
    import pyttsx3
    import json
    import speech_recognition as sr
    r = sr.Recognizer()
    engine = pyttsx3.init()
    print("Hello This is Bilals Bot:")
    bolo = "Hello This is Bilal's Bot"
    engine.say(bolo)
    engine.runAndWait()
    print("I am an automated System, I shall be very thankful if you could answer my questions.")
    bolo = "I am an automated System, I shall be very thankful if you could answer my questions"
    engine.say(bolo)
    engine.runAndWait()
    print("Would you like to go ahead? If yes, Say 'Yes' else say anything:")
    bolo = "Would you like to go ahead? If yes, Say 'Yes' else say anything:"
    engine.say(bolo)
    engine.runAndWait()
    with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            r.adjust_for_ambient_noise(source,duration=1)
            print ("Say Something")
            audio = r.listen(source)
            try:
                    text = r.recognize_google(audio)
                    print (text)
            except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio")
	
            except sr.RequestError as e:
                    print("Could not request results from Google")
    lst=[]
    if text=="yes":
        print("What is your name?")
        bolo ="What is your name?"
        engine.say(bolo)
        engine.runAndWait()
        a=input()
        lst.append(a)
        print("How old are you?")
        bolo ="How old are you?"
        engine.say(bolo)
        engine.runAndWait()
        a=int(input())
        lst.append(a)
        print("Were you tested positive for corona Virus?")
        bolo ="Were you tested positive for corona Virus?"
        engine.say(bolo)
        engine.runAndWait()
        a=input()
        lst.append(a)
        if a=="Y":
            bolo ="Did you have high fever?"
            engine.say(bolo)
            engine.runAndWait()
            b=input("Did you have high fever?")
            lst.append(b)
            bolo ="Thanks for your time Really appreciate it."
            engine.say(bolo)
            engine.runAndWait()
           
        else:
            bolo ="Thanks for your time Have a good Day."
            engine.say(bolo)
            engine.runAndWait()
            print("Thanks for your time Have a good Day.")
    else:
        bolo ="Thanks for your time Have a good Day."
        engine.say(bolo)
        engine.runAndWait()
        print("Thanks for your time Have a good Day.")
       
    print (lst)
   
    with open('test.txt', 'a') as f:
        f.write(json.dumps(lst))
