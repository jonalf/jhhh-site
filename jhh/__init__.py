from flask import Flask, request, render_template, url_for, redirect
from csv import DictReader
from random import sample
from requests import head

site = Flask( __name__ )
AD_TYPES = ['monologue', 'text', 'score'] #, 'playwright']
LINK_PREFIX = 'src="'

DIR = os.path.dirname(__file__) or '.'
AD_FILE = DIR + 'ad_links.csv'

@site.route( '/' )
def root():
    return render_template( 'main.html' )

@site.route( '/episodes.html' )
def episodes():
    return render_template( 'episodes.html' )

@site.route( '/the_worst.html' )
def the_worst():
    return render_template( 'worst.html' )

@site.route( '/about.html' )
def about():
    return render_template( 'about.html' )

@site.route( '/prep.html' )
def prep():
    f = open(AD_FILE)
    d = DictReader(f)
    d = [ l for l in d ]
    links = {}
    for t in AD_TYPES:
        links[t] = [ r['link'] for r in d if r['type'] == t ]
        links[t] = sample(links[t], 2)
    return render_template( 'prep.html', links=links )

@site.route( '/resources/<type>' )
def resources(type):
    if type not in AD_TYPES:
        type = AD_TYPES[0]

    f = open(AD_FILE)
    d = DictReader(f)
    print type
    links= [ r['link'] for r in d if r['type'] == type ]
    for l in links:
        pos = l.find(LINK_PREFIX)
        l = l[(pos+len(LINK_PREFIX)):-2]
        #r = head('https:' + l)
        #print l + '\t' + str(r.status_code)
    return render_template( 'resources.html', links=links )



@site.route( '/support.html' )
def support():
    return render_template( 'support.html' )

@site.route( '/photos.html' )
def photos(GAL_NAME = None):
    return render_template( "photos.html" )

if __name__ == '__main__':
    site.debug = True    
    site.run()
    
