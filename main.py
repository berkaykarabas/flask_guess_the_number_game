from flask import Flask
import random
app= Flask(__name__)
number=random.randint(1,9)
@app.route("/")
def guess_the_number():
    return '<h1> Guess The Number </h1>'\
            '<img src=https://media.giphy.com/media/l378khQxt68syiWJy/giphy.gif>'

@app.route("/<int:guess>")
def select_number(guess):
    if guess>number:
        return '<h1> Too high! </h1>'\
            '<img src=https://media.giphy.com/media/fqst7AVqF6AVLlYklE/giphy.gif>'
    if guess<number:
        return '<h1> Too low! </h1>'\
            '<img src=https://media.giphy.com/media/H4oLWS4veh9kqxQ1z2/giphy.gif>'
    if guess==number:
        return "<h1 style='color: green'> YOU FOUND ME! </h1>"\
            "<img src=https://media.giphy.com/media/13ByqbM0hgfN7y/giphy.gif>"
if __name__=="__main__":
    app.run(debug=True)
