import csv
import json
import os
import time
import requests

api_key = 'RGAPI-5f59d95b-ab8a-421f-8488-35c9a20628a9'
headers = {"X-Riot-Token": api_key}

def check_summoner_exists(summoner_name):
    global headers
    summoner_base_url = "https://kr.api.riotgames.com"
    summoner_endpoint = f"/lol/summoner/v4/summoners/by-name/{summoner_name}"
    response = requests.get(summoner_base_url + summoner_endpoint, headers=headers)
    summoner_data = response.json()
    if response.status_code != 200:
        return None
    else:
        return summoner_data['puuid']

def get_recent_match(summoner_puuid):
    global headers
    match_base_url = 'https://asia.api.riotgames.com'
    matches_endpoint = f"/lol/match/v5/matches/by-puuid/{summoner_puuid}/ids?startTime=1699514445&queue=420&count=100"
    response = requests.get(match_base_url + matches_endpoint, headers=headers)
    matches_data = response.json()
    data = []
    if response.status_code != 200:
        print("Error")
        return None
    else:
        for i in matches_data:
            data.append(i)
        return data

def get_puuid_from_summoerid(encryptedSummonerId):
    global headers
    summoner_base_url = "https://kr.api.riotgames.com"
    summoner_endpoint = f"/lol/summoner/v4/summoners/{encryptedSummonerId}"
    response = requests.get(summoner_base_url + summoner_endpoint, headers=headers)
    summoner_data = response.json()
    if response.status_code != 200:
        print(response.status_code)
        return None
    else:
        return summoner_data["puuid"]

def get_challengers_summonerid():
    global headers
    summoner_base_url = "https://kr.api.riotgames.com"
    summoner_endpoint = f"/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5"
    response = requests.get(summoner_base_url + summoner_endpoint, headers=headers)
    summoner_data = response.json()
    if response.status_code != 200:
        print(response.status_code)
        return None
    else:
        return summoner_data["entries"]
def check_summoner_by_puuid(puuid):
    global headers
    summoner_base_url = "https://kr.api.riotgames.com"
    summoner_endpoint = f"/lol/summoner/v4/summoners/by-puuid/{puuid}"
    response = requests.get(summoner_base_url + summoner_endpoint, headers=headers)
    summoner_data = response.json()
    if response.status_code != 200:
        return None
    else:
        return summoner_data["id"]

def check_summoner_league_by_id(id):
    global headers
    summoner_base_url = "https://kr.api.riotgames.com"
    summoner_endpoint = f"/lol/league/v4/entries/by-summoner/{id}"
    response = requests.get(summoner_base_url + summoner_endpoint, headers=headers)
    summoner_data = response.json()
    if response.status_code != 200:
        return None
    else:
        return summoner_data[0]["tier"]

def get_match_data(match_id):
    global headers
    match_base_url = 'https://asia.api.riotgames.com'
    matches_endpoint = f"/lol/match/v5/matches/{match_id}"
    response = requests.get(match_base_url + matches_endpoint, headers=headers)
    matches_data = response.json()
    return matches_data

id = check_summoner_by_puuid("snIrSQDEC4F6FrlrZssMdH41jnR3WeU1-yOR3bqRy5coi3rWPDrDKolu2AYvr5TNJvVL8uQuMU4ihQ")
print(id)
print(check_summoner_league_by_id(id))