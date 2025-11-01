from fastapi import FastAPI

app = FastAPI()


Dictionary = {
    "achieve": "to successfully complete a task or goal",
    "brave": "ready to face danger or pain without showing fear",
    "curious": "eager to know or learn something",
    "delight": "a feeling of great pleasure or happiness",
    "eager": "wanting very much to do or have something",
    "faith": "strong belief or trust in someone or something",
    "generous": "willing to give and share with others",
    "honest": "always telling the truth, not lying",
    "kind": "friendly, helpful, and caring towards others",
    "loyal": "showing constant support and faithfulness"
}

@app.get("/")
def welcome():
    return {"message": "Welcome to the Dictionary API!"}

@app.get("/dictionary/{word}")
def get_meaning(word: str):
    word = word.lower()   
    if word in Dictionary:
        return {"word": word, "meaning": Dictionary[word]}
    else:
        return {"error": f"'{word}' not found in dictionary"}
