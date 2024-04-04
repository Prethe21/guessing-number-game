from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

def generate_random_number():
    return random.randint(1, 100)

secret_number = generate_random_number()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def check_guess():
    guess = int(request.form['guess'])
    result = check_guess_helper(guess)
    return jsonify({'result': result})

def check_guess_helper(guess):
    if guess == secret_number:
        return "Correct"
    elif guess < secret_number:
        return "Too low"
    else:
        return "Too high"

if __name__ == '__main__':
    app.run(debug=True)
