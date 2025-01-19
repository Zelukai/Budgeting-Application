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

        # list of the column headers
        headersList = ["Envelope ID","Envelope Name","Parent ID","Allocation","Net Running Total","Expenses Running Total"]
        csv_file_path = os.path.join(self.folder_path, f'{self.name}.csv')
        with open(csv_file_path, mode='w+', newline="") as file:
            writer = csv.writer(file)
            writer.writerow(headersList)
        
        allocation_pay = payment.Payment(self.allocation, date.today(), False, False, self.name)
        allocation_pay.record()

        # update user
        print(f"Envelope {self.name} was created") 
        print(f"Funds allocated: {self.allocation}")
        

    