from auction_art import logo

print(logo)

bidders = {}

are_there_people_left = True
while are_there_people_left:
    name = input("What is your name?: ")
    bid = input("What is your bid?: ")
    bidders[name] = bid
    bidders_left = input("Are there other bidders left? yes/no: ")
    if bidders_left == "no":
        are_there_people_left = False
    else:
        print("\n" * 100)

max_sum = 0
winner = ""

for bid in bidders:
    if (max_sum < int(bidders[bid])):
        max_sum = int(bidders[bid])
        winner = bid

print(f"The winner is {winner} with a bid of {max_sum}$")
