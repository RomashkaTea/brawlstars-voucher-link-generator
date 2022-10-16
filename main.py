import random

url = "https://link.brawlstars.com/en?action=voucher&code="

def randombytes(length):
    return random.randbytes(length).hex()

def generate_voucher_code():
    result = ""
    
    result += f"{randombytes(4)}-{randombytes(2)}-{randombytes(2)}-{randombytes(2)}-{randombytes(6)}"
   
    return result

r = ""

count = int(input("count: "))
for i in range(count):
    res = url + generate_voucher_code()
    r += f"{res}\n"

f = open("links.txt", "w")
f.write(r)
f.close()
del f