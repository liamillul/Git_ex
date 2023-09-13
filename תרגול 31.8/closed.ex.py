import random
from collections import Counter

# PART A
candidates_list = []
# candidates number. with limitations
num_of_candidates = int(input("how many candidates are there?: "))
while num_of_candidates < 4 or num_of_candidates > 15:
    print("invalid number of candidates")
    num_of_candidates = int(input("how many candidates are there?: "))
# candidates names (with limitations), and put them into a list.
for num in range(1, num_of_candidates + 1):
    print("what is the name of candidate", num, "?")
    name = input()
    while not name.isalpha():
        print("invalid name. what is the name of candidate", num, "?")
        name = input()
    candidates_list.append(name)
# number of votes. with limitations. the num of votes will be the length of the votes list.
num_of_votes = int(input("how many votes are there?"))
if num_of_votes < 100 or num_of_votes <= 0:
    print("The number of votes is too low. The election is disqualified.")
else:
    # make the votes list
    votes_list = []
    for i in range(num_of_votes):
        random_name = random.choice(candidates_list)
        votes_list.append(random_name)
    # count how many votes are given for every candidate
    count = Counter(votes_list)
    max_votes = max(count.values())
    # took the key by the value, from the list of values
    winner = list(count.keys())[list(count.values()).index(max_votes)]
    print("the winner is:", winner, max_votes)

    # PART B

    # first I need to remove all the occurrences of the winner from the votes list
    votes_list = list(filter(winner.__ne__, votes_list))
    # also need to update my candidate list
    candidates_list.remove(winner)
    # now need to print the other candidates
    for name in candidates_list:
        count = Counter(votes_list)
        # again took the key out
        the_next_winner = list(count.keys())[list(count.values()).index(max(count.values()))]
        print(the_next_winner, max(count.values()))
        votes_list = list(filter(the_next_winner.__ne__, votes_list))
