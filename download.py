from huggingface_hub import hf_hub_download
from dotenv import load_dotenv
from subprocess import call
load_dotenv()

def install_model(model_id):
    # call(["git", "lfs", "install"])
    return call(["git", "-C", "models/", "lfs", "clone", f"git@hf.co:{model_id}"])

if __name__ == '__main__':
    model_id='google/flan-t5-small'
    install_model(model_id)