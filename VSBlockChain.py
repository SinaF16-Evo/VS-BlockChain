from Block import Block
import hashlib
import json

class VSB :
    def __init__ (self) :
        self.blockchain = []

    def blocksizeremain (self) :
        byte8x = 0
        for i in self.blockchain[-1].data[-1] :
            byte8x += len(i)
        return 16 - byte8x
    
    def addblock (self , data = None) :
        if len(self.blockchain) == 0  :
            self.blockchain.append(Block("" , 0 , ""))
            if len(data) <= 16 :
                self.blockchain.append(Block(hashlib.sha256(json.dumps(self.blockchain[-1].__dict__).encode("utf-8")).hexdigest() , self.blockchain[-1].data[1] + 1 , data))
            else :
                print("The Input is More Than 256-Bit ")

        elif data == None :
            pass
        else :
            if len(data) <= 16 :
                if len(data) <= self.blocksizeremain():
                    self.blockchain[-1].data[-1].append(data)
                else :
                     self.blockchain.append(Block(hashlib.sha256(json.dumps(self.blockchain[-1].__dict__).encode("utf-8")).hexdigest() , self.blockchain[-1].data[1] + 1 , data))
                    
            else :
                print("The Input is More Than 256-Bit ")
    def showblockprop (self , num) :
        if num <= len(self.blockchain) :
            self.blockchain[num - 1].showblock()
        else :
            print ("No such Block")


    def addtext (self , data) :
        if self.blockchain == [] :
            self.addblock()
        else :
            self.addblock(data)