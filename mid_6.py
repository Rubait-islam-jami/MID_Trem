class Show:
    def __init__(self,name,time,total_seats):
        self.name=name
        self.time=time
        self.total_seats=total_seats
        self.available_seats= total_seats
class Hall:
    def __init__(self,name):
        self.name=name 
        self.shows=[]

    def add_show(self,show):
        self.shows.append(show)

    def view_available_seats(self,show_id):
        if show_id< 1 or show_id > len(self.shows):
            print("Invalid show ID.")
            return
        show= self.shows[show_id-1]
        print(f"Available seats for{show.name}({show.time}):{show.available_seats}/{show.total_seats}")
hall=Hall("Main Hall")
show1 = Show("Concert","7:00 PM",100)

hall.add_show(show1)

hall.view_available_seats(1)
