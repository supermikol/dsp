import csv
import re

faculty_dict = {}

with open('faculty.csv', 'r') as csvfile:
  spamreader = csv.reader(csvfile)
  headers = next(spamreader, None)  # skip the headers

  for row in spamreader:
    full_name = row[0].split(' ')
    first_name, last_name = full_name[0], full_name[-1]
    if (first_name, last_name) in faculty_dict:
      faculty_dict[first_name, last_name].append(row[1:])
    else:
      faculty_dict[first_name, last_name] = [row[1:]]

# print keys sorted by last name
print(sorted(faculty_dict.keys(), key=lambda x: x[1]))
