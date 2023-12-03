relative = [
    "allInPings",
    "assistMePings",
    "assists",
    "baitPings",
    "basicPings",
    "bountyLevel",
    "commandPings",
    "champLevel",
    "consumablesPurchased",
    "damageDealtToBuildings",
    "damageDealtToObjectives",
    "damageDealtToTurrets",
    "damageSelfMitigated",
    "dangerPings",
    "deaths",
    "doubleKills",
    "enemyMissingPings",
    "enemyVisionPings",
    "itemsPurchased",
    "killingSprees",
    "kills",
    "largestKillingSpree",
    "largestMultiKill",
    "longestTimeSpentLiving",
    "getBackPings",
    "goldEarned",
    "goldSpent",
    "holdPings",
    "needVisionPings",
    "neutralMinionsKilled",
    "objectivesStolen",
    "objectivesStolenAssists",
    "onMyWayPings",
    "pentaKills",
    "pushPings",
    "quadraKills",
    "timeCCingOthers",
    "totalAllyJungleMinionsKilled",
    "totalDamageDealtToChampions",
    "totalDamageShieldedOnTeammates",
    "totalDamageTaken",
    "totalEnemyJungleMinionsKilled",
    "totalHeal",
    "totalHealsOnTeammates",
    "totalMinionsKilled",
    "totalTimeSpentDead",
    "totalUnitsHealed",
    "tripleKills",
    "turretKills",
    "turretTakedowns",
    "visionClearedPings",
    "visionScore",
    "visionWardsBoughtInGame",
    "wardsKilled",
    "wardsPlaced"]

relative_onehot = [
    "firstBloodAssist",
    "firstBloodKill",
    "firstTowerAssist",
    "firstTowerKill",] #위 네개는 ture,false로 돼있음

relative_total = [ "inhibitorsLost","turretsLost"]

team_first_factors = ['baron','dragon','inhibitor', 'riftHerald']

unrelative =["championId", "championName"]

need_additional_process = ["챔피언 픽", "룬 정보",
                           "summoner1Casts",  #스펠 사용 횟수
                           "summoner1Id",   #스펠 아이디
                           "summoner2Casts",
                           "summoner2Id",
                           "item0",
                           "item1",
                           "item2",
                           "item3",
                           "item4",
                           "item5",
                           "item6",]

team_factors = [
    "turretsLost",
]

target = "win"
team_id = ["teamID"]
team_position = ["teamPosition"]
