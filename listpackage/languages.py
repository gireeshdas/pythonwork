framework=[
    ["django","python",4],
    ["flask","python",3],
    ["spring","java",5],
    ["express","javascript",4],
    ["angular","typescript",4]
]

# print python frameworks details

python_fw=[fw for fw in framework if fw[1]=="python"]
print(python_fw)