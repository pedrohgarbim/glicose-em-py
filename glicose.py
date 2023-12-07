nome = str(input("DIGITE O NOME DO PACIENTE: "))
glicose = float(input("DIGITE A MEDIDA DA GLICOSE DO PACIENTE: "))

print("CLASSIFICAÇÃO: ", end="")

if glicose <= 100:
    print(f"NIVEL DE GLICOSE NORMAL DO(A) PACIENTE {nome}")
elif glicose <= 140:
    print(f"NIVEL DE GLICOSE ELEVADO DO(A) PACIENTE {nome} TOMAR CUIDADO")
else:
    print(f"CUIDADO, PACIENTE {nome} POSSUI DIABETES")

