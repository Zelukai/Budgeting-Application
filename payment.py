import envelope
from datetime import date
import csv
import main
import os

class Payment: 
    def __init__(self, amount=0.00, date = date.today(), recurring = False, projection = False, envelope = 'total'):
        self.amount = amount
        self.date = date
        self.recurring = recurring
        self.projection = projection
        self.envelope = envelope
        self.record()
    def record(self):
        
        print('running record')

        file_path = main.find(self.envelope) 
        
        entryListPayments = [self.amount, self.date, self.envelope]
        csv_file_path = os.path.join(file_path, f'{self.envelope}.csv')

        amountToAdd = float(self.amount)
        stats_csv_file_path = os.path.join(file_path, f'stats_{self.envelope}.csv')

        # Write payment entry to the payment CSV
        with open(csv_file_path, mode='a+', newline="") as file:
            writer = csv.writer(file)
            writer.writerow(entryListPayments)

        NetTotal = 0.0
        TotalExpenses = 0.0

        # Check if stats file exists and read its content
        if os.path.exists(stats_csv_file_path):
            with open(stats_csv_file_path, mode='r', newline="") as statsfile:
                reader = csv.DictReader(statsfile)
                rows = list(reader)

                # If the file contains rows, update the first row
                if rows:
                    NetTotal = float(rows[0]['NetTotal'])
                    TotalExpenses = float(rows[0]['TotalExpenses'])

        # Update the stats based on the payment amount
        if amountToAdd < 0:
            TotalExpenses += abs(amountToAdd)  # Add to expenses
    
        NetTotal += amountToAdd  # Add to net total

        # Write updated stats back to the CSV
        with open(stats_csv_file_path, mode='w', newline="") as statsfile:
            fieldnames = ['NetTotal', 'TotalExpenses']
            writer = csv.DictWriter(statsfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow({'NetTotal': NetTotal, 'TotalExpenses': TotalExpenses})

        print(f"Payment of ${self.amount} was created")
