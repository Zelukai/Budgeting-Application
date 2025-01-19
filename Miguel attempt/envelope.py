import csv
import datetime
import payment
from datetime import date
import os 

class Envelope: 
    envelope_names = []
    def __init__(self, name:str, allocation:int, parent=None, children=[]): 
        self.name = name
        self.parent = parent 
        self.allocation = allocation 
        self.children = children
        self.expense_total = 0 
        # creating folder and nesting it in envelopes
        # nested_dir = os.path.join("envelopes", self.name)
        # os.makedirs(nested_dir, exist_ok=True)
        # self.folder_path = nested_dir

        if parent: 
            if isinstance(parent, Envelope) and parent.name == self.name: # if the envelope is nested, do the following
                self.parent = parent
                assert self.allocation <= parent.allocation, f"Child envelope allocation {self.allocation} exceeds parent allocation {parent.allocation}"
                parent.add_child(self)
                nested_dir = os.path.join("envelopes", parent.name, self.name) # creating the proper file structure: envelopes\parent.name\self.name

            else: 
                raise ValueError(f"Parent envelope {parent.name} not valid")
        else: 
            nested_dir = os.path.join("envelopes", self.name) # since the first doesn't work, it means we are the FIRST folder so its just envelopes\self.name
            # self.parent = None
        os.makedirs(nested_dir, exist_ok=True) # actually makes the directy with the proper path
        self.folder_path = nested_dir         

        Envelope.envelope_names.append(self.name)

        # upon creation, it will call the record function 
        self.record() 


    def add_child(self, child): 
        self.children.append(child)
    

    def record(self): 
        # Ensure the folder structure exists
        os.makedirs(self.folder_path, exist_ok=True)

        # Define the list of column headers
        headersList = ["Amount", "Date", "Envelope"]

        # Create the full path for the CSV file
        csv_file_path = os.path.join(self.folder_path, f'{self.name}.csv')

        # Open the CSV file and write the headers
        with open(csv_file_path, mode='w+', newline="") as file:
            writer = csv.writer(file)
            writer.writerow(headersList)
        
        # Record the initial allocation as a payment
        allocation_pay = payment.Payment(self.allocation, date.today(), False, False, self.name)
        allocation_pay.record()

        # Update user
        print(f"Envelope {self.name} was created in folder '{self.folder_path}'") 
        print(f"Funds allocated: {self.allocation}")
        

    