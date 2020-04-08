'''
    The %s converts the object using str(), used for displaying to users
    The %r converts it using repr(), used for showing raw data
'''

x = "There are %d types of people" % 2
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who don't know %s" % (binary, do_not)

print(x)
print(y)

hilarious = False
joke_evaluation = "Isn't that joke so funny!? %r" % hilarious
joke_evaluation_but_it_is_different = "Isn't that joke so funny!? %d" % hilarious

print(joke_evaluation)
print(joke_evaluation_but_it_is_different)
#???: Different between %r and %s, %d?
#Ans: Use %r for debugging, it shows raw data
# others used for displaying to users


w = "This is the left side of..."
e = "a string with a right side"

print(w + e)
#???: Why adding two strings w, e makes it longer strong
#Ans: 