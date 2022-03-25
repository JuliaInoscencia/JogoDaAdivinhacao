"""
  AO PREENCHER ESSE CABECALHO COM O MEU NOME E O MEU NUMERO USP, 
  DECLARO QUE SOU O UNICO AUTOR E RESPONSAVEL POR ESSE PROGRAMA. 
  TODAS AS PARTES ORIGINAIS DESSE EXERCICIO PROGRAMA (EP) FORAM 
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUCÕES
  DESSE EP E QUE PORTANTO NAO CONSTITUEM DESONESTIDADE ACADEMICA
  OU PLAGIO.  
  DECLARO TAMBEM QUE SOU RESPONSAVEL POR TODAS AS COPIAS
  DESSE PROGRAMA E QUE EU NAO DISTRIBUI OU FACILITEI A
  SUA DISTRIBUICAO. ESTOU CIENTE QUE OS CASOS DE PLAGIO E
  DESONESTIDADE ACADEMICA SERAO TRATADOS SEGUNDO OS CRITERIOS
  DIVULGADOS NA PAGINA DA DISCIPLINA.
  ENTENDO QUE EP SEM ASSINATURA NAO SERAO CORRIGIDOS E,
  AINDA ASSIM, PODERAO SER PUNIDOS POR DESONESTIDADE ACADEMICA.

  Nome : Julia Inoscencia Oliveira dos Santos
  Prof.: Leo^nidas de Oliveira Branda~o

  - O algoritmo Quicksort foi baseado em
  http://wiki.python.org.br/QuickSort

"""

import math; # para math.sqrt( x )

# Para geracao de numeros pseudo-aleatorios: inicio
#
CPA_NUM1    =  16807;
CPA_NUM2    =   2836;
CPA_MOD     = 127773;

# Variavel global necessaria para "sortear" uma sequencia de valores
_PROXIMO_INTERNO = 127; # se nao alterar a "semente" comece pelo 127

# Define semente do gerador de pseudo-aleatorios
def _define_semente (valor) :
  global _PROXIMO_INTERNO; # define valor da variavel global '_PROXIMO_INTERNO'
  _PROXIMO_INTERNO = valor;

# Devolve resto da divisao do proximo 'pseudo-aleatorio' por 'mod'  - usando iterador '_PROXIMO_INTERNO'
def _proximo_pseudo_lim (mod) : # devolve entre 0 e 'mod-1'
  global _PROXIMO_INTERNO; # variavel global '_PROXIMO_INTERNO'
  _PROXIMO_INTERNO = ((CPA_NUM1 * _PROXIMO_INTERNO + CPA_NUM2) % CPA_MOD);
  return _PROXIMO_INTERNO % mod;

# Solicita do usuario uma semente para iniciar os "sorteios" (definindo '_PROXIMO_INTERNO')
def _inicia ():
  global semente;
  semente = int(input(" Digite a semente do sorteio: "));
  _define_semente(semente);
  return _proximo_pseudo_lim(20); # devolve proximo num. pseudo-aleatorio (apos 'semente')

# Para gerao de numeros pseudo aleatorios: fim
# Voce^ deve usar "_inicia()" para obter o numero sorteado

tent = 0
sorteado = _inicia()
print("\nEscolhi um numero inteiro entre 1 e 20. Adivinhe-o!")
while tent <= 5:
    chute = int(input("Seu chute:\n"))
    if chute == sorteado:
        tent += 1
        print("Legal, acertou na tentativa", tent)
        tent = 6
    else:
        if chute < sorteado:
            print("Chutou baixo")
            tent += 1
        else:
            print("Chutou alto")
            tent += 1
        if sorteado%2 == 0 and chute%2 != 0:
            print("O meu numero eh par")
        if sorteado%2 != 0 and chute%2 == 0:
            print("O meu numero eh impar")
    if tent == 5 and chute !=sorteado:
        print("Tentativas esgotadas!","\nO meu numero eh:",sorteado)
        tent += 1
