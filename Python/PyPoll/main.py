

##################################################################################################
#
# Use the poll data called election_data.csv. 
# The dataset is composed of three columns: Voter ID, County, and Candidate. 
# 
# Analyzes the votes and calculates each of the following:
# (a) The total number of votes cast
# (b) A complete list of candidates who received votes
# (c) The percentage of votes each candidate won
# (d) The total number of votes each candidate won
# (e) The winner of the election based on popular vote
#
##################################################################################################



# Modules
import os
import csv
from sys import exit


# Set path for file
filename = "election_data.csv"
csvpath = os.path.join("..", "Resources", filename)

# Print absolute path for this file. Just for reference
print(os.path.abspath(__file__))


# --------------------------------------------------------------------------
# Use "try"-"except" to prevent program crash due to file not available 
# --------------------------------------------------------------------------
try:
    with open(csvpath, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

        # skip the Header
        next(csvreader)
                
        
        # Create a dictionary called "candidate_information{}":
        #
        # candidate_information{}
        #       key (string):       name of candidate
        #       value (list):       candidate_vote_details[]
        # candiate_information{} = {name of the candidate: candidate_vote_details[]}

        # Dictionary will look like this (for illustration purpose):
        # candiate_information = { "name of Candiadate 1": [vote count, percentage vote],
        #                          "name of Candiadate 2": [vote count, percentage vote],
        #                          "name of Candiadate 3": [vote count, percentage vote],
        #                           .....
        #                         }    
        candidate_information = {}
    

        # Create a new list called "candidate_vote_details[]":
        #
        # candidate_vote_details[]
        #       Index 0:      candidate vote count 
        #       Index 1:      percentage votes
        #
        # candidate_vote_details = [candidate vote count, percentage votes]
        candidate_vote_details = [0, 0]
        

        # Initialize total vote counts to 0
        total_vote_count = 0

        # Examine each row in the csv file and fill the dictionary. 
        for row in csvreader:

            if row[2] not in candidate_information:
                # If candidate name is not in the dictionary then:
                # 
                # (a) Initialize the List:
                #  - List:candidate_vote_details[0: vote count] = 1
                #  - List:candidate_vote_details[1: percent vote] = 0
                #
                # (b) Using candidate name create a NEW key. Assign the list to this key:
                #  - Dict:candidate_information[<candidate name>] = List:candidate_vote_details
                #
                # (c) Increment total no of vote count 
                del candidate_vote_details
                candidate_vote_details = [1, 0]       
                candidate_information[row[2]] = candidate_vote_details                   
                total_vote_count = total_vote_count + 1
           
            else:
                # If candiate name is already in the dictionary then:
                # (a) Increment vote count for the matching candidate by 1
                # (b) Increment total no of vote count
                candidate_information[row[2]][0] = candidate_information[row[2]][0] + 1
                total_vote_count = total_vote_count + 1
               
except FileNotFoundError:
        # Handle missing file with exception.
        # Print out clear message to the user.
        # Make a clean exit.
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
        exit()


# Examine the dictionary to calculate:
# (a) Percentage votes for each candidate
# (b) Find the candidate with the highest number of votes
highest_votes = 0
for candidate, vote_info in candidate_information.items():
    
    percentage_vote = (vote_info[0] / total_vote_count) * 100
    candidate_information[candidate][1] = percentage_vote

    if vote_info[0] > highest_votes:
        highest_votes = vote_info[0]
        candidate_with_highest_votes = candidate




#################################################################
#                                                               #
#       PRINT THE RESULTS ON TERMINAL AND A TEXT FILE           #
#                                                               #
#################################################################


# Concatenate smaller strings to create one BIG messsage.
# Use this message to print on terminal and to write to text file.

# Create Header Message
msg1 = 'Election Results\n'
msg2 = '---------------------\n'
msg3 = f'Total Votes: {total_vote_count}\n'
msg4 = '---------------------\n'
msg = msg1 + msg2 + msg3 + msg4


# Create Candidate specific message with their voting record
for candidate, vote_info in candidate_information.items():
    msg = msg + f'{candidate}: {vote_info[1]:.2f}% ({vote_info[0]})\n'


# Create Footer Message
msg1 = '---------------------\n'
msg2 = f'Winner: {candidate_with_highest_votes}\n'
msg3 = '---------------------\n'
msg = msg + msg1 + msg2 + msg3


# Print the message to the terminal
print(msg)


# Write the message to the text file
filename = "PyPoll.txt"
with open(filename, 'w') as txtwrite:
    txtwrite.write(msg+'\n')

