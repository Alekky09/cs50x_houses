import cs50
import sys
import csv

if len(sys.argv) != 2:
    sys.exit("Correct form: python import.py csv_file")

db = cs50.SQL("sqlite:///students.db")

with open(sys.argv[1], "r") as characters:

    reader = csv.DictReader(characters)

    for row in reader:

        names = row["name"].split()

        firstName = names[0]

        if len(names) == 3:

            middleName = names[1]
            lastName = names[2]

        else:

            middleName = "None"
            lastName = names[1]

        house = row["house"]
        birth = row["birth"]

        db.execute("INSERT INTO students(first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)", firstName, middleName, lastName, house, birth)




