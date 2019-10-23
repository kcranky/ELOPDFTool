"""
Provide:
- a directory, containing subdirectories all holding a submission,
- a csv of names and student numbers.
The program will check all submissions and rename them
The student will be marked if they have a submission
"""

import csv
import os
import glob

# load in the CSV

# check submissions in the primary directory

# for each submission dir, rename (whether file or folder) the submission text


def process(root_dir):
    # Get practicals
    entries = os.listdir(root_dir)
    print("Found {} folders in directory {}".format(len(entries), root_dir))
    print("The following tasks will be processed:")
    for entry in entries:
        if os.path.isdir(root_dir + '/' + entry):
            print(" - {}".format(entry))

    # Load the CSV
    for entry in entries:
        if entry[-4:] == ".csv":
            csv_name = root_dir + '/' + entry
            break
    print("Found {} as the source names file".format(csv_name))

    csv_in = open(csv_name)
    reader = csv.DictReader(csv_in)

    students = []
    for s in reader:
        students.append(s)

    # cosntruct a list of only student numebers
    stud_nums = []
    for s in students:
       stud_nums.append(s["Student ID"])


    # open a subdirectory
    for entry in entries:
        if os.path.isdir(root_dir + '/' + entry):
            print("Now working with {}".format(entry))
            for item in os.listdir(root_dir + '/' + entry):
                # Build a regex string to find all occurences of a subtstring
                pass
                #print("renaming {}".format(item))

    # rename a file
    # os.rename(r'file path\OLD file name.file type', r'file path\NEW file name.file type')

    # update the dictionary

    # write out the file
    csv_out = open(csv_name[:-4] + "_processed.csv", 'w')
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csv_out, fieldnames=fieldnames)

    # Finally, close the file
    csv_out.close()
    csv_in.close()

    return


if __name__ == "__main__":
    process("RenamingTest")