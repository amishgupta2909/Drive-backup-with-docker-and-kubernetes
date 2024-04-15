from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from oauth2client.service_account import ServiceAccountCredentials
import os

def authenticate_with_service_account():
    gauth = GoogleAuth()
    scope = ['https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scope)
    gauth.credentials = credentials
    return GoogleDrive(gauth)

def upload_folder(drive, folder_path, parent_folder_id=None):
    folder_name = os.path.basename(folder_path)
    folder_metadata = {'title': folder_name, 'mimeType': 'application/vnd.google-apps.folder'}
    if parent_folder_id:
        folder_metadata['parents'] = [{'id': parent_folder_id}]
    folder = drive.CreateFile(folder_metadata)
    folder.Upload()
    
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            upload_folder(drive, item_path, folder['id'])
        else:
            file = drive.CreateFile({'title': item, 'parents': [{'id': folder['id']}]})
            file.SetContentFile(item_path)
            file.Upload()

drive = authenticate_with_service_account()

# upload_folder(drive, "C:\\Amish\\Books")
upload_folder(drive, "Books")
