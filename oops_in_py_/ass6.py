# if not present in dictionary
# maintain an arrangement for stock y or n
class pb:
    _counter=100
    def calculatebill(self,item,quantity):
        self.d = {"tv": 20000 , "ac":50000,"table":30000}
        for k in self.d.keys():
            if k==item:
                self:_billamount=self.d[k]*quantity
        def desbill(self):
            o=pd()
            o.scanchar("*")
            o.ph(20)
            o.ph1("Easy shop")
            o.ph(20)
        def getbillamount(self):
            return self.__billamount
        def purchasebill(self,billamount):
            self._billamount=billamount
            pb._counter+=1
            self.billid=pb._counter
            print(self.getbillid())
            print(self._billamount)
            self.dispbill()
            