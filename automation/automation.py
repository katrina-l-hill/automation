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
phone_pattern = re.compile("\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}")
email_pattern = re.compile(
    "[a-zA-Z][a-zA-Z0-9]*[\.]{0,1}[a-zA-Z0-9]*[a-zA-Z]\@[a-zA-Z][a-zA-Z0-9\.]*\.[a-zA-Z]{3,12}"
)

with open("assets/existing-contacts.txt") as existing_contacts:
    lines = existing_contacts.readlines()
# print(lines)
numbers = set()  # returns a new set object
emails = set()  # returns a new set object

for line in lines:
    matches = phone_pattern.findall(line)
    if len(matches) > 0:
        for phone_number in matches:
            numbers.add(normalize_phone_number(phone_number))
    matches = email_pattern.findall(line)
    if len(matches) > 0:
        for email in matches:
            emails.add(normalize_email(email))


# Opens the potential-contacts.txt file to find the phone numbers and email addresses
with open("assets/potential-contacts.txt") as potential_contacts:
    lines = potential_contacts.readlines()

for line in lines:
    matches = phone_pattern.findall(line)
    if len(matches) > 0:
        for phone_number in matches:
            numbers.add(normalize_phone_number(phone_number))
    matches = email_pattern.findall(line)
    if len(matches) > 0:
        for email in matches:
            emails.add(normalize_email(email))


# Opens the phone_numbers.txt file and writes the output into it
with open("assets/phone_numbers.txt", "w") as phone_number_file:
    for number in sorted(numbers):
        phone_number_file.write(f"{number}\n")

# Opens the emails.txt file and writes the output into it
with open("assets/emails.txt", "w") as emails_file:
    for email in sorted(emails):
        emails_file.write(f"{email}\n")
