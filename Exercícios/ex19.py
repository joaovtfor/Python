salario = float(input("Qual é o seu salário? "))
tempoS = int(input("Trabalha na empresa há quantos meses? "))

if salario <= 500:
    salarioR1 = salario * 1.25
    if tempoS < 12:          
        print(f"Seu novo salário é:{salarioR1}")
    if 12 <= tempoS <= 36:
        print(f"Seu novo salário é:{salarioR1 + 100}")
    if 36 < tempoS <= 72:
        print(f"Seu novo salário é:{salarioR1 + 200}")
    if 72 < tempoS <= 120:
        print(f"Seu novo salário é:{salarioR1 + 300}")
    if tempoS > 120:
        print(f"Seu novo salário é:{salarioR1 + 500}")
        
if 500 < salario < 1000:
    salarioR2 = salario * 1.20
    if tempoS < 12:          
        print(f"Seu novo salário é:{salarioR1}")
    if 12 <= tempoS <= 36:
        print(f"Seu novo salário é:{salarioR1 + 100}")
    if 36 < tempoS <= 72:
        print(f"Seu novo salário é:{salarioR1 + 200}")
    if 72 < tempoS <= 120:
        print(f"Seu novo salário é:{salarioR1 + 300}")
    if tempoS > 120:
        print(f"Seu novo salário é:{salarioR1 + 500}")
             
if 1000 <salario < 1500:
    salarioR3 = salario * 1.15
    if tempoS < 12:          
        print(f"Seu novo salário é:{salarioR1}")
    if 12 <= tempoS <= 36:
        print(f"Seu novo salário é:{salarioR1 + 100}")
    if 36 < tempoS <= 72:
        print(f"Seu novo salário é:{salarioR1 + 200}")
    if 72 < tempoS <= 120:
        print(f"Seu novo salário é:{salarioR1 + 300}")
    if tempoS > 120:
        print(f"Seu novo salário é:{salarioR1 + 500}")
             
if 1500 < salario <= 2000:
    salarioR4 = salario * 1.10
    if tempoS < 12:          
        print(f"Seu novo salário é:{salarioR1}")
    if 12 <= tempoS <= 36:
        print(f"Seu novo salário é:{salarioR1 + 100}")
    if 36 < tempoS <= 72:
        print(f"Seu novo salário é:{salarioR1 + 200}")
    if 72 < tempoS <= 120:
        print(f"Seu novo salário é:{salarioR1 + 300}")
    if tempoS > 120:
        print(f"Seu novo salário é:{salarioR1 + 500}")
             
if salario > 2000:
    if tempoS < 12:          
        print(f"Seu salário continua:{salario}")
    if 12 <= tempoS <= 36:
        print(f"Seu novo salário é:{salario + 100}")
    if 36 < tempoS <= 72:
        print(f"Seu novo salário é:{salario + 200}")
    if 72 < tempoS <= 120:
        print(f"Seu novo salário é:{salario + 300}")
    if tempoS > 120:
        print(f"Seu novo salário é:{salario + 500}")
    
