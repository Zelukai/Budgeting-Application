import envelope

class Payment: 
    def __init__(self, amount=0, recurring = False, projection = False, envelope: Envelope):
        self.amount = amount
        self.recurring = recurring
        self.projection = projection
        self.envelope = envelope
    def record(self):
        csv_file_path
    