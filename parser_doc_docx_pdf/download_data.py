import gdown
import zipfile

def download():

    url = 'https://drive.google.com/file/d/1_E3GLMkbboLZcUPVfQHw99RWU11znbAq/view?usp=share_link'
    file_name = 'data'
    gdown.download(url, file_name, fuzzy=True)

    with zipfile.ZipFile('data', 'r') as zip_ref:
        print('unzip')
        zip_ref.extractall('data_dir')
    print('done')