Projeto

O projeto consiste realizar uma busca de distritos industriais em Pernambuco para uma determinada empresa. Ele tenta encontrar um bom distrito, ou seja, com as melhores caracter�sticas para uma empresa se instalar. Toda a busca � feita com base nas necessidades das empresas e nas caracter�sticas dos distritos.
O algoritmo l� o arquivo gerado pela a equipe de Busca Local, o nome do arquivo � saidadados.csv. Nesse arquivo cont�m o CNPJ, N�MERO DE EMPREGADOS, CNAE E FAOR DE EXPORTA��O.

O fluxo:

	Ele pega a primeira empresa do arquivo gerado pela equipe de busca global e vai buscar um bom distrito para ela, c�digo toma como base as caracter�sticas da empresa, que � o CNAE. Para cada CNAE(Ramo de atividade da empresa), foram atribu�dos pesos, esses pesos podem ser alterados. Os pesos est�o na seguinte ordem:
	
	[COMERCIO E SERVI�OS, EDUCACAO, ENERGIA, FINAN�AS, PIB, SAUDE]

Os pesos foram atribu�dos de 1 a 5.

Esses pesos ir�o dar match com as caracter�sticas do munic�pio, que est� na seguinte ordem:

[[COMERCIO E SERVI�OS,EDUCACAO,ENERGIA, FINAN�AS, PIB, SAUDE, PESOPROXIMIDADE AO PORTO]]

Por conta disso, � de extrema import�ncia deixar a ordem equivalente dos dados dos munic�pios com os dados dos pesos.

O Fator de exporta��o � adicionado na ultima posi��o do cnae, ent�o caso queiram mudar algo, � de extrema import�ncia que a vari�vel da proximidade do porto do munic�pio seja a �ltima. Pode-se colocara quantos pesos quiser, no entanto o tamanho do vetor do cane e o tamanho do vetor dados de munic�pio devem ser o mesmo. A vari�vel do peso CNAE vai ter sempre um a menos, pois o fator de exporta��o ser� adicionado no tempo de execu��o do c�digo.

A Aplica��o ir� gerar dois arquivos, um arquivo com o nome da data e hora do memento da execu��o, esse arquivo conter� os logs da execu��o, caso haja falha. O segundo arquivo � o melhorDistrito.csv, onde ir� conter os mesmos dados gerados pelo algoritmo de busca global, s� que adicionando mais uma coluna com um bom distrito para a empresa se instalar.

Por onde Come�ar

Basta criar o execut�vel do script ou rodar o pr�prio script, lembrando que o execut�vel deve estar no mesmo diret�rio onde est� o arquivo gerado pela a equipe de busca global. Que � o arquivo: saidadados.csv.


Especifica��es T�cnicas

A linguagem utilizada foi Python e foram importadas as seguintes bibliotecas:

import csv
import types
import os.path
from time import gmtime, strftime
from datetime import datetime
import random


A execu��o desse scritp foi feita no Windows, no entanto acredito que n�o ter� nenhum problema ao executar em uma plataforma Linux.

Testes

O �nico teste a ser feito � verificar se ele est� gerando o arquivo de log e o arquivo com o resultado desejado.

Instala��o

Basta gerar um execut�vel ou rodar o pr�prio script. Lembrando de importar as bibliotecas previamente citadas.

Colaboradores

Professor da Universidade de Pernambuco

Prof. FERNANDO BUARQUE
(http://www.fbln.pro.br/)

Alunos da Universidade de Pernambuco

Giovanni Lucas Lima de Souza - POLI/UPE

Maria Laura Petrovna Matos � POLI/UPE

Felipe Augusto da Silva Ribeiro � POLI/UPE



Gerente - Ger�ncia de Tecnologia da Informa��o � AD-diper 

JO�O LUIZ LESSA




