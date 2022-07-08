mobile=open("mobiles.txt","r")
all_mobiles=[]


# all_mobiles=[mobiles.rstrip("\n").split(",") for mobiles in mobile]
# for line in mobile:
#     mob=line.rstrip("\n").split(",")
# #
#     all_mobiles.append(mob)
all_mobiles=[mobiles.rstrip("\n").split(",") for mobiles in mobile]
print(all_mobiles)
costly_mobile=max(all_mobiles,key=lambda m: int(m[2]))
print(costly_mobile)


# list complrehension

fiveg_mob=[five for five in all_mobiles if five[3]=="5g"]
print(fiveg_mob)