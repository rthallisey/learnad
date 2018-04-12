import sys
import re
import os
import json
from newspaper import Article

PROJECT_ROOT = os.path.abspath(os.path.join(
        os.path.dirname(os.path.realpath(__file__))))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import article

class MatthewBerry(article.News):
    # Matthew Berry Love Hate Fantasy Football article

    def __init__(self, url):
        super(MatthewBerry, self).__init__(url)
        self.article.set_authors(["Matthew Berry"])
        self.authors = self.article.authors

        json_data=open(PROJECT_ROOT+"/nfl_teams.json").read()
        self.nfl_teams = json.loads(json_data)

        self.love_filter = re.compile("^.*I love")
        self.hate_filter = re.compile("^.*I hate")
        self.stream_filter = re.compile("^.*to stream")

        self.love_hate = {"love": {}, "hate": {}, "stream": {}}
        self.positions = ["Players", "Quarterbacks", "Running backs", "Kickers", "Wide recievers", "Pass-catchers", "Defenses"]


    def players(self):
        player_filter = re.compile("^(?:(?!:).)*")
        # Split into lines
        paragraphs = self.text.split('\n')
        feeling = None
        for p in paragraphs:
            # Look for love/hate titles
            love_hate = self.love_hate_titles(p)
            if love_hate is not None:
                position = love_hate[0]
                feeling = love_hate[1]
                if position not in self.love_hate[feeling].keys():
                    self.love_hate[feeling][position] = []
                continue

            # Look for individual players
            if ":" in p:
                # Filter for the player name and team
                if player_filter.match(p) is not None:
                    match = player_filter.match(p)

                    # Check the result has a team in it
                    for team in self.nfl_teams['short_name']:
                        data = match.group()
                        if team in data:
                            player_team = data.split(',')
                            if feeling is not None:
                                self.love_hate[feeling][position].append(player_team)


    def love_hate_titles(self, p):
        # Look for 'I love' or 'I hate' or 'to stream'
        for pos in self.positions:
            if "{} I love".format(pos) in p:
                if self.love_filter.match(p) is not None:
                    return pos, "love"
            if "{} I hate".format(pos) in p:
                if self.hate_filter.match(p) is not None:
                    return pos, "hate"
            if "{} to stream".format(pos) in p:
                if self.stream_filter.match(p) is not None:
                    return pos, "stream"


    def get_love_hate_list(self):
        return self.love_hate
