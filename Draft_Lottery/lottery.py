__author__ = 'tpolace2'
import team
import random

class Lottery():
    lotto_balls = range(1, 101)
    standings = []

    # constructor
    def __init__(self, teams):
        self.teams = teams

    # calculate previous standings
    def make_standings(self):
        # add each team to the standings list
        for team in self.teams:
            self.standings.append(team)

        # sort standings by win percentage
        self.standings.sort()
        return self.standings

    # method to get each team's winning combos, and set odds
    def set_team_combos(self):
        balls = range(1,101)

        # define set of lotto combos for the team
        self.standings[0].winning_combos = random.sample(balls, 25)
        # remove combos from available pool
        balls = [x for x in balls if x not in self.standings[0].winning_combos]
        # determine odds of winning for each team
        self.standings[0].odds_of_winning = \
            float(len(self.standings[0].winning_combos) / 100.0)

        self.standings[1].winning_combos = random.sample(balls, 22)
        balls = [x for x in balls if x not in self.standings[1].winning_combos]
        self.standings[1].odds_of_winning = \
            float(len(self.standings[1].winning_combos) / 100.0)

        self.standings[2].winning_combos = random.sample(balls, 20)
        balls = [x for x in balls if x not in self.standings[2].winning_combos]
        self.standings[2].odds_of_winning = \
            float(len(self.standings[2].winning_combos) / 100.0)

        self.standings[3].winning_combos = random.sample(balls, 15)
        balls = [x for x in balls if x not in self.standings[3].winning_combos]
        self.standings[3].odds_of_winning = \
            float(len(self.standings[3].winning_combos) / 100.0)

        self.standings[4].winning_combos = random.sample(balls, 10)
        balls = [x for x in balls if x not in self.standings[4].winning_combos]
        self.standings[4].odds_of_winning = \
            float(len(self.standings[4].winning_combos) / 100.0)

        self.standings[5].winning_combos = random.sample(balls, 8)
        balls = [x for x in balls if x not in self.standings[5].winning_combos]
        self.standings[5].odds_of_winning = \
            float(len(self.standings[5].winning_combos) / 100.0)

    # method to determine order of picks
    def run_lottery(self, standings):
        # empty list to store teams in order
        pick_order = []

        # counting variables
        pick = 1
        count = 1

        # empty string to add results to, will return this value
        results = ""

        # loop to get a winning combo, assign team to pick order list and repeat for all teams
        while count <= len(standings):
            # choose random combination from initialized list
            winning_number = random.choice(self.lotto_balls)
            for team in standings:
                for combo in team.winning_combos:
                    if combo == winning_number:
                        # add team to pick order list
                        pick_order.append([team, winning_number])
                        # remove remaining winning combos for the chosen team to avoid repeats
                        self.lotto_balls = [x for x in self.lotto_balls if x not in team.winning_combos]
                        # increment counters
                        pick += 1
                        count += 1
        # counting variable
        order = 1

        # cut off spots 4-6 in the pick order
        pick_order_cutoff = pick_order[:3]

        # update here to only assign top 3 spots in the lottery, and for spots 4-6, use standings
        # add team info to empty string to return to function call
        for entry in pick_order_cutoff:
                results += ("Pick #" + str(order) +
                               ": " + entry[0].name + " - Winning Combination: " + str(entry[1]) + "\n")
                order += 1

        # warn user that window will close
        results += "\n\nProgram will close when you click OK\nPlease make sure to record lottery results"
        return results
