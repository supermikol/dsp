import csv
import re

with open('faculty.csv', 'r') as csvfile:
  spamreader = csv.reader(csvfile)
  headers = next(spamreader, None)  # skip the headers
  degrees = {}
  titles = {}
  emails = []
  email_domains = set()

  for row in spamreader:
    # Count degrees
    row_degrees = row[1].strip().split(' ')
    for degree in row_degrees:
      strip_periods = degree.replace('.', '')
      if strip_periods in degrees:
        degrees[strip_periods] += 1
      else:
        degrees[strip_periods] = 1

    # Count titles
    title = re.search(r'(.+)of', row[2])
    stripped_title = title.group(1).strip()
    if stripped_title in titles:
      titles[stripped_title] += 1
    else:
      titles[stripped_title] = 1

    # store emails
    emails.append(row[3])

    # Count unique email domains
    try:
      found = re.search('.+(@.+)', row[3]).group(1)
      email_domains.add(found)
    except AttributeError:
      found = ''

print('degrees: ', degrees)
print('titles: ', titles)
print('emails: ', emails)
print('email_domains: ', email_domains)