from sys import argv

script, user_name = argv
prompt = '> '

print("Hi %s, I'm the %s script" % (user_name, script))
print("I would like to ask you a few questions.")
print("Do you like me, %s ?" % user_name)
like = (input(prompt))

if like == "Yes": 
    print("So lovely!")
else:
    print("So sad to hear that from you :(")

