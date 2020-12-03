import requests
def getNumDraws(year):
    page=1
    draw=0
    for j in range(0, 11):
        res = requests.get("https://jsonmock.hackerrank.com/api/football_matches?year=" + str(year) + "&page=1&team1goals=" + str(j) + "&team2goals=" + str(j)).json()
        pages=res["total_pages"]
        draw += len(res["data"])
        for i in range(2,pages+1):
            res = requests.get("https://jsonmock.hackerrank.com/api/football_matches?year=" + str(year) + "&page="+str(i)+"&team1goals=" + str(j) + "&team2goals=" + str(j)).json()
            draw += len(res["data"])
    return draw
print(getNumDraws(2011))