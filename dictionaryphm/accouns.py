accounts={"ac_no":1000,
          "name":"gireesh das",
          "ac_type":"joint_account",
          "branch":"Koothattukulam"}

print(accounts["ac_no"])
print(accounts["name"])
print(accounts["ac_type"])
print(accounts["branch"])


print("bank name" in accounts)
accounts["bank name"]="sbi"
print(accounts)



# update
accounts["name"]="hareesh das"
print(accounts)


