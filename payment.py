import envelope
import csv

class Payment: 
    def __init__(self, amount=0, date = datetime.today(), recurring = False, projection = False, envelope = 'total'):
        self.amount = amount
        self.date = date
        self.recurring = recurring
        self.projection = projection
        self.envelope = envelope
        self.record()

    def record(self):
        entryList = [self.amount, self.date, self.envelope]
        csv_file_path = f'{self.envelope}.csv'
        with open(csv_file_path, mode='w', newline="") as file:
            writer = csv.writer(file)
            writer.writerow(entryList)

        # update user
        print(f"Envelope {self.name} was created") 
        print(f"Funds allocated: {self.allocation}")
        print(f"Current total: {self.exp_running_t}")

    