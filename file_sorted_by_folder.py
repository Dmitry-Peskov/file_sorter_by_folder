import os

folders_and_extensions = {'Видео': ['mp4', 'mov', 'avi', 'mkv', 'wmv', '3gp', '3g2', 'mpg', 'mpeg', 'm4v', 'h264', 'flv', 'rm', 'swf', 'vob'],
               'Фото': ['jpg', 'png', 'bmp', 'ai', 'psd', 'ico', 'jpeg', 'ps', 'svg', 'tif', 'tiff', 'gif'],
               'Аудио': ['mp3', 'wav', 'ogg', 'flac', 'aif', 'mid', 'midi', 'mpa', 'wma', 'wpl', 'cda'],
               'Документы': ['pdf', 'txt', 'doc', 'docx', 'rtf', 'tex', 'wpd', 'odt', 'xlsx', 'xls', 'xlsm', 'ods', 'pptx', 'ppt', 'pps', 'key', 'odp'],
               'Архивы': ['zip', 'rar', '7z', 'z', 'gz', 'rpm', 'arj', 'pkg', 'deb']
               }
current_directory = os.getcwd()

def create_folders(path: str, folders_name: dict) -> None:
    '''Создаём папки, в которые будут сортироваться файлы'''
    for folder in folders_name.keys():
        if not os.path.exists(fr'{path}\{folder}'):
            os.mkdir(fr'{path}\{folder}')
            print(f'Создана папка "{folder}"')

def get_paths_file(path:str) -> list:
    '''Собираем пути к файлам, которые будут отсортированны'''
    file_list = [file.path for file in os.scandir(path) if not file.is_dir()]
    return file_list

def sort_files(path: str):
    '''Производим сортировку файлов по ранее созданным папкам'''
    file_paths = get_paths_file(path)
    ext_list = list(folders_and_extensions.items())
    for file_path in file_paths:
        extension = file_path.split('.')[-1]
        file_name = file_path.split('\\')[-1]
        for dict_key_int in range(len(ext_list)):
            if extension in ext_list[dict_key_int][1]:
                os.rename(file_path, f'{current_directory}\\{ext_list[dict_key_int][0]}\\{file_name}')
                print(f'"{file_name}" скопирован в папку "{ext_list[dict_key_int][0]}"')

def delete_empty_folders(path: str):
    '''Удаляем пустые папки, находящиеся в корневом каталоге'''
    folders_dir = [folder.path for folder in os.scandir(path) if folder.is_dir()]
    for p in folders_dir:
        if len(os.listdir(p)) == 0:
            os.rmdir(p)
            print(f'Папка {p} удалена т.к. в ней отсутствовали файлы')

def main():
    create_folders(current_directory, folders_and_extensions)
    sort_files(current_directory)
    delete_empty_folders(current_directory)
    input('Сортировка окончена\nДля завершения нажмити "Enter"')

if __name__ == "__main__":
    main()
