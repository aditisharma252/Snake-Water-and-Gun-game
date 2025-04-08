from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    data = request.get_json()
    user_choice = data['choice']
    youDict = {"s": 1, "w": -1, "g": 0}
    reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

    computer = random.choice([-1, 0, 1])
    you = youDict[user_choice]

    if computer == you:
        result = "It's a tie!"
    elif (computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
        result = "You win!"
    else:
        result = "You lose!"

    return jsonify({
        "you": reverseDict[you],
        "computer": reverseDict[computer],
        "result": result
    })

if __name__ == '__main__':
    app.run(debug=True)