#!/usr/bin/python
from sys import argv

KEY = '<h2>Season 2</h2>'

if len(argv) != 3:
    print 'please provide a title and a link'
else:
    embed_div = """<div class="media-container">
<h3>NAME</h3>
<div class="embed">
FRAME
</div>
</div>
"""
    embed_div = embed_div.replace("NAME", argv[1])
    embed_div = embed_div.replace("FRAME", argv[2])
    print 'This is the div to be added:\n'
    print embed_div
    choice = raw_input('\nIs this ok? (y/n): ')
    if choice == 'y':
        f = open('templates/episodes.html')
        s = f.read()
        f.close()
        position = s.find(KEY) + len(KEY) + 2
        new_s = s[:position] + embed_div + s[position:]
        #backup episodes file just in case
        f = open('templates/episodes-old.html', 'w')
        f.write(s)
        f.close()
        f = open('templates/episodes.html', 'w')
        f.write(new_s)
        f.close()
        print 'Done'
