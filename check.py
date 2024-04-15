from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from pydrive.auth import ServiceAccountCredentials

def list_files(service_account_json_path):
    gauth = GoogleAuth()
    scope = ['https://www.googleapis.com/auth/drive']
    gauth.credentials = ServiceAccountCredentials.from_json_keyfile_name('service_account.json', scope)
    drive = GoogleDrive(gauth)
    
    # List all files in the Drive
    file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    
    # Print details of each file
    for file in file_list:
        print('Title: {}, ID: {}'.format(file['title'], file['id']))

# Path to your service account JSON key file
service_account_json_path = 'service_account.json'

list_files(service_account_json_path)
