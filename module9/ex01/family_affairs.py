

def filtering(family):
    key,value = family
    head = "red"
    if value == head:
        return key
    else:
        return None

def find_the_redheads(name):
    array = []
    final_dict = list(filter(filtering,name.items())) 
    for key,value in final_dict:
        array.append(key)
    return array
    

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}
print(find_the_redheads(dupont_family))