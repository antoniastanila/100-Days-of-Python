import random

nrs = [nr*2 for nr in range(1, 5)]
print(nrs)

names = ["alex", "beth", "Caroline", "Dave", "Eleanor", "freddie"]
short_names = [name for name in names if len(name) <= 4]
print(short_names)

all_caps_names = [name.upper()
                  for name in names if name not in short_names]
print(all_caps_names)

student_scores = {name: random.randint(1, 100) for name in names}
print(student_scores)

passed_students = {name: score for (
    name, score) in student_scores.items() if score > 60}

print(passed_students)
