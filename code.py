from games import games_db
from match import match
from typing import List, Tuple, Callable, Any

# Year, City, Attendance, Winning team, Score

# Who won the superbowl in year?
# Where was the superbowl in year?
# What was the attendance at the year superbowl?
# What was the final score of the year superbowl?

def get_year(game: Tuple[int, str, int, str, str]) -> int:
    return game[0]
def get_city(game: Tuple[int, str, int, str, str]) -> str:
    return game[1]
def get_attendance(game: Tuple[int, str, int, str, str]) -> int:
    return game[2]
def get_winner(game: Tuple[int, str, int, str, str]) -> str:
    return game[3]
def get_score(game: Tuple[int, str, int, str, str]) -> int:
    return game[4]

def 