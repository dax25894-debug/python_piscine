
def famous_births(a):
    sorted_people = sorted(a.items(), key=lambda item: item[1]["date_of_birth"])
    
    for fn, date in sorted_people:
        print(date["name"], "is a great scientist born in", date["date_of_birth"])


women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}
famous_births(women_scientists)