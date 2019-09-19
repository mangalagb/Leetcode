import json
with open('realestate.csv') as reader:
    # Further file processing goes here
    print("hello")
    house_transactions = []
    line = reader.readline()
    while line != '':  # The EOF char is an empty string
        print(line, end='')
        line = reader.readline()
        details = line.split(sep=",")
        house_transactions.append(details)

    with open('house_transactions', 'w') as writer:
        # Write the dog breeds to the file in reversed order
        json.dump(house_transactions, writer)