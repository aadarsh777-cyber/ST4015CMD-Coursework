students = [
    {"name": "Alice", "friends": ["Bob"], "city": "Kathmandu"},
    {"name": "Bob",   "friends": ["Alice"], "city": "Pokhara"},
    {"name": "Carol", "friends": [],        "city": "Kathmandu"},
    {"name": "Dave",  "friends": [],        "city": "Pokhara"},
]

def conflicts(student, neighbor):
    if neighbor["name"] in student["friends"]:
        return True
    if student["city"] == neighbor["city"]:
        return True
    return False

# Sort by number of friends descending (most constrained first)
sorted_students = sorted(students, key=lambda s: len(s["friends"]), reverse=True)

arrangement = [sorted_students[0]]
remaining = sorted_students[1:]

for _ in range(len(remaining)):
    placed = False
    for candidate in remaining:
        if not conflicts(arrangement[-1], candidate):
            arrangement.append(candidate)
            remaining.remove(candidate)
            placed = True
            break
    if not placed:
        # Place anyway (heuristic - not always perfect)
        arrangement.append(remaining.pop(0))

print("Heuristic arrangement:")
for s in arrangement:
    print(f"  {s['name']} ({s['city']})")
```

**Run them** by opening terminal in Task2 folder:
```
python brute_force.py
python heuristic.py
