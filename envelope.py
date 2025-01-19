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
        # upon creation, it will call the record function 

        if parent: 
            if isinstance(parent, Envelope) and parent.name == self.name: 
                self.parent = parent
                parent.add_child(self)
            else: 
                raise ValueError(f"Parent envelope {parent.name} not valid")
        else: 
            self.parent = None

        Envelope.envelope_names.append(self.name)
        self.record() 


    def add_child(self, child): 
        self.children.append(child)
    
    def record(self): 

        # list of the column headers
        headersList = ["Envelope ID","Envelope Name","Parent ID","Allocation","Net Running Total","Expenses Running Total"]
        csv_file_path = f'{self.name}.csv'
        with open(csv_file_path, mode='w+', newline="") as file:
            writer = csv.writer(file)
            writer.writerow(headersList)
        
        allocation_pay = payment.Payment(self.allocation, date.today(), False, False, self.name)
        allocation_pay.record()

        # update user
        print(f"Envelope {self.name} was created") 
        print(f"Funds allocated: {self.allocation}")
        

    