
def average(a):
    total = []
    for key,value in a.items():
        total.append(int(f"{value}"))
    
    y = sum(total)/len(total)
    return y

class_3B = {
"marine": 18,
"jean": 15,
"coline": 8,
"luc": 9
}
class_3C = {
"quentin": 17,
"julie": 15,
"marc": 8,
"stephanie": 13
}
print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")