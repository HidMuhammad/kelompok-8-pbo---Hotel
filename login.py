class tamu():
    def __init__(self, Nama, ktp, telp):
        self.nama = Nama
        self.__ktp = ktp
        self.__telp = telp
    @property
    def ktp(self):
        pass
    @ktp.getter
    def ktp(self):
        return self.__ktp
    @ktp.setter
    def ktp(self, ktp):
        self.__ktp = ktp
    @property
    def telp(self):
        pass
    @telp.getter
    def telp(self):
        return self.__telp
    @telp.setter
    def telp(self, telp):
        self.__telp = telp


tamu1 = tamu("taukhid", 68566465, 76)
print("nama saya",tamu1.nama, "no ktp saya", tamu1.ktp, "no telp saya", tamu1.telp)

class login(tamu):

def __init__(self, user, passw)
pass




        