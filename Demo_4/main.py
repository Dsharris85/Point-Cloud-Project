import os
import sys
import shutil

dirName = ''

if __name__ == "__main__":

    # For GUI: will get rid of all of this
    if (len(sys.argv) > 1):
        dirName = "dataset/" + sys.argv[1]
            
        if not os.path.exists(dirName):
            os.mkdir(dirName)
            os.makedirs(dirName + "/depth")
            os.makedirs(dirName + "/color")
            print("\nDirectory '{}' Created ".format(dirName))
        else:    
            print("\nDirectory '{}' already exists... ".format(dirName))
            yn = raw_input("\nOverwrite? (Y/N): ") 
            if(yn.lower() == "y"):
                shutil.rmtree(dirName)
                os.makedirs(dirName)
                os.makedirs(dirName + "/depth")
                os.makedirs(dirName + "/color")
            else:
                print("\n\nExiting...")
                exit()
    else:
        print("\nGive a new directory name... Exiting")
        exit() 

    print("dirName: {}".format(dirName))

    from capture_test import *
    #main_capture(dirName) # for GUI, need to make new directory, give path here

    from run_system import *
    main_register_capture(dirName) # GUI: give path to dir made, or option to register from chosen folder?
            
    from view import *
    main_view_cloud("{}/scene/integrated.ply".format(dirName)) # GUI: replace with a chosen .ply/.pcd file
    main_view_mesh("{}/scene/integrated.ply".format(dirName))  # GUI: replace with a chosen .ply/.pcd file
        
