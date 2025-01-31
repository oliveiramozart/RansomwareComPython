## bibliotecas do python necessarias para acessar recursos do SO e de criptografia
import os
import pyaes

## abrindo o arquivo criptografado
file_name = "ArquivoAlvo.txt.ransomwaretrollcriptografado"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## chave para descriptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## removendo o arquivo criptografado
os.remove(file_name)

## criando o arquivo descriptografado
new_file = "ArquivoAlvo.txt"
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()
