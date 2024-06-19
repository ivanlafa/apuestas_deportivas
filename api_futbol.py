from flask import Flask, jsonify
import random

app = Flask(__name__)

teams = ["Team A", "Team B", "Team C", "Team D", "Team E", "Team F"]

def generate_random_match():
    team1, team2 = random.sample(teams, 2)
    score1, score2 = random.randint(0, 5), random.randint(0, 5)
    return {
        "team1": team1,
        "team2": team2,
        "score1": score1,
        "score2": score2
    }

@app.route('/random_match', methods=['GET'])
def random_match():
    match = generate_random_match()
    return jsonify(match)

if __name__ == '__main__':
    app.run(debug=True)
