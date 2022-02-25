from flask import Flask, Response

app = Flask(__name__)

@app.route("/scoreboard/<start>/<end>.json")
def scoreboard(start, end):
    data = open('./scoreboard.json').read()
    return Response(data, mimetype='application/json')

@app.route("/team_rankings.json")
def team_rankings():
    data = open('./team_rankings.json').read()
    return Response(data, mimetype='application/json')