from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/table")
def table():
    return jsonify([
        "1. Manchester City | Played: 30 | Wins: 22 | Draws: 6 | Losses: 2 | GD: +50 | Pts: 72",
        "2. Arsenal | Played: 30 | Wins: 21 | Draws: 6 | Losses: 3 | GD: +45 | Pts: 69",
        "3. Liverpool | Played: 30 | Wins: 20 | Draws: 8 | Losses: 2 | GD: +40 | Pts: 68"
    ])

if __name__ == "__main__":
    app.run(debug=True)
