#4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
#• SP – R$67.836,43
#• RJ – R$36.678,66
#• MG – R$29.229,88
#• ES – R$27.165,48
#• Outros – R$19.849,53
#Escreva um programa na linguagem que desejar onde calcule o percentual de representação que 
# cada estado teve dentro do valor total mensal da distribuidora. 

faturamento_dos_estados = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

faturamento_total = sum(faturamento_dos_estados.values())

for estado, valor in faturamento_dos_estados.items(): 
    percentual = (valor/ faturamento_total)* 100
    print(f"{estado}: {percentual:.2f}%")

#como resultado devemos obter: 
#SP: 37.53%
#RJ: 20.29%
#MG: 16.17%
#ES: 15.03%
#Outros: 10.98%