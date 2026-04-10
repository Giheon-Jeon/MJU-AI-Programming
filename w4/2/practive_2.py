with open("w4/2/practice.txt", "r", encoding="utf-8") as f:
    data = f.read()

index = data.find("programming")

if index != -1:
    print("Found")
else:
    print("Not found")