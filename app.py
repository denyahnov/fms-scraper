from flask import Flask, render_template

from main import *

app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/leaderboard')
def leaderboard():
	return "\n".join([f'{team["rank"]}. {team["teamNumber"]}' for team in GetRankings()["Rankings"]])

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=8080)