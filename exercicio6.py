
import sys

# Aumenta o limite da pilha de recursão (se necessário)
sys.setrecursionlimit(90000)

def investimento_acoes(saldo=0, meses=0, atingiu_meta100k=False, atingiu_meta1M=False, valor_investido_mensal=80):
    # Metas
    meta100k, meta1M = 100000, 1000000
    
    
    dividendo_petrobras = 0.3548
    dividendo_itau = 0.0117
    dividendo_csna3 = 0.1397
    
   
    valor_acao_csna3 = 9.20
    valor_acao_itau = 33.22
    valor_acao_petrobras = 34.29
    
    # Calculando o número de ações inteiras adquiridas (1 de cada)
    contador_acoes_petrobras = saldo // valor_acao_petrobras
    contador_acoes_itau = saldo // valor_acao_itau
    contador_acoes_csna3 = saldo // valor_acao_csna3
    
    # Calculando o valor restante após comprar ações inteiras
    saldo_restante = saldo - (contador_acoes_petrobras * valor_acao_petrobras + 
                              contador_acoes_itau * valor_acao_itau + 
                              contador_acoes_csna3 * valor_acao_csna3)
    
    # Verificando se o saldo restante é positivo para comprar frações
    if saldo_restante > 0:
        # Agora, vamos calcular as frações para as 3 ações proporcionalmente
        quantidade_de_fracoes_petrobras = saldo_restante * (valor_acao_petrobras / (valor_acao_petrobras + valor_acao_itau + valor_acao_csna3)) / valor_acao_petrobras

    else:
        
        quantidade_de_fracoes_petrobras = 0
        quantidade_de_fracoes_csna3 = 0
        quantidade_de_fracoes_itau = 0
    
    
    dividendo_csna3 = valor_acao_csna3 * dividendo_csna3
    dividendo_itau = valor_acao_itau * dividendo_itau
    dividendo_petrobras = valor_acao_petrobras * dividendo_petrobras
    
    dividendo_fracao_petrobras = dividendo_petrobras * quantidade_de_fracoes_petrobras
   
    
   
    dividendo_total_petrobras = (dividendo_petrobras * contador_acoes_petrobras) + dividendo_fracao_petrobras
    dividendo_total_csna3 = (dividendo_csna3 * contador_acoes_csna3) 
    dividendo_total_itau = (dividendo_itau * contador_acoes_itau) 
    
    
    retorno_investimento = dividendo_total_petrobras + dividendo_total_csna3 + dividendo_total_itau

   
    if saldo + retorno_investimento >= meta100k and not atingiu_meta100k:
        anos = meses // 12
        meses_restantes = meses % 12
        print("-------------------------------------------")
        print(f"  Meta de R$ 100.000,00 atingida!")
        print("-------------------------------------------")
        print(f"  Valor total investido: R$ {saldo:.2f}")
        print(f"  Dividendos totais: R$ {retorno_investimento:.2f}")
        print(f"  Tempo gasto: {anos} anos e {meses_restantes} meses")
        print("-------------------------------------------")
        print(f"  Ações Petrobras: {contador_acoes_petrobras + quantidade_de_fracoes_petrobras:.4f}")
        print(f"  Ações Itaú: {contador_acoes_itau + quantidade_de_fracoes_itau:.4f}")
        print(f"  Ações CSNA3: {contador_acoes_csna3 + quantidade_de_fracoes_csna3:.4f}")
        print("-------------------------------------------")
        atingiu_meta100k = True
    
    
    if saldo + retorno_investimento >= meta1M and not atingiu_meta1M:
        anos = meses // 12
        meses_restantes = meses % 12
        print("-------------------------------------------")
        print(f"  Meta de R$ 1.000.000,00 atingida!")
        print("-------------------------------------------")
        print(f"  Valor total investido: R$ {saldo:.2f}")
        print(f"  Dividendos totais: R$ {retorno_investimento:.2f}")
        print(f"  Tempo gasto: {anos} anos e {meses_restantes} meses")
        print("-------------------------------------------")
        print(f"  Ações Petrobras: {contador_acoes_petrobras + quantidade_de_fracoes_petrobras:.4f}")
        print(f"  Ações Itaú: {contador_acoes_itau + quantidade_de_fracoes_itau:.4f}")
        print(f"  Ações CSNA3: {contador_acoes_csna3 + quantidade_de_fracoes_csna3:.4f}")
        print("-------------------------------------------")
        atingiu_meta1M = True
        return saldo + retorno_investimento 
    

    saldo += valor_investido_mensal 
    meses += 1 
    

    return investimento_acoes(saldo=saldo, meses=meses, atingiu_meta100k=atingiu_meta100k,  atingiu_meta1M=atingiu_meta1M, valor_investido_mensal=valor_investido_mensal)


investimento_acoes()
