import xkcd

#print parsable object in the json
print "Parsable: " + xkcd.parsable

#get the json of page 666
print "JSON of 666: " + str(xkcd.get_json(666))

#get the image url of page 666
print "Image URL of 666: " + xkcd.get_image_url(666)

#get the alt text and title of page 666
print "Alt of 666: " + xkcd.parse_comic(666, "alt") + " | Title: " + xkcd.parse_comic(666, "safe_title")

#get the json of the latest xkcd comic
print "JSON of newest: " + str(xkcd.get_newest())

#get the page number of the newest xkcd comic
print "Page number of newest: " + str(xkcd.get_newest_page_number())

#get the image url of the latest xkcd comic
print "Image URL of newest: " + xkcd.get_newest_image_url()

#get the alt text and title of the latest xkcd comic
print "Alt of newest: " + xkcd.parse_newest("alt") + " | Title: " + xkcd.parse_newest("safe_title")

"""
Output (as of 2016-10-04):
Parsable: month, num, link, year, news, safe_title, transcript, alt, img, title, day
JSON of 666: {u'img': u'http://imgs.xkcd.com/comics/silent_hammer.png', u'title': u'Silent Hammer', u'month': u'11', u'num': 666, u'link': u'', u'year': u'2009', u'news': u'', u'safe_title': u'Silent Hammer', u'transcript': u'[[Hat guy is hammering something on a table.]]\nGuy: What--\nHat Guy: Silent hammer. I\'ve made a set of silent tools.\nGuy: Why?\nHammer: <<whoosh whoosh whoosh>>\n\nHat Guy: Stealth carpentry. Breaking into a house at night and moving windows, adjusting walls, etc.\n[[He takes his silent hammer over to a tool bench with other things on it. Two boxes underneath are labeled "Drills" and "Non-Drills."]]\n\nHat Guy, narrating: After a week or so of questioning his own sanity, the owner will stay up to watch the house at night. I\'ll make scratching noises in the walls, pipe in knockout gas, move him up to his bed, and never bother him again.\n[[The events he\'s describing are shown in two mini-panels below.]]\n\nGuy, off-panel: Nice prank, I guess, but what\'s the point?\nHat Guy: Check out the owner\'s card, on the table.\nGuy, off-panel: Chair of the American Skeptics Society? Oh, god.\nHat guy: Yeah, this doesn\'t end well for him.\n\n{{Title text: I bet he\'ll keep quiet for a couple weeks and then-- wait, did you nail a piece of scrap wood to my antique table a moment ago?}}', u'alt': u"I bet he'll keep quiet for a couple weeks and then-- wait, did you nail a piece of scrap wood to my antique table a moment ago?", u'day': u'23'}
Image URL of 666: http://imgs.xkcd.com/comics/silent_hammer.png
Alt of 666: I bet he'll keep quiet for a couple weeks and then-- wait, did you nail a piece of scrap wood to my antique table a moment ago? | Title: Silent Hammer
JSON of newest: {u'img': u'http://imgs.xkcd.com/comics/work.png', u'title': u'Work', u'month': u'10', u'num': 1741, u'link': u'', u'year': u'2016', u'news': u'', u'safe_title': u'Work', u'transcript': u'', u'alt': u'Despite it being imaginary, I already have SUCH a strong opinion on the cord-switch firing incident.', u'day': u'3'}
Page number of newest: 1741
Image URL of newest: http://imgs.xkcd.com/comics/work.png
Alt of newest: Despite it being imaginary, I already have SUCH a strong opinion on the cord-switch firing incident. | Title: Work
"""