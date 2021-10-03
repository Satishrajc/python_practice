class Employee:
    def __init__(self, name, CTC):
        self.name = name
        self.__CTC = CTC
        self.__perce_increament = 0

    def __new_salary(self):
        pass
        # return self.__CTC

    def __increament(self, percent):
        self.__CTC = self.__CTC + (self.__CTC * percent / 100)
        print("Private : ", self.__CTC)

    hike = property(__new_salary, __increament)


obj = Employee('Satish', 1000)

obj.hike = 10
