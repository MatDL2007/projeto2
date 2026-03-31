import random
import datetime

def menu():
    nome_arq = 'log.txt'
    while True:
        print('Monitor LogPy')
        print('1 - Gerar Logs')
        print('2 - Análisar Logs')
        print('3 - Gerar e Análisar Logs')
        print('4 - Sair')
        opcao = input('Escolha um opção: ')
        if opcao == '1':
            try: 
                qtd = int(input('Quantidade de Logs'))
                gerarArquivo(nome_arq, qtd)
            except:
                print('Qtd incorreta')
        elif opcao == '2':
            analisarLog(nome_arq)
        elif opcao == '3':
            try:
                qtd = int(input('Quantidade de Logs'))
                gerarArquivo (nome_arq, qtd)
                analisarLog (nome_arq)
            except:
                print ('Qtd incorreta')
        elif opcao == '4':
            print('Até mais')
            break
        else:
            print("Opção errada")
            
def gerarArquivo(nome_arq, qtd):
    with open(nome_arq, 'w', encoding='UTF-8') as arq:
        for i in range (qtd):
            arq.write(montarLog(i) + '\n')
        print('Logs gerados')
        
def montarLog(i):
    data = gerarDataHora(i)
    ip = gerarIp(i)
    recurso = gerarRecurso(i)
    metodo = gerarMetodo(i)
    status = gerarStatus(i)
    tempo = gerarTempo(i)
    agente = gerarAgente(i)
    return f'[{data}] {ip} - {metodo} - {status} - {recurso} - {tempo}ms - 500mb - HTTP/1.1 - {agente} - /home'
     
def gerarDataHora(i):
    base = datetime.datetime(2026, 3, 30, 22, 8, 0)
    data = datetime.timedelta(seconds = i * random.randint(5, 20))
    return (base + data.strftime('%d/%m/$Y %H:%M:%S'))

def gerarIp(i):
    r = random.randint(1, 6)
    
    if i >= 20 and i <= 30:
        return '200.0.111.345'
    #return f'{random.radint(10, 255)}.{random.radint(1,255)}.{random.radint(1, 255). {random.radint (1,255)}
    if r == 1:
        return '192.168.5.6'
    elif r == 2:
        return '192.168.12.2'
    elif r == 3:
        return '192.168.0.2'
    elif r == 4:
        return '192.168.7.2'
    elif r == 5:
        return '192.168.2.2'
    else:
        return '192.168.65.68'
    