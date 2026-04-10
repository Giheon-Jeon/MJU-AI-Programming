with open("w4/2/practice.txt", "r", encoding="utf-8") as f:
    new_data = f.read()

new_data = new_data.replace("Java", "Python")

with open("w4/2/practice.txt", "w", encoding="utf-8") as f:
    f.write(new_data)