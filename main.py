import room

x = float(input("Enter width of your room: "))
y = float(input("Enter lenght of your room: "))
z = float(input("Enter hight of your room: "))
r = room.Room(x, y, z)
n = int(input("Enter number of windows and doors: "))
for i in range(n):
    w = float(input("Enter width of a window/door #{}: ".format(i + 1)))
    h = float(input("Enter hight of a window/door #{}: ".format(i + 1)))
    wd = room.WinDoor(w, h)
    r.addWD(wd)
roll_w = float(input("Enter width of a papier roll: "))
roll_l = float(input("Enter length of a papier roll: "))
input("Calculate?")
print("Your work surface {:.2f} square meters".format(r.workSurface()))
print("You need {} rolls".format(room.rollsNeed(r, roll_w, roll_l)))
