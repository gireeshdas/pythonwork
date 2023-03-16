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


# mob=len(mobiles)
# print(mob)
#
# # print all mobile names
#
# samsung_mobiles=[mob for mob in mobiles if mob[-2]=="samsung"]
# print(samsung_mobiles)

aml_dis=[mob for mob in mobiles if mob[3]=="AMOLED"]
print(aml_dis)


price=max([ mob[4] for mob  in mobiles])
print(price)

costy_price=[ mob for mob in mobiles if mob[4]==price]
print(costy_price)