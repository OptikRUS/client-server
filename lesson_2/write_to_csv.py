import csv

from get_data import get_data


def write_to_csv(filename):
    with open(filename, 'w') as f:
        f_n_writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        for row in get_data():
            f_n_writer.writerow(row)
