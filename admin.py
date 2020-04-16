class admin:

    def __init__(self, nama, id):
        self.__nama = nama
        self.__id = id

    @property
    def nama(self):
        pass
    @nama.getter
    def nama(self):
        return self.__nama
    @nama.setter
    def nama(self, nama):
        self.__nama = nama

    @property
    def id(self):
        pass
    @id.getter
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        self.__id = id

admin1 = admin("Fara", 1011)
print("nama admin", admin1.nama, "dengan id", admin1.id)


