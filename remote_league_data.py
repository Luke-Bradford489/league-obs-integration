import json
import requests
import os
from dotenv import load_dotenv, dotenv_values 
import datetime

from models.match_v5 import MatchDto, TimelineDto

from models.search_match_model import SearchMatchModel

now = datetime.datetime.now()
load_dotenv() 

class RemoteClient:
    def __init__(self, *args, **kwargs):
        region_url = kwargs.get('region_url', None)
        account_url = kwargs.get('account_url', None)
        match_url = kwargs.get('match_url', None)
        self.region_url = region_url if region_url is not None else "https://euw1.api.riotgames.com"  
        self.account_url = account_url if account_url is not None else "https://developer.riotgames.com/api-methods/execute" 
        self.match_url = match_url if match_url is not None else "https://europe.api.riotgames.com" 
        self.headers = {"X-Riot-Token": os.getenv("API_KEY")}

    def add_to_file(self, data, filename):
        if not os.path.exists("out"):
            os.makedirs("out")
        with open(os.path.join("out", f'{filename}.json'), 'w') as json_file:
            json.dump(data, json_file, indent=4)  # 'indent' makes the output more readable

    def get_match(self, match_id)-> MatchDto:
        result = requests.get(f"{self.match_url}/lol/match/v5/matches/{match_id}", verify=False, headers=self.headers).json()
        return MatchDto(**result)


    def get_timeline(self, match_id) -> TimelineDto:
        result = requests.get(f"{self.match_url}/lol/match/v5/matches/{match_id}/timeline", verify=False, headers=self.headers).json()
        return TimelineDto(**result)

    def get_riot_id(self, **kwargs):
        name = kwargs.get("name", None)
        if name and name.find('#')!=-1 :
            display_name, tag = name.split('#')
            print(f"Split name: {display_name} and {tag}")
            return requests.get(f"https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{display_name}/{tag}", verify=False, headers=self.headers).json()['puuid']
        elif name and name.find('#')==-1:
            tag = kwargs.get("tag", None)
            if tag:
                return requests.get(f"https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{name}/{tag}", verify=False, headers=self.headers).json()['puuid']
        else:
            raise Exception("Shits fucked yo, wrong name or tag")


    def search_matches(self, puuid, search_model:SearchMatchModel) -> list[str]:    
        return requests.get(f"{self.match_url}/lol/match/v5/matches/by-puuid/{puuid}/ids", verify=False, headers=self.headers, params=search_model.toJson()).json()


    def get_user(self,puuid):
        return requests.get(f"https://europe.api.riotgames.com/riot/account/v1/accounts/by-puuid/{puuid}", verify=False, headers=self.headers).json()
    

if __name__ == "__main__":
    client = RemoteClient()
    match_list = ['EUW17147272890' ,
'EUW17147340510' ,
'EUW17147430681']

    for i in match_list:
        match = client.get_match(i)
        client.add_to_file(match, i)