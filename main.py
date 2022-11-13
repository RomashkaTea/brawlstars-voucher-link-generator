import random

url = "https://link.brawlstars.com/?action=voucher&code="

def generate_voucher_code():
    result = uuid.uuid4()
   
    return str(result)

r = ""

count = int(input("count: "))
for i in range(count):
    res = url + generate_voucher_code()
    r += f"{res}\n"

f = open("links.txt", "w")
f.write(r)
f.close()
del f
