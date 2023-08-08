# Advanced Cricket Simulation

This is an advanced cricket tournament simulation program written in Python. The program simulates a cricket match  <br>
between two teams with multiple features including player attributes,team selection, commentary, and more.

# Features

**Player Class**: Represents a cricket player with attributes such as bowling, batting, fielding, running, and experience.  <br>
**Team Class:** Represents a cricket team with methods for selecting captains, next players, and bowlers.    <br>
**Field Class:** Represents the field conditions with attributes like size, fan ratio, pitch conditions, and home advantage.  <br>
**Umpire Class:** Represents the umpire with methods to update scores, wickets, and overs, and predict ball outcomes.    <br>
**Commentator Class:** Provides commentary on the match, describing ball outcomes, game information, and match results.    <br>
**Match Class:*** Manages the cricket match, handling innings, gameplay, and match outcome.    <br>

# Usage

**Clone the repository:**  <br>

```git clone https://github.com/yourusername/cricket-tournament-simulation.git```

```cd cricket-tournament-simulation```

**Run the simulation:**  <br>

```python cricket_simulation.py```


# How It Works

The simulation begins by initializing two teams, each with a list of player objects. Team captains are randomly selected, 
and batting orders are set. Players' attributes are used to predict outcomes during the match. 
The Umpire class keeps track of scores, wickets, and overs, while the Commentator class provides real-time commentary.

During the match, players from the batting team face bowlers from the opposing team. Ball outcomes are predicted based on
players' attributes and pitch conditions. Commentary is provided for each ball played, including descriptions of runs scored 
and wickets taken. The simulation continues for the specified number of overs, and the final match result is displayed.
