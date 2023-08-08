import random

class Cricketer:
    def __init__(self, name, bowling, batting, fielding, running, experience):
        self.name = name
        self.bowling = bowling
        self.batting = batting
        self.fielding = fielding
        self.running = running
        self.experience = experience

class CricketTeam:
    def __init__(self, name, players):
        self.name = name
        self.players = players
        self.captain = None
        self.batting_order = players.copy()
        self.bowlers = []

    def select_captain(self, captain):
        self.captain = captain

    def select_next_batsman(self):
        if len(self.batting_order) > 0:
            return self.batting_order.pop(0)
        return None

    def select_bowler(self):
        if len(self.bowlers) > 0:
            return random.choice(self.bowlers)
        return None

    def select_next_bowler(self):
        bowler = self.select_bowler()
        while bowler is None:
            bowler = self.select_bowler()
        return bowler


class CricketField:
    def __init__(self, size, fan_ratio, pitch_conditions, home_advantage):
        self.size = size
        self.fan_ratio = fan_ratio
        self.pitch_conditions = pitch_conditions
        self.home_advantage = home_advantage

class CricketUmpire:
    def __init__(self, field):
        """
        Initialize a CricketUmpire object with the provided attributes.
        
        Args:
            field (CricketField): The CricketField object representing the field conditions.
        """
        self.field = field
        self.runs = 0
        self.wickets = 0
        self.overs = 0

    def update_score(self, runs):
        """
        Update the score based on the runs scored.
        
        Args:
            runs (int): The runs scored in the ball.
        """
        self.runs += runs

    def update_wickets(self):
        """
        Update the wickets count.
        """
        self.wickets += 1

    def update_overs(self):
        """
        Update the overs count.
        """
        self.overs += 1

    def predict_outcome(self, batsman, bowler):
        """
        Predict the outcome of a ball based on batsman and bowler stats.
        
        Args:
            batsman (CricketPlayer): The CricketPlayer object representing the batsman.
            bowler (CricketPlayer): The CricketPlayer object representing the bowler.
        
        Returns:
            str: The outcome of the ball (either "OUT" or "NOT OUT").
        """
        batting_prob = batsman.batting * self.field.pitch_conditions * random.random()
        bowling_prob = bowler.bowling * self.field.pitch_conditions * random.random()
        if batting_prob > bowling_prob:
            return "OUT"
        return "NOT OUT"


class CricketCommentator:
    def __init__(self, umpire):
        self.umpire = umpire

    def get_ball_description(self, batsman, bowler):
        outcome = self.umpire.predict_outcome(batsman, bowler)
        if outcome == "OUT":
            description = f"{batsman.name} is OUT!"
        else:
            description = f"{batsman.name} plays the shot."
        return description

    def describe_match_start(self, team_name):
        print(f"\n---- {team_name} Batting ----\n")

    def describe_match_end(self):
        print(f"\nFinal Score: {self.umpire.score}/{self.umpire.wickets} in {self.umpire.overs} overs")

    def describe_final_result(self, winner_name, winning_score):
        print(f"\n---- {winner_name} wins by {winning_score} runs ----\n")

    def describe_game(self, captain1, captain2, country1, country2, over):
        """
        Provide a description of the cricket match.
        
        Args:
            captain1 (str): The name of the captain of the first team.
            captain2 (str): The name of the captain of the second team.
            country1 (str): The name of the first team.
            country2 (str): The name of the second team.
            over (int): The total number of overs in the match.
        """
        print("\n--------- Game Information ---------\n")
        print(f"{country1} Vs {country2}")
        print(f"Captain 1 : {captain1}, Captain 2 : {captain2}")
        print(f"Over : {over}")
        print("\n---------------------------------------------\n")

    def describe_start(self, team):
        """
        Provide a description of the start of an innings.
        
        Args:
            team (str): The name of the team currently batting.
        """
        print("\n------------- GAME STARTED ------------------\n")
        print(f"Team {team} playing: ")
    
    def describe_end(self):
        """
        Provide a description of the end of an innings.
        """
        print(f"\n\nFinal Run: {self.umpire.runs} Wicket: {self.umpire.wickets} Overs: {self.umpire.overs}")
        print("\n---------------------------------------------\n")

    def describe_final_result(self, name, scores):
        """
        Provide a description of the final result of the match.
        
        Args:
            name (str): The name of the winning team.
            scores (int): The score achieved by the winning team.
        """
        print("--------------- Winner -----------------------")
        print(f"TEAM : {name} WON BY SCORE: {scores}")
        print("\n---------------------------------------------\n")


class CricketMatch:
    def __init__(self, team1, team2, field, total_overs):
        self.team1 = team1
        self.team2 = team2
        self.field = field
        self.umpire = CricketUmpire(field)
        self.commentator = CricketCommentator(self.umpire)
        self.total_overs = total_overs

    def start_match(self):
        """
        Starts the cricket match.
        """
        self.team1.select_captain(random.choice(self.team1.players))
        self.team2.select_captain(random.choice(self.team2.players))
        self.team1.batting_order = self.team1.players.copy()
        self.team2.batting_order = self.team2.players.copy()
        self.team1.bowlers = self.team1.players.copy()
        self.team2.bowlers = self.team2.players.copy()

        self.commentator.describe_game(
            self.team1.captain.name, self.team2.captain.name, self.team1.name, self.team2.name, over=self.total_overs
        )

        # Team 1 playing    
        self.commentator.describe_start(self.team1.name)
        self.play_innings(self.team1, self.team2)
        self.commentator.describe_end()
        lastScores = self.commentator.umpire.runs

        # Team 2 playing    
        self.commentator.umpire.scores = 0
        self.commentator.umpire.wickets = 0
        self.commentator.umpire.overs = 0
        self.commentator.describe_start(self.team2.name)
        self.play_innings(self.team2, self.team1)
        self.commentator.describe_end()
        newScores = self.commentator.umpire.scores

        # Final outcome
        if lastScores > newScores:
            self.commentator.describe_final_result(self.team1.name, lastScores)
        else:
            self.commentator.describe_final_result(self.team2.name, newScores)


    def play_innings(self, batting_team, bowling_team):
        over = 0
        ball_count = 1
        bowler = bowling_team.select_next_bowler()
        batsman = batting_team.select_next_batsman()

        while over < self.total_overs:
            print("\n-------------------")
            print(f"Over: {over+1} Ball: {ball_count} Batsman: {batsman.name} Bowler: {bowler.name} Score: {self.umpire.runs}/{self.umpire.wickets}")
            print("-------------------\n")

            ball_description = self.commentator.get_ball_description(batsman, bowler)
            print(ball_description)

            if ball_description.endswith("OUT!"):
                batsman = batting_team.select_next_batsman()
                if batsman is None:
                    break
                self.umpire.update_wickets()
                print(f"{batsman.name} is in!")
            else:
                runs = random.randint(0, 6)
                self.umpire.update_score(runs)
                print(f"Runs scored: {runs}")

            ball_count += 1
            print(f"Over {over+1} starting...")
            if ball_count > 6:
                ball_count = 1
                over += 1
                self.umpire.update_overs()
                bowler = bowling_team.select_bowler()
               

# Creating fake data
players1 = []
for i in range(10):
    players1.append(Cricketer("Player1_" + str(i + 1), round(random.random(), 1), round(random.random(), 1),
                              round(random.random(), 1), round(random.random(), 1), round(random.random(), 1)))

players2 = []
for i in range(10):
    players2.append(Cricketer("Player2_" + str(i + 1), round(random.random(), 1), round(random.random(), 1),
                              round(random.random(), 1), round(random.random(), 1), round(random.random(), 1)))

# Creating teams
team1 = CricketTeam("Country1", players1)
team2 = CricketTeam("Country2", players2)

team1.batting_order = team1.players.copy()
team1.bowlers = team1.players.copy()


team2.batting_order = team2.players.copy()
team2.bowlers = team2.players.copy()
# Creating field
field = CricketField("Large", 0.7, 0.8, 0.9)

# Starting match simulation
total_overs = 2
match = CricketMatch(team1, team2, field, total_overs)
match.start_match()
