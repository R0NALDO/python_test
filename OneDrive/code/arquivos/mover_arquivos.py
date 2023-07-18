#move arquivos caso tenham a mesma extensão

import os
import shutil

# Pasta de origem
source_folder = 'c:/ron/pasta1'

# Pasta de destino
destination_folder = r'C:\Users\ronaldo\Documents'

# Extensão de arquivo a ser movida
file_extension = '.txt'

# Percorre todos os arquivos na pasta de origem
for file in os.listdir(source_folder):
    # Verifica se o arquivo tem a extensão especificada
    if file.endswith(file_extension):
        # Monta o caminho completo para o arquivo
        file_path = os.path.join(source_folder, file)
        # Move o arquivo para a pasta de destino
        shutil.move(file_path, destination_folder)      
'''
Esse código assume que a pasta de origem e a pasta de destino já existem. Ele percorre todos os arquivos na pasta de origem, 
verifica se o arquivo tem a extensão especificada e, em seguida, move o arquivo para a pasta de destino. 
É importante notar que este código sobrescreverá arquivos com o mesmo nome na pasta de destino.
'''