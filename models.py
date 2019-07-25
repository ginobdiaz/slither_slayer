
class Player:
    """
    For teams
    """
    def __init__(self,gender,experience,position,name=[],nick='',starter=0):
        self.name = name
        self.first_name = name[1]
        self.last_name = name[0]
        self.position = position
        self.experience = experience
        self.starter = starter
        self.gender = gender
        self.nick = nick
        self.league_rank = 0
        self.conference_rank = 0
        self.scores = 0
        self.counts = 0
        self.caught = 0
        self.circles = 0
        self.traps = 0
        self.good2b_kings = 0
        self.killed_kings = 0

    def __str__(self):
        return "{a},{b} \t\t|POS: {c} |EXP: {d} |TRP: {f} |GEN: {e}".format(a=self.last_name,b=self.first_name,c=self.position,d=self.experience,e=self.gender,f=self.caught)

class Team:
    """        
    For conference and players
    """        
    def __init__(self,name='',players=[],tid=0,colors=''):
        self.name = name
        self.players = players
        self.tid = tid
        self.colors=colors
        self.logo = ''
        self.home = False
        self.league_rank = 0
        self.conference_rank = 0
        self.scores = 0
        self.counts = 0
        self.caught = 0
        self.circles = 0
        self.traps = 0
        self.good2b_kings = 0
        self.killed_kings = 0
        self.record = {'WIN': 0, 'LOST': 0, 'TIE': 0}
        self.last_played_on = None
        self.last_position_played = None
        self.lineup = {'Tip':'', 'Blade':'','Spine':'','Spinner':'','Nocker':'','Shooter':''}
        
        pos_key = ''
        for player in players:
            pos_key = self.position_num_to_key(player.position)

            if pos_key in self.lineup.keys():
                self.lineup[pos_key] = player

    def position_num_to_key(self, arg):
        switcher = {
            1: "Tip",
            2: "Blade",
            3: "Spine",
            4: "Spinner",
            5: "Nocker",
            6: "Shooter"
        }
        return switcher.get(arg,"no-go")

    def show_lineup(self):
        line = 'Arrowhead\n'
        line += "Tip    : {a}\n".format(a=self.lineup.get('Tip','-'))
        line += "Blade  : {a}\n\n".format(a=self.lineup.get('Blade','-'))
        line += "Shaft\n"
        line += "Spine  : {a}\n".format(a=self.lineup.get('Spine','-'))
        line += "Spinner: {a}\n\n".format(a=self.lineup.get('Spinner','-'))
        line += "Nock\n"
        line += "Nocker : {a}\n".format(a=self.lineup.get('Nocker','-'))
        line += "Shooter: {a}\n\n".format(a=self.lineup.get('Shooter','-'))
        return line            

    def __str__(self):
        return "{a}\n\n".format(a=self.name)


class Conference:
    '''
    For league
    '''
    def __init__(self,name,teams=[]):
        self.name = name
        self.teams = teams
        self.league_rank = 0
        self.conference_rank = 0
        self.reserve_players=[]
        self.injured_players=[]
        self.games = []
        self.logo = ''
        self.loc = ''

    def __str__(self):
        return self.name

class League:
    '''
    For conference
    '''
    def __init__(self,name):
        self.name = name
        self.conferences=[]
        self.seasons=[]
        self.league_rank = 0
        self.conference_rank = 0
        self.logo = ''

class Season:
    '''
    For games
    '''
    def __init__(self,name):
        self.name = name
        self.season_date = None
        self.season_id=0
        self.games=[]
        self.league_ranks = []

class Game:
    '''
    For teams
    '''
    lineup = {1:'Tip',2:'Blade',3:'Spine',4:'Spinner',5:'Nocker',6:'Shooter'}
    team_up = None
    player_up = None

    def __init__(self,away_team,home_team):
        self.away_team = away_team
        self.home_team = home_team
        self.away_counts=0
        self.home_counts=0
        self.away_score=0
        self.home_score=0
        self.season_id=0
        self.game_id=0
        self.home_team.home = True
        self.curr_player = None
        self.away_circled = False
        self.home_circled = False
        self.when = None
        self.on_field = '-'
        self.player_on = 0
        self.next_team()
        self.next_player()

    def next_player(self):

        if self.player_on < 6:
            self.player_on += 1
            if Game.team_up.home:
                self.home_team.last_position_played = Game.lineup.get(self.player_on,'-')
            else:
                self.away_team.last_position_played = Game.lineup.get(self.player_on,'-')
        else:
            if Game.team_up.home == False:
                self.next_team()

    def next_team(self):
        if self.player_on == 0 and Game.team_up is None:
            Game.team_up = self.away_team
            self.on_field = 'away'
        else:
            if team_up.home:
                self.home_team.counts = team_up.counts
                Game.team_up = self.away_team
                self.on_field = 'away'
            else:
                self.away_team.counts = team_up.counts
                Game.team_up = self.home_team
                self.on_field = 'home'
            
            '''self.round += 1     '''

class Board:
    '''
    For game control
    '''
    team_up = None
    player_up = None

    def __init__(self,game,contest='standard'):
        self.contest = contest
        self.game = game
        self.slay_king = False
        self.king = False
        self.circled = False
#        self.hero_qual = {'H1':False,'H2':False,'H3':False,'H4':False}
        self.status = 'not started'
        self.round = 0
        self.board_count = 0
        self.hero_run = Hero()
        self.next_team()

    def next_team(self):
        if self.round == 0:
            Board.team_up = self.game.away_team
        else:
            if Board.team_up.home:
                self.game.home_team.counts = Board.team_up.counts
                Board.team_up = self.game.away_team
            else:
                self.game.away_team.counts = Board.team_up.counts
                Board.team_up = self.game.home_team
            
            self.round += 1     

    def count(self, cnt=1):
        if self.hero_run.active_run() and not self.hero_run.saw_wall:
            return
        
        if isinstance(Board.team_up, Team):
            if self.has_scored():
                # the 'not self.hero_run.active_run()' means it's an anti-hero run
                # the 'self.hero_run.can_kill()' means it's a qual-hero run
                if (not self.hero_run.active_run()) or (self.hero_run.can_kill()):
                    self.team_scored()
            elif Board.team_up.counts < 6 and (not self.hero_run.active_run() or self.hero_run.can_kill()):
                Board.team_up.counts += self.board_count
                self.board_count = 0
                if (Board.team_up.counts + cnt) > 6:
                    cnt = 6 - Board.team_up.counts
                Board.team_up.counts += cnt
                self.hero_run.accum_count(cnt)
                if Board.team_up.counts == 6:
                    self.count()

    def catch(self,snakes=1):
        for i in range(snakes*2):
            self.count()

    def team_circled(self):
        if isinstance(Board.team_up, Team):
            if ((not self.hero_run.active_run() or self.hero_run.can_circle()) and not self.circled):
                self.circled = True
                Board.team_up.circles += 1

            if (self.has_scored()):
                self.team_scored()

    def has_scored(self):
        return Board.team_up.counts >= 6 and self.circled

    def special_count(self):
        self.board_count += 1
        if  Board.team_up.counts < 6 and (not self.hero_run.active_run() or self.hero_run.can_kill()):
            cnt = self.board_count
            self.board_count = 0
            for i in range(cnt):
                self.count()
        
    def team_scored(self):
        if Board.team_up.home:
            self.game.home_team.scores += 1
#            print(self.game.home_team.scores)
        else:
            self.game.away_team.scores += 1
#            print(self.game.away_team.scores)

        self.hero_run.activate(self.has_scored())
        if self.hero_run.active_run():
            self.circled = False
            Board.team_up.counts = 0

    def get_hero_status(self):
        print(self.hero_run)

    def __str__(self):
        return "current count: {}\tcircled? {}\nAway: {} - Home: {}".format(Board.team_up.counts,self.circled,self.game.away_team.scores,self.game.home_team.scores)
    
class Hero:
    def __init__(self):
        self.active = False
        self.run = 1
        self.saw_wall = False
        self.deactive = False
        self.is_hero = False
        self.team_up_counts = 0

    def activate(self,is_qual_hero=False):
        if self.deactive or not is_qual_hero:
            return False
        elif self.run >= 4:
            self.deactive = True
            self.is_hero = True
            return False

        if self.active:
            self.run += 1
        else:
            self.active = True
        
        self.is_hero = False
        self.saw_wall = False
        self.team_up_counts = 0

        return True

    def active_run(self):
        if (self.active and not self.deactive):
            return True
        
        return False

    def accum_count(self,by=1):
        if self.can_kill():
            self.team_up_counts += by

    def can_circle(self):
        if self.active_run() and self.saw_wall and self.team_up_counts >= 6:
            return True
        
        return False

    def can_kill(self):
        if self.active_run() and self.saw_wall and self.team_up_counts < 6 :
            return True

        return False

    def found_wall(self):
        self.saw_wall = True
        #check for special counts

    def found_circle(self):
        if self.can_circle() and not self.is_hero:
            self.activate(True)

    def __str__(self):
        status = "Anti-Hero"
        if self.active_run() and not self.is_hero:
            status = "Qual-Hero"
        elif self.is_hero:
            status = "A Hero"

        msg = "\nTitle: {}\n".format(status)
        msg += "Hero Run:    {}\n".format(self.run)
        msg += "Saw Wall?:   {}\n".format(self.saw_wall)
        msg += "Can Kill?:   {}\n".format(self.can_kill())
        msg += "Kill Count:  {}\n".format(self.team_up_counts)
        msg += "Can Circle?: {}\n".format(self.can_circle())
        if self.deactive:
            msg += "\nAll Hero runs accomplished. You are a HERO!"
        
        return msg
        

