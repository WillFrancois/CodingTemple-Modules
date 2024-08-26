#Task 1
def return_mood_response(mood):
    if mood.lower() == "happy":
        return "I'm glad to hear you are happy!"
    elif mood.lower() == "sad":
        return "I'm sorry to hear you are sad!"
    elif mood.lower() == "excited":
        return "Oh, boy! It's great to be excited for something, isn't it?!"
    else:
        return "You have given the mood " + mood + "!"

