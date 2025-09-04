import re

text = "Call me at 123 456-7890 or 908 765-4321"

# create a regular expression with re.compile()
# "r" at the start means "raw string" so we do not neet to negate
# the backslash in the regular expressions
pattern = re.compile(r'\d{3} \d{3}-\d{4}')

# apply regular expression on a string. It is stored as object
# search() return only the first match
res1 = pattern.search(text)
# res1 = re.search(r'\d{3} \d{3}-\d{4}', text).group()  # the regex will compile every single time

# to find all then use findall()
res2 = pattern.findall(text)

# get the results with .group()
print(res1.group())
print(res2)  # returns a list of matches
