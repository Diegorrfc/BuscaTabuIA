Busca Local - Tabu Search

Equipe: Diego Celestino
		Felipe Ribeiro
		Giovanni Lucas
		Maria Laura Petrovna

Para funcionamento do algoritmo, é necessário o arquivo saidadados.csv que será gerado pelo algoritmo da equipe de busca global.
O código irá gerar dois arquivo, um arquivo com o nome: dataatualhoratual, nesse arquivo deverá conter os logs de erros, caso existem.
O segundo arquivo será o resultado da busca local. Será gerado um aquivo com o nome de melhorDistrito.csv

Na variável dadosDosDistritos, está contido os dados dos distritos na rodem abaixo: 
#dados dos distritos[[AGROPECU, COMERCIO E SERVIÇOS,EDUCACAO,ENERGIA,  FINANÇAS, PIB, sAUDE, PESOPROXIMIDADE AO PORTO]]
Na variavel distritos é colocado o nome dos municios, o nome dos municipios precisam está na mesma ordem do dados dos minupios, mesma paridade.
Na função def pegarPesosCnae(cnae):
foi atribuido para cada setor
a ordem dos pesos são: [COMERCIO E SERVIÇOS,  EDUCACAO, ENERGIA, FINANÇAS,  PIB,  SAUDE]

os pesos são os niveis de necessidade que a empresa precisa, esses vertor ira se relacionar com os parametros de cada cidade, por isso é importante
colocar os pesos na mesma ordem dos atributos do distritos. ou seja pareado. Dessa forma:
