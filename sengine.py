from models import (Board, Team, Game, Player)

#gender,experience,position,name=[],nick='',starter=0
players1 = []
players1.append(Player('M',2,1,['Thun','Jon'],'',1))
players1.append(Player('M',2,2,['Jami','Nick'],'',1))
players1.append(Player('M',3,3,['Jones','Relando'],'',1))
players1.append(Player('F',0,4,['Greigo','Dee'],'',1))
players1.append(Player('M',4,5,['Ellis','Elister'],'',1))
players1.append(Player('M',3,6,['Greigo','Dan'],'',1))
t1 = Team('Test1',players1,1)
print(t1)
print(t1.show_lineup())
'''
tip1 = Player('M',2,1,['Thun','Jon'],'',1)
p1 = ['t.jon','t.jen','t.jim']
t1 = Team('Test1',p1,1)

tip2 = Player('F',1,1,['Gomez','Monica'],'',1)
p2 = ['t.gina','t.gino','t.gama']
t2 = Team('Test2',p2,2)
'''

'''START HERE
def count_all():
    print("TEAM01: {a} |Counts: {b}".format(a=t1.name,b=t1.counts))
    print("TEAM02: {a} |Counts: {b}\n".format(a=t2.name,b=t2.counts))

count_all()
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
    
