class Robot:
    jumlah_turn = 0
    
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
        self.jumlah_turn += 1

    def lakukan_aksi(self, lawan):
        print(f"{self.name}  menyerang  {lawan.name} sebanyak {self.damage} DMG")
        lawan.health -= self.damage
        if self.jumlah_turn % 3 == 2 and isinstance(self, Antares):
            self.damage = int(self.damage * 1.5)
            print(f"{self.name}  damage meingkat sebanyak {self.damage} DMG")

        elif self.jumlah_turn % 2 == 1 and isinstance(self, Alphasetia):
            self.health += 4000
            print(f"{self.name} darah bertambah sebanyak 4000 HP")

        elif self.jumlah_turn % 4 == 3 and isinstance(self, Lecalicus):
            self.damage = int(self.damage * 2)
            self.health += 7000
            print(f"{self.name} damage meningkat sebanyak  {self.damage} DMG dan darah bertambah sebanyak 7000 HP")

    def terima_aksi(self, lawan):
        print(f"{self.name}  menerima serangan dari {lawan.name} sebanyak {lawan.damage} DMG")
        self.health -= lawan.damage


class Antares(Robot):
    def __init__(self):
        super().__init__("Antares", 50000, 5000)


class Alphasetia(Robot):
    def __init__(self):
        super().__init__("Alphasetia", 40000, 6000)


class Lecalicus(Robot):
    def __init__(self):
        super().__init__("Lecalicus", 45000, 5500)


print("Pilih robot :\n 1 = Antares \n 2 = Alphasetia \n 3 = Lecalicus")

robot_saya = int(input("Masukkan Pilihan Robot Kamu : "))
if robot_saya == 1:
    robot_saya = Antares()
elif robot_saya == 2:
    robot_saya = Alphasetia()
elif robot_saya == 3:
    robot_saya = Lecalicus()
else:
    print("Error!")

robot_lawan = int(input("Masukkan Pilihan Robot Lawan  : "))
if robot_lawan == 1:
    lawan = Antares()
elif robot_lawan == 2:
    lawan = Alphasetia()
elif robot_lawan == 3:
    lawan = Lecalicus()
else:
    print("Error!")

print("Pilihan Tangan :\n 1 untuk batu\n 2 untuk kertas\n 3 untuk gunting\n")

for turn in range(1, 10):
    print("Turn : ", turn)
    print(f"Robotmu ({robot_saya.name})  {robot_saya.health} HP,  robot lawan ({lawan.name}) {lawan.health} HP")
    robot = int(input(f"Pilih tangan robotmu ({robot_saya.name}) : "))
    robot_lawan = int(input(f"Pilih tangan robot lawan ({lawan.name}) : "))
    if robot == 1 and robot_lawan == 2:
        lawan.lakukan_aksi(robot_saya)
    elif robot == 1 and robot_lawan == 3:
        robot_saya.lakukan_aksi(lawan)
    elif robot == 2 and robot_lawan == 1:
        lawan.lakukan_aksi(robot_saya)
    elif robot == 2 and robot_lawan == 3:
        robot_saya.lakukan_aksi(lawan)
    elif robot == 3 and robot_lawan == 1:
        lawan.lakukan_aksi(robot_saya)
    elif robot == 3 and robot_lawan == 2:
        robot_saya.lakukan_aksi(lawan)
