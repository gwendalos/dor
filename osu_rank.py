import discord, time, requests, subprocess, json
from pypresence import Presence

with open('config.json') as file:
    config = json.load(file)

while True:
    subprocess.call("cls", shell=True)
    req = requests.get(f'https://osu.ppy.sh/api/get_user?&k={config["key"]}&u={config["username"]}')
    f = req.json()
    country = str(f[0]['country'])
    flag = country.swapcase()
    pp_rank = str(f[0]['pp_rank'])
    pp_country_rank = str(f[0]['pp_country_rank'])
    RPC = Presence('900798384942743603')
    RPC.connect()
    RPC.update(state=f"Global Rank: {pp_rank}\nCountry Rank: {pp_country_rank}", large_image='large', large_text=f'Global: {pp_rank}', small_image=f'{flag}', small_text=f'Country: {pp_country_rank}', start=time.time())
    print("Loaded")
    time.sleep(10)