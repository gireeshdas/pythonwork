mobiles = [
    [1000, "samsungA52", "4g", "AMOLED", 27000, "samsung", 12],
    [1001, "samsungA52s", "5g", "AMOLED", 32000, "samsung", 20],
    [1002, "redminote10", "4g", "led", 17000,"redmi", 50],
    [1003, "redminote11pro", "5g", "superAMOLED", 20000, "redmi", 70],
    [1004, "samsungA72", "5g", "AMOLED", 27000, "samsung", 1],
    [1005, "samsungA53", "5g", "AMOLED", 27000, "samsung", 34],
    [1006, "samsungm52", "5g", "AMOLED", 27000, "samsung", 7],
    [1007, "samsungm53", "5g", "AMOLED", 27000, "samsung", 89],
    [1008, "samsungA22", "5g", "AMOLED", 27000, "samsung", 0],
    [1009, "iphone13", "5g", "AMOLED", 97000, "apple", 0],
    [1010, "oneplusnordce2", "5g", "AMOLED", 23000, "oneplus", 67]
]
# # total number  mobiles
# print(f"total number of mobiles={len(mobiles)}")
#
# # total out of stock
# out_of_stock=[mob for mob in mobiles if mob[-1]==0]
# print(out_of_stock)
#
# # total number of out of stock mobiles
# out_of_stock=[mob for mob in mobiles if mob[-1]==0]
# print(len(out_of_stock))
#
# # total stock
# available_stock=[mob[-1] for mob in mobiles]
# print(sum(available_stock))
#
# # print available mobiles in range 20k and 30k
# # mobiles_gt=[mob for mob in mobiles if mob[4]>=20000 and mob[4]<=30000]
# mobiles_gt=[mob for mob in mobiles if mob[4] in range(20000,30000)]
# print(mobiles_gt)
#
# # print all 5g mobiles
# fiveg_mobiles=[mob for mob in mobiles if mob[2]=="5g"]
# print(fiveg_mobiles)
#
# # print all samsung mobiles
# samsung_mobiles=[mob for mob in mobiles if mob[-2]=="samsung"]
# print(samsung_mobiles)

# print costly mobile
# price=max([mob[4] for mob in mobiles ])
# costly_pro=[mob for mob in mobiles if mob[4]==price]
# print(costly_pro)
#
# costly_pro=max(mobiles,key=lambda mob:mob[4])
# print(costly_pro)
#
# # # print low cost mobile
# # price=min([mob[4] for mob in mobiles ])
# # costly_pro=[mob for mob in mobiles if mob[4]==price]
# # print(costly_pro)
# costly_pro=min(mobiles,key=lambda mob:mob[4])
# print(costly_pro)
#
#
# # print all mobile having stock > 10
# mob_stock =[mob for mob in mobiles if mob[-1]>10]
# print(mob_stock)
#
# # count of mobiles having display AMOLED
# display_amoled=[mob for mob in mobiles if mob[3]=="AMOLED"]
# print(display_amoled)

# sort mobiles based on price order by desending
# mobiles.sort(reverse=True,key=lambda mob:mob[4])
# price_order=(mobiles,key=lambda mob:mob[4])
# print(price_order)

# is there any mobiles available at rs 10000?
# mob_ten=[mob[4]==10000  for mob in mobiles ]
# print("available" if True in mob_ten else "not available")

# list all mobiles having same price
same_price=[mob for mob in mobiles if mob[4]==27000 ]
print(same_price)


