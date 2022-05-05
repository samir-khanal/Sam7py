print("welcome to Computer bazaar")
print("here are the laptops that are available in our store right now\n"
      "dell\n"
      "toshiba\n"
      "mac")
dell = 20000
toshiba = 30000
mac = 50000
lap = input("enter the laptop name:")
if lap == "dell":
    print("cost: Rs", dell)
elif lap == "toshiba":
    print("cost: Rs", toshiba)
else:
    print("cost: Rs", mac)
quan = int(input("quantity:"))

home = 1000
pick_up = ": free"
deli = input("enter the delivery option[home,pick_up]:")
if deli == "home":
    print("delivery cost Rs", home)
elif deli == "pick_up":
    print("delivery cost", pick_up)

plastic = 500
bag = 1000
gift_box = 5000
pack = input(
    "enter a packaging option you want from these options, For ex: write [plastic] if you want that packaging :\n"
    "a)plastic\n"
    "b)bag\n"
    "c)gift_box\n"
    "d)none\n"
    "a quick reminder that packaging will cost you extra money[enter here]:")
if pack == "plastic":
    print("packaging cost Rs", plastic)
elif pack == "bag":
    print("packaging cost Rs", bag)
elif pack == "gift_box":
    print("packaging cost Rs", gift_box)
else:
    print("none")


ktm = dell + (13 / 100) * dell
lit = 0
bkt = 0
loc = input("enter a delivery location:\n"
            "a)ktm\n"
            "b)lit\n"
            "c)bkt [Enter here]:")
if loc == "ktm":
    print("Tax applied for products is: Rs", ktm)

