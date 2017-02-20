from lxml import html
import requests
import time
import datetime
import pandas as pd
import numpy as np

month = 1
day = 1
year = 1946

now = datetime.datetime.now()
currentYear = now.year
currentMonth = now.month
currentDay = now.day

while month != currentMonth or day != currentDay or year != currentYear:
    url = 'http://www.basketball-reference.com/boxscores/index.fcgi?month=' + str(currentMonth).zfill(2) + "&day=" + str(day) + "&year=" + str(year)
    page = requests.get(url)
    tree = html.fromstring(page.content)
    games = tree.xpath('//div[@class="game_summary expanded nohover"]/p[@class="links"]/a/@href')
    allGameLinks = pd.DataFrame(columns=["year", "month", "day", "team1", "team2", "score1", "score2", "attendance"])
    for game in games:
        i = 5 #CHANGE ME
    day = day + 1
    if (day == 32):
        month = month + 1
        day = 1
    if (month == 13):
        year = year + 1
        month = 1
