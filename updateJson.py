import json
from file import check_folder_structure
import sys
sys.path.append(".")
from initialize_config import initialize_config
from updateJson import *

def updateConfig(dirName):
    
    with open("config/kinect_config.json", "r") as json_file:
        config = json.load(json_file)
        initialize_config(config)
        
        tmp = config["path_dataset"]
        config["path_dataset"] = dirName

        check_folder_structure(config["path_dataset"])

    assert config is not None

    with open("config/kinect_config.json", "w+") as json_file:
        json_file.write(json.dumps(config))

