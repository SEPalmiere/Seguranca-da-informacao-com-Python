import ctypes

pasta = input("Digite o caminho da pasta a ser ocultada ex (C:\pasta): " )
atributo_ocultar = 0x02 # arquivo no formato hexadecimal

retorno = ctypes.windll.kernel32.SetFileAttributesW("ocultar.txt", atributo_ocultar)

if retorno:
    print ("Arquivo foi ocultado")
else:
    print ("Arquivo não foi ocultado")