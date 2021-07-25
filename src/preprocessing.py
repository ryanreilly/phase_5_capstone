# --------------------------------------------------------------
# Define library for handling the preprocessing of data.
#
# Currently, only image dividing is implemented
#
# --------------------------------------------------------------

# Standard Library imports.
import warnings

# #For dividing the images into correct folders
import shutil


def image_divider(data, split_type):

    '''This function divides the images into 
        train, dev, and test folders to be used 
        for model building with Keras. The data 
        argument refers to the folder where all 
        the images are located. The split_type is 
        a string either train, dev, or test'''
    
    # Create a list of disaster types"
    disasters = ['fire', 'earthquake','flood','landslide', 'hurricane','other_disaster','not_disaster']
    #Loop through the list and create a new dataset that is labled by disaster type
    for name in disasters:
        new_dataset = data[data['class_label'] == name]
        #Create a destination for the new dataset using split_type and name  
        destination = split_type + '/' + name 
        #Loop thorugh the image path column and copy over the new data to the destination folder
        for source in new_dataset['image_path']:
            shutil.copy(source, destination)

    