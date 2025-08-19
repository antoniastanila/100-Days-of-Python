def calculate_love_score(name1, name2):
    love_score = ""
    total = 0
    for letter1 in "TRUE":
        counter = name1.count(letter1.lower()) + name2.count(letter1.lower())
        print(f"{letter1} occurs {counter} times")
        total += counter

    print(f"Total = {total}")

    love_score += str(total)

    total = 0

    for letter1 in "LOVE":
        counter = name1.count(letter1.lower()) + name2.count(letter1.lower())
        print(f"{letter1} occurs {counter} times")
        total += counter

    print(f"Total = {total}")
    love_score += str(total)
    print(f"Love Score = {love_score}")


calculate_love_score("Kim Kardashian", "Kanye West")
