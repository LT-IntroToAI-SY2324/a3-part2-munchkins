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

def winner_by_year(matches: List[str]) -> str:
    input_year = int(matches[0])
    for game in games_db:
        if get_year(game) == input_year:
            return get_winner(game)

def city_by_year(matches: List[str]) -> str:
    input_year = int(matches[0])
    for game in games_db:
        if get_year(game) == input_year:
            return get_city(game)

def attendance_by_year(matches: List[str]) -> int:
    input_year = int(matches[0])
    for game in games_db:
        if get_year(game) == input_year:
            return get_attendance(game)

def score_by_year(matches: List[str]) -> str:
    input_year = int(matches[0])
    for game in games_db:
        if get_year(game) == input_year:
            return get_score(game)

assert winner_by_year(["2000"]) == "St.Louis Rams", "winner_by_year not working"
assert city_by_year(["2007"]) == "Miami", "city_by_year not working"
assert attendance_by_year(["2016"]) == 71088, "atendance_by_year not working"
assert score_by_year(["2021"]) == "31-9", "score_by_year not working"
print("all tests passed")