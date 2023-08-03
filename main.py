import os
import json
import requests
from base64 import b64encode

from settings import *

AUTHORIZATION = b64encode("{}:{}".format(USERNAME,TOKEN).encode('utf-8')).decode('utf-8')

BASE_URL = "https://frc-api.firstinspires.org/v3.0"

# RAW GET REQUESTS

def GetEventInfo() -> dict:
	return requests.get("{}/2023/events?eventCode={}".format(BASE_URL,EVENT_CODE),headers = {'Authorization': f"Basic {AUTHORIZATION}"}).json()

def GetTeams() -> dict:
	return requests.get("{}/2023/teams?eventCode={}".format(BASE_URL,EVENT_CODE),headers = {'Authorization': f"Basic {AUTHORIZATION}"}).json()

def GetAllMatches(match_type:str = "qual") -> dict:
	return requests.get("{}/2023/scores/{}/{}".format(BASE_URL,EVENT_CODE,match_type),headers = {'Authorization': f"Basic {AUTHORIZATION}"}).json()

def GetSchedule(schedule_type:str = "qual") -> dict:
	return requests.get("{}/2023/schedule/{}/{}".format(BASE_URL,EVENT_CODE,schedule_type),headers = {'Authorization': f"Basic {AUTHORIZATION}"}).json()

def GetRankings() -> dict:
	return requests.get("{}/2023/rankings/{}".format(BASE_URL,EVENT_CODE),headers = {'Authorization': f"Basic {AUTHORIZATION}"}).json()

# FILTERED GET REQUESTS

def GetTeamSchedule(team_id: int, schedule_type:str = "qual") -> dict:
	return {"Schedule": [match for match in GetSchedule()["Schedule"] if team_id in [team["teamNumber"] for team in match["teams"]]]}

def GetMatch(match_id: int, match_type:str = "qual") -> dict:
	return [match for match in GetAllMatches()["MatchScores"] if match["matchNumber"] == match_id][0]