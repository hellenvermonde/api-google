import os
import pickle
# Gmail API utils
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
# for encoding/decoding messages in base64
from base64 import urlsafe_b64decode, urlsafe_b64encode
# for dealing with attachement MIME types
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from mimetypes import guess_type as guess_mime_type
from email.mime.application import MIMEApplication


class Gmail():
    def __init__(self):
        # Request all access (permission to read/send/receive emails, manage the inbox, and more)
        self.SCOPES = ['https://mail.google.com/'] #If modifying these scopes, delete the file token.json.
        self.our_email = 'dev.vermonde@gmail.com.br' #Usar mesmo e-mail que criou a autenticação da API

    #AUTENTICAÇÃO
    def gmail_authenticate(self):
        ''' Autenticação com a API do Gmail
            *** Verificar somente uma vez
            retorna
                objeto de serviço: que poderá ser usado posteriormente em todas as nossas próximas funções
        '''
        creds = None
        
        # the file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first time
        if os.path.exists("token_gmail_dev.pickle"):
            with open("token_gmail_dev.pickle", "rb") as token:
                creds = pickle.load(token)
        
        # if there are no (valid) credentials availablle, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('./src/Integrations/credentials.json', self.SCOPES)
                creds = flow.run_local_server(port=0)
            # save the credentials for the next run
            with open("token_gmail_dev.pickle", "wb") as token:
                pickle.dump(creds, token)
        
        return build('gmail', 'v1', credentials=creds)

    #CRIAÇÃO DE UM EMAIL, ADICIONANDO ANEXO E ENVIANDO MSG
    def add_attachment(self, message, filename):
        ''' Função que adiciona um anexo a uma mensagem, uma mensagem é uma instância de MIMEMultipart(ou MIMEText, se não contém anexos).
            Adds the attachment with the given filename to the given message 
        '''

        content_type, encoding = guess_mime_type(filename)
        if content_type is None or encoding is not None:
            content_type = 'application/octet-stream'
        main_type, sub_type = content_type.split('/', 1)
        if main_type == 'text':
            fp = open(filename, 'rb')
            msg = MIMEText(fp.read().decode(), _subtype=sub_type)
            fp.close()
        elif main_type == 'image':
            fp = open(filename, 'rb')
            msg = MIMEImage(fp.read(), _subtype=sub_type)
            fp.close()
        elif main_type == 'audio':
            fp = open(filename, 'rb')
            msg = MIMEAudio(fp.read(), _subtype=sub_type)
            fp.close()
        else:
            fp = open(filename, 'rb')
            msg = MIMEApplication(fp.read(), sub_type)
            # msg = MIMEBase(main_type, sub_type)
            # msg.set_payload(fp.read())
            fp.close()

        filename = os.path.basename(filename)
        msg.add_header('Content-Disposition', 'attachment', filename=filename)
        message.attach(msg)
    
    def build_message(self, destination, obj, body, attachments=[]):
        ''' Função que recebe alguns parâmetros de mensagem, cria e retorna uma mensagem de email
        '''
        if not attachments: # no attachments given
            message = MIMEText(body, 'html')
            message['to'] = destination
            message['from'] = self.our_email
            message['subject'] = obj
        else:
            message = MIMEMultipart()
            message['to'] = destination
            message['from'] = self.our_email
            message['subject'] = obj
            message.attach(MIMEText(body, 'html'))
            for filename in attachments:
                self.add_attachment(message, filename)
        
        return {'raw': urlsafe_b64encode(message.as_bytes()).decode()}
    
    def send_message(self, service, destination, obj, body, attachments=[]):
        print("ENTREI AQUI 4")
        return service.users().messages().send(
            userId="me",
            body=self.build_message(destination, obj, body, attachments)
        ).execute()

    #STATUS MENSAGEM
    def get_messages_infos(self, service, message_id):
        full_message = service.users().messages().get(userId='me', id=message_id).execute()       
        msg_headers = full_message['payload']['headers']

    def list_ids_message(self, service):
        # results = service.users().messages().list(userId='me',q="from:xyz@wso2.com", maxResults=10).execute()
        # results = service.users().messages().list(userId='me', labelIds=['INBOX'],  q="is:read").execute()
        results = service.users().messages().list(userId='me', labelIds=['INBOX'],  q="is:unread").execute()
        messages = results.get('messages', [])


# gm = Gmail()
# service = gm.gmail_authenticate() #Autenticar apenas uma vez
# gm.teste(service, '1828cfc09d0b053f')
# gm.list_ids_message(service)
# response = gm.send_message(service, "hellenvermonde@gmail.com.br", "Mensagem de olá", "Olá Hellen Vermonde", ["C:\\Users\\Hellen Vermonde\\Documents\\documento.pdf"])