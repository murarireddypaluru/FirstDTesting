import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to, mode=WriteMode('overwrite'))
def main():
    # Read the Dropbox access token from an environment variable — never hard-code secrets.
    access_token = os.environ["DROPBOX_TOKEN"]
    transferData = TransferData(access_token)
    file_from = os.environ.get("SOURCE_FILE", "text.txt")
    file_to = os.environ.get("DEST_PATH", "/test.txt")

    transferData.upload_file(file_from, file_to)
    print("File has been moved")
main()