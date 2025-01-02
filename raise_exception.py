# class Accident(Exception):
#     def __init__(self,msg):
#         self.msg = msg
#     def handle(self):
#         print("accident occured, take detour",self.msg)



# try:
#     raise Accident('crash between two cars')
# except Accident as e:
#     e.handle()

def process_file():
    try:
        f = open("G:\\New learning\\python\\book.txat")
        x = 1/0
    except FileNotFoundError as e:
        print("inside except")
    finally:
        print("cleaning up file")
        f.close()

process_file()