import csv


def read_csv(path):
  with open(path, 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    header = next(reader)
    data = [dict(zip(header, row)) for row in reader]
    return data

if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data)