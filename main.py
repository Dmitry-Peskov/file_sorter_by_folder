import os

folders_and_extensions = {'Видео': ['mp4', 'mov', 'avi', 'mkv', 'wmv', '3gp', '3g2', 'mpg', 'mpeg', 'm4v', 'h264', 'flv', 'rm', 'swf', 'vob'],
               'Фото': ['jpg', 'png', 'bmp', 'ai', 'psd', 'ico', 'jpeg', 'ps', 'svg', 'tif', 'tiff', 'gif'],
               'Аудио': ['mp3', 'wav', 'ogg', 'flac', 'aif', 'mid', 'midi', 'mpa', 'wma', 'wpl', 'cda'],
               'Документы': ['pdf', 'txt', 'doc', 'docx', 'rtf', 'tex', 'wpd', 'odt', 'xlsx', 'xls', 'xlsm', 'ods', 'pptx', 'ppt', 'pps', 'key', 'odp'],
               'Архивы': ['zip', 'rar', '7z', 'z', 'gz', 'rpm', 'arj', 'pkg', 'deb']
               }
current_directory = os.getcwd()

def create_folders(path: str, folders_name: dict) -> None:
    '''Создаёт папки, в которые будут сортироваться файлы'''
    for folder in folders_name.keys():
        if not os.path.exists(fr'{path}\{folder}'):
            os.mkdir(fr'{path}\{folder}')

def create_paths(path: str, folders_name: dict) -> dict:
    '''Создаём пути к папкам, в которые будут сортироваться файлы'''
    path_list = dict()
    for folder in folders_name.keys():
        path_list[folder] = fr'{path}\{folder}'
    return path_list


def main():
    #create_folders(current_directory, folders_and_extensions)
    #create_paths(current_directory, folders_and_extensions))
    pass

if __name__ == "__main__":
    main()