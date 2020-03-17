# \\ Backslash (\)
# \' Single-quote (') \" Double-quote (")
# \a ASCII bell (BEL)
# \b ASCII backspace (BS)
# \f ASCII formfeed (FF)
# \n ASCII linefeed (LF)
# \N{name} Character named name in the Unicode database (Unicode only) \r ASCII carriage return (CR)
# \t ASCII horizontal tab (TAB)
# \uxxxx Character with 16-bit hex value xxxx (Unicode only) \Uxxxxxxxx Character with 32-bit hex value xxxxxxxx (Unicode only) \v ASCII vertical tab (VT)
# \ooo Character with octal value oo
# \xhh Character with hex value hh

tabby_cat = "\tI'm a tabby cat"
persian_cat = "I'm split\non a line"
backsplash_cat = "I'm \\ a \\ cat"

fat_cat = """
My food list:
\t * Beefsteak
\t * Sushi
\t * Fried Chicken
"""

print(tabby_cat)
print(persian_cat)
print(backsplash_cat)
print(fat_cat)

while True:
    for i in ["/","-","|","\\","|"]:
        print ("%s\r" % i, end="")
