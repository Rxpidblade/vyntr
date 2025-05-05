from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

# Replace this with your actual Solana wallet name generator
def generate_wallet_name():
    return ''.join(random.choices(string.ascii_lowercase, k=4))

@app.route('/', methods=['GET', 'POST'])
def index():
    wallet_name = None
    if request.method == 'POST':
        wallet_name = generate_wallet_name()
    return render_template('index.html', wallet_name=wallet_name)

if __name__ == '__main__':
    app.run(debug=True)