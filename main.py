from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Premier League API is running!"

@app.route("/table")
def table():
    return jsonify([
        "1. Manchester City | Played: 30 | Wins: 22 | Draws: 6 | Losses: 2 | GD: +50 | Pts: 72",
        "2. Arsenal | Played: 30 | Wins: 21 | Draws: 6 | Losses: 3 | GD: +45 | Pts: 69",
        "3. Liverpool | Played: 30 | Wins: 20 | Draws: 8 | Losses: 2 | GD: +40 | Pts: 68",
        "4. Aston Villa | Played: 30 | Wins: 18 | Draws: 5 | Losses: 7 | GD: +22 | Pts: 59"
    ])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
