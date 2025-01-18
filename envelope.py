import csv

class Envelope: 
    def __init__(self, name, allocation, parent=None): 
        self.name = name
        self.parent = parent 
        self.allocation = allocation 
        self.exp_running_t =  allocation# upon creation, it will call the record function 
        self.record() 
    
    def record(self): 

        # list of the column headers
        headersList = ["Name", "Allocation", "Exp_Running_T"]
        csv_file_path = f'{self.name}.csv'
        with open(csv_file_path, mode='w', newline="") as file:
            writer = csv.writer(file)
            writer.writerow(headersList)

        # update user
        print(f"Envelope {self.name} was created") 
        print(f"Funds allocated: {self.allocation}")
        print(f"Current total: {self.exp_running_t}")

    