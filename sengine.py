from models import (Team, Game, Player)

#gender,experience,position,name=[],nick='',starter=0
players1 = [] 
players1.append(Player('M',2,1,['Thun','Jon'],'',1))
players1.append(Player('M',2,2,['Jami','Nick'],'',1))
players1.append(Player('M',3,3,['Jones','Relando'],'',1))
players1.append(Player('F',0,4,['Greigo','Dee'],'',1))
players1.append(Player('M',4,5,['Ellis','Elister'],'',1))
players1.append(Player('M',3,6,['Greigo','Dan'],'',1))
t1 = Team('aTeam',players1,1)
#print('AWAY TEAM')
#print(t1)
#print(t1.show_lineup())
players2 = []
players2.append(Player('F',0,1,['Greemzehese','Tonka'],'',1))
players2.append(Player('F',1,2,['Sou','Natisha'],'',1))
players2.append(Player('F',2,3,['Smith','Sue'],'',1))
players2.append(Player('F',2,4,['Grey','Shea'],'',1))
players2.append(Player('F',3,5,['Martiz','Amber'],'',1))
players2.append(Player('F',3,6,['Jackson','Toyia'],'',1))
t2 = Team('hTeam',players2,2)
#print('HOME TEAM')
#print(t2)
#print(t2.show_lineup())
game1 = Game(t1,t2)
game1.start_game()

#START HERE
def count_all():
    print("TEAM01: {a} |Counts: {b}".format(a=t1.name,b=t1.counts))
    print("TEAM02: {a} |Counts: {b}\n".format(a=t2.name,b=t2.counts))

count_all()
'''
game1 = Game(t1,t2)

stadium = Board(game1)

""" for s in range(2):
    for i in range(10):
        stadium.count()

    print("TEAM: {a} |Counts: {b}".format(a=stadium.team_up.name,b=stadium.team_up.counts))
    stadium.next_team()
 """

stadium.count()
stadium.count()
stadium.count()

print(stadium.get_hero_status())
#stadium.hero_run.activate()
stadium.team_circled()
for s in range(3):
    stadium.count()
print('has scored: ' + str(stadium.has_scored()))

print('# run 1')
print(stadium.get_hero_status())
stadium.hero_run.found_wall()
for s in range(6):
    stadium.count()
print(stadium.get_hero_status())
stadium.team_circled()

print('# run 2')
print(stadium.get_hero_status())
stadium.hero_run.found_wall()
for s in range(6):
    stadium.count()
print(stadium.get_hero_status())
stadium.team_circled()

print('# run 3')
print(stadium.get_hero_status())
stadium.hero_run.found_wall()
for s in range(6):
    stadium.count()
stadium.special_count()
print(stadium.get_hero_status())
stadium.team_circled()

print('# run 4')
#print(stadium.get_hero_status())
stadium.hero_run.found_wall()
for s in range(2):
    stadium.count()
print(stadium.get_hero_status())
#stadium.catch(2)
stadium.team_circled()
print(stadium.get_hero_status())


print(stadium)

count_all()
'''



""" #See wall
stadium.hero_run.saw_wall = True
print(stadium.get_hero_status())
stadium.team_circled()
print(stadium.get_hero_status())
print("\nTEAM01: {a} |Counts: {b}".format(a=t1.name,b=t1.counts))
print("TEAM02: {a} |Counts: {b}\n".format(a=t2.name,b=t2.counts))
 """
    
