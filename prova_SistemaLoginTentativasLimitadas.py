def SistemaLoginTentativasLimitadas():
    try:
        tentativas = 0
        while tentativas < 3:
            usuario = input("Digite seu nome de usuário: ")
            senha = input("Digite sua senha: ")
            if usuario == "admin" and senha == "123":
                print("Login bem-sucedido!")
                return
            else:
                tentativas += 1
                print(f'Nome de usuário ou senha incorretos. Restão  {3 - tentativas} tentativas.')
        print("Número máximo de tentativas excedido. Acesso negado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")    
SistemaLoginTentativasLimitadas()