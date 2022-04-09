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
    
loop = True

while loop:
    user_input = input("Digite URL para inserir uma URL nova\nOu digite WORD para testar uma palavra\nPara abortar o programa, digite -1")
    if user_input == "-1":
        loop = False
        
    elif user_input.lower() == "url":
        user_input = input("Digite a URL da página:\n")
        trie_tree.add_url(user_input)
        print(f"Palavras da URL {user_input} foram adicionadas na busca por palavras")
        
    elif user_input.lower() == "word":
        user_input = input("Digite a palavra a ser procurada:\n")
        trie_tree.display_word(user_input.upper())
        
    print("\n\n")