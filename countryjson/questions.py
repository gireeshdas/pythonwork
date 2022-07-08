# print total number of country details
# print languages of ukrane
# print currency of china
# print population of india
# print nigehbouring countries of australia

import json
with open("countries.json",encoding="utf-8") as f:
    data=json.load(f)
# print(len(data))

#
# india_details=[country for country in data if country["name"]=="India"]
# print(india_details)

# costly_mobile=max(all_mobiles,key=lambda m: int(m[2]))
# print(costly_mobile)


# population_data=[popu for popu in data1 if popu["population"]=="India"]
# print(len(population_data))
#
# # total number of country details?
# # total_country_details=[for country in data if country []]
#
# china_details=[country for country in data if country["name"]=="China"]
# print(china_details)
#
# currency_of_china=[cur["currencies"] for cur in china_details if cur["name"]=="China"]
# print(currency_of_china)
#
# # print nigehbouring countries of australia
#


#
language_by_country=[country["languages"] for country in data if country["name"]=="Ukraine"]
for lan in language_by_country[0]:
    print(lan["name"])
#
currency_of_china=[cur["currencies"] for cur in data if cur["name"]=="China"]
print(currency_of_china)

def get_country_data(country_name):
    return[country for country in data if country["name"].lower().startswith(country_name)]


currency_details=[cur["currencies"] for cur in data if cur["name"].startswith("India")]
# print(currency_details)
for curr in currency_details[0]:
    print(curr["name"])
# neibouring country details?

india_data=get_country_data("india")
#

country_data=get_country_data("india")
country_borders=country_data[0].get("borders")
sharing_borders=[country.get("name")for country in data if country["alpha3Code"] in country_borders]
print(sharing_borders)


heighest_population=max(data,key=lambda ite:ite.get("population"))
print(heighest_population["name"])

heighest_population=min(data,key=lambda ite:ite.get("population"))
print(heighest_population["name"])
