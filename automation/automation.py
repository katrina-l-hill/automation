import re

# Things that need to be done:
# [] Find and collect all email addresses and phone numbers.
# [] Store email addresses in emails.txt
# [] Store phone numbers in phone_numbers.txt
# [] Sort info in ascending order
# [] No duplicate entries

# pattern from regex
pattern = r"\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}"

# Need to get into the potential-contacts.txt file and get email and numbers out
# Need to open the potential-contacts.txt file
# open_file = open("assets/potential-contacts.txt", "r")
# print(open_file.read())
with open("assets/potential-contacts.txt") as numbers:
    lines = numbers.readlines()
print(lines)


# create a report (joined list of #s), save to variable, write the variable to the phone_numbers.txt
# clean up the numbers using regex (standardize)
# use a replace method first, then regex
