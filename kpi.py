# Decalarando a constante do valor do Bônus:
CONSTANTE_BONUS = 1000
# Input do nome do usuário:
nome_usuario = input('Digite aqui o seu nome: ')
# Input do valor do salário:
vlr_salario = float(input("Digite aqui o valor do seu salário: "))
# Input do % de bônus:
pct_bonus = float(input("Digite aqui a porcentagem do seu bônus: "))
# Fazendo o calculo:
bonus_kpi_2024 = CONSTANTE_BONUS + vlr_salario * pct_bonus
# Mensagem de sáida:
saída = f'Olá, {nome_usuario}, o seu bônus foi de: {bonus_kpi_2024} '
# Imprimindo a mensagem de saída:
print(saída)
