class routine:
    def monday(self):
        print("studying")
    def tuesday(self):
        print("exercise")
    def wednesday(self):
        print("washing")
    def thursday(self):
        print("hair care")
    def friday(self):
        print("skin care")
    def saturday(self):
        print("baking")
    def sunday(self):
        print("chilling")
    def other_day(self):
        print("it's invalid choice")
        exit()
class Menu:
    def __init__(self):
        pass
    def get_menu(self,event):
        menu={
            1:event.monday,
            2:event.tuesday,
            3:event.wednesday,
            4:event.thursday,
            5:event.friday,
            6:event.saturday,
            7:event.sunday,
            8:event.other_day
        }
        return menu
    def run_menu(self):
        event=routine()
        while True:
            choice=int(input("enter 1:monday 2:tuesday 3:wednesday 4:thursady 5:friday 6:saturday 7:sunday 8:exit"))
            m=self.get_menu(event)
            print(type(m))
            m.get(choice)()
        print("end of the program")
menu=Menu()
menu.run_menu()