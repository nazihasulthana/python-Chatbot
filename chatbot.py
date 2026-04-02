import random 
greetings = ["Hello","Hi there","Hey","Nice to meet you!"]
how_are_you = ["Im fine","Doing great","All good","Awesome"]
welcome = ["You are welcome","No problem","Anytime!"]
while True:
    user = input("You:").lower().strip()
    if user in ["hi","hey"]:
        print("Bot:",random.choice(greetings))
    elif "how are you" in user:
        print("Bot:",random.choice(how_are_you))
    elif "thank" in user:
        print("Bot:",random.choice(welcome))
    elif user in ["bye","exit","quit"]:
        print("Bot:Goodbye",)
        break
    else:
        print("Bot: idont understand")
