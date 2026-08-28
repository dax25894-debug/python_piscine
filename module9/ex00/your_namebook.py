
def array_of_names(a):
    array = []
    for key,value in a.items():
        array.append(f"{key.capitalize()} {value.capitalize()}")
    return array

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}
print(array_of_names(persons))