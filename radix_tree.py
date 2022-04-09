from utils import *

## ARQUIVO BASE PARA CRIAR A ARVORE RADIX

url = "https://www.gutenberg.org/cache/epub/23336/pg23336.txt"
req = requests.get(url)
req.close()
req.text

#Tira caracter de txt feio
text = req.text.replace("\n","").replace("\r","").replace("\ufeff","").upper()
#Transforma em lista de palavras
word_list = text.split(" ")
#Remove palavras duplicadas e só pega quem tem >3 caracteres
word_set = {x for x in word_list if len(x) >= 3}

#Declarado em Utils
trie_tree = Trie()
#Cria arvore com base no texto
trie_tree.add_wordlist(list(word_set))

#Lista de URLs scrapeadas logo pra facilitar o teste
base_url = "https://www.gutenberg.org/cache/epub/"
url_list = [base_url+f"{x}/pg{x}.txt" for x in range(23300,23333)]
url_list

#Metodo entra na url por httprequest, transforma em texto e checa palavra a palavra.
for url in url_list:
    trie_tree.add_url(url)
    print(f"Done URL: {url}")
    
loop = True

while loop:
    user_input = input("Digite a palavra a ser procurada ou -1 para encerrar: \n")
    if user_input == "-1":
        loop = False
    else:
        trie_tree.display_word(user_input.upper())
    print("\n\n")