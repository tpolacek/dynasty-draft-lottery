__author__ = 'tpolace2'

class Team():
    """holds info on a team object"""
    winning_combos = []
    wpct = 0.0
    odds_of_winning = 0.0

    #constructor
    def __init__(self, name, owner, prev_win, prev_loss, prev_tie, prev_points):
        self.name = name
        self.owner = owner
        self.prev_win = prev_win
        self.prev_loss = prev_loss
        self.prev_tie = prev_tie
        self.prev_points = prev_points
        self.wpct = self.calc_win_pct(self.prev_win, self.prev_loss, self.prev_tie)

    #get winning percentage
    def calc_win_pct(self, wins, losses, ties):
        #find total number of games
        total_games = float(wins + losses + ties)

        #add in ties as half win half loss
        if ties > 0:
            halves = float(ties / 2.0)
            wins = float(wins + halves)
            losses = float(losses + halves)

        #calculate wpct and return value
        wpct = float(wins / total_games)
        return float(wpct)

    #comparator function for team wpct
    #def __cmp__(self, team2):
    #    if self.wpct > team2.wpct:
    #        return 1
    #    elif self.wpct < team2.wpct:
    #        return -1
    #    elif self.wpct == team2.wpct:
    #        if self.prev_points > team2.prev_points:
    #            return 1
    #        elif self.prev_points < team2.prev_points:
    #            return -1
    #    else:
    #        return 0

    #return a string with all pertinent draft information for the team
    def show_draft_info(self):
        info = self.name + " draft information:\n" + \
                "Team owner:\t" + self.owner + "\n" + \
                "Previous record:\t" + \
                str(self.prev_win) + "-" + str(self.prev_loss) + "-" + str(self.prev_tie) + "\n" + \
                "Winning lottery combinations:\n" + str(self.winning_combos) + "\n" + \
                "Odds of winning draft lottery:\n" + str((self.odds_of_winning)*100) + "%\n"

        return info

    # new set of comparator functions that work in python3
    def __eq__(self, team2):
        return (self.wpct == team2.wpct)

    def __ne__(self, team2):
        return not (self.wpct == team2.wpct)

    def __lt__(self, team2):
        if self.wpct == team2.wpct:
            return (self.prev_points < team2.prev_points)
        else:
            return (self.wpct < team2.wpct)
        
    def __le__(self, team2):
        if self.wpct == team2.wpct:
            return (self.prev_points <= team2.prev_points)
        else:
            return (self.wpct <= team2.wpct)

    def __gt__(self, team2):
        if self.wpct == team2.wpct:
            return (self.prev_points > team2.prev_points)
        else:
            return (self.wpct > team2.wpct)

    def __ge__(self, team2):
        if self.wpct == team2.wpct:
            return (self.prev_points >= team2.prev_points)
        else:
            return (self.wpct >= team2.wpct)

