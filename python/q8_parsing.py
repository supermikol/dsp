# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv

with open('football.csv', 'r') as csvfile:
  spamreader = csv.reader(csvfile)
  next(spamreader, None)  # skip the headers
  first_row = next(spamreader, None)
  min_row = (first_row[0], int(first_row[5]) - int(first_row[6])) # set first team as minimum
  for row in spamreader:
    difference = int(row[5]) - int(row[6])
    if difference < min_row[1]: # if difference is less, then replace min_row
      min_row = (row[0], difference)
  print(min_row)