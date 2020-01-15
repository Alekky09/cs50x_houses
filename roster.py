import cs50
import sys

if len(sys.argv) != 2:
    sys.exit("Correct form: python roster.py house_name")

db = cs50.SQL("sqlite:///students.db")

house = sys.argv[1]

rows = db.execute("SELECT * FROM students WHERE house = ? ORDER BY last, first", house)

for row in rows:

    if row["middle"] == "None":

        print("{0} {1}, born {2}".format(row["first"], row["last"], row["birth"]))

    else:

        print("{0} {1} {2}, born {3}".format(row["first"], row["middle"], row["last"], row["birth"]))
