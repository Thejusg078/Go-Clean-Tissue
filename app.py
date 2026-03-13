from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/checkout', methods=['POST'])
def checkout():
    print("Checkout initiated for: Go Clean Tissue Paper")
    return jsonify({
        "status": "success",
        "message": "Order created. Ready for payment integration.",
        "product": "Go Clean",
        "price": 100 
    })

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)