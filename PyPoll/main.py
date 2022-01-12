import os
import csv

#set path for election data file
csvpath = os.path.join("Resources", "election_data.csv")

voter_count=[]
candidate_list=[]
num_votes=0

#open election data file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)

    #skip header row
    next(csvreader)

    for row in csvreader:
        num_votes=num_votes+1

        candidate = row[2]

        if candidate in candidate_list:
            candidate_index=candidate_list.index(candidate)
            voter_count[candidate_index]=voter_count[candidate_index]+1

        else:
            candidate_list.append(candidate)
            voter_count.append(1)

percentages=[]
max_votes= voter_count[0]
max_index=0

for count in range(len(candidate_list)):
    vote_percentage= voter_count[count]/num_votes*100
    percentages.append(vote_percentage)

    if voter_count[count]> max_votes:
        max_votes=voter_count[count]
        print(max_votes)
        max_index=count
winner=candidate_list[max_index]



#specify file to write results to
output_path = os.path.join("Analysis","output.txt")

output_1 = (  f"Election Results\n"
            f"------------------------------\n"
            f"Total Votes: {num_votes}\n"
            f"------------------------------\n")
output_2 =  (f"{candidate_list[count]}:{percentages[count]:.2f}% ({voter_count[count]})\n")
output_3 =  (f"------------------------------\n"
            f"Winner:  {winner}\n"
            f"------------------------------\n")

with open(output_path, "w") as txt_file:
   txt_file.write(output_1)
   for count in range(len(candidate_list)):
        txt_file.write(output_2)
   txt_file.write(output_3)