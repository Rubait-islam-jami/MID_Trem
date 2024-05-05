class Hall:
    def __init__(self,rows,cols,hall_no):
        self.seats={}
        self.show_list=[]
        self.rows=rows
        self.cols=cols
        self.hall_no= hall_no
        self.allocate_seats()

    def __str__(self):
        return f"Hall No:{self.hall_no}, Rows:{self.rows},Colums:{self.cols}"    
    
    def entry_show(self,show_id,movie_name,time):
        show_info =(show_id,movie_name,time)
        self.show_list.append(show_info)
        self.seats[show_id]=[[0]*self.cols for _ in range(self.rows)]

    def allocate_seats(self):    
        self.seats["default"]=[['Free' for _ in range(self.cols)] for _ in range(self.rows) ]

hall1=Hall(rows=3,cols=4,hall_on=1)
hall1.entry_show("1","Movie 1","12.00 PM")

print(hall1.show_list)
print(hall1.seats)

