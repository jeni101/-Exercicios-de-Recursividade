import sys

# Aumenta o limite da pilha de recursão
sys.setrecursionlimit(20000)

def investimento_bitcoin(bitcoins_na_conta=0, mes=0, total_investido=0, metas_atingidas=None):
    if metas_atingidas is None:
        metas_atingidas = set()
    
    # Preços do Bitcoin para 2024
    valores_do_bitcoin_2024 = [
        212323.71409958936, 249420.53670165068,
        339551.22740492615, 339213.9082836856, 
        336848.3951363235, 357564.0160982237, 
        349741.6927697542, 335065.9230811904, 
        335032.3351231667, 370754.0022858458, 
        506238.35740654235, 603809.0741112948
    ]
    
    valor_bitcoin = 664484  # Meta de 1 Bitcoin
    investimento_mensal = 250
    rendimento = 0.0005
    metas = {100000, 1000000, valor_bitcoin}  
    
    cotacao_atual = valores_do_bitcoin_2024[mes % 12] 
    investimento_em_bitcoin = investimento_mensal / cotacao_atual  # Converte o valor em reais para Bitcoin
    bitcoins_na_conta *= (1 + rendimento) 
    bitcoins_na_conta += investimento_em_bitcoin  
    total_investido += investimento_mensal  
    
    saldo_final = bitcoins_na_conta * cotacao_atual  
    
    metas_nao_atingidas = metas - metas_atingidas  

    
    for meta in metas_nao_atingidas:
        if saldo_final >= meta:
            anos = mes // 12
            meses_restantes = mes % 12
            juros_acumulados = saldo_final - total_investido
            if meta == 664484:  
                print(f"Atingiu a meta de 1 Bitcoin!")
                print('')
                print(f"Valor investido total: R$ {total_investido:,.2f}")
                print(f"Tempo gasto: {anos} anos e {meses_restantes} meses")
                print(f'Juros totais: R$ {juros_acumulados:,.2f}')
                print('-----------------------------------------------------')
            else:   
                print(f"◦= Meta de R$ {meta:,.2f} atingida!")
                print(".__________________________________________________.")
                print(f"""
    ◦= Tempo gasto: {anos} anos e {meses_restantes} meses
    ◦= Valor total investido: R$ {total_investido:,.2f}
    ◦= Juros totais: R$ {juros_acumulados:,.2f}
    """)
                print(".==================================================.")
            metas_atingidas.add(meta)  
    
    
    if metas_atingidas == metas:
        print("Todas as metas foram atingidas!")
        return  

    return investimento_bitcoin(bitcoins_na_conta, mes + 1, total_investido, metas_atingidas)


print("")
print(".==================================================.")
investimento_bitcoin()

