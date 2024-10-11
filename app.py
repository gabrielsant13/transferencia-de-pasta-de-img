import os
import cx_Oracle
import time
import datetime

os.system("cls")

#caminho de diretorio local
# cx_Oracle.init_oracle_client(lib_dir=r"C:\app\client\product\12.2.0\client_1\bin")

# Configuração do banco de dados Oracle
dsn = cx_Oracle.makedsn("ip", "port", service_name="service_name")
user = "user"
password = "password"

# Configuração de caminho da pasta
caminho = str("C:\\ION Sistemas\\CLIENTES\\")

#funcao de tempo
def sysdate():
    ano,mes,dia,hora,min,seg,diaSemana,diaAno, horarioVerao= time.localtime()
    #return(f'{dia}/{mes}/{ano} {hora}:{min}:{seg} diaSemana:{diaSemana} diaAno:{diaAno}')
    return (f'{'{:02d}'.format(dia)} {'{:02d}'.format(mes)} {ano} {'{:02d}'.format(hora)} {'{:02d}'.format(min)} {'{:02d}'.format(seg)} {diaSemana} {diaAno}')

# Função utilizada para captar dias da semana
def datahora():
    tempo = sysdate().split()
    datahora = datetime.datetime.strptime(f'{tempo[0]}/{tempo[1]}/{tempo[2]} {tempo[3]}:{tempo[4]}:{tempo[5]}', "%d/%m/%Y %H:%M:%S")
    return datahora

# lógica
print('validação da logica\n')
while 1:
    while sysdate().split()[2] < '2027': # Trava de tempo
        tempo = sysdate().split()
        
        # Valida se o tempo está de acordo com os valores abaixo, se estiver inicia os processos
        if tempo[4] == '57' and tempo[5] <= '01':
            
            # Verifica o nome das pastas na Ion e salva em variável para validação
            clientes = [pasta for pasta in os.listdir(caminho) if os.path.isdir(os.path.join(caminho, pasta))]

            conn = cx_Oracle.connect(user=user, password=password, dsn=dsn)
            cursor = conn.cursor()

            for cliente in clientes:
                try:
                    cursor.execute(f"select codcli,numeros(cgcent) cgcent from pcclient where numeros(cgcent) in ('{cliente}')")
                    valor = cursor.fetchall()

                    codcli = str(valor[0][0])
                    cgcent = str(valor[0][1])

                    # Renomeia e altera a pasta
                    os.renames(caminho+cgcent, caminho+'00'+codcli)

                    # Salva no log
                    arquivo = open(caminho+'log.txt',"a")
                    arquivo.write(f'Importado cgcent: {cliente}, codcli: {codcli} - {datahora()}\n')
                    arquivo.close()

                    print(f'Ok: {cliente} - {codcli}')
                except:
                    print(f'Cliente não cadastrado ou não existe: {cliente}')
                
            print('------------------------------------------------------------------')

                    

            cursor.close()
            conn.close()
