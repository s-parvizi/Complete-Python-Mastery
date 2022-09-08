import uuid

# make a UUID based on the host address and current time
with open("uuid.txt","w") as file:
    for i in range(10):
        file.write(" UUID: %s\n" % uuid.uuid1().hex[:24])
