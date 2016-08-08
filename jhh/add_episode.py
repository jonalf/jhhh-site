#!/usr/bin/python
from sys import argv

KEY = ''

if len(argv) != 4:
    print 'Usage: SEASON #|worst TITLE LINK'
else:
    embed_div = """<div class="media-container">
<h3>NAME</h3>
<div class="embed">
FRAME
</div>
</div>
"""
    if argv[1] == 'worst':
        KEY = '<h2>The Worst</h2>'
    else:
        KEY = '<h2>Season ' + argv[1] + '</h2>'
    
    embed_div = embed_div.replace("NAME", argv[2])
    embed_div = embed_div.replace("FRAME", argv[3])
    print 'This is the div to be added:\n'
    print embed_div
    choice = raw_input('\nIs this ok? (y/n): ')
    if choice == 'y':
        fname = ''
        if argv[1] == 'worst':
            fname = 'templates/worst.html'
        else:
            fname = 'templates/episodes.html'
        f = open( fname )
        s = f.read()
        f.close()
        position = s.find(KEY) + len(KEY) + 2
        new_s = s[:position] + embed_div + s[position:]
        #backup episodes file just in case
        f = open(fname + '.backup', 'w')
        f.write(s)
        f.close()
        f = open(fname, 'w')
        f.write(new_s)
        f.close()
        print 'Done'
