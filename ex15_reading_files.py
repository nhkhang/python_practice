from sys import argv

script, filename = argv

txt = open(filename) # file object

print("Here's your file %s" % filename)
print(txt.read())

