import dropbox


class Tranfer:
    def __init__(self,acessToken):
       self.acessToken=acessToken
    def uploadFile(self,fileFrom,fileTo):
        dbx=dropbox.Dropbox(self.acessToken)
        f=open(fileFrom,'rb')
        dbx.files_upload(f.read(),fileTo)

    
def main():
    acessToken='LCmSViI6eP4AAAAAAAAAAdYviwwZUxA2WM72JWeXFN-oxHj0tlrYtPtiJCeo2ntA'


    TransferData=Tranfer(acessToken)

    fileFrom=input("Enter your file path")

    fileTo=input("Enter destination path")

    TransferData.uploadFile(fileFrom,fileTo)
    
    print("Your file is transferred")


main()


