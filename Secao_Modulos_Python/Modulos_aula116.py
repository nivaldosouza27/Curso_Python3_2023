# os.listdir para navegar em caminhos
# /Users/luizotavio/Desktop/EXEMPLO
# C:\Users\luizotavio\Desktop\EXEMPLO
# caminho = r'C:\\Users\\luizotavio\\Desktop\\EXEMPLO'

import os

caminho = os.path.join('C:\\Users\\nival\\OneDrive\\Imagens\\icons')

for item in os.listdir(caminho):
    print(item)
