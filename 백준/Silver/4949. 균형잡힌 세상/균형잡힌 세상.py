import re

while True:
    text = input()
    if text == '.':
        break
    else:
        text = re.sub(r"[a-zA-Z]", "", text)
        text = text.replace(" ", "")
        while '()' in text or '[]' in text:
            text = text.replace("()", "")
            text = text.replace("[]", "")
        if text == ".":
            print("yes")
        else: 
            print("no")
        
