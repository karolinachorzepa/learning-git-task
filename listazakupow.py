a=("lista zakupów:")
print(a.capitalize())
list1= {"piekarnia":["chleb", "bułka", "pączek"],"warzywniak" : ["rukola", "seler", "pomidor"]}
for c,b in list1.items():
  print(f"Idę do {c.capitalize()} i kupuję {b}")


articles = {"chleb", "bułka", "pączek","rukola", "seler", "pomidor"}

c=len(articles)
print(f"W sumie kupuję: {c} produktów")
print("Pozdrowienia z Krakowa ;)")