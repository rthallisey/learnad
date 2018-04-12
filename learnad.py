#!/usr/bin/env python

import sys
import os
import datetime
from datetime import date
from learnad import matthew_berry

PROJECT_ROOT = os.path.abspath(os.path.join(
        os.path.dirname(os.path.realpath(__file__))))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


def gatherURL(article_date):
    year = article_date.strftime('%y')
    month = article_date.strftime('%m')
    day = article_date.strftime('%d')
    return "http://www.espn.com/fantasy/football/story/_/page/TMRlovehate" + year + month + day


def dateRange(article_date):
    helper = 7
    for h in range(1, helper):
        d = article_date + datetime.timedelta(days=h)
        try:
            weekly_love_hate = matthew_berry.MatthewBerry(gatherURL(d))
            print(d)
            return weekly_love_hate
        except Exception:
            pass

        d = article_date - datetime.timedelta(days=h)
        try:
            weekly_love_hate = matthew_berry.MatthewBerry(gatherURL(d))
            print(d)
            return weekly_love_hate
        except Exception:
            pass


# preseason_love_hate = matthew_berry.MatthewBerry('http://www.espn.com/fantasy/football/story/_/id/23028073/fantasy-football-players-2018-value-increased-decreased-following-free-agency-trades')
weeks = 15
article_date=date(2017, 9, 7)
for week in range(weeks):
    article_date = article_date + datetime.timedelta(days=7)
    try:
        weekly_love_hate = matthew_berry.MatthewBerry(gatherURL(article_date))
        print(article_date)
    except Exception:
        # Check 3 days earlier and 3 days later
        weekly_love_hate = dateRange(article_date)
        #print(Exception)

    if weekly_love_hate is not None:
        weekly_love_hate.players()
        print(weekly_love_hate.get_love_hate_list())
    else:
        print("Didn't find Love Hate for %s" % article_date)
