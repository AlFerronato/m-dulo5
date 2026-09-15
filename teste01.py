numero1= 12
numero2= "12"
numero3= 2.5

print(type(numero1))
print(type(numero2))
print(type(numero3))

n4=10
n5=2
print(10/2)
print(10//2)
print(10**2)
print(10*2)
print(10%3)

n4==n5
n4!=n5
print(n4==n5)
print(n4!=n5)
print(n4>n5)
print(n5<n4)
print(not (2>3) and (2!=3)) #2>3 falso, porem ta not, so true, and 2!=3 is true, so true true is true
print(-7//2)
print("hello world")

w1= "hello"
w2= "world"
print(w1[0])
print(w1[1])
print(w1[-1])
print(w1[2:4])

f2= "eu comi maca,banana,mamao"

palavras = f2.split()
print(palavras)
palavras = f2.split(",")
print(palavras)
p=["olha","la","aquele","caminhao"]
frase = " ".join(p)
print(frase)
frase = "-".join(p)
print(frase)

f="paralelepipedo"
print(len(f))
print(f"{f} tem {len(f)} letras")
print(f[:4])
print(f[4:])
u=f.upper()
print(u)
f3= "  eu  gosto de  python  "
f3a=f3.split(" ")
print(f3a)

lista= [1,4,3,2,4,]
print(lista)
print(len(lista))
lista.append(7)
print(lista)
print(len(lista))
tupla=(1,2,3,4)
print(tupla)
anos = {"ale":16,"si":44}
print(anos["ale"])
print("ale" in anos)
lista= set["banana", "mamao", "abacaxi"]
print(lista)
l1=[1,3,4,5,2]
l1.sort()
print(l1)

dados = {
    "nome": "alexandre",
    "idade": "16",
    "linguagem": "python"
}
print(dados["nome"])
if 2>1:
    print("2 is bigger than 1")
else:
    print("2 isnt bigger than 1")

nota = 6
if nota>8:
    print("muito bem")
elif nota>7:
    print("ok")
else:
    print("melhore")

n1 = 95
if n1>= 90:
    print("bom")
if n1>= 70:
    print("mais ou menos")
if n1>=69:
    print("melhore")

##

#food= input("coloque sua comida favorita (q to quit): ")
#while food != "q":
  #  print(f"sua comida favorita é {food}, que legal!")
 #   food = input("coloque outra comida que voce gosta muito/favorita (q to quit): ")
#print("Ok, quit")

#num = int(input("Enter a number between 1 to 10: "))
#while num < 1 or num >10:
#    num=int(input("voce colocou um numero fora dos limites, coloque um numero entre 1 e 10: "))
#print(f"seu numero e {num}")

total = 0
#for n in [2,3,12,5]:
    #total = total+n
#print(total)

#for letter in "cat":
    #print(letter)

#for i in range(4):
    #print(i)

count = 3
#while count>0:
   # count = count - 1
    #print(count)
#print("acabou")

#count = 10
#for n in range(count):
  #  print(n)

words = ["gato","elefante","cachorro"]
def longest(words):
    best = ""
    for w in words:
        if len(w)>len(best):
            best = w
    return best