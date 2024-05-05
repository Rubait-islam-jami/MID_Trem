class Hall:
    def __init__(self,rows,cols,hall_no):
        self.rows=rows
        self.cols=cols
        self.hall_no=hall_no
        self.seats={}
        self.show_list=[]

    def entry_show(self,show_id,movie_name,time):
        show_info =(show_id,movie_name,time)
        self.show_list.append(show_info)
        self.seats[show_id]=[['Free' for _ in range(self.cols)]for _ in range(self.rows)]

    def book_seats(self,show_id,seat_list):
        if show_id not in self.seats:
            print("Invalid show ID.")
            return
        for seat in seat_list:
            row,col=seat
            if 0<=row <self.rows and 0<=col <self.cols:
                if self.seats[show_id][row][col]=='Free':
                    self.seats[show_id][row][col] ='Booked'
                    print(f"Seat ({row},{col} )booked successfully.")
                else:
                    print(f"Seat({row},{col}) is already booked.")
    def __str__(self):
        return f"Hall No: {self.hall_no},Rows:{self.rows},Columns:{self.cols}"

hall1 =Hall(rows=3,cols=4,hall_no=1)
hall1.entry_show("1","Movies 1","12:00 PM")

print(hall1.show_list)
print(hall1.seats)

hall1.book_seats("1",[(0,0),(1,1),(2,2),(3,3)])
hall1.book_seats("1",[(0,0),(1,1),(1,2)])

print(hall1.seats)
    
    
