import cloudinary
import os

from dotenv import load_dotenv

load_dotenv()

def config_storage():
  cloudinary.config( 
    cloud_name = os.environ.get('CLD_CLOUD_NAME'), 
    api_key = os.environ.get('CLD_API_KEY'), 
    api_secret = os.environ.get('CLD_API_SECRET'),
    secure = True
  )