import pyttsx3
import subprocess as sub
import os

pyttsx3.speak("Welcome To The Automated Assistant How May I Help You")
print("##############################Welcome To The Automated Assistant! How May I Help You!!!!###################################\n")
yes = "yes"
while (yes):
    pyttsx3.speak("Tell Me Your Requirements")
    print("Tell Me Your Requirements  : ", end='')
    command = input()
    pyttsx3.speak("You Requested To" + command)
    command.lower()

    if (command == "didn't") or (command == "don't") or (command == "do not") or (command == "did not"):
        print("Command Not Found !!! Please Try With The Correct Requirements")

    else:
        if (("run" in command) or ("execute" in command) or ("open" in command)) and (("camera" in command)):
            pyttsx3.speak("Opening Camera")
            os.system("start microsoft.windows.camera:")

        elif (("run" in command) or ("execute" in command) or ("open" in command)) and (("notepad" in command) or ("editor" in command)):
            pyttsx3.speak("Opening Notepad")
            os.system("notepad")

        elif (("run" in command) or ("execute" in command) or ("open" in command)) and (("browser" in command) or ("chrome" in command)):
            pyttsx3.speak("Opening Chrome")
            os.system("chrome")

        elif (("run" in command) or ("execute" in command) or ("open" in command)) and ("calculator" in command):
            pyttsx3.speak("Opening Calculator")
            os.system("start calculator:")

        elif (("run" in command) or ("execute" in command) or ("open" in command)) and (("microsoft photos" in command) or ("photos" in command)):
            pyttsx3.speak("Opening Photos")
            os.system("start ms-photos:")

        elif (("run" in command) or ("execute" in command) or ("open" in command)) and (("microsoft weather" in command) or ("weather" in command)):
            pyttsx3.speak("Opening Weather")
            os.system("start bingweather:")

        elif (("run" in command) or ("execute" in command) or ("open" in command)) and (("microsft store" in command) or ("store" in command)):
            pyttsx3.speak("Opening Microsoft Store")
            os.system("start ms-windows-store:")

        elif (("run" in command) or ("execute" in command) or ("open" in command)) and("calendar" in command):
            pyttsx3.speak("Opening Calendar")
            os.system("start outlookcal:")
    
        elif (("run" in command) or ("execute" in command) or ("open" in command)) and (("vlc" in command) or ("vedio player" in command)):
            pyttsx3.speak("Opening VLC")
            os.system("vlc")
            
        elif(("run" in command) or ("execute" in command) or ("open" in command)) and (("groove" in command) or ("music player" in command)):
            pyttsx3.speak("Opening Groove Music Player")
            os.system("start mswindowsmusic:")

        elif ("exit" in command) or ("quit" in command) or ("close" in command):
            pyttsx3.speak("Thanks For Joining Me!!!!")
            break

    pyttsx3.speak("Do You Want To Countinue Reply With Yes Or No")
    print("\nDo You Want To Countinue Reply With Yes Or No?",end=" ")
    ans = input
    if (ans == "yes"):
        continue
    elif (input() == "no"):
        print("\nThanks For Joining!!!!\n")
        pyttsx3.speak("Thanks For Joining Me!!!!")
        break

