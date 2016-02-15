from flask import Flask, request, render_template, url_for, redirect
import os
import random
from socket import gethostname

site = Flask( __name__ )

GALLERY_LOCATION_WEB = 'static/img/galleries'
GALLERY_LOCATION_LOCAL = GALLERY_LOCATION_WEB
if gethostname() == 'fry':
    GALLERY_LOCATION_LOCAL = '/var/www/html/jamie/jamie/static/img/galleries'

GALLERIES = [ ('Headshots', 'headshots'), ('Cabaret','cabaret'), ('The Marvelous Wonderettes','marvelous'), ('Carousel','carousel'), ('A Funny Thing Happened on the Way to the Forum','forum'), ('Disney Dreams','disney'), ('Eleemosynary','eleemosynary') ]

@site.route( '/' )
def root():
    gals = GALLERIES[1:]
    pic1 = gals.pop( random.randint(0, len(gals)-1 ) )[1]
    pic2 = gals.pop( random.randint(0, len(gals)-1 ) )[1]
    return render_template( 'main.html',  pic1=pic1, pic2=pic2 )

@site.route( '/bio.html' )
def bio():
    return render_template( 'bio.html' )

@site.route( '/resume.html' )
def resume():
    return render_template( 'resume.html' )

@site.route( '/audio.html' )
def audio():
    return render_template( 'audio.html' )

@site.route( '/video.html' )
def video():
    return render_template( 'video.html' )

@site.route( '/photos/<GAL_NAME>.html' )
@site.route( '/photos.html' )
def photos(GAL_NAME = None):

    if not GAL_NAME:
        post = '/square/1.jpg'
        return render_template( "photos.html", galleries = GALLERIES, pre = GALLERY_LOCATION_WEB + '/', post = post )
    
    else:
        if not any( GAL_NAME in item for item in GALLERIES ):
            return redirect( url_for('photos') )
        
        local = GALLERY_LOCATION_LOCAL + '/' + GAL_NAME + '/square/'
        location = 'img/galleries/' + GAL_NAME + '/square/'
        pics = os.listdir( local )
        i = 0
        while i < len(pics):
            pics[i] = location + pics[i]
            i+= 1            

        i = 0
        while i < len( GALLERIES ) and GALLERIES[i][1] != GAL_NAME:
            i+= 1

        if i == len(GALLERIES) - 1:
            next_link = 'headshots'
            next_gallery = 'Headshots'
        else:
            next_link = GALLERIES[i+1][1]
            next_gallery = GALLERIES[i+1][0]

        return render_template( 'gallery.html', pics = pics, next_link = next_link, next_gallery = next_gallery )

if __name__ == '__main__':
    site.debug = True
    site.run()
    
