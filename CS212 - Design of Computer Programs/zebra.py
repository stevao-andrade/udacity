# -*- coding: UTF8 -*-

import itertools


def aDireita(casa1 , casa2):
    #A casa 1 está imediatamente à direita da casa 2
    return casa1 - casa2 == 1

def proxima(casa1, casa2):
    #A casa 1 está à direita ou à esquerda da casa 2
    return abs(casa1 - casa2) == 1

def zebra_puzzle():
    #retorna uma tupla (agua, zebra) indicando o numero da casa de cada um.
    casas = primeira, _, meio, _,_ = [1,2,3,4,5] #1
    combinacoes = list(itertools.permutations(casas)) #todas as combinações possiveis de soluções 5!**5
    return next((AGUA,ZEBRA)
                    #Existem 5 combinações para cada dica: Cor, Nacionalidade, Animal, Bebida, Cigarro. Por isso o total de permutações é igual a 5! elevado a 5.
                    for(vermelho, verde, marrom, amarela, azul) in combinacoes
		    if aDireita(verde, marrom) #6
                    for(ingles, espanhol, ucraniano, japones, noroegues) in combinacoes
                    if ingles is vermelho #2
		    if noroegues is primeira #10
		    if proxima(noroegues, azul) #15
		    for(cafe, cha, leite, sucoLaranja, AGUA) in combinacoes					                    
                    if cafe is verde #4
		    if ucraniano is cha #5
		    if leite is meio #9
		    for(oldGold, kools, chesterfields, luckyStrike, parliaments) in combinacoes #Marcas de cigarro
		    if kools is amarela #8
                    if luckyStrike is sucoLaranja #13
                    if japones is parliaments #14
		    for(cachorro, caracol, raposa, cavalo, ZEBRA) in combinacoes
                    if espanhol is cachorro #3
                    if oldGold is caracol #7                    
                    if proxima(chesterfields, raposa) #11
                    if proxima(kools, cavalo) #12
                    ) # Fim do Gerador de expreções

#Gerador de expressões evida que o laço seja executado por completo caso a condição seja aceita.
#Gerador de experessões cria uma promessa de executar algo. Só executa quando existe a chamada NEXT

#Fatos:

#1 Existem 5 casas.

#2 O ingles vive na casa vermelha

#3 O espanhol tem um cachorro.

#4 O morador da casa verde bebe café.

#5 O ucraniano bebe cha.

#6 A casa verde fica imediatamente à direita da casa marrom.

#7 O fumante de Old Gold possui um caracol.

#8 Kools são fumados na casa amarela.

#9 Quem bebe leite mora na casa do meio.

#10 O noroegues vive na primeira casa.

#11 O homem que fuma Chesterfields vive proximo à casa com uma raposa.

#12 O fumanete de Kools mora proximo à casa com um cavalo

#13 O fumante de Lucky Strike bebe suco de laranja.

#14 O japones fuma Parliaments.

#15 O noroegues vive proximo à casa azul

# Quem bebe AGUA? Quem tem uma ZEBRA?
