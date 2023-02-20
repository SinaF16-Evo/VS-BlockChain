class Block :
    def __init__(self , preblockhash,preblocknum , bdata) :
        self.data = [preblockhash ,preblocknum, [bdata]]

    def showblock (self) :
        print(f"Block Number {self.data[1]}\nData : {self.data[2]}\nPrevious Block Hash : {self.data[0]}")

    

    
        