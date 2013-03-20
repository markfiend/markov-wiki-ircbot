#!/usr/bin/python
""" Uses markov.py to generate texts from the source text. 
    Released under GNU GPL v3 http://www.gnu.org/licenses/gpl.html
"""

from markov import Markov
from sys import path

class MarkovTweet(object):

    def __init__(self, url):
        "Generate the markov chain stuff first."
        file_ = open(url, 'r')
        self.mkov = Markov(file_)

    def tweet(self, words=('', '')):
        "Capitalise the first word and trim to the end of a sentence."
        twit = self.mkov.generate_markov_text(50, words)
        twit = twit[0].upper() + twit[1:]
        while twit != '' and twit[-1] not in ';:?.,!':
            twit = twit[:-1]
        
        if twit == '':
            twit = self.tweet()
        else:
            if twit[-1] in ';:,':
                twit = twit[:-1] + '.'
        return twit
    
if __name__ == '__main__':
    m = MarkovTweet(path[0] + '/KingJamesBible.txt')
    print m.tweet()

