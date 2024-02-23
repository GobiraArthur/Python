import numpy as np
from faker import Faker
import pandas as pd

faker = Faker('pt_BR')
x = 1000
sexo = [faker.boolean() for _ in range(x)]
nome=[]
for _ in range(x):
    if sexo[_] == True:
        nome.append(faker.name_male())
        sexo[_]='Masculino'
    else:
        sexo[_]='Feminino'
        nome.append(faker.name_female())

cpf = [faker.cpf() for _ in range(x)]

idade = np.random.randint(18, 29, x)
email = [faker.email() for _ in range(x)]
notaEnem = np.random.randint(640, 801, x)
abandonou = [faker.boolean(chance_of_getting_true=30) for _ in range(x)]
cra2 = np.full(x, np.nan)
cra4 = np.full(x, np.nan)
cra6 = np.full(x, np.nan)
semestreAbandonou = [None]*x
for i in range(x):
    semestreAbandon = np.random.randint(1, 7)
    if abandonou[i] == False:
        cra2[i] = round(np.random.uniform(5, 10),2)
        cra4[i] = round(np.random.uniform(5, 10),2)
        cra6[i] = round(np.random.uniform(5, 10),2)
    else:
        semestreAbandonou[i] = semestreAbandon
        if semestreAbandon > 2 and semestreAbandon <= 4:
            cra2[i] = round(np.random.uniform(5, 10),2)
        if semestreAbandon > 4 and semestreAbandon <= 6:
            cra2[i] = round(np.random.uniform(5, 10),2)
            cra4[i] = round(np.random.uniform(5, 10),2)
    
dados = {'Nome': nome,
         'Sexo': sexo, 
         'CPF': cpf, 
         'Idade': idade, 
         'Email': email, 
         'Nota Enem': notaEnem, 
         'CRA2': cra2, 
         'CRA4': cra4, 
         'CRA6': cra6, 
         'Abandonou': abandonou, 
         'Semestre Abandonou': semestreAbandonou}
df = pd.DataFrame(dados)
df.to_csv('Alunos.csv')