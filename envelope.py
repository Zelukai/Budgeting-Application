class Envelope: 
    def __init__(self, name, parent, allocation): 
        self.name = name
        self.parent = parent # would pass in the name of the parent Envelope object
        self.allocation = allocation 
        self.exp_running_t =  allocation# upon creation, it will call the record function 
        self.record() 
    
    def record(self): 
        data = [
            []
        ]
        
        # opening file then writing to it
        csv_file_path = f'{self.name}.csv'
        with open(csv_file_path, mode='w') as file: 
            for row in data: 
                pass 
                # need to look at documentation to write this
    