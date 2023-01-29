class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def __str__(self):
        return f"CPU: {self.__cpu} MEMORY: {self.memory}"

    def make_computations(self):
        a = self.cpu + self.memory
        b = self.cpu - self.cpu
        c = self.cpu * self.memory
        d = self.cpu // self.memory
        return f"cpu {self.cpu} + memory {self.memory} = {a}\n" \
               f"cpu {self.cpu} - memory {self.memory} = {b}\n" \
               f"cpu {self.cpu} * memory {self.memory} = {c}\n" \
               f"cpu {self.cpu} // memory {self.memory} = {d}\n"

    def __gt__(self, other):
        return self.__cpu > self.other

    def __lt__(self, other):
        return self.__cpu < self.other

    def __eq__(self, other):
        return self.__cpu == self.other


class Phone:
    def __init__(self, sim_card_list: list):
        self.__sim_card_list = sim_card_list

    @property
    def sim_card_list(self):
        return self.__sim_card_list

    @sim_card_list.setter
    def sim_card_list(self, value):
        self.__sim_card_list = value

    def __str__(self):
        return f"sim card list: {self.__sim_card_list}"

    def call(self, sim_card_number, call_to_number):
        self.sim_card_number = sim_card_number
        self.call_to_number = call_to_number
        return f"идёт звонок на номер: {self.call_to_number} с сим-карты: {self.sim_card_list[self.sim_card_number]}"


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_card_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_card_list)

    def use_gps(self, location):
        self.location = location
        return f"проложен маршрут до: {self.location}"

    def __str__(self):
        return f'cpu: {self.cpu} memory: {self.memory} sim card list: {self.sim_card_list}'


asus = Computer(23, 32)
iphone = Phone(['Beeline', 'O!'])
samsung = SmartPhone(600, 32, ["Beeline", "o!", "MegaCom"])
huawei = SmartPhone(650, 16, ["Beeline", "o!", "MegaCom"])
print(iphone.call(1, 123453456))
print(samsung.use_gps("Цум"))
print(asus.make_computations())
print(asus)
print(iphone)
print(samsung)
print(huawei)
