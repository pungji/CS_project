from flask import Flask, jsonify, request

app = Flask(__name__)

menu_prices = {'타코야끼': 6000, '문꼬치': 5000}
order_count = 0
order_history = {'타코야끼': 0, '문꼬치': 0}
total_price = 0

@app.route('/order', methods=['POST'])
def place_order():
    global order_count, order_history, total_price
    data = request.json
    item = data['item']
    quantity = data['quantity']
    order_count += quantity
    order_history[item] += quantity
    total_price += menu_prices[item] * quantity
    print(f"Received order: {quantity} {item}(s)")
    print(f"Order count: {order_count}, Order history: {order_history}, Total price: {total_price}")
    return jsonify({'message': 'Order placed successfully'})

@app.route('/reset', methods=['POST'])
def reset_order():
    global order_count, order_history, total_price
    order_count = 0
    order_history = {'타코야끼': 0, '문꼬치': 0}
    total_price = 0
    print("Order reset")
    return jsonify({'message': 'Order reset successfully'})


if __name__ == '__main__':
    app.run(debug=True)