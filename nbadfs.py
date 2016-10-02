import csv
'''



'''
#"Position","Name","Salary","GameInfo","AvgPointsPerGame","teamAbbrev"
with open('DKSalaries.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    players = [row for row in csvreader]
    
for player in players:
    player[2] = float(player[2])
    player[4] = float(player[4])

players = [[p[0], p[1], p[2], p[3], p[4], p[5], p[4]/p[2]* 1000] for p in players if p[4] != 0 and p[4]/p[2]* 1000 < 8]

nbalineup = {'C': None, 'PG': None, 'SG': None, 'SF': None, 'PF': None, 'G': None, 'F': None, 'UTIL': None}

nfllineup = {'QB':None,
             'RB1':None,
             'RB2':None,
             'WR1':None,
             'WR2':None,
             'WR3':None,
             'TE':None,
             'FLEX':None,
             'DST':None
            }

lineup=nbalineup

for player in players: 
    for pos in lineup:
        if pos.startswith(player[0]):
            if lineup[pos]==None or lineup[pos][6]<player[6]:
                lineup[pos] = player
                players.remove(player)
                break

for player in players: 
    for pos in lineup:
        if pos != player[0] and pos in player[0]:
            if lineup[pos]==None or lineup[pos][4]<player[4]:
                lineup[pos] = player
                players.remove(player)


lineupsalary = 0
for pos in lineup:
    lineupsalary += lineup[pos][2] if lineup[pos]!=None else 0
leftOver = 50000 - lineupsalary
print(leftOver)
for player in players:
    if player[2]<=leftOver:
        if lineup['UTIL'] == None:
            lineup['UTIL'] = player
        elif  lineup['UTIL'][4] < player[4]:
            lineup['UTIL'] = player
#for player in players:
#    if player[2]<=leftOver:
#        if lineup['FLEX'] == None:
#            lineup['FLEX'] = player
#        elif  lineup['FLEX'][4] < player[4]:
#            lineup['FLEX'] = player            



lineupsalary += lineup['UTIL'][2]

for pos in lineup:
    lineup[pos].pop()
    print(lineup[pos])
    print(lineupsalary)
    
