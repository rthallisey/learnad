#!/usr/bin/env python

import sys
import os
from learnad import matthew_berry

PROJECT_ROOT = os.path.abspath(os.path.join(
        os.path.dirname(os.path.realpath(__file__))))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


week_10_love_hate = matthew_berry.MatthewBerry('http://kwese.espn.com/fantasy/football/story/_/page/TMRlovehate171109/fantasy-football-picks-sleepers-busts-week-10')

preseason_love_hate = matthew_berry.MatthewBerry('http://www.espn.com/fantasy/football/story/_/id/23028073/fantasy-football-players-2018-value-increased-decreased-following-free-agency-trades')

week_10_love_hate.players()
preseason_love_hate.players()
print(week_10_love_hate.get_love_hate_list())
print(preseason_love_hate.get_love_hate_list())
