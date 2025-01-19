import envelope
from datetime import date
import os
import csv
from datetime import date
import main

class Payment:
    def __init__(self, amount=0.00, date=date.today(), recurring=False, projection=False, envelope='total'):
        self.amount = float(amount)
        self.date = date
        self.recurring = recurring
        self.projection = projection
        self.envelope = envelope
        self.record()

    def record(self):
        print('Running record')

        # Find the file path for the envelope
        file_path = main.find(self.envelope)

        # Payment entry for the current envelope
        entryListPayments = [self.amount, self.date, self.envelope]
        csv_file_path = os.path.join(file_path, f'{self.envelope}.csv')

        # Write the payment to the envelope's main CSV
        with open(csv_file_path, mode='a+', newline="") as file:
            writer = csv.writer(file)
            writer.writerow(entryListPayments)

        # Update stats for the current envelope
        stats_csv_file_path = os.path.join(file_path, f'stats_{self.envelope}.csv')
        self.update_stats(stats_csv_file_path, self.amount)

        # Handle the parent envelope (if any)
        parent_path = os.path.dirname(file_path)
        parent_name = os.path.basename(parent_path)
        parent_csv_path = os.path.join(parent_path, f'{parent_name}.csv')
        parent_stats_path = os.path.join(parent_path, f'stats_{parent_name}.csv')

        if os.path.exists(parent_csv_path):
            # Write an entry for the parent envelope
            parent_entry = [self.amount, self.date, self.envelope]
            with open(parent_csv_path, mode='a+', newline="") as parent_file:
                writer = csv.writer(parent_file)
                writer.writerow(parent_entry)

            # Update stats for the parent envelope
            self.update_stats(parent_stats_path, self.amount)

        print(f"Payment of ${self.amount} was recorded in '{self.envelope}.csv'")

    @staticmethod
    def update_stats(stats_csv_file_path, amount_to_adjust):
        """Update the stats file for an envelope."""
        amount_to_adjust = float(amount_to_adjust)
        TotalContained = 0.0
        TotalExpenses = 0.0
        Unallocated = 0.0


        # Check if stats file exists and read its content
        if os.path.exists(stats_csv_file_path):
            with open(stats_csv_file_path, mode='r', newline="") as statsfile:
                reader = csv.DictReader(statsfile)
                rows = list(reader)

                if rows:
                    TotalContained = float(rows[0]['TotalContained'])
                    TotalExpenses = float(rows[0]['TotalExpenses'])
                    Unallocated = float(rows[0]['Unallocated'])

        # Adjust the stats based on the payment amount
        if amount_to_adjust < 0:
            TotalExpenses += abs(amount_to_adjust)
        TotalContained += amount_to_adjust
        Unallocated += amount_to_adjust

        # Write the updated stats back to the stats file
        with open(stats_csv_file_path, mode='w', newline="") as statsfile:
            fieldnames = ['TotalContained', 'TotalExpenses', 'Unallocated']
            writer = csv.DictWriter(statsfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow({'TotalContained': TotalContained, 'TotalExpenses': TotalExpenses, 'Unallocated': Unallocated})