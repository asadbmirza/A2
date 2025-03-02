from flask import Flask

app = Flask(__name__)

@app.route('/<name>')
def name(name: str):
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

    return "Welcome, " + formattedName + ", to my CSCB20 website!"

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