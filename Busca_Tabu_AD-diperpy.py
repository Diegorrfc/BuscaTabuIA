import csv
import types
import os.path
from time import gmtime, strftime
from datetime import datetime
import random # módulo para gerar números randômicos


#configuracao distritos
#PESOPROXIMIDADE AO PORTO FORAM ATRIBUIDOS PESOS ALEATÓRIOS A CADA DISTRITO,  MAIOR O PESO, MAIS PR[OXIMO É DO PORTO DE SUAPE]
#dados dos distritos[[AGROPECU, COMERCIO E SERVIÇOS,EDUCACAO,ENERGIA,  FINANÇAS, PIB, sAUDE, PESOPROXIMIDADE AO PORTO]]
distritos=["PAULISTA","MORENO","GOIANA","IPOJUCA"
          ,"JABOATAO","PETROLINA","IGARASSU", "JATOBÁ","LIMOEIRO","OURICURI"
	  ,"PALMARES","SANTA CRUZ DO CAPIBARIBE","SERRA TALHADA","SURUBIM"
	  ,"TAMANDARÉ","VITORIA DE SANTO ANTAO","XEXEU","TIMBAUBA","TORITAMA"
	  ,"PARNAMIRIM","GRAVATA","FLORESTA","CAMARAGIBE","CARUARU","BEZERROS"
	  ,"ARCOVERDE","ARARIPINA"]
dadosDosDistritos=[[956,4828,94.13,491041,37832971.55,12770,417],
                  [4564,913,84.27,55223,3203027.09,9283,101],
                  [1693,1639,82.52,408540,6714133.68,28400,354],
                  [2205,2402,80.79,391,46084962.14,80814,328],
                  [263,316,90,65119.58,173,1350,200],
                  [15200,10017,90.13,551479,56993890.53,5230472,1572],
                  [2033,1518,86.82,487774,9871552.12,20988,156],
                  [1855,225,78.88,12282,1853118.56,7114,23],
                  [17800,1533,81.77,58713,4435425.82,10631,231],
                  [32459,1028,73.15,53531,3384449.34,7334,88],
                  [11358,1336,80.21,52346,13035,2503532.10,378],
                  [3787,3537,85.24,91044,8888457.08,12718,75],
                  [32265,2252,80.35,94489,16323196.52,14900,454],
                  [15100,1486,77.334,64743,4083587.56,10592,184],
                  [5441,466,82.06,28794,7027146.99,10390,16],
                  [6964,2983,80.60,243909,12358613.72,21570,434],
                  [6316,119,69.93,7354,5414417.06,6350,14],
                  [9444,1518,81.99,47186,4828638.71,11897,142],
                  [1930,1795,80.89,44977,1179052.81,14712,31],
                  [17369,247,8240,19844,3909392.39,7480,29],
                  [16969,2631,80.75,108341,7243065.92,11594,60],
                  [13200,454,85.25,40103,3141216.32,11674,89],
                  [1130,2003,89.70,145509,11337363.52,8656,57],
                  [21372,12691,86.86,432880,3939240.66,18226,814],
                  [15983,1348,75.10,59535,4645876.46,9743,166],
                  [11000,2125,83.77,62590,584868.93,11972,116],
                  [20378,2057,80.76,91499,8753546.28,9481,164]
                  ]
resultado=["CNPJ;Numero de empregados;CNAE;Fator de exportacao;Distrito\n"]
iteracao = melhor_iteracao = 0
melhor_solucao=[] # irá guardar a melhor solução
lista_tabu = [] # lista tabu inicialmente vazia
lista_tabu_cidades= []
bt_max = 1000 # quantidade máxima de iterações sem melhora no valor da melhor solução
max_vizinhos = 2#2# quantidade máxima de vizinhos
NomeDoArquivo = "saidadados.csv"
NomeColunaCNPJ = "CNPJ"
PosicaoCNPJ=0
NomeColunaNumeroDeEmpregados="Numero de empregados"
PosicaoNUmeroDeEmpregados=1
NomeColunaCNAE="CNAE"
PosicaoCanae=2
NomeColunaFatorDeExportacao="Fator de exportacao"
PosicaoFatoDeExportacao=3
TamanhoDaLinha = 4
textoLog = []
dataParaOArquivoLog=datetime.now().strftime('%Y-%m-%d - %H:%M:%S')

# função para gerar pegar os vizinhos 
def pegar_vizinhos(melhor_solucao, max_vizinhos,dados_distritos,pesosDaEmpresa):
  maxima_peso = max(pesosDaEmpresa)  
  posicao = pesosDaEmpresa.index(maxima_peso)  
  contadorDevizinhos=0
  vizinhos = []
  for i in range(0,len(dados_distritos)):
        if(((melhor_solucao[posicao]/dadosDosDistritos[i][posicao])<1.3 or (melhor_solucao[posicao]/dadosDosDistritos[i][posicao])>0.7)
        and melhor_solucao!=dados_distritos[i]):
          vizinhos.append(dadosDosDistritos[i])
          contadorDevizinhos+=1          
        else:
          pass
  
  if(len(vizinhos)==0):
    return melhor_solucao
  return vizinhos


def obter_vizinho_melhor_avaliacao(vizinhos_avaliacao, lista_tabu, melhor_solucao, vizinhos):  
  maxima_avaliacao = max(vizinhos_avaliacao)  
  posicao = vizinhos_avaliacao.index(maxima_avaliacao)
  pos = 0
  bit_proibido = -1



  for i in (0,len(vizinhos)):
    if(vizinhos[posicao] in lista_tabu):
      vizinhos_avaliacao.pop(posicao)
      maxima_avaliacao = max(vizinhos_avaliacao)  
      posicao = vizinhos_avaliacao.index(maxima_avaliacao)
    else:
      return posicao
      #lista_tabu.append(maxima_avaliacao)
      #lista_tabu_cidades.append(vizinho[posicao])
      break
  return posicao

#while (existe):
 #   if(max_vizinhos in lista_tabu):

  #  else:
#pass
  #  pass



  #if len(lista_tabu) != 0:
   # for j in (0,len(vizinhos_avaliacao)):
##for i in (0,len(lista_tabu)):
#if vizinhos[posicao]==lista_tabu[i]:
     #     break
    #    elif i==len(lista_tabu):
#lista_tabu.append(vizinhos[j])
    #       break
#else:
      #    pass
     # vizinhos_avaliacao.pop(posicao)
#vizinhos.pop(posicao)
#3#  maxima_avaliacao = max(vizinhos_avaliacao)  
    #  posicao = vizinhos_avaliacao.index(maxima_avaliacao)    
  #else:
   # lista_tabu.append(vizinhos[posicao])   

	# verifica se a lista tabu não possui elementos
  #if len(lista_tabu) != 0:
		# se possuir, é porque tem bit proibido, então pega esse bit
   # bit_proibido = lista_tabu[0]
	# for para obter a posição do melhor vizinho
  #for i in range(0, len(vizinhos_avaliacao)):
   # if vizinhos_avaliacao[i] == maxima_avaliacao:
    #  pos = i
    #  break
	# verifico se o vizinho é resultado de movimento proibido
 # if bit_proibido != -1:
		# se for, então obtém a posição do bit que foi modificado para gerar esse vizinho
   # bit_pos = obter_bit_modificado(melhor_solucao, vizinhos[pos])
		# verifica se é um bit que está na lista_tabu (compara com bit_proibido)
#if bit_pos == bit_proibido:
			# se cair nesse if, então procura o segundo melhor vizinho
      #melhor_pos = 0
#for i in range(1, len(vizinhos_avaliacao)):
#if i != bit_pos:
       #   if vizinhos_avaliacao[i] > vizinhos_avaliacao[melhor_pos]:
#melhor_pos = i
#return melhor_pos # retorna a posição do segundo melhor vizinho
  #return pos # retorna a posição do melhor vizinho


def pegarPesosCnae(cnae):
  
  doisprimeirosnumero = cnae[:2]

  if (int(doisprimeirosnumero)>0 and int(doisprimeirosnumero)<=3):

    return [5,1,1,2,2,2,1]

  elif (int(doisprimeirosnumero)>4 and int(doisprimeirosnumero)<=5):

      return [1, 1, 1, 4, 3, 4, 2]

  elif (int(doisprimeirosnumero) == 35):

      return [1, 1, 5, 4, 3, 3, 1]

  elif (int(doisprimeirosnumero)>=36 and int(doisprimeirosnumero) <=39):

    return [1,5,1,4,3,3,1]

  elif (int(doisprimeirosnumero)>=40 and int(doisprimeirosnumero) <= 43):

    return [1,5,2,2,3,3,1]

  elif(int(doisprimeirosnumero)>48 and int(doisprimeirosnumero) <=53):

    return [1,5,1,4,3,3,1]

  elif (int(doisprimeirosnumero)>= 69 and int(doisprimeirosnumero)<=75):

    return [1,5,2,2,3,3,1]

  elif(int(doisprimeirosnumero)>=86 and int(doisprimeirosnumero)<=88):

    return [1,2,5,5,3,3,4]

  elif(int(doisprimeirosnumero)>=94 and int(doisprimeirosnumero)<=96):

    return [1,5,1,4,4,4,2]

  else:
    return[]

# função para obter o valor de avaliação de cada vizinho
# vizinhos - lista de todos os vizinhos
# max_vizinhos - quantidade máxima de vizinhos
def obter_avaliacao_vizinhos(vizinhos, pesosDaEmpresa, max_vizinhos):
  vizinhos_avaliacao = []
 
  for i in range(0, len(vizinhos)):#obs 
    if isinstance(vizinhos[i], (int, float)):   
      vizinhos_avaliacao.append(obter_avaliacao(vizinhos, pesosDaEmpresa))
    else:
      vizinhos_avaliacao.append(obter_avaliacao(vizinhos[i], pesosDaEmpresa))
  return vizinhos_avaliacao

def obter_avaliacao(melhor_solucao, pesosDaEmpresa):
    avaliacao=0    
    for i in range(len(melhor_solucao)):
      avaliacao += melhor_solucao[i]*pesosDaEmpresa[i]
    return avaliacao

# função para obter o bit modificado
# melhor_solucao - melhor solução corrente
# melhor_vizinho - melhor vizinho
def obter_bit_modificado(melhor_solucao, melhor_vizinho): 
  for i in range(0, len(melhor_solucao)):
    if (melhor_solucao[i] != melhor_vizinho[i]):
      return i

def buscaTabu(empresa):
  iteracao = melhor_iteracao = 0
  melhor_solucao=[]
  empresa1=empresa.split(",")
  cnae=empresa1[2]  
  # gera uma solução inicial \CIDADE
  posicaoCidade = random.randrange(len(dadosDosDistritos))
  melhor_solucao=dadosDosDistritos[posicaoCidade]
  
 
  # pegarPesosDaEmpresa
  pesosDaEmpresa = pegarPesosCnae(cnae)
  if(len(pesosDaEmpresa)==0):    
    return
  else:
    pesosDaEmpresa.append(int(empresa[3]))   
    melhor_avaliacao = obter_avaliacao(melhor_solucao, pesosDaEmpresa)
    print(melhor_avaliacao)
    #pegaOsVizinhos
    vizinhos = pegar_vizinhos(melhor_solucao, max_vizinhos,dadosDosDistritos,pesosDaEmpresa);#ajustes passar dados distritos
    print(vizinhos)
    #obtem a avalicao dos Vizinhos
    vizinhos_avaliacao = obter_avaliacao_vizinhos(vizinhos, pesosDaEmpresa, max_vizinhos) 
    print(vizinhos_avaliacao)
    # obtém a posição do melhor vizinho
    pos_melhor_vizinho = obter_vizinho_melhor_avaliacao(vizinhos_avaliacao, lista_tabu, melhor_solucao, vizinhos)
    #print(posicao)
    # verifica se o melhor vizinho tem avaliação melhor do que a melhor avaliação até o momento
    if vizinhos_avaliacao[pos_melhor_vizinho] > melhor_avaliacao:
          # obtém o bit que foi modificado do melhor vizinho        
          #bit_modificado = obter_bit_modificado(melhor_solucao, vizinhos[pos_melhor_vizinho])           
          lista_tabu_cidades.append(vizinhos[pos_melhor_vizinho]) 
          lista_tabu.append(vizinhos_avaliacao[pos_melhor_vizinho]) # guarda o movimento proibido
          melhor_solucao = vizinhos[pos_melhor_vizinho][:] # temos uma solução melhor, faz uma cópia
          melhor_iteracao += 1 # incrementa a iteração onde foi achada a melhor solução até o momento
    iteracao += 1 # incrementa iteração

        # Aqui terminou o PASSO 0, agora iremos entrar em loop (executar os outros passos)
    
    while True:
          # a condição de parada é se a diferença da iteração e melhor_iteracao for maior que bt_max
          # iteracao é a iteração global (sempre é incrementada)
          # melhor_iteracao é a iteração onde se achou a melhor solução (nem sempre é incrementada)
          # bt_max é o máximo de iterações sem melhora no valor da melhor solução
          if (iteracao - melhor_iteracao) > bt_max:
            break
          # abaixo temos linhas de código quase idêntico ao PASSO 0
          # gerando novos vizinhos, faz uma cópia dos novos vizinhos        
          vizinhos = pegar_vizinhos(melhor_solucao, max_vizinhos,dadosDosDistritos,pesosDaEmpresa)[:]
          print(vizinhos)
          # obtém o valor de avaliação de todos os vizinhos
          vizinhos_avaliacao = obter_avaliacao_vizinhos(vizinhos, pesosDaEmpresa, max_vizinhos)[:]
          print(vizinhos_avaliacao)
          # obtém a posição do melhor vizinho
          pos_melhor_vizinho = obter_vizinho_melhor_avaliacao(vizinhos_avaliacao, lista_tabu, melhor_solucao, vizinhos)
          print(pos_melhor_vizinho)
          # verifica se o melhor vizinho tem avaliação melhor do que a melhor avaliação corrente
          
          if vizinhos_avaliacao[pos_melhor_vizinho] > melhor_avaliacao:
          
            #print(vizinhos_avaliacao[pos_melhor_vizinho])
            #print(melhor_avaliacao)
            # obtém o bit que foi modificado para gerar o melhor vizinho
            #bit_modificado = obter_bit_modificado(melhor_solucao, vizinhos[pos_melhor_vizinho])

            lista_tabu_cidades.append(vizinhos[pos_melhor_vizinho])
            lista_tabu.append(vizinhos_avaliacao[pos_melhor_vizinho]) # guarda o movimento proibido
         
            #lista_tabu[0] = bit_modificado # guarda o movimento proibido (Essa linha NÃO existia no Passo 0)
            melhor_solucao = vizinhos[pos_melhor_vizinho][:] # temos uma solução melhor, faz uma cópia da lista
          
            melhor_avaliacao = vizinhos_avaliacao[pos_melhor_vizinho] # atualiza a melhor avaliação
            melhor_iteracao += 1 # incrementa a iteração onde foi achada a melhor solução (nem sempre é incrementada)
          iteracao += 1 # incremento da iteração (sempre é incrementada)
         

  print('Solução final: {0}, Avaliação: {1}'.format(melhor_solucao, obter_avaliacao(melhor_solucao, pesosDaEmpresa)))
  print('Melhor iteração: {0}'.format(melhor_iteracao)) # mostra a iteração onde foi achada a melhor solução
  print('Iteração: {0}'.format(iteracao)) # mostra a iteração global
  print(lista_tabu)
  print(lista_tabu_cidades)
  i=0 
  while True:    
    if(melhor_solucao==dadosDosDistritos[i]):
      nomeCidade=distritos[i]
      break
    else:
      i+=1
      pass
  empresaSemQuebradeLinha=empresa.rstrip()
  resultado.append(empresaSemQuebradeLinha+";"+nomeCidade+'\n')



def funcaoValidarConteudoDaEmpresa(empresa):
  arrayEmpresa = empresa.split(",")  
  if(len(arrayEmpresa)==TamanhoDaLinha):
    if(arrayEmpresa[PosicaoCNPJ].strip().isdigit() and arrayEmpresa[PosicaoNUmeroDeEmpregados].strip().isdigit()
     and arrayEmpresa[PosicaoCanae].strip().isdigit() and arrayEmpresa[PosicaoFatoDeExportacao].strip().isdigit()):
     return True
    else:
      
      return False
  else:
      
      return False

     

def funcaovalidarCabecalho(conteudoDaColuna, nomedaColuna):
  if(conteudoDaColuna!=nomedaColuna):   
     textoLog.append(dataParaOArquivoLog+" | "+"O Conteúdo do campo: "+nomedaColuna+" é: "+conteudoDaColuna+", portanto está inválido\n")
     return False
  else:
    return True

#def validarCabecalhoArquivo(LinhasArquivo):    
 #   colunasdoCabecalho = LinhasArquivo[0].split(",")
  #  if(len(colunasdoCabecalho)==TamanhoDaLinha):
      #print(colunasdoCabecalho[3])
   #   if (funcaovalidarCabecalho(colunasdoCabecalho[0],NomeColunaCNPJ)  and 
   #     funcaovalidarCabecalho(colunasdoCabecalho[1],NomeColunaNumeroDeEmpregados) and 
    #    funcaovalidarCabecalho(colunasdoCabecalho[2],NomeColunaCNAE)):
    #    return True        
     # else:
     #   textoLog.append(dataParaOArquivoLog+" | "+"cabeçaçho invalido\n")
     #   return False        
   # else:
    #  return False
    #  textoLog.append(dataParaOArquivoLog+" | "+"O cabeçalho possui o tamanho diferente\n")      

def validarExistenciaDoAqruivo(nomeDOArquivo):
  if(os.path.exists(nomeDOArquivo)==True):
    return True
  else:
    return False

def Main(nomeDoArquivoAserLido):
      if (validarExistenciaDoAqruivo(nomeDoArquivoAserLido)):
        ArquivoAberto = open(nomeDoArquivoAserLido, 'r')
        LinhasLidas = ArquivoAberto.readlines()
        for i in range(0,len(LinhasLidas)):
            if(funcaoValidarConteudoDaEmpresa(LinhasLidas[i])):
              buscaTabu(LinhasLidas[i])
              textoLog.append(dataParaOArquivoLog+" | "+"linha: "+str(i+1)+" do Arquivo: "+nomeDoArquivoAserLido +" foi validada e processada\n")
            else:
              textoLog.append(dataParaOArquivoLog+" | "+"linha: "+str(i+1)+" do Arquivo: "+nomeDoArquivoAserLido +" é inálida\n")
        
      else:
        textoLog.append(dataParaOArquivoLog+" | "+"Arquivo: "+nomeDoArquivoAserLido +" não existe\n")
      arq = open("melhorDistrito.csv", 'w') 
      arq.writelines(resultado)
      arq.close()
     
       



Main(NomeDoArquivo)
data=datetime.now().strftime('%Y%m%d%H%M%S')
arq = open(data+".txt", 'w')
arq.writelines(textoLog)
arq.close()