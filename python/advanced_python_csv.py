import csv
import re

with open('faculty.csv', 'r') as csvfile:
  spamreader = csv.reader(csvfile)
  headers = next(spamreader, None)  # skip the headers
  emails = []

  for row in spamreader:
    # store emails in list
    emails.append(row[3])

with open('emails.csv', 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  # write to csv
  for email in emails:
    writer.writerow([email])
