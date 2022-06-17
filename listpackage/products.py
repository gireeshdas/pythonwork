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

#
# print(f"total number of mobiles={len(mobiles)}")
# fatten_list=[num for sub_list in mobiles for num in sub_list]
# print(fatten_list)
# #
# out_stock=[stock for stock in mobiles  if stock[5]=="apple"]
# print(out_stock)

# total number of out of stock mobiles
# out_stock_mobiles=[num for num in mobiles if num[-1]=="0"]
# print(out_stock_mobiles)
# print(len(out_stock_mobiles))
# #
# #total stock
# avl_stock=[mob[-1] for mob in mobiles]
# print(sum(avl_stock))
# print mobiles 20k and 30k
# mobiles_gt=[mob for mob in mobiles if mob[4]>=20000 and mob[4]<=30000]
# print(mobiles_gt)
#
# # print samsung mobiles
# samsung_mobiles=[sam for sam in mobiles if sam[5]=="samsung"]
# print(samsung_mobiles)
# #
# # print all 5g mobiles
# fiveg_mobiles=[five for five in mobiles if five[2]=="5g"]
# print(fiveg_mobiles)
# #
# # # # print costly mobile
# max_prices=max([mob[4] for mob in mobiles])
# costly_pro=[mob for mob in mobiles if mob[4]==max_prices]
# print(costly_pro)


# #
# # # print low cost mobile
# # lowcost_mobile=[]
# #
#
# # print all mobiles having stock greater than 10
# greater_then_ten=[great for great in mobiles if great[-1]>10]
# print(greater_then_ten)

# count of mobiles having display AMOLED
# display_amoled=[dis for dis in mobiles if dis[3]=="AMOLED"]
#
# print(display_amoled)

# sort mobile order based on price list bt descending

# mobiles.sort(reverse=True)


# is there any mobile can available at rs 10000/-
# mob_ten=[True if mob[4]==10000 else False  for mob in mobiles ]
# print("available" if True in mob_ten else "not")
# print(mob_ten)

mob_ten=[mob[4]==10000 for mob in mobiles ]
print("available" if True in mob_ten else "not")
print(mob_ten)



# list all mobiles having same price
# mobiles.sort()
# print(mobiles)
# same_price=[sprice for sprice in mobiles if sprice[4]=="27000"]
# print(same_price)

# mobiles.sort(reverse=True,key=lambda mob:mob[4])
# max(mobiles,lambda mob:mob[4])

costly_mobile=max(mobiles,key=lambda m:m[4])
print(costly_mobile)