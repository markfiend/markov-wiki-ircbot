#!/usr/bin/python2
''' Wiki scraper. Pull the first paragraph of a wikipedia article, remove HTML,
    then save the result onto the end of wikiparagraphs.txt. Also strips out
    citation numbers. 

    Released under GNU GPL v3 http://www.gnu.org/licenses/gpl.html
'''

import os, re

from HTMLParser import HTMLParser

AllData = ''
regex = re.compile('\[\d+\]')

class MyParser(HTMLParser):
    def handle_data(self, data):
        global AllData
        AllData += data

class WikiScraper:
    def its_a_paragraph(self, line):
        parser = MyParser()
        parser.feed(line)

    def main(self):
        global AllData, regex
        AllData = ''
        subject = 'Special:Random'
        wikiurl = 'http://en.wikipedia.org/wiki/' + subject
        os.system('rm ' + subject)
        os.system('wget ' + wikiurl + ' 2>/dev/null')

        filehandle = open(subject, 'r')
        for line in filehandle:
            if '<p>' in line:
                self.its_a_paragraph(line)

        filehandle.close()

        AllData = AllData.strip()
        AllData = re.sub(regex, '', AllData)

        f = open('wikiparagraphs.txt', 'a')
        f.write(AllData + '\n')
        f.close()

if __name__ == '__main__':
    w = WikiScraper()
    w.main()
