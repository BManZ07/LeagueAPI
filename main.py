from lib.module import bmAPI
import config as cfg

summoner_name = input("Enter Summoner Name: ")
res = bmAPI(cfg.apiKey, summoner_name)
print(res.summoner_rankings())

ask_champ = input("Would you like to see champion stats? Y | N ")
ask_champ = ask_champ.lower()
if ask_champ == "yes" or ask_champ == "y":
    champ = input("Enter Champion: ")
    champ_num = list(cfg.champion_ids.keys())[list(cfg.champion_ids.values()).index(champ)] # credit Stênio Elson for finding value from key
    print(res.champion_data(champ_num))


status = input("Would you like to know the current server status? Y | N ")
status = status.lower()
if status == "yes" or status == "y":
    print(res.status())

    


