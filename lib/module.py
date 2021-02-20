import json
import requests
import config as cfg

class bmAPI:
    def __init__(self, api_key, summoner_name):
        self.api_key = api_key
        self.summoner_name = summoner_name
    
    def get_summoner_account(self):
        r = requests.get(f"https://oc1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{self.summoner_name}?api_key={cfg.apiKey}")
        data = r.json()
        account_id = data["id"]
        return account_id


    def summoner_info(self):
        r = requests.get(f"https://{cfg.region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{self.summoner_name}?api_key={cfg.apiKey}")
        data = r.json()
        if "id" in data:
            res = "All summoner information has been saved in summoner_info.json"
        else:
            res = "Not a valid user!"

        with open('data\summoner_info.json', 'w') as f:
            json.dump(data, f, sort_keys=True, indent=4)
        return res

    def champion_rotation(self):
        r = requests.get(f"https://{cfg.region}.api.riotgames.com/lol/platform/v3/champion-rotations?api_key={self.summoner_name}")
        data = r.json()
        free_champs = data['freeChampionIds']

        for i in free_champs:
            i = str(i)
            champs = []
            print(cfg.champion_ids[f"{i}"])

            

    def status(self):
        r = requests.get(f"https://{cfg.region}.api.riotgames.com/lol/status/v4/platform-data?api_key={cfg.apiKey}")
        data = r.json()
        with open('data\status.json', 'w') as f:
            json.dump(data, f, sort_keys=True, indent=4)
        res = data['incidents'][0]['titles'][0]['content']
        return f"{res} - More information on server status in status.json"
    

    def summoner_rankings(self):
        r = requests.get(f"https://{cfg.region}.api.riotgames.com/lol/league/v4/entries/by-summoner/{self.get_summoner_account()}?api_key={cfg.apiKey}")
        data = r.json()
        ranked_data = f"""
        Rank: {data[0]['tier']} {data[0]['rank']}
        LP: {data[0]['leaguePoints']}
        Wins: {data[0]['wins']}
        Losses: {data[0]['losses']}
        W/L: {(data[0]['wins'] / (data[0]['losses'] + data[0]['wins'])) * 100}
        """
        return ranked_data
    
    def champion_data(self, champion_id):
        r = requests.get(f"https://{cfg.region}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{self.get_summoner_account()}/by-champion/{champion_id}?api_key={cfg.apiKey}")
        data = r.json()
        champion_data = f"""
        Champion: {cfg.champion_ids[f"{champion_id}"]}
        Points: {data['championPoints']}
        Mastery: {data['championLevel']}
        """
        return champion_data
        

