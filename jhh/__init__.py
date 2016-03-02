from flask import Flask, request, render_template, url_for, redirect

site = Flask( __name__ )

@site.route( '/' )
def root():
    print '======================================================='
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

@site.route( '/photos.html' )
def photos(GAL_NAME = None):
    return render_template( "photos.html" )

if __name__ == '__main__':
    #site.debug = True    
    site.run()
    
