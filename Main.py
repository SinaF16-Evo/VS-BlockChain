from VSBlockChain import VSB

class Main :
    def __init__ (self) :
        print ("Welcome to VSB Block Chain.\nEnter EveryThing You Want But Not More Than 256 Bit!")
        print ("For Show Specific Block Please Write \"SHOW\" and then write number of block with SPACE to show Properties of that Block")
        print ("To Exit Write \"EXIT\"")
        vs = VSB()
        while True :
            data = input("Enter Your Input : ")
            if data[0:4] == "SHOW":
                if data.split()[1] in "1234567890" :
                    vs.showblockprop(int(data.split()[1]))
            elif data == "EXIT" :
                exit()
            else :
                vs.addblock(data)

Main()

            
