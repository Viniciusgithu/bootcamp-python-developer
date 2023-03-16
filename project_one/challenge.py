menu = '''
  ------------------
  |  [d] Deposito  |
  |  [s] Sacar     |
  |  [e] Extrato   |
  |  [q] Sair      |
  ------------------
'''

saldo = 0
extrato = ''
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3

while True:
  
  print(f'''
        ---------------------------------------------
        |  Seja bem vindo!(a) ao banco mundial. 🏦 |
        |  Escolha uma opção para inicar 🤑       |
        -------------------------------------------
        ''')
  
  opcao = input(menu)
  
  if opcao == 'd':
    valor = float(input(f'''
                        
                        ---------------------------------
                        | Informe o valor do depósito:💵  | 
                        ---------------------------------
                        '''))
    
    if valor > 0:
      saldo += valor
      extrato += f'''
      ------------------------------------------
      | Depósito no valor de R${valor:.2f}💵\n |
      ------------------------------------------
      '''
      
    else:
      print(f'''
            -----------------------------------
            |💢 Valor informado é inválido 💢|
            ----------------------------------
            ''')  
      
  elif opcao == 's':
    valor = float(input(f'''
                        
                        -------------------------------
                        |Informe o valor do saque:💸  | 
                        -------------------------------
                        
                        '''))
    
    if valor > saldo:
      print(f'''
            
            -----------------------------------------
            |💢 Você não possui saldo suficiente 💢|
            ----------------------------------------
             
            '''
            )
      
    elif valor > limite:
      
      print(f''' 
            
            ------------------------------------------------
            | O valor do saque excede o limite: R${limite} |
            ------------------------------------------------
            ''')  
      
    elif numero_saques >= LIMITE_SAQUES:
      print(f'''
            
            ---------------------------------------------------
            |💢 Limite de saques: {LIMITE_SAQUES}x excedido 💢|
            --------------------------------------------------
            
            ''')  
    elif valor > 0:
      saldo -= valor
      extrato += f'''
      
            -----------------------------------------
            | Saque no valor de: R${valor:.2f}\n 💸|
            ----------------------------------------
      
      '''
      
      numero_saques += 1
      
    else:
      print(f'''
            
          ------------------------------------------------------
          |💢 Operação falhou, o valor informado é inválido 💢|
          -----------------------------------------------------                      
            ''')  
  
  elif opcao == 'e':
    
    print(f''''
          ----------------------------
          | 🧧🧧🧧 EXTRATO 🧧🧧🧧 |
          ----------------------------
          ''')
    
    print('Não foram realizadas movimentações' if not extrato else extrato )    
    
    print(f'''
          
          ------------------------------------
          |Seu saldo é de: R${saldo:.2f} 💵 |
          ------------------------------------
          ''')
    
    print('*️⃣*️⃣*️⃣*️⃣*️⃣*️⃣')
  
  elif opcao == 'q':
    break
  
  else:
    print('Operação inválida, por favor selecione as opções do painel')  
      