from flask import Flask, render_template, request

from main import *

import pandas as pd

app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')

@app.route('/',methods=['GET'])
def index():
	return render_template("index.html")

@app.route('/leaderboard',methods=['GET'])
def leaderboard():
	df = pd.DataFrame(data={
		values["rank"]: {
			"Team":values["teamNumber"],
			"AverageRP":values["sortOrder1"],
			"Record":"%s - %u - %s" % (values["wins"], values["losses"], values["ties"]),
			"Matches": values["matchesPlayed"],
	} for values in GetRankings()["Rankings"]}).transpose()

	return "<link rel='stylesheet' href='/staticFiles/main.css' />" + df.to_html(classes="customTable")

@app.route('/schedule',methods=['GET'])
def schedule():
	try:
		data = GetTeamSchedule(int(request.args.get('team')))
	except:
		data = GetSchedule()

	df = pd.DataFrame(data={values["description"]: {team["station"] : team["teamNumber"] for team in values["teams"]}  for values in data["Schedule"]}).transpose()

	return "<link rel='stylesheet' href='/staticFiles/main.css' />" + df.to_html(classes="customTable")

@app.route('/results',methods=['GET'])
def results():
	try:
		return GetMatch(int(request.args.get('match')))
	except:
		return GetAllMatches()

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=8080)