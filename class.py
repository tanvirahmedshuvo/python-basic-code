#************Class************

class Human:
    def __init__(self,n,o):
        self.name = n
        self.occupation = o
                                            #this one is properties
    
    def do_work(self):
        if self.occupation == "tennis player":
            print(self.name,"Plays tennis")
        elif self.occupation == "actor":
            print(self.name,"Shoots a flim")
                                                #do_work and speaks are mathod
    
    def speaks(self):
        print(self.name,"says, how are you?")

tom = Human("tom cruise","actor")
tom.do_work()
tom.speaks()

maria = Human("maria sharapova","tennis player")
maria.do_work()
maria.speaks()