from csv import DictReader
perfernces = {
    "cats":0,
    "dogs":0,
    "birds":0,
}
with open("data.csv","r") as data:
    database = DictReader(data)
    next(data)
    for row in database:
        pets = row["animal"]
        perfernces[pets] += 1

for animal in perfernces:
    print(f"{animal} :{perfernces[animal]}")




