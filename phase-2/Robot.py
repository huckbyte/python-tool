
class Robot_into:
    first_name =""
    second_name =""
    old=""
    task =""

    def Get_Info(self):
        self.first_name= input("What's your first_name ::")
        self. second_name= input("What's second_name ::")
        self. old= input("How old are your :")
        self. task= input("what task doy want me to perform ::")

    def Display_Info(self):
        print("first_name: "'{}'.format(self.first_name))
        print(" second_name: "'{}'.format(self. second_name))
        print(" old: "'{}'.format(self. old))
        print(" task: "'{}'.format(self. task))

#robot = Robot_into()
#robot.Get_Info()
#robot.Display_Info()

#-------------------------------------------------

class Task_info():

    def __init__(self,task_one, task_two, task_start, task_stop):
        self.task_one = task_one
        self. task_two =  task_two
        self. task_start =  task_start
        self. task_stop =  task_stop

    def Task_info(self):
        print("task_one: "'{}'.format(self.task_one))
        print(" task_two: "'{}'.format(self. task_two))
        print(" task_start: "'{}'.format(self. task_start))
        print(" task_stop: "'{}'.format(self. task_stop))


#robot = Task_info("memo","cool",1.00,1.30)
#robot.Task_info()

#-------------------------------------------------

class Task():
    cook = ""
    wash = ""
    walk = ""

    def Task_info(self):

        self. cook = ""
        self.wash = ""
        self.walk = ""
        a = int(input("select the task number you want assistance : \n 1 : cook \n 2: wask \n 3: walk"))
        if a == 1:
            self. cook = "What to want to cook."
        elif a == 2:
            self.wash = "were are the cloths to be washed ."
        elif a == 3:
            self.walk = "where should we visit....."
        else:
            print("sorry provide the task number correctly if you still need assistance ")

    def Disolay_task_info(self):
        print("Task 1 => "'{}'.format(self. cook))
        print("Task 2 => "'{}'.format(self.wash))
        print("Task 3 =>"'{}'.format(self.walk))

robot1 = Task()
# robot1.Task_info()
# robot1.Disolay_task_info()

#-------------------------------------------------

class Assis_Robot():
    
    def __init__(self,  cook, wash, walk):
        self. cook =  cook
        self.wash = wash
        self.walk = walk

    def Display_robot_info(self):
        b = 0
        while b<5:
            print("Task 1 => "'{}'.format(self. cook))
            print("Task 2 => "'{}'.format(self.wash))
            print("Task 3 =>"'{}'.format(self.walk))

            a = int(input("enter a number of task your ordered to be done:\n"))
            if a == 1:
                self. cook = "food is ready .... do you want to test it......"
            elif a == 2:
                self.wash = "where should put this clothes i think they are ready"
            elif a == 3:
                self.walk = "i think this habit is quite empowering our life should we keep it as a routine"
            else:
                print("sorry provide the task number correctly .. ")
            b += 1

robot1 = Assis_Robot("=>", "=>", "=>")
# robot1.Display_robot_info()

