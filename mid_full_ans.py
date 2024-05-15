
class Star_Cinema:
        __hall_list=[]

        def entry_hall(cls,hall):
                cls.__hall_list.append(hall)



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


    def view_show_list(self):
        return self._show_list
    
    def view_available_seats(self,show_id):
        if show_id< 1 or show_id > len(self.shows):
            print("Invalid show ID.")
            return
        show= self.shows[show_id-1]
        print(f"Available seats for{show.name}({show.time}):{show.available_seats}/{show.total_seats}")

    
    
class counter:
    def __init__(self,hall):
        self.hall=hall
    
    def view_all_shows(self):
        return self.hall.view_all_shows()
    def view_available_seats(self,show_id):
        return self.hall.view_available_seats(show_id)
    
    def book_tickes(self,show_id,seat):
        self.hall.book_ticket(show_id,seat)



              
def book_seat(show_id,seat_number):
    if not is_valid_show_id(show_id):
        return "Error: Invalid show ID"
    if not is_valid_seat_number(show_id,seat_number):
        return "Error: Invalid seat number"
    if is_seat_booked(show_id,seat_number):
        return "Error:seat already booked"
    

    book_seat_for_show(show_id,seat_number)
    return " Seat booked successfully"


def is_valid_show_id(show_id):
    return show_id 

def is_valid_seat_number(show_id,seat_number):
    return seat_number>=1 and seat_number <= [show_id]

def is_seat_booked(show_id,seat_number):
    return (show_id,seat_number) in book_seat

def book_seat_for_show(show_id,seat_number):
    book_seat.append((show_id,seat_number))


