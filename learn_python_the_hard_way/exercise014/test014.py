from sys import argv
import sys

script, name = sys.argv
prompt = ">"

print "Hello, %s, I'm %r script."%(name, script)
print "I'd like to ask you some questions."

print "Do you like me, %r"%name
likes = raw_input(prompt)

print "Where do you live %r?"%name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """Alright, so you said %r about liking me.\nYou live in %r. Not sure where that is. \nAnd you have a %r computer. Nice
"""%(likes, lives, computer)

