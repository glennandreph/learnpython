s = "Strings are awesome!"

#Length should be 20
print("Length of s = %d" % len(s))

#First "a" should be at index 8
print("First occurense of the letter a = %d" % s.index("a"))

#"a" should occur 2 times
print("a occurs %d times" %s.count("a"))

print("The first five characters are '%s'" % s[:5])

print("The next five characters are '%s'" % s[5:10])

print("The thirteenth character is '%s'" % s[12])

print("The characters with odd index are '%s'" % s[1::2])

print("The last five characters are '%s'" % s[-5])

if s.startswith("str"):
    print("String starts with 'Str'. Good!")

if s.endswith("ome"):
    print("String ends with 'ome'. Good!")

print("Split the words of the string: %s" % s.split(" "))
