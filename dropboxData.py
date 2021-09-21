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
    access_token = 'Jlm2XGiyQukAAAAAAAAAAae58vBq3-2R21Eo35NYY1ksUJ4M7Qt0n-fiXyEbmNjJ'
    transferData = TransferData(access_token)
    file_from = '/Users/madhupaluru/Desktop/WhiteHatjr/text.txt'
    file_to = '/Applications/WhiteHatDropbox/test.txt'

    transferData.upload_file(file_from, file_to)
    print("File has been moved")
main()