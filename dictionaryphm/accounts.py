accounts = [
    {
        "acno": 1000, "ac_type": "savings", "balance": 5000, "transactions": [
        {"to": 1001, "amount": 500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1001, "ac_type": "savings", "balance": 6000, "transactions": [
        {"to": 1000, "amount": 500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1002, "ac_type": "current", "balance": 8000, "transactions": [
        {"to": 1001, "amount": 700, "note": "ebill", "method": "g-pay"},
        {"to": 1000, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 800, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1003, "ac_type": "credit", "balance": 15000, "transactions": [
        {"to": 1001, "amount": 1500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 800, "note": "geto", "method": "neft"},
        {"to": 1000, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1004, "ac_type": "savings", "balance": 50000, "transactions": [
        {"to": 1001, "amount": 500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },

]

#q1 print details 1002
# for ac in accounts:
#     if ac["acno"]==1002:
#         transactions =ac.pop("transactions")
#         print(ac)
# ac_details=[ ac["acno"] for ac in accounts if ac["acno"]==1002]
# print(ac_details)
#

#
# #q2 print saving type account details
#
savings_type=[ac["acno"] for ac in accounts if ac["ac_type"]=="savings"]
print(savings_type)
#
# #q3 sort accounts based on balance order by desc
# accounts.sort(reverse=True,key=lambda ac:ac["balance"])
# print(accounts)
#

# #q4 print all online transaction
# online_tra=[ac["acno"] for ac in accounts if ac["method"]=="transaction_method"]
# print(online_tra)

# #q4 prit all phone pay transactions
all_transactions=[ac["transactions"]for ac in accounts]

# phone_pay=[trans for tlist in all_transactions for trans in tlist if trans["method"]=="phone-pay" ]
# print(phone_pay)

# # #q4 prit all transactions where transaction amount > 500
# amunt=[trans for tlist in all_transactions for trans in tlist if trans["amount"]>500]
# print(amunt)
# #
# # #q5 credit transactions of 1002
# credit_transaction=[trans for tlist in all_transactions for trans in tlist if trans["to"]==1002]
# print(credit_transaction)
# #
#
# #q6 aggregate transactions based on payment method?
pms={ }
all_transactions=[ac["transactions"]for ac in accounts]
transactions=[t for tlist in all_transactions for t in tlist]
for transaction in transactions:
    p_method=transaction["method"]
    amount=transaction["amount"]
    if p_method in pms:
        pms[p_method]+=amount
    else:
        pms[p_method]=amount
# print(pms)
print(max(pms.items(),key=lambda ite:ite[1]))



