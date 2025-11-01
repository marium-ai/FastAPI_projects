from fastapi import FastAPI

app=FastAPI()

moods = {
    "happy": {
        "quote": "Happiness is not by chance, but by choice 😊",
        "suggestion": "Share your smile with someone today 😄"
    },
    "sad": {
        "quote": "It’s okay to feel down sometimes 🌧️",
        "suggestion": "Go for a walk and listen to music 🎧"
    },
    "angry": {
        "quote": "For every minute you remain angry, you lose sixty seconds of peace 😤",
        "suggestion": "Take deep breaths and count to ten 🧘"
    },
    "tired": {
        "quote": "Rest is not idleness, it’s recharging 🌙",
        "suggestion": "Take a short nap or drink some water 💤"
    },
    "motivated": {
        "quote": "Don’t stop until you’re proud 🚀",
        "suggestion": "Plan your next small goal and crush it 💪"
    },
    "stressed": {
        "quote": "You can’t control everything, and that’s okay 🌿",
        "suggestion": "Stretch, breathe, and focus on what you can do ✨"
    },
    "bored": {
        "quote": "Boredom is just a chance to be creative 🎨",
        "suggestion": "Try learning something new or play your favorite song 🎧"
    },
    "confused": {
        "quote": "It’s fine not to have all the answers right now 🤔",
        "suggestion": "Write down your thoughts, clarity will follow 📝"
    },
    "excited": {
        "quote": "Your energy is contagious — keep shining ✨",
        "suggestion": "Celebrate your wins and spread the joy 🎉"
    },
    "lonely": {
        "quote": "You are never truly alone; your thoughts are your company 🌌",
        "suggestion": "Call a friend or spend time doing what you love 💖"
    }
}

@app.get("/")
def welcome():
    return{"message":"welcome to mood api here you can get quotes & segestion regarding your MOOD"}

@app.get("/mood/{user_mood}")
def Get(user_mood:str):
    user_mood==user_mood.lower()
    if  user_mood in moods:
        return{
            "mood":user_mood,
            "quote":moods[user_mood]["quote"],
            "suggestion":moods[user_mood]["suggestion"]
        }
    else:
     return {"error": f"Sorry, mood '{user_mood}' not found!"}