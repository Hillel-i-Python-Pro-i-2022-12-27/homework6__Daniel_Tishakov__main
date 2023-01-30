import csv

from application.config.PATHS import INPUT_FILES


def csv_reader():
    data = csv.DictReader(open(INPUT_FILES / "people.csv"))
    for row in data:
        row
        print(row)


if __name__ == "__main__":
    csv_reader()
