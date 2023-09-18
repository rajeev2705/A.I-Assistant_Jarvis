import pywhatkit
from jarvis import Speak,takeCommand

name_array = ["kunal","dad","me"]
mobile = ["7380029671","9915937231","9878566807"]

def detail(query):
  global name_array,mobile
  ret =0
  for index,i in enumerate(name_array):
      if query ==i:
        return mobile[index]
        break
        



def Message(query):
    global name_array,mobile
    if 'send a whatsapp message to' in query:
        query=query.replace("send a whatsapp message to ","")
    elif 'send whatsapp message to' in query:
        query=query.replace("send a whatsapp message to ","")
    elif 'whatsapp message to' in query:
        query=query.replace("whatsapp message to ","")

       
    name = query
    phone = detail(query)

    if name in name_array :
        Speak("What is the message you want to send?")
        message = takeCommand()
        Speak("Tell me the timing to send the message.")
        Speak("Time in Hour")
        Hour = takeCommand()
        Hour = int(Hour)
        Speak("Time in minute")
        min = takeCommand()  # Corrected 'takecommand' to 'takeCommand'
        min = int(min)
        pywhatkit.sendwhatmsg("+91"+phone, message, Hour, min + 1, 20)  # Added +1 to the minute to send the message 1 minute later
        Speak("Ok sir! Message sent")

    else :
        Speak("tell me the phone number!")
        Phone = int(takeCommand())
        mobile.append(f"{Phone}")
        Speak("Tell me the name of the person")
        to = takeCommand()
        name_array.append(to)
        ph = f'+91+{Phone}'
        Speak("Tell me the message!")
        msg = takeCommand()
        Speak("Tell me the time Sir!")
        Speak("Time in Hour")
        Hour = int(takeCommand())
        Speak("Time in minute")
        min = int(takeCommand())
        pywhatkit.sendwhatmsg(ph,message,Hour,min,20)
        Speak("Ok sir! Message will be sent on given time")
    return




