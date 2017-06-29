# normal string concat
msg1 = 3
msg2 = "from Bangalore"
print msg1,msg2

#string concat with variable substitution
name = 'Shashanka'
topic = "his work"
print "lets talk about %s and %s" %(name, topic)

age = 29.9

print "Hi, my name is %s aged %s" %(name, age)
print '%r' %(name) #%r prints out string literals

salutation = 'Mr.'

print salutation + name # this works too

print "Hello",
print "multiline?" # , produces stuff in same line

print "Hello"
print "multiline" # each print statement induces a \n