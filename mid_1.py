class Star_Cinema:
        __hall_list=[]

        def entry_hall(cls,hall):
                cls.__hall_list.append(hall)

class Hall:
        def __init__(self,name,capacity):
                self.name= name
                self.capacity=capacity
        def __str__(self):
                return f"Hall:{self.name},capacity:{self.capacity}" 
       
hall1=Hall("Hall 1",300)
hall2=Hall("Hall 2",200)

Star_Cinema.entry_hall(hall1)
Star_Cinema.entry_hall(hall2)

print(Star_Cinema._star_Cinema__hall_list)
