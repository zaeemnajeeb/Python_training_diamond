# note all duplicates removed+
s = { x + y for x in range(10) for y in range(10) }
print(s)

#Same as previous chapter
department = "Silly Walk"
t = {c for c in "Silly Walk"}
print(t)
print({x: department.count(x) for x in {c for c in "Silly Walk"}})