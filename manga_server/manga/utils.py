import os
import patoolib
import cloudinary
import cloudinary.uploader
import cloudinary.api

# from cloud_storage.config import config_storage
from .models import Manga, Chapter

from pathlib import Path

# config_storage()

def gen_cloudinary_public_ID(chapter: Chapter):
    manga = chapter.manga.id
    uploader = chapter.manga.owner.id
    return f'{uploader}_{manga}_{chapter.id}'

def get_all_page_from_chapter(chapter : Chapter):
    num_of_page = chapter.num_of_page
    
    public_ID = gen_cloudinary_public_ID(chapter)
    list_of_url = []

    for i in range(num_of_page):
        url = cloudinary.utils.cloudinary_url(f'{public_ID}_{i}')
        list_of_url.append(url[0])

    return list_of_url

def upload_png_from_local(chapter : Chapter, folder_name):
    path_to_img = f'{str(Path(__file__).resolve().parent.parent)}\\{folder_name}'

    try:        
        list_of_page = sorted(os.listdir(path_to_img))    
        public_ID_pattern = gen_cloudinary_public_ID(chapter)

        for i in range(len(list_of_page)):
            cloudinary.uploader.upload(f'{path_to_img}/{list_of_page[i]}',
                                    public_id=f'{public_ID_pattern}_{i}')
    except Exception as ex:
        chapter.delete()
        cloudinary.api.delete_resources_by_prefix(f'{public_ID_pattern}')
        raise Exception(str(ex))
    
def get_and_save_upload_file(data):
    path = str(Path(__file__).resolve().parent.parent)

    data_file = data.read()
    file_name = data.name[:-4]
    extention = data.name[-4:]

    try:
        with open(f'{path}/{file_name}_temp{extention}', 'wb') as fi:
            fi.write(data_file)

        return f'{file_name}_temp', f'{path}/{file_name}_temp{extention}'
    
    except:
        raise Exception('Sth wrong when get upload file')
    
def extract_and_remove_compress_file(path):
    try:
        patoolib.extract_archive(path)
        os.remove(path)

    except Exception as ex:
        raise Exception(str(ex))
    
def remove_temp_folder(temp_name):
    path = str(Path(__file__).resolve().parent.parent)
    list_of_file = os.listdir(f'{path}\\{temp_name}')
    try:
        for file_ in list_of_file:
            os.remove(f'{path}\\{temp_name}\\{file_}')
        
        os.rmdir(f'{path}\\{temp_name}')

    except Exception as ex:
        raise Exception(str(ex))
