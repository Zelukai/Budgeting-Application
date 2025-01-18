import envelope
import datetime

class Payment: 
    def __init__(self, amount=0, date = datetime.now(), recurring = False, projection = False, envelope: Envelope):
        self.amount = amount
        self.date = date
        self.recurring = recurring
        self.projection = projection
        self.envelope = envelope
    def record(self):
        csv_file_path = f'{self.envelope}.csv'
        with open(csv_file_path, mode='w') as file: 
            file.write([self.amount, self.date, self.envelope])
    