class contador:
    def __init__(self, limite):
# Atributo da classe definido com 'self'
        self.limite = limite
        
    def contar(self):
        contador = 0
        while True:
            print(contador)
            contador += 1
# Verifica se o contador atingiu o limite
            if contador == self.limite:
# Sai do loop quando o limite é alcançado
                break
        
meu_contador = contador(4)
meu_contador.contar()