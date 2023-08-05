import win32com.client as win32
import os
import pandas as pd

# Define os destinatários e as abas correspondentes
destinatarios = ['otavio-cunha@hotmail.com', 'otavio-cunha@hotmail.com', 'otavio-cunha@hotmail.com', 'otavio-cunha@hotmail.com']
abas = ['teste', 'teste1', 'teste2', 'teste3']

# Cria uma instância do objeto outlook
outlook = win32.Dispatch('outlook.application')

# Loop para iterar por cada destinatário e por cada aba
for i, destinatario in enumerate(destinatarios):
    # Cria um novo e-mail
    mail = outlook.CreateItem(0)

    # Define o destinatário
    mail.To = destinatario

    # Define o assunto
    mail.Subject = f'Assunto do e-mail - {abas[i]}'

    # Define o corpo da mensagem
    mail.Body = f'Corpo do e-mail - {abas[i]}'

    # Carrega a aba correspondente do arquivo Excel
    excel_path = r"C:\Users\Otavio.cunha\OneDrive - RECH IMPORTADORA E DISTRIBUIDORA S A\Área de Trabalho\códigos\teste.xlsx"
    df = pd.read_excel(excel_path, sheet_name=abas[i])

    # Salva a aba em um arquivo temporário
    temp_path = r"C:\Users\Otavio.cunha\OneDrive - RECH IMPORTADORA E DISTRIBUIDORA S A\Área de Trabalho\códigos\temp.xlsx"
    df.to_excel(temp_path, index=False)

    # adiciona a sua assinatura do Outlook ao final do corpo do e-mail
    email.GetInspector().WordEditor.Range.InsertAfter('\n\n--\nSua assinatura aqui')

        
        
        
    # Anexa o arquivo Excel temporário (que contém apenas a aba correspondente)
    attachment = os.path.abspath(temp_path)
    mail.Attachments.Add(attachment)

    # Envia o e-mail
    mail.Send()

    # Remove o arquivo temporário
    os.remove(temp_path)



# #########################################################################################################################################################################################################

# # Define os destinatários e as abas correspondentes
#         destinatarios = ['otavio-cunha@hotmail.com', 'otavio-cunha@hotmail.com', 'otavio-cunha@hotmail.com', 'otavio-cunha@hotmail.com']
        
#         ##Consigo alterar o nome dos destinatarios x
#         # destinatario = self.text_destinatario.text()
        
#         # destinatarios = [destinatario]

#         # Cria uma instância do objeto outlook
#         outlook = win32.Dispatch('outlook.application')

#         # Loop para iterar por cada destinatário e por cada aba
#         for destinatario in destinatarios:
            
#             abas = ['teste', 'teste1', 'teste2', 'teste3']
#             # Cria um novo e-mail
#             mail = outlook.CreateItem(0)

#             # Define o destinatário
#             mail.To = destinatario

#             # Define o assunto
#             mail.Subject = f'Assunto do e-mail - {abas[1]}'

#             # Define o corpo da mensagem
#             mail.Body = f'Corpo do e-mail - {abas[1]}'

#             # Carrega a aba correspondente do arquivo Excel
#             excel_path = r"C:\Users\Otavio.cunha\OneDrive - RECH IMPORTADORA E DISTRIBUIDORA S A\Área de Trabalho\códigos\teste.xlsx"
#             df = pd.read_excel(excel_path, sheet_name=abas[1])

#             # Salva a aba em um arquivo temporário
#             temp_path = r"C:\Users\Otavio.cunha\OneDrive - RECH IMPORTADORA E DISTRIBUIDORA S A\Área de Trabalho\códigos\temp.xlsx"
#             df.to_excel(temp_path, index=False)

#             # Anexa o arquivo Excel temporário (que contém apenas a aba correspondente)
#             attachment = os.path.abspath(temp_path)
#             mail.Attachments.Add(attachment)

#             # Envia o e-mail
#             mail.Send()

#             # Remove o arquivo temporário
#             os.remove(temp_path)
#         print('email enviado')   



