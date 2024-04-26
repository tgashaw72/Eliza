import random
import re

""" Eliza homework. Relation advisor """
_author_ = "Tilahun Gashaw"

def name():
    print("Eliza: Hello! What's your name?")
def find_and_name(response):
    match = re.match(r'(?:I am |my name is )([a-zA-Z]+)', response, re.I)
    if match:
        return "Hello " + match.group(1) + ", tell me more"
    return None

def find_and_actions(response):
    matches = re.findall(r'\b(\w+)(ed)\b', response, re.I)
    if matches:
        match = random.choice(matches)
        return "How did you " + match[0] + "?"
    return None

def find_and_feelings(response):
    negative_feeling_words = ["sadness", "sad", "bad", "sick"]
    positive_feeling_words = ["happy", "happiness", "good", "ok", "well", "wonderful", "awesome"]

    for word in negative_feeling_words:
        if word in response:
            return "When are you feeling " + word + "?"

    for word in positive_feeling_words:
        if word in response:
            return "great ! What's making you feel " + word + "?"

    return None

def find_and_family(response):
    family = ["mother", "father", "brother", "sister", "mom", "dad", "cousin", "friend"]
    family_matches = [word for word in family if word in response]
    if family_matches:
        return "Tell me more about your " + ", ".join(family_matches) + "?"
    return None

def process(response):
    name_response = find_and_name(response)
    if name_response:
        return name_response
    past_actions_response = find_and_actions(response)
    if past_actions_response:
        return past_actions_response
    feelings_response = find_and_feelings(response)
    if feelings_response:
        return feelings_response
    family_response = find_and_family(response)
    if family_response:
        return family_response
    return random.choice(["Tell me more.", "Can you elaborate?", " Could you give more details?", "Can you explain?", "would you clarify, please ?"])

name()
while True:
    response = input("You: ")
    eliza_response = process(response)
    print("Eliza:", eliza_response)
    if 'bye' in response.lower():
        print("Eliza: Goodbye!")
        break
