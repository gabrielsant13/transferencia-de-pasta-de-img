Este executável tem como função pegar todas as pastas de imagens que vem do Cadastro de Clientes da Ion, e levar para o Winthor, mais precisamente rotina 1203.

A pasta de origem está sendo salva no caminho (hml) C:\CLIENTES (passível de mudança) e o formato de salvamento é o número do cpf/CNPJ do cliente. 
Portanto quando este exe rodar deverá pegar o nome dessa pasta (cpf/CNPJ), consultar no banco, verificar se já esta cadastrado, caso sim, retorna o 
codcli e salva na pasta de destino (é interessante identificar de alguma forma que a pasta já está salva no winthor, seja renomeando ou excluindo ela), 
caso não, não faz nada.

A pasta de destino deverá ser (hml) D:\Winthor\Teste\ETC\ANEXOS\U_CE2FZW_WI\CLIENTES e o nome da pasta para salvar deverá ser o código do cliente.
