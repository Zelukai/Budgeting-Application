import envelope
from datetime import date
import csv

class Payment: 
    def __init__(self, amount=0.00, date = date.today(), recurring = False, projection = False, envelope = 'total'):
        self.amount = amount
        self.date = date
        self.recurring = recurring
        self.projection = projection
        self.envelope = envelope
        self.record()

    def record(self):
        entryList = [self.amount, self.date, self.envelope]
        csv_file_path = f'{self.envelope}.csv'
        with open(csv_file_path, mode='a+', newline="") as file:
            writer = csv.writer(file)
            writer.writerow(entryList)

        # update user
        print(f"Payment of ${self.amount} was created")

    