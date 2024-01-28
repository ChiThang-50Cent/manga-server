import os
import cloudinary
import cloudinary.uploader
import cloudinary.api

from cloud_storage.config import config_storage
from .models import Manga, Chapter
from user.models import CustomUser

config_storage()

def gen_cloudinary_path(model):

    if isinstance(model, Chapter):
        manga = model.manga.id
        uploader = model.manga.owner.id
        return f'{uploader}/{manga}/{model.id}'
    
    if isinstance(model, Manga):
        uploader = model.owner.id
        return f'{uploader}/{model.id}'
    
    if isinstance(model, CustomUser):
        return f'{model.id}'

def get_all_page_from_chapter(chapter : Chapter):
    num_of_page = chapter.num_of_page
    
    public_ID = gen_cloudinary_path(chapter)
    list_of_url = []

    for i in range(num_of_page):
        url = cloudinary.utils.cloudinary_url(f'{public_ID}/{i}')
        list_of_url.append(url[0])

    return list_of_url

def upload_chapter_from_local(chapter : Chapter):
    path_to_img = os.path.dirname(__file__) + '\\temp'
    list_of_page = sorted(os.listdir(path_to_img))
    
    public_ID = gen_cloudinary_path(chapter)

    try:
        for i in range(len(list_of_page)):
            cloudinary.uploader.upload(f'{path_to_img}/{list_of_page[i]}',
                                    public_id=f'{public_ID}/{i}')
    except:

        return {"mess" : "Sth not right"}
    
    return {"mess" : "Done"}
