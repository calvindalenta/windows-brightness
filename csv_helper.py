import csv

def read_file(path):
    result = {}
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            result[row[0]] = row[1]
    return result