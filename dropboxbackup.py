import dropbox
class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
    
    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)

        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token='vtT-bnWoOxsAAAAAAAAAAeylP6JfSLuEaAjGkmJ_FVmMENMzR09lwo7OWzBCiUJ7'
    transferdata=TransferData(access_token)

    file_from=input("enter a file path to transfer.")
    # to give path for dropbox give  /foldername/filename
    file_to=input("Enter the full apth to upload the file to the dropbox")

    transferdata.upload_file(file_from,file_to)
    print("file has been moved")

main()

