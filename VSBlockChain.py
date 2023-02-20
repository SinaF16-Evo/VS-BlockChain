import Block
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
        if data == None  :
            self.blockchain.append(Block("" , 0 , None))
        else :
            if len(data) <= self.blocksizeremain() :
                self.blockchain[-1].append(data)
            else :
                self.blockchain.append(Block(hashlib.sha256(json.dumps(self.blockchain[-1].__dict__).encode("utf-8")).hexdigest() , self.blockchain[-1][1] + 1 , [data]))
                



    def addtext (self , data) :
        if self.blockchain == [] :
            self.addblock()
        else :
            self.addblock(data)