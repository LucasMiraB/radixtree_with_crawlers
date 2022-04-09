# radixtree_with_crawlers

O presente projeto para aprovação à disciplina Análise de Algoritmo foi desenvolvido utilizando python 3.7.9

Para a execução do código é recomendado ter instalado o Anaconda, gerenciador de ambientes de python. É possível também rodar o código apenas contendo o python através do PIP, mas as bibliotecas terão que ser instaladas manualmente.

Uma vez criado, é recomendado criar um virtualenv do conda para a versão 3.7.9, utilizando do pacote de requirements também nesse git, seguindo um formato similar à:

conda env create python=3.7.9 --file requirements.txt

Associado a esse git, no notebook encontra-se uma execução de como são os resultados parciais da execução do arquivo .py

Ao chamar radix_tree.py dentro do ambiente do anaconda, ele automaticamente carregará 33 páginas sequenciais diferentes do que foi utilizado para criar a arvore radix, a fim de econimizar tempo para testar a aplicacão, contendo *apenas* a funcionalidade de procurar uma palavra e listar as urls que a contém

Chamando radix_tree_user_url, o usuário tem a possibilidade de informar manualmente cada uma das páginas que gostaria de passar pela aplicação e testar palavras individuais.