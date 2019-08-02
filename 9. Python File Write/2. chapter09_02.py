# Chapter09_02
# Write & Read CSV File

# CSV : MEME - text/csv
import csv

# Ex1
with open('./resource/test1.csv', 'r') as f:
    reader = csv.reader(f)
    # next(reader)    # Header Skip

    # Check Object
    print(reader)

    # Check Type
    print(type(reader))

    # Check Property
    print(dir(reader))  # __iter__
    print()

    # Read
    for c in reader:
        # print(c)
        # print(type(c))  # list
        # list to str
        print(' : '.join(c))

# Ex2
with open('./resource/test2.csv', 'r') as f:
    reader = csv.reader(f, delimiter='|')

    for c in reader:
        print(c)

# Ex3
with open('./resource/test1.csv', 'r') as f:
    reader = csv.DictReader(f)
    # Check
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:
        for k, v in c.items():
            print(k, v)
        print('-----------------')

# Ex4
w = [[1, 2, 3, ], [4, 5, 6], [7, 8, 9], [10, 11, 12],
     [13, 14, 15], [16, 17, 18], [19, 20, 21]]

with open('./resource/write1.csv', 'w', encoding='utf-8') as f:
    print(dir(csv))
    wt = csv.writer(f)

    # Check dir
    # print(dir(wt))
    # Check Type
    # print(type(wt))

    for v in w:
        wt.writerow(v)

# Ex5
with open('./resource/write2.csv', 'w', encoding='utf-8') as f:
    # Field Name
    fields = ['One', 'Two', 'Three']

    # Dict Writer
    wt = csv.DictWriter(f, fieldnames=fields)
    # Header Writer
    wt.writeheader()

    for v in w:
        wt.writerow({'One': v[0], 'Two': v[1], 'Three': v[2]})
