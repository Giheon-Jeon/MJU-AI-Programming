import pickle

data = [1, 3, 5, 7, 9]

with open("data.pkl", "wb") as f:
	pickle.dump(data, f)

with open("data.pkl", "rb") as f:
	loaded = pickle.load(f)

print(loaded)