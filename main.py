import uuid
with open("links.txt", "w") as w:
    w.write("\n".join(["https://link.brawlstars.com/?action=voucher&code=%s" % str(uuid.uuid4()) for _ in range(int(input("count: ")))]))
