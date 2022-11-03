from argparse import ArgumentParser
import secrets
import random
import string

#setting up the Argument Parser
parser = ArgumentParser(
    prog='Password Generator',
    description='Generate any number of password with this tool.'
)
#Adding the argument to the parser
parser.add_argument("-n", "--numbers", default=0, help="Number of digits in the PW", type=int)
parser.add_argument("-l", "--lowercase", default=0, help="Number of lowercase chars in the PW", type=int)
parser.add_argument("-u", "--uppercase", default=0, help="Number of uppercase chars in the PW", type=int)
parser.add_argument("-s", "--special-chars", default=0, help="Number of special chars in the PW", type=int)
#add total pw lenth argument
parser.add_argument("-", "--total-length", type=int,
                    help="The total password length. If passed, it will ignore -n, -l, -u and -s," \
                    "and generate completely random passwords with the specified length")

#the amount is a number so we check it to be of type int.
parser.add_argument("-a", "--amount", default=1, type=int)
parser.add_argument("-o", "--output-file")

#Parsing the command line arguments.
args = parser.parse_args()

#THE PW LOOP

#list of passwords
passwords = []
#looping through the amount of passwords.
for _ in range(args.amount):
    if args.total_length:
        #generate random password with the length
        #of total_length based on all available characters
        passwords.append("".join(
            [secrets.choice(string.digits + string.ascii_letters + string.punctuation) \
             for _ in range(args.total_length)]))
    else:
        password = []
        # if / how many numbers the password should contain
        for _ in range(args.numbers):
            password.append(secrets.choice(string.digits))

        # if / how many uppercase characters the password should contain
        for _ in range(args.uppercase):
            password.append(secrets.choice(string.ascii_uppercase))

        # if / how many lowercase characters the password should contain
        for _ in range(args.lowercase):
            password.append(secrets.choice(string.ascii_lowercase))

        # use the random shuffle, Shuffle the list with all possible letters, numbers and symbols.
        random.shuffle(password)

        #Get the letters of the string up to the length argument and then join them.
        password = ''.join(password)

        # append this password to the overall list of password
        passwords.append(password)


# SAVING THE PASSWORDS

#store the password to a .txt file.
if args.output_file:
    with open(args.output_file, 'w') as f:
        f.write('\n'.join(passwords))

print('\n'.join(passwords))

# Examples., now lets use the script for generating different password combinations. first, lets print the help

