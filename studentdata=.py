studentdata={
    "id1":{"name":["Aitihya"],"class":["9"],"subintregation":["enlish,math,science"]},
    "id2":{"name":["David"],"class":["9"],"subintregation":["enlish,math,science"]},
    "id3":{"name":["Aitihya"],"class":["9"],"subintregation":["enlish,math,science"]},
    "id4":{"name":["Messi"],"class":["9"],"subintregation":["enlish,math,science"]}
}
result={}
for key,value in studentdata.items():
    if value not in result.values():
        result[key]=value
print(result)