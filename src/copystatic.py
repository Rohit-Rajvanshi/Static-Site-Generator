import os 
import shutil 



def copy_static(source , destination , working_directory="."):

    

    source_path = os.path.join(working_directory , source)
    destination_path = os.path.join(working_directory , destination)


    if not os.path.exists(destination_path):
        os.mkdir(destination_path)
    else:
        shutil.rmtree(destination_path)
        os.mkdir(destination_path)

    if not os.path.exists(source_path):
        raise Exception("Wrong path directory")


    def copy_static_recursion(source_path , destination_path):
        files_list = os.listdir(source_path)

        for file in files_list:

            file_path = os.path.join(source_path , file)
            if os.path.isfile(file_path):
                shutil.copy(file_path , destination_path)
            else:
                dir_path = os.path.join(destination_path , file)
                os.mkdir(dir_path)
                copy_static_recursion(file_path , dir_path)



    copy_static_recursion(source_path , destination_path)



    
    




    

    