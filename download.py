from huggingface_hub import hf_hub_download
from dotenv import load_dotenv
from subprocess import call
import os
load_dotenv()

def install_model(model_id, typ):
    # call(["git", "lfs", "install"])
    return call(["git", "-C", f"models/{typ}/", "lfs", "clone", f"git@hf.co:{model_id}"])

def create_dirs():
    if not os.path.exists('models'):
        os.makedirs('models')
    if not os.path.exists('models/t2t'):
        os.makedirs('models/t2t')
    if not os.path.exists('models/tg'):
        os.makedirs('models/tg')


if __name__ == '__main__':
    # model_id='roneneldan/TinyStories-1M'
    # install_model(model_id)
    create_dirs()