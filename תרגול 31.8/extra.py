vote_dict = {"Toronto": [2800000, "38%"], "Montreal": [2000000, "29%"],
             "Jasper": [4700, "64%"], "Vancouver": [660000, "87%"],
             "Calgary": [1300000, "46%"], "Ottawa": [880000, "30%"]}
big_list_of_values = []
for list_ in vote_dict.values():
    big_list_of_values += list_
national_population = 0
# find the national population, and get rid of the % sign
for i in range(len(big_list_of_values)):
    if i % 2 == 0:
        national_population += big_list_of_values[i]
    else:
        num_of_percentage = big_list_of_values[i]
        num_of_percentage = int(num_of_percentage[:len(num_of_percentage)-1])
        big_list_of_values[i] = num_of_percentage
# now need to find how many people from every city voted
total_num_of_votes = 0
voters_dict = {}
for i in range(len(big_list_of_values)):
    if i % 2 == 0:
        num1 = big_list_of_values[i]
        num2 = big_list_of_values[i + 1]


        def percentage(percent, whole):
            return (percent * whole) / 100.0

        num_of_voters_per_city = percentage(num2, num1)
        total_num_of_votes += num_of_voters_per_city
        # want to create  a dictionary with: key = name of the city, val = num of voters
        # then, I can print the city with the most voters
    else:
        continue
print("the number of the total votes all over the country is:", total_num_of_votes)

# find the percentage of voters all over the country
def percentage(part, whole):
    percentage = 100 * float(part)/float(whole)
    return str(int(percentage))


the_percentage = (percentage(total_num_of_votes, national_population))
print("the percentage of people who voted for the MOOMINS is", the_percentage, "%")





