import re

# Things that need to be done:
# [] Find and collect all email addresses and phone numbers.
# [] Store email addresses in emails.txt
# [] Store phone numbers in phone_numbers.txt
# [] Sort info in ascending order
# [] No duplicate entries

# assumption input is a valid phone number found by regex
def normalize_phone_number(input):
    integers = "0123456789"
    temp_output = ""
    output = ""
    # this will output only numbers, no non-number values
    for char in input:
        # check to see if character is an integer
        if char in integers:
            temp_output += char
    # if only 7 integers long, add 206 to the front
    if len(temp_output) == 7:
        temp_output = "206" + temp_output

    if len(temp_output) == 10:
        # this will place the dash after the index 2 and 5
        dash_indexes = {2, 5}
        # loops though the temp_output and adds dashes after index 2 and 5
        for i in range(len(temp_output)):
            if i in dash_indexes:
                # this adds the integer and a dash
                output += f"{temp_output[i]}-"
            else:
                # just adds an integer
                output += temp_output[i]
    return output


# assumption the input will be a valid email address found by regex
def normalize_email(input):
    # this returns the email as lowercase
    return input.lower()


# pattern from regex
phone_pattern = r"\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}"
email_pattern = r"^[a-zA-Z][a-zA-Z0-9]*[\.]{0,1}[a-zA-Z0-9]*[a-zA-Z]\@[a-zA-Z][a-zA-Z0-9\.]*\.[a-zA-Z]{3,12}$"

with open("assets/existing-contacts.txt") as existing_contacts:
    lines = existing_contacts.readlines()
# print(lines)
numbers = set()
emails = set()

for line in lines:
    match = phone_pattern.match(line)
    print(match)

# Need to get into the potential-contacts.txt file and get email and numbers out
# Need to open the potential-contacts.txt file
# open_file = open("assets/potential-contacts.txt", "r")
# print(open_file.read())
with open("assets/potential-contacts.txt") as potential_contacts:
    lines = potential_contacts.readlines()
# print(lines)


# create a report (joined list of #s), save to variable, write the variable to the phone_numbers.txt
# clean up the numbers using regex (standardize)
# use a replace method first, then regex
