import csv
import datetime
import payment
from datetime import date
import os 
import main

class Envelope: 
    envelope_names = []
    def __init__(self, name:str, allocation:int, parent=None, children=[]): 
        self.name = name
        self.parent = parent 
        self.allocation = allocation 
        self.children = children
        self.expense_total = 0

        if self.parent != None:
            print(self.parent)
            file_path = main.find(self.parent)
            print(f'file path:{file_path}')
            nested_path = os.path.join(file_path, self.name) 
            os.makedirs(nested_path, exist_ok=True) # creates directory
            self.folder_path = nested_path     
        else:
            file_path = 'envelopes'
            print(f'file path:{file_path}')
            nested_path = os.path.join(file_path, self.name) 
            os.makedirs(nested_path, exist_ok=True) # creates directory
            self.folder_path = nested_path    

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
        statsHeadersList = ['TotalContained', 'TotalExpenses', 'Unallocated']
        # Create the full path for the CSV file
        csv_file_path = os.path.join(self.folder_path, f'{self.name}.csv')
        stats_csv_file_path = os.path.join(self.folder_path, f'stats_{self.name}.csv')

        # Open the CSV file and write the headers
        with open(csv_file_path, mode='w+', newline="") as file:
            writer = csv.writer(file)
            writer.writerow(headersList)
        
        with open(stats_csv_file_path, mode='w+', newline="") as statsfile:
            stats_writer = csv.writer(statsfile)
            stats_writer.writerow(statsHeadersList)

        # Record the initial allocation as a payment
        allocation_pay = payment.Payment(self.allocation, date.today(), False, False, self.name)

        the_parent = main.find(self.parent)
        allocation_balance = payment.Payment(-self.allocation, date.today(), False, False, self.parent)
        
        with open(the_parent + f"/stats_{self.parent}.csv", mode='r', newline="") as statsfile:
                reader = csv.DictReader(statsfile)
                rows = list(reader)

                if rows:
                    TotalContained = float(rows[0]['TotalContained'])
                    TotalExpenses = float(rows[0]['TotalExpenses'])
                    Unallocated = float(rows[0]['Unallocated'])

        Unallocated -= self.allocation

        # Write the updated stats back to the stats file
        with open(the_parent + f"/stats_{self.parent}.csv", mode='w', newline="") as statsfile:
            fieldnames = ['TotalContained', 'TotalExpenses', 'Unallocated']
            writer = csv.DictWriter(statsfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow({'TotalContained': TotalContained, 'TotalExpenses': TotalExpenses, 'Unallocated': Unallocated})

        # Update user
        print(f"Envelope {self.name} was created in folder '{self.folder_path}'") 
        print(f"Funds allocated: {self.allocation}")
        

    