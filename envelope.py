import csv
import payment

class Envelope: 
    def __init__(self, name:str, allocation:int, parent=None, children=[]): 
        self.name = name
        self.parent = parent 
        self.allocation = allocation 
        self.children = children
        self.exp_running_t =  allocation# upon creation, it will call the record function 
        self.record() 
    
    def record(self): 

        # list of the column headers
        headersList = ["Envelope ID","Envelope Name","Parent ID","Allocation","Net Running Total","Expenses Running Total"]
        csv_file_path = f'{self.name}.csv'
        with open(csv_file_path, mode='w', newline="") as file:
            writer = csv.writer(file)
            writer.writerow(headersList)
            
        

        # update user
        print(f"Envelope {self.name} was created") 
        print(f"Funds allocated: {self.allocation}")
        print(f"Current total: {self.exp_running_t}")
        

    