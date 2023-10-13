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


def bye_action(dummy: List[str]) -> None:
    raise KeyboardInterrupt

pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("who won the superbowl in _"), winner_by_year),
    (str.split("where was the superbowl in _"), city_by_year),
    (str.split("what was the attendance at the _ superbowl"), attendance_by_year),
    (str.split("what was the final score of the _ superbowl"), score_by_year),
    (["bye"], bye_action),
]


def search_pa_list(src: List[str]) -> str:
    for pat, act in pa_list:
        mat = match(pat,src)
        if mat is not None:
            answer = act(mat)
            return answer if answer else ["No answers"]

    return ["I don't understand"]


def query_loop() -> None:
    print("Welcome to the SuperBowl database!\n")
    while True:
        try:
            print()
            query = input("Your question? ").replace("?", "").lower().split()
            answers =search_pa_list(query)
            print(answers)
        except (KeyboardInterrupt, EOFError):
            break

    print("\nSo long!\n")

query_loop()

assert winner_by_year(["2000"]) == "St.Louis Rams", "winner_by_year not working"
assert city_by_year(["2007"]) == "Miami", "city_by_year not working"
assert attendance_by_year(["2016"]) == 71088, "atendance_by_year not working"
assert score_by_year(["2021"]) == "31-9", "score_by_year not working"

assert search_pa_list(["what", "was", "the", "attendance", "at", "the", "2020","superbowl"]) == 62417, "failed search_pa_list test 3"
assert search_pa_list(["what", "was", "the", "final", "score", "of", "the", "2020", "superbowl" ]) == "31-20", "failed search_pa_list test 4"
assert search_pa_list (["who","won","the","superbowl","in","2024"]) == ["No answers"], "failed search_pa_list test 5"
print("all tests passed")