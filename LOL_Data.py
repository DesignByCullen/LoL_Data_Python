import pandas as pd
import pandas.io.json as json
from datetime import datetime
pd.set_option('display.max_rows', 1000) 
pd.set_option('display.max_columns', 1000) 
 
matches1  = pd.read_json("matches1.json",  orient='records')
matches2  = pd.read_json("matches2.json",  orient='records')
matches3  = pd.read_json("matches3.json",  orient='records')
matches4  = pd.read_json("matches4.json",  orient='records')
matches5  = pd.read_json("matches5.json",  orient='records')
matches6  = pd.read_json("matches6.json",  orient='records')
matches7  = pd.read_json("matches7.json",  orient='records')
matches8  = pd.read_json("matches8.json",  orient='records')
matches9  = pd.read_json("matches9.json",  orient='records')
matches10 = pd.read_json("matches10.json", orient='records')
 
matches = pd.concat([matches1, matches2, matches3, matches4, matches5, matches6, matches7, matches8, matches9, matches10], ignore_index = True)
 
matchdata = pd.read_json((matches['matches']).to_json(), orient='index')
 
teamdata = json.json_normalize(data = matches['matches'], record_path='teams', meta=['gameId','mapId','gameDuration'])
 
def partres(value):
    game = value['gameId']
    team = value['teamId']
    result = ""
     
    gamedata = matchdata[matchdata['gameId'] == game]
     
    for i in range(0, 10):
        if gamedata.iloc[0]['participants'][i]['teamId'] == team:
            result = result + str(gamedata.iloc[0]['participants'][i]['championId']) + " "
     
    return result
 
teamdata["champions"] = teamdata.apply(partres, axis=1)
 
#
     
teamdata_ex1 = json.json_normalize(data = matches['matches'], record_path='teams', meta=['gameId','mapId','gameDuration', 'gameCreation'])
 
teamdata_ex1["gameDuration"].mean()
 
#
 
def unixTimeToReadableDate(value):
    ts = value["gameCreation"]
    return datetime.fromtimestamp(ts / 1000)
 
teamdata_ex1["GameStart"] = teamdata_ex1.apply(unixTimeToReadableDate, axis=1)
 
#
 
teamdata_ex2 = json.json_normalize(data = matches['matches'], record_path='teams', meta=['gameId'])
 
#
 
teamdata_ex2["baronKills"].mean()
teamdata_ex2["dragonKills"].mean()
teamdata_ex2["inhibitorKills"].mean()
teamdata_ex2["riftHeraldKills"].mean()
teamdata_ex2["towerKills"].mean()
teamdata_ex2["vilemawKills"].mean()
 
#average kills for each boss in each game
 
teamdata_ex2.groupby("gameId")["baronKills"].mean()
teamdata_ex2.groupby("gameId")["dragonKills"].mean()
teamdata_ex2.groupby("gameId")["inhibitorKills"].mean()
teamdata_ex2.groupby("gameId")["riftHeraldKills"].mean()
teamdata_ex2.groupby("gameId")["towerKills"].mean()
teamdata_ex2.groupby("gameId")["vilemawKills"].mean()
 
#average kills for each boss in by team
 
teamdata_ex2.groupby("teamId")["baronKills"].mean()
teamdata_ex2.groupby("teamId")["dragonKills"].mean()
teamdata_ex2.groupby("teamId")["inhibitorKills"].mean()
teamdata_ex2.groupby("teamId")["riftHeraldKills"].mean()
teamdata_ex2.groupby("teamId")["towerKills"].mean()
teamdata_ex2.groupby("teamId")["vilemawKills"].mean()
 
#% of teams who kill 0, 1, 2, or all 3 bosses in a game
 
# function to take a dataframe row as 'value' and return number of boss types killed
def numBossTypesKilled(value):
     
    bossTypesKilled = 0
     
    if (value["dragonKills"] > 0): 
        bossTypesKilled += 1
         
    if (value["baronKills"] > 0): 
        bossTypesKilled += 1
         
    if (value["riftHeraldKills"] > 0): 
        bossTypesKilled += 1
         
    return bossTypesKilled
 
# apply above function to the ex2 dataframe
teamdata_ex2["BossTypesKilled"] = teamdata_ex2.apply(numBossTypesKilled, axis=1)
 
# loop to calc percentages and print out the results
for i in range(0, 4):
 
    killedIBossTypes = teamdata_ex2[teamdata_ex2["BossTypesKilled"] == i]    
     
    pct = (len(killedIBossTypes.index) / len(teamdata_ex2.index)) * 100
     
    print("Killed", i, "bosses:", pct)
 
# dragonkills to baronkills correlation is 0.422
 
teamdata_ex2.corr()
 
#do teams who get more firsts win mopre of the time?
 
# function to take a dataframe row as 'value' and return number of firsts
def numFirsts(value):
     
    firsts = 0
     
    if (value["firstBaron"] == True): 
        firsts += 1
         
    if (value["firstBlood"] == True): 
        firsts += 1
         
    if (value["firstDragon"] == True): 
        firsts += 1
 
    if (value["firstInhibitor"] == True): 
        firsts += 1
 
    if (value["firstRiftHerald"] == True): 
        firsts += 1
 
    if (value["firstTower"] == True): 
        firsts += 1
         
    return firsts
 
# make new ex3 dataframe
teamdata_ex3 = json.json_normalize(data = matches['matches'], record_path='teams')
 
# apply above function to the ex3 dataframe
teamdata_ex3["NumFirsts"] = teamdata_ex3.apply(numFirsts, axis=1)
 
# loop to calc percentages and print out the results
for i in range(0, 7):
     
    firstsData = teamdata_ex3[teamdata_ex3["NumFirsts"] == i]
     
    winData  = firstsData[firstsData["win"] == "Win"]
    loseData = firstsData[firstsData["win"] == "Fail"]
     
    pctWin  = (len(winData.index)  / len(firstsData.index)) * 100
    pctLose = (len(loseData.index) / len(firstsData.index)) * 100
     
    print("Firsts:", i, ",Win:", pctWin, ",Lose:", pctLose)
    
    
    
    def GoldEarned(valvue):
        
    
    
    
    
    
    