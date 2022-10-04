import csv
import sys
import string


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    # TODO: Read database file into a variable
    database = []
    input = sys.argv[1]
    with open(input) as file:
        reader = csv.DictReader(file)
        for data in reader:
            # data["name"] = data["name"]
            data["AGATC"] = int(data["AGATC"])
            print("dataTest1: ", data["AGATC"])
            data["AATG"] = int(data["AATG"])
            print("dataTest2: ", data["AATG"])
            data["TATC"] = int(data["TATC"])
            print("dataTest3: ", data["TATC"])
            database.append(data)
            print()

    # TODO: Read DNA sequence file into a variable
    # string dna
    txt = sys.argv[2]
    with open(txt) as txtfile:
        text = txtfile.read()
        print(text)


    # TODO: Find longest match of each STR in DNA sequence
    agatc = longest_match(text, "AGATC")
    print("agatc: ", agatc)
    aatg = longest_match(text, "AATG")
    print("aatg: ", aatg)
    tatc = longest_match(text, "TATC")
    print("tatc: ", tatc)
    # total = string(agatc, ", ", aatg, ", ", tatc)

    # TODO: Check database for matching profiles
    for i in range(0, len(database)):
        print("database[", i, "]: ", database[i])
        for j in range(len(database[i])):

            if database[i].data["AGATC"] == agatc:
                print("Match found!")
            else:
                print("no match :(")

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
