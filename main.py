from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Serve the homepage with the form
@app.route("/")
def home():
    return render_template("index.html")  # Ensure the 'index.html' file is in a folder named 'templates'

# Handle the calculation logic via a POST request
@app.route("/calculate", methods=["POST"])
def calculate_pricing():
    data = request.json  # Parse JSON data from the request
    cost = float(data['cost'])
    code = int(data['code'])
    margin = float(data['margin'])

    # Calculate multiplier x
    x = 1 / (1 - (margin / 100))

    # Logic for calculation
    if code == 10:
        if margin >= 35:
            y = 0.1
        elif 25 <= margin < 35:
            y = 0.08
        elif 15 <= margin < 25:
            y = 0.06
        else:
            y = 0
    elif code == 24:
        if margin >= 45:
            y = 0.06
        elif 35 <= margin < 45:
            y = 0.04
        elif 25 <= margin < 35:
            y = 0.02
        else:
            y = 0
    elif code == 50:
        if margin >= 45:
            y = 0.06
        elif 35 <= margin < 45:
            y = 0.04
        elif 25 <= margin < 35:
            y = 0.02
        else:
            y = 0
    elif code == 55:
        if margin >= 35:
            y = 0.1
        elif 25 <= margin < 35:
            y = 0.08
        elif 15 <= margin < 25:
            y = 0.06
        else:
            y = 0
    elif code == 60:
        y = 0.1 if margin >= 15 else 0
    elif code == 65:
        y = 0.15 if margin >= 15 else 0
    elif code == 70:
        y = 0.1 if margin >= 25 else 0
    elif code == 75:
        if margin >= 35:
            y = 0.1
        elif 25 <= margin < 35:
            y = 0.08
        elif 15 <= margin < 25:
            y = 0.06
        else:
            y = 0
    elif code == 77:
        if margin >= 45:
            y = 0.1
        elif 35 <= margin < 45:
            y = 0.08
        elif 25 <= margin < 35:
            y = 0.06
        else:
            y = 0
    else:
        return jsonify({"error": "Invalid code. Please enter a valid code."}), 400


    # Calculate selling prices and payouts
    s_new = ((cost * (x * (y + 0.125) - 0.125)) / 0.125) + cost
    s_old = cost * x
    payout_new = (s_new - cost) * 0.125
    payout_old = ((s_old - cost) * 0.125) + (s_old * y)

    # Return JSON response
    return jsonify({
        "s_new": round(s_new, 2),
        "s_old": round(s_old, 2),
        "payout_new": round(payout_new, 2),
        "payout_old": round(payout_old, 2)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

