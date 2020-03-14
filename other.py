import random

def generate_id(amount=8):
    id = ""
    
    chars = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '?', '#', '$', '%')

    for i in range(amount):
        capt = random.choice([True, False])
        choice_ = random.choice(chars)
        
        if capt and choice_.isalpha():
            choice_ = choice_.upper()
            
        id = id + choice_
        
    return str(id)