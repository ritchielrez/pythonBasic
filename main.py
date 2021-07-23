import random
import os
import sys
import subprocess
from rofi import Rofi 

if __name__ == '__main__':
    dmbrowser = 'firefox'
    r = Rofi()

    options = [
"amazon - https://www.amazon.com/s?k=",
"archaur - https://aur.archlinux.org/packages/?O=0&K=",
"archpkg - https://archlinux.org/packages/?sort=&q=",
"archwiki - https://wiki.archlinux.org/index.php?search=",
"arxiv - https://arxiv.org/search/?searchtype=all&source=header&query=",
"bbcnews - https://www.bbc.co.uk/search?q=",
"bing - https://www.bing.com/search?q=",
"cliki - https://www.cliki.net/site/search?query=",
"cnn - https://www.cnn.com/search?q=",
"coinbase - https://www.coinbase.com/price?query=",
"debianpkg - https://packages.debian.org/search?suite=default&section=all&arch=any&searchon=names&keywords=",
"discogs - https://www.discogs.com/search/?&type=all&q=",
"duckduckgo - https://duckduckgo.com/?q=",
"ebay - https://www.ebay.com/sch/i.html?&_nkw=",
"github - https://github.com/search?q=",
"gitlab - https://gitlab.com/search?search=",
"google - https://www.google.com/search?q=",
"googleimages - https://www.google.com/search?hl=en&tbm=isch&q=",
"googlenews - https://news.google.com/search?q=",
"imdb - https://www.imdb.com/find?q=",
"reddit - https://www.reddit.com/search/?q=",
"slashdot - https://slashdot.org/index2.pl?fhfilter=",
"socialblade - https://socialblade.com/youtube/user/",
"sourceforge - https://sourceforge.net/directory/?q=",
"stack - https://stackoverflow.com/search?q=",
"startpage - https://www.startpage.com/do/dsearch?query=",
"stockquote - https://finance.yahoo.com/quote/",
"thesaurus - https://www.thesaurus.com/misspelling?term=",
"translate - https://translate.google.com/?sl=auto&tl=en&text=",
"urban - https://www.urbandictionary.com/define.php?term=",
"wayback - https://web.archive.org/web/*/",
"webster - https://www.merriam-webster.com/dictionary/",
"wikipedia - https://en.wikipedia.org/wiki/",
"wiktionary - https://en.wiktionary.org/wiki/",
"wolfram - https://www.wolframalpha.com/input/?i=",
"youtube - https://www.youtube.com/results?search_query=",
"quit" ]
    
    engine = 0
    i = 0

    if (engine == 0):
        engine, key = r.select('Choose a search engine:', options)
        print(key)
