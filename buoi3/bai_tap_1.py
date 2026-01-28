class Car:
    loai_xe = "Xe hơi"  

    def __init__(self, ten_xe, mau_sac, nguyen_lieu):
        self._ten_xe = ten_xe
        self._mau_sac = mau_sac
        self._nguyen_lieu = nguyen_lieu

    @property
    def ten_xe(self):
        return self._ten_xe
    
    @property
    def mau_sac(self):
        return self._mau_sac
    
    @property
    def nguyen_lieu(self):
        return self._nguyen_lieu

    def stop(self, reasons):
        return "Xe {} dừng lại vì {}.".format(self.ten_xe, reasons)
    
    def run(self):
        return "Xe {} đang chạy.".format(self.ten_xe)
    
    def startEngine(self):
        return "{} đang nổ máy".format(self.ten_xe)

toyota = Car("Toyota Camry", "Trắng", "Xăng")
honda = Car("Honda Civic", "Đen", "Dầu diesel")
porsche = Car("Porsche 911", "Đỏ", "Xăng")

toyota = Car("Toyota", "Đỏ", "Điện")
lamborghini = Car("Lamborghini", "Vàng", "Deisel")
porsche = Car("Porsche", "Xanh", "Gas")

print("Porsche là {}.".format(porsche.__class__.loai_xe))
print("Toyota là {}.".format(toyota.__class__.loai_xe))
print("Lamborghini cũng là {}.".format(lamborghini.__class__.loai_xe))

print("Xe {} có màu {}. {} là nguyên liệu vận hành.".format(toyota.ten_xe, toyota.mau_sac,
toyota.nguyen_lieu))
print("Xe {} có màu {}. {} là nguyên liệu vận hành.".format(lamborghini.ten_xe,
lamborghini.mau_sac, lamborghini.nguyen_lieu))
print("Xe {} có màu {}. {} là nguyên liệu vận hành.".format(porsche.ten_xe, porsche.mau_sac,
porsche.nguyen_lieu))

print(toyota.stop("nạp điện"))
print(lamborghini.run())
print(porsche.startEngine())