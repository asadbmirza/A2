from flask import Flask

app = Flask(__name__)

@app.route('/emoji/<name>')
def emoji(name: str):
    formattedName = formatEmojiName(name)

    return formatResponse(formattedName)

def formatEmojiName(name):
    emoji_dict = {"A": "🔺", "E": "🎗", "I": "👁", "O": "🔵", "U": "🆙"}

    formattedEmojiName = ""
    for char in name:

        if char.upper() in emoji_dict:
            formattedEmojiName += emoji_dict[char.upper()]
        else:
            formattedEmojiName += char
    return formattedEmojiName

@app.route('/<name>')
def name(name: str):
    formattedName = formatName(name)

    return formatResponse(formattedName)

def formatResponse(name: str):
    response = "Welcome, " + name + ", "
    endText = "to my CSCB20 website!"
    if isPalindrome(name):
        endText = "Your name is a palindrome!"

    return response + endText

def isPalindrome(text: str):
    length = len(text) - 1
    for i in range(length // 2):
        if text[i] != text[length - i]:
            return False
    return True

def formatName(name: str):
    formattedName = name.strip()
    print(formattedName)
    if hasDigit(formattedName):
        formattedName = removeNumbers(formattedName).upper()
    elif formattedName.isupper():
        formattedName = name.lower()
    elif formattedName.islower():
        formattedName = name.upper()
    else:        
        formattedName = formattedName.title()
    return formattedName

def removeNumbers(name: str):
    formattedName = ''
    for char in name:
        if not char.isdigit():
            formattedName += char

    return formattedName

def hasDigit(name: str):
    for char in name:
        if char.isdigit():
            return True
    return False


if __name__ == '__main__':
    app.run(debug=True)