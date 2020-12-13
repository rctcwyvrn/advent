import requests
from pathlib import Path

session_key = open("../session_key.txt").read().strip()
login_cookie = dict(session=session_key)

aoc_day = str(Path(__file__).parent.absolute()).split("/")[-1].replace("day","")
aoc_year = str(Path(__file__).absolute().parents[1].absolute())[-4:] # last 4 chars is the year

def aoc_submit(soln, part):
    url = f"https://adventofcode.com/{aoc_year}/day/{aoc_day}/answer"
    data = {"level": str(part), "answer": str(soln)}
    ready = input(f"About to submit '{soln}' for day {aoc_day}, {aoc_year}. Ready to submit? (y,n)")
    if ready.lower() == "y":
        r = requests.post(url, data, cookies=login_cookie)
        x = r.text.split("<main>")[1].split("</main>")[0]
        print(x)
    else:
        print("Not submitting")