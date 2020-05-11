# Open3D: www.open3d.org
# The MIT License (MIT)
# See license file or visit www.open3d.org for details

# examples/Python/ReconstructionSystem/run_system.py


import time, datetime
import sys
from file import check_folder_structure
sys.path.append(".")
from initialize_config import initialize_config
from updateJson import *

def main_register_capture(dirName):
    '''
    # need to tweak config file 
    with open("config/kinect_config.json", "r") as json_file:
        config = json.load(json_file)
        initialize_config(config)
        check_folder_structure(config["path_dataset"])

    assert config is not None

    tmp = config["path_dataset"] 
    config["path_dataset"] = dirName
    '''
    updateConfig(dirName)


    # save changes to file
    #with open("config/kinect_config.json", "w+") as json_file:
    #    json_file.write(json.dumps(config))

    with open("config/kinect_config.json", "r") as json_file:
        config = json.load(json_file)

    # will change 
    config['debug_mode'] = False

    print("Updated .json with {}".format(config["path_dataset"]))

    print("====================================")
    print("Configuration")
    print("====================================")

    times = [0, 0, 0, 0]

    print('\nMAKING FRAGMENTS')
    start_time = time.time()
    import make_fragments
    make_fragments.run(config)
    times[0] = time.time() - start_time
    print('MADE FRAGMENTS')

    print('\nREGISTERING FRAGMENTS')
    start_time = time.time()
    import register_fragments
    register_fragments.run(config)
    times[1] = time.time() - start_time
    print('REGISTERED FRAGMENTS')

    print('\nREFINING REGISTRATION')
    start_time = time.time()
    import refine_registration
    refine_registration.run(config)
    times[2] = time.time() - start_time
    print('REFINED REGISTRATION')

    print('\nINTEGRATING SCENE')
    start_time = time.time()
    import integrate_scene
    integrate_scene.run(config)
    times[3] = time.time() - start_time
    print('INTEGRATED SCENE')

    print("====================================")
    print("Elapsed time (in h:m:s)")
    print("====================================")
    print("- Making fragments    |\t%s" % datetime.timedelta(seconds=times[0]))
    print("- Register fragments  |\t%s" % datetime.timedelta(seconds=times[1]))
    print("- Refine registration |\t%s" % datetime.timedelta(seconds=times[2]))
    print("- Integrate frames    |\t%s" % datetime.timedelta(seconds=times[3]))
    print("-\n- Total               |\t%s" % datetime.timedelta(seconds=sum(times)))
    sys.stdout.flush()
