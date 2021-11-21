class Kipas :
    brand = None
    rotasi = False
    _gear = 3
    _capacity = 103 


    def __init__(self, brand, capacity) :
        self.brand = brand
        self._capacity = capacity

  
    def setGear(self, gear):
        self._gear = gear

    def _getGear(self):
        return f"Gear : {self._gear}"

    def _getCapacity(self):
        return f"Kapasistas {self._capacity} Watt"

    def turnOnrotasi(self):
        self.rotasi = True

    def turnOffrotasi(self):
        self.rotasi = False

    def _getrotasi(self):
      return F"rotasi {'nyala ' if self.rotasi else 'Mati'}"

    def detail(self):
        print("------------------------")
        print(f"Brand : {self.brand}")
        print(self._getGear())
        print(self._getCapacity())
        print(self._getrotasi())
        print("------------------------")


# Subclass
class Sharp(Kipas):
    def __init__(self, type):
      
        if(type == 'Ruang tamu') :
            capacity = 120 
        elif (type == 'Kamar'):
            capacity = 110 
        else :
            capacity = 100

        super(Sharp, self).__init__(f"Sharp {type}", 12)

    
    def setGear(self, gear):
        self._gear = "kiri kanan" if gear < 3 else gear



 ##Super class
kipas = Kipas("Polytron", 110)
kipas.setGear(3)
kipas.turnOnrotasi()
kipas.detail()
kipas.turnOffrotasi()
kipas.detail()

 ##Subclass

sharp = Sharp("Kamar")
sharp.setGear(3)
sharp.turnOnrotasi()
sharp.detail()
sharp.setGear(-1)
sharp.turnOffrotasi()
sharp.detail()