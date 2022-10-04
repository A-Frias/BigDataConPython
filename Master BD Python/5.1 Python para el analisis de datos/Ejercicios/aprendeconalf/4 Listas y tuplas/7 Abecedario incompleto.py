abecedario : list = [chr(i) for i in range(97,123)]
a_eliminar= []
for i in range(len (abecedario)):
    if (i+1)%3==0:
        a_eliminar = a_eliminar + [abecedario[i]]

[abecedario.remove(i) for i in a_eliminar]
print(abecedario)