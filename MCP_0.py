from email.errors import NoBoundaryInMultipartDefect
from MCP_i import cylinder
from MCP_i import line
from MCP_i import Simple_Interest

#Creating a class that does the greeting
class Greeting():
    def __init__(self,req="Nobody"):
        self.req = input(" Welcome,what is  your name?  ")
    '''
    create a method that welcomes
    '''
    def welcome(self):
        try:
            print("welcome, " + str(self.req))
        except:
            TypeError("There was an input error")
    '''
    this class does the farewell greeting
    '''
    def farewell(self):
        print(f"Thank you {self.req} for using this app!")

#this function is used in the while loop to control the running of the app
def stop_operation():
    choice = str(input(" press 1 to continue and 2 to stop:  "))
    return choice == "1"

#Running the prrogram
while True:
    #greeting the users 
    greet = Greeting()
    print(greet.welcome())
    '''
    Asking user to select operator
    '''
    def choose_operation():
        operator = input("""
        FOLLOW THE INSTRUCTIONS[NUMBERS]
        1 - Volume of a cylinder 
        2 - Surfave Area of a cylinder
        3 - Slope of a line
        4 - Distance between two  points
        5 - Simple Interest
                            """     )
        
        if operator == "1":
            mycyl = cylinder()
            return mycyl.volumer()
        elif operator == "2":
            mycyl = cylinder()
            return mycyl.total_surf_area()
        elif operator == "3":
            myline = line()
            return myline.slope()
        elif operator == "4":
            myline = line()
            return myline.distance()
        elif operator == "5":
            simp = Simple_Interest()
            return simp.output()
        else:
            print("No operation chosen")
    choose_operation()

    #breaking the while loop with some conditions
    if not stop_operation():
            print(greet.farewell())
            break

if __name__ == "__main__":
    Greeting(req='Nobody')
    stop_operation()