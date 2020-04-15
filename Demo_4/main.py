import os
import sys
import shutil

dirName = ''

if __name__ == "__main__":
    if (len(sys.argv) > 1):
        dirName = sys.argv[1]
            
        if not os.path.exists(dirName):
            os.mkdir(dirName)
            print("\nDirectory '{}' Created ".format(dirName))
        else:    
            print("\nDirectory '{}' already exists... ".format(dirName))
            yn = raw_input("\nOverwrite? (Y/N): ") 
            if(yn.lower() == "y"):
                shutil.rmtree(dirName)
                os.makedirs(dirName)
            else:
                print("\n\nExiting...")
                exit()
    else:
        print("\nGive a new directory name... Exiting")
        exit() 

    # delay imports
    from capture import *
    from clean import *

    print("dName: {}".format(dirName))

    main_capture(dirName)
    main_clean(dirName)
