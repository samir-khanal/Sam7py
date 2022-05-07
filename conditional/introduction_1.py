# print("=========welcome to Computer bazaar==========")
# total_price = 0
# gt = 0
# tax_amount = 0
# quantity = 0
# print("here are the laptops that are available in our store right now\n"
#       "1.Dell(Rs:20000)\n"
#       "2.Toshiba(Rs:30000)\n"
#       "3.Mac(Rs:50000)")
# dell = 0
# toshiba = 0
# mac = 0
# lap = int(input("Select any option:"))
# if lap == 1:
#     quantity = int(input("quantity:"))
#     dell = 20000 * quantity
# elif lap == 2:
#     quantity = int(input("quantity:"))
#     toshiba = 30000 * quantity
# elif lap == 3:
#     quantity = int(input("quantity:"))
#     mac = 50000 * quantity
# else:
#     print("Exit")
#     exit()
#
# print("Delivery options: 1.home(Rs.1000) 2.Pick_up(free)")
# deli_price = 0
# home = 1000
# pick_up = 0
# deli = int(input("enter the delivery option number:"))
# if deli == 1:
#     deli_price += home
# elif deli == 2:
#     deli_price += pick_up
#
# print("Packaging options:\n"
#       "a.plastic(Rs.500)\n"
#       "b.bag(Rs.1000)\n"
#       "c.gift_box(Rs.5000)\n"
#       "d.none")
# plastic = 0
# bag = 0
# gift_box = 0
# pack = (input("Enter option:"))
# if pack == "a":
#     plastic += 500
# elif pack == "b":
#     bag += 1000
# elif pack == "c":
#     gift_box += 5000
# else:
#     print("none")
#
# print("Locations: 1.KTM(13% tax) 2.LTP(free) 3.BKT(free)")
# ktm = (13 / 100)
# lit = 0
# bkt = 0
# loc = int(input("Enter a delivery option:"))
# total_price += dell + toshiba + mac
# if loc == 1:
#     tax_amount += total_price * ktm
#
# gt = total_price + deli_price + bag + plastic + gift_box + tax_amount
# print(f"Total quantity:{quantity} Total price:{total_price} Tax amount:{tax_amount} Gt:{gt}")


