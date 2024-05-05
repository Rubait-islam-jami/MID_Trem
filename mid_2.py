class Star_Cinema:
    __hall_list=[]

    def entry_hall(cls,hall):
        cls.__hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no):
        self.seats={}
        self.show_list=[]
        self.rows= rows
        self.cols=cols
        self.hall_on=hall_no
        self.entry_hall(self)
    
    def __str__(self):
        return f"Hall No:{self.hall_no},Rows:{self.rows},Columns:{self.cols}"
    
hall1 = Hall(rows=10, cols=8,hall_on=1)
hall1 = Hall(rows=12, cols=10,hall_on=2)

print(Star_Cinema._Star_Cinema__hall_list)