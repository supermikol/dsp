import csv

def write_to_csv(list_of_emails):
    with open('emails.csv', 'w') as csvfile:
        spamwriter = csv.writer(csvfile)
        spamwriter.writerow(['list_of_emails'])
        for row in list_of_emails:
            spamwriter.writerow([row])

write_to_csv(['hi','bye'])
