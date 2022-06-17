results = [ {"district":"tvm","win": 98,"A+": 45000},
            {"district":"ktm","win": 95, "A+": 44000},
            {"district":"apy","win": 97, "A+": 47000},
            {"district":"idk","win": 90 ,"A+": 38000},
            {"district":"ekm","win": 99, "A+": 56000},
            {"district":"pta","win": 99, "A+": 58000},
            {"district":"tsr","win": 98, "A+": 57000},
            {"district":"kzd","win": 99, "A+": 58000},
            {"district":"pkd","win" :95, "A+": 50000},
            {"district":"mpm","win": 90,"A+": 4500},
            ]



# sum of marks
aplus=[res["A+"] for res in results ]
print(sum(aplus))

# max result
print(max(results ,key=lambda  m:m["A+"]))

# min result
print(min(results ,key=lambda  m:m["A+"]))

# sort with dec
print(sorted(results ,key=lambda  m:m["A+"], reverse=True))


