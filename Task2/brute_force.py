from itertools import permutations

students = [
    {"name": "Alice", "friends": ["Bob"], "city": "Kathmandu"},
    {"name": "Bob",   "friends": ["Alice"], "city": "Pokhara"},
    {"name": "Carol", "friends": [],        "city": "Kathmandu"},
    {"name": "Dave",  "friends": [],        "city": "Pokhara"},
]

def is_valid(arrangement):
    for i in range(len(arrangement) - 1):
        a = arrangement[i]
        b = arrangement[i + 1]
        # Friends should not sit next to each other
        if b["name"] in a["friends"] or a["name"] in b["friends"]:
            return False
        # Same city should not sit next to each other
        if a["city"] == b["city"]:
            return False
    return True

found = False
for perm in permutations(students):
    if is_valid(perm):
        print("Valid arrangement found:")
        for student in perm:
            print(f"  {student['name']} ({student['city']})")
        found = True
        break

if not found:
    print("No valid arrangement exists.")
