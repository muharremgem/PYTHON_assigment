def ilk_fonksiyonum(x, y) :
    print(x ** 2 + y ** 2)

ilk_fonksiyonum(3, 4)    

kere = int(input("senı sevıyorum"))

print(" seviyorum "  * kere)  


def hipotenus(a, b) :
    print((a ** 2 + b ** 2) ** 0.5)

hipotenus(3, 4)    

def rumi():
    print("""Ay doğmuyorsa yüzüne, Güneş vurmuyorsa pencerene, Kabahati ne güneşte ne de ayda ara... Gözlerindeki perdeyi arala!""")

rumi()    

def add(a, b):
    print(a + b)

add(2,3)



def calculator(a,b,string):
    if string=="+":
        print(a+b)
    elif string=="-":
        print(a-b)
    elif string=="*":
        print(a*b)
    elif string=="/":
        print(a/b)

calculator(3,5,"+")


def multiply(a,b):
    return(a*b)

print(multiply(5,5))

def string():
    return "alivelideli"
print(string())



def boolean():
    return True

if boolean():
    print("yaşasın python")




