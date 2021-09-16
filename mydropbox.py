import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token) 


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    '''
    test multiline comment
    test multiline comment
    '''
    access_token = '6jZbsXzWqwkAAAAAAAAAAcUUQ68_um2_n5PfPn0y-za9y4wWEFSMz8t_l3ncNejr'
    transferData = TransferData(access_token)

    #file_from = input("Enter the file path to transfer : -")
    #file_to = input("enter the full path to upload to dropbox:- ")  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    # API v2
    #transferData.upload_file(file_from, file_to)
    transferData.upload_file('test.txt', '/test1.txt')
    print("file has been moved !!!")

main()