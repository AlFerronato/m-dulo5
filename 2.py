words = ["gato","cachorro", "papagaio","elefanteeeee"]
def longest(word):
    best= ""
    for w in word:
        if len(w) > len(best):
            best = w
    return best
resultado = longest(words)
print(resultado)

print(longest(["banana","maca","kiwi"]))