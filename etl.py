import requests
import json

score_endpoint = 'http://127.0.0.1:5000/scoreboard/%s/%s.json?api_key=%s'
ranking_endpoint = 'http://127.0.0.1:5000/team_rankings.json?api_key=%s'

def query(start, end, key):
    scores = requests.get( score_endpoint % (start,end,key)).json()
    rankings = requests.get(ranking_endpoint % key).json()

    rankidx={}
    for rank in rankings:
        rankidx[rank['team_id']] = rank
   
    ret=[]

    for score in scores:
        score['away_rank'] = rankidx[score['away_team_id']]['rank']
        score['away_rank_points'] = rankidx[score['away_team_id']]['rank_points']
        score['home_rank'] = rankidx[score['home_team_id']]['rank']
        score['home_rank_points'] = rankidx[score['home_team_id']]['rank_points']

        ret.append(score)
        
    return ret

resp = query('2020-01-01','2020-02-01', 'somekey')

print(resp)