Projeto

O projeto consiste realizar uma busca de distritos industriais em Pernambuco para uma determinada empresa. Ele tenta encontrar um bom distrito, ou seja, com as melhores características para uma empresa se instalar. Toda a busca é feita com base nas necessidades das empresas e nas características dos distritos.
O algoritmo lê o arquivo gerado pela a equipe de Busca Local, o nome do arquivo é saidadados.csv. Nesse arquivo contém o CNPJ, NÚMERO DE EMPREGADOS, CNAE E FAOR DE EXPORTAÇÃO.

O fluxo:

	Ele pega a primeira empresa do arquivo gerado pela equipe de busca global e vai buscar um bom distrito para ela, código toma como base as características da empresa, que é o CNAE. Para cada CNAE(Ramo de atividade da empresa), foram atribuídos pesos, esses pesos podem ser alterados. Os pesos estão na seguinte ordem:
	
	[COMERCIO E SERVIÇOS, EDUCACAO, ENERGIA, FINANÇAS, PIB, SAUDE]

Os pesos foram atribuídos de 1 a 5.

Esses pesos irão dar match com as características do município, que está na seguinte ordem:

[[COMERCIO E SERVIÇOS,EDUCACAO,ENERGIA, FINANÇAS, PIB, SAUDE, PESOPROXIMIDADE AO PORTO]]

Por conta disso, é de extrema importância deixar a ordem equivalente dos dados dos municípios com os dados dos pesos.

O Fator de exportação é adicionado na ultima posição do cnae, então caso queiram mudar algo, é de extrema importância que a variável da proximidade do porto do município seja a última. Pode-se colocara quantos pesos quiser, no entanto o tamanho do vetor do cane e o tamanho do vetor dados de município devem ser o mesmo. A variável do peso CNAE vai ter sempre um a menos, pois o fator de exportação será adicionado no tempo de execução do código.

A Aplicação irá gerar dois arquivos, um arquivo com o nome da data e hora do memento da execução, esse arquivo conterá os logs da execução, caso haja falha. O segundo arquivo é o melhorDistrito.csv, onde irá conter os mesmos dados gerados pelo algoritmo de busca global, só que adicionando mais uma coluna com um bom distrito para a empresa se instalar.

Por onde Começar

Basta criar o executável do script ou rodar o próprio script, lembrando que o executável deve estar no mesmo diretório onde está o arquivo gerado pela a equipe de busca global. Que é o arquivo: saidadados.csv.


Especificações Técnicas

A linguagem utilizada foi Python e foram importadas as seguintes bibliotecas:

import csv
import types
import os.path
from time import gmtime, strftime
from datetime import datetime
import random


A execução desse scritp foi feita no Windows, no entanto acredito que não terá nenhum problema ao executar em uma plataforma Linux.

Testes

O único teste a ser feito é verificar se ele está gerando o arquivo de log e o arquivo com o resultado desejado.

Instalação

Basta gerar um executável ou rodar o próprio script. Lembrando de importar as bibliotecas previamente citadas.

Colaboradores

Professor da Universidade de Pernambuco

Prof. FERNANDO BUARQUE
(http://www.fbln.pro.br/)

Alunos da Universidade de Pernambuco

Giovanni Lucas Lima de Souza - POLI/UPE

Maria Laura Petrovna Matos – POLI/UPE

Felipe Augusto da Silva Ribeiro – POLI/UPE



Gerente - Gerência de Tecnologia da Informação – AD-diper 

JOÃO LUIZ LESSA




