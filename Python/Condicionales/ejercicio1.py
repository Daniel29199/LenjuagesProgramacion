letra=input("Digite una letra: ")

if letra.lower()=="a" or "e" or "i" or "o" or "u":
    print("es una vocal")
else:
    print("no es una vocal")

#    Metodo 2 

if letra.lower() in "aeiou":
    print("es una vocal")
else:
    print("no es una vocal")