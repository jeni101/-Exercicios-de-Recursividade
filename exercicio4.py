
import sys

# Aumenta o limite da pilha de recursão
sys.setrecursionlimit(2000)



def poupanca(saldo, meses, valor_investido_mensal, taxa_juros, marco ):
    #comforme o saldo vai aumentando ele compara com o marco expecificado, caso n seja maior ou igual ele continuara investindo e aplicando o juros  
    if saldo>= marco:
        anos = meses // 12
        meses_restantes = meses % 12
        valor_total = valor_investido_mensal * meses
        juros_acumulados = saldo - valor_total
        print(f"""\n
             .____________________________________________________.
             |  Tempo gasto:   {anos} anos   {meses_restantes} messes  
             |----------------------------------------------------|
             |  Valor tatal do investimento: R$ {valor_total}
             |----------------------------------------------------|
             |  Juros compostos obtidos ate atingir de R${marco}: 
             |----------------------------------------------------|
             |  Juros_acumulados: R${juros_acumulados}
             .____________________________________________________.
              """)
        
        return saldo
    else:
        novo_saldo = saldo + valor_investido_mensal
        juros = saldo * 0.0005
        novo_saldo = novo_saldo + juros
        
        return poupanca(novo_saldo, meses +1, valor_investido_mensal, taxa_juros, marco)
        
    
    
# Dados importantes para comecar a funcao

valor_investido_mensal = 500
taxa_rendimento = 0.0005

saldo_inicial = 0
meses_iniciais = 0

marco_100_pila = 100000
marco_mil_pila = 1000000
print("")
print("""Parabens você chegou no marco de R$ 100.000.00
      segue teu score: """)
poupanca(saldo_inicial, meses_iniciais, valor_investido_mensal, taxa_rendimento, marco_100_pila )

print("")
print("""Parabens você chegou no marco de R$ 1.000.000.00
      segue teu score: """)
poupanca(saldo_inicial, meses_iniciais, valor_investido_mensal, taxa_rendimento, marco_mil_pila )