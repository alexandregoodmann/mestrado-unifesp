# --------------------------------------------------------------------------------------
# UNIFESP - Programa de Pós Graduação em Ciência da Computação
# AAED 2 sem 2024
# Professora: LILIAN BERTON
# Aluno: Alexandre Ferreira e Silva
# Trabalho final do semestre
# Fonte: ChatGPT, Google Gemini
# --------------------------------------------------------------------------------------

import os
import uuid
os.system('cls' if os.name == 'nt' else 'clear')

lista_uuid = []
for i in range(0, 1000*1000):
    lista_uuid.append(uuid.uuid1())

arquivo = open("C:\\projetos\\mestrado-unifesp\\algoritmo\\trabalho_final\\base_dados_tipo1.txt", "a")  # Abre o arquivo para escrita
arquivo.writelines("%s\n" % l for l in lista_uuid)
arquivo.close()  # Fecha o arquivo

print('-- fim --')