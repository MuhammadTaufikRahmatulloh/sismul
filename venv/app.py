from flask import Flask, render_template
import os
import logging

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)