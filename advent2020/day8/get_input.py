import requests 
from advent_lib import login_cookie, aoc_day, aoc_year

print(f"Getting input data for day {aoc_day} of AOC year {aoc_year}")
url = f"https://adventofcode.com/{aoc_year}/day/{aoc_day}/input"

r = requests.get(url, cookies = login_cookie)

with open("input.py", "w") as dest:
    dest.write("x = \"\"\"")
    dest.write(r.text.strip())
    dest.write("\"\"\"")