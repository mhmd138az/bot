import speech_recognition as sr
import pyttsx3
import json
import os

# تنظیمات تبدیل متن به گفتار
engine = pyttsx3.init()
engine.setProperty("rate", 150)
engine.setProperty("volume", 1)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source)
            user_input = recognizer.recognize_google(audio)
            print(f"You said: {user_input}")
            return user_input.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            return None

# بارگذاری یا ایجاد پایگاه داده
data_file = "knowledge.json"
if os.path.exists(data_file):
    with open(data_file, "r") as f:
        knowledge = json.load(f)
else:
    knowledge = {}

# ذخیره‌سازی پایگاه داده
def save_knowledge():
    with open(data_file, "w") as f:
        json.dump(knowledge, f)

# پاسخ‌دهی هوشمند
def get_response(user_input):
    if user_input in knowledge:
        return knowledge[user_input]
    else:
        speak("balad niistaam . mieshee yaadam beedii?")
        print("Teach me: What should I respond?")
        new_response = listen()
        if new_response:
            knowledge[user_input] = new_response
            save_knowledge()
            return "mamnon yadd ggereftaam."
        else:
            return "naafaahh midaamm ! yek baare digge beggoo."

# شروع چت‌بات
def chatbot():
    speak("Hello!")
    while True:
        user_input = listen()
        if user_input is None:
            continue
        if "exit" in user_input or "goodbye" in user_input:
            speak("Goodbye! Have a great day!")
            break
        response = get_response(user_input)
        print(f"AI: {response}")
        speak(response)

# اجرای ربات
chatbot()
