bike={"name":"r15","color":"black","make":"2011","brand":"yamaha","gear":6,"price":250000}

# print(bike["brand"])
# print(bike["name"])
# print(bike["color"])
# print(bike["make"])
#
# print("breaking_system" in bike)
#
# bike["breaking_system"]="abs"
# print(bike)
#
# # updation
# bike["color"]="blue"
# print(bike)
#
# dict_name.get(key)
print(bike.get("name"))
print(bike.get("brand"))
print(bike.get("price"))

# if "gear " in bike:
#     bike["gear"]=5
# else:
#     bike["gear"]=4
# print(bike)
bike["gear"]= 5 if "gear" in bike else 4
# bike price update c_price -1000 if cur_price>40000 else c_price -500

if bike["price"]>40000:
    bike["price"]-=1000
else:
    bike ["price"]-=500
print(bike)