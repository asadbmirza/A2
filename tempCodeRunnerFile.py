from flask import Flask

app = Flask(__name__)

@app.route('/<name>')
def name(name: str):
    formattedName = name.strip()

    if formattedName.isupper():
        formattedName = name.lower()
    elif formattedName.islower():
        formattedName = name.upper()
    elif formattedName.isalnum:
        formattedName = removeNumbers(formattedName).upper()
    else:
        formattedName = name.title()

    return "Welcome, " + formattedName + ", to my CSCB20 website!"

def removeNumbers(name: str):
    formattedName = ''
    for char in name:
        if not char.isdigit():
            formattedName += char

    return formattedName


if __name__ == 'main':
    app.run(debug=True)