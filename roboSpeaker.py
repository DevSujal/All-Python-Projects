import win32com.client as wincom

speak = wincom.Dispatch("SAPI.SpVoice")
while True:
    text = input("Enter a text to convert into a speech: ")
    if(text == "stop"):
        speak.Speak("Bye Bye")
        break
    elif(text.find('who invented you') != -1):
        speak.Speak("i am invented by sujal nimje")
    else: 
        speak.Speak(text)   
        