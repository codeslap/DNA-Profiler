import csv
import sys


def main():

    # Check for command-line usage
    if len(sys.argv) != 3:
        print("Please use correct arguemnts: database.csv sequence.txt")

    # Open CSV file and put lines into list of dictionaries into dict_list
    with open(sys.argv[1],'r') as csv_file:
        table = [strline[:-1].split(',') for strline in csv_file.readlines()]
        dict_list = [{table[0][i]:elem for i, elem in enumerate(line)} for line in table[1:]]


    #store length of dict and length of keys which are STRs to look for in DNA
    lend = len(dict_list)
    #keys is a list of STRs to be checked for in longest_match below
    keys = list(dict_list[0].keys())
    lenkeys = len(keys)

    #open the txt file to read dna sequence
    dna = open(sys.argv[2])
    dnaseq = dna.read()
    dna.close
    count = []

    #call longest_match on dna sequence for each STR in keys, store result in count
    for j in range(1, lenkeys):
        keycheck = keys[j]
        count.append(longest_match(dnaseq, keycheck))

    #Use check to match STR counts for every person in database
    for i in range (0,lend):
        check = []
        for k, v in dict_list[i].items():
            check.append(v)
            if len(check) == lenkeys:
                #name is first value in dict_list, other values are STR counts for each person
                name = check[0]
                track = 0
                for r in range(1, lenkeys):
                    #checking each STR value against count found in dna to match person
                    if int(check[r]) - count[r-1] == 0:
                        track += 1
                        #if all STR counts match, that is the person DNA belongs to
                        if track == lenkeys - 1:
                            match = name

    #If match was found print the name of person, if not, No Match.
    try:
        match
    except NameError:
        print("No Match")
    else:
        print(match)
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