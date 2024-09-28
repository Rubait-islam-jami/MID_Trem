class Star_Cinema:
        hall_list=[]

        def entry_hall(self,hall):
             Star_Cinema.hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no)-> None:
        self.seats={}
        self.show_list=[]
        self.rows=rows
        self.cols=cols
        self.hall_no= hall_no
        self.entry_hall(self)

    def entry_show(self,show_id,movie_name,time):
        show_info =(show_id,movie_name,time)
        self.show_list.append(show_info)
        seatAvailable=[]
        for row in range(self.rows):
            rowInfo=[]
            for x in range(self.cols):
                  rowInfo.append(0)
            seatAvailable.append(rowInfo)
        self.seats[show_id]=seatAvailable

    def book_seats(self,show_id,list):
        for key,values in self.seats.items():
            if show_id == key:


                if list[0] >= self.rows or list[1] >=self.cols:
                    print("Invalid seat selection")
                    return
                
                if values[list[0]][list[1]] == 1:
                    print("seat are already booked")
                else:
                   print("seat booked succesfully")
                   values[list[0]][list[1]] =1
                   return
            else :
                print("Invalid ID")
                return

    def view_show_list(self):
        for view in self.show_list:
            print(view)
    
    def view_available_seats(self,show_id):
        for key,value in self.seats.items():
            if show_id != key:
                print("Invalid ID")
                return
            else:
                for row_index in range(len(value)):
                    row=value[row_index]
                    for col_index in range(len(row)):
                        seat_status ="Available" if row[col_index] == 0 else "Booked"
                        print(f"({row_index},{col_index})-{seat_status}",end=" ")
                    print()
                return
                
       
           
hall1= Hall(5,5,121)
hall1.entry_show(111,'the dark knight(111)','25/10/2023 11.00 AM')
hall1.entry_show(333,'black(333)','25/10/2023 2.00 AM')
run = True
while run:
    print("Welcome to our Cinema Hall")
    print('1.\t View all show today')
    print('2.\t view available seats')
    print('3.\t Book Ticket')
    print('4.\tEXIT')
    option =int(input("Enter options:"))
    if(option==1):
      hall1.view_show_list()
      print('......................')
    elif(option==2):
      show_id=int(input('Enter Show ID:'))
      hall1.view_available_seats(show_id)
    elif(option==3):
      show_id=int(input("Enter show ID:"))
      rows=int(input("Enter rows: "))
      cols=int(input("Enter Cols:"))
      list=(rows,cols)
      A=hall1.book_seats(show_id,list)
    elif option==4:
      break
