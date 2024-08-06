#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:                                  
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir
from typing import Dict, List


# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this
    # function
    # Creates list of files in directory
    filenames = listdir(image_dir)
    results_dic = dict()

    for filename in filenames:
        # If filename start with "." skips
        if filename.startswith('.'):
            continue
        # Split the filename to get the label
        label_parts = filename.lower().split('_')
        # Initialize an empty list to hold the alphabetic parts
        pet_label_parts = []
        # Loop through each part and filter out non-alphabetic parts
        for part in pet_label_parts:
            if part.isalpha():
                label_parts.append(part)
        # Join the filtered parts with a space
        pet_label = ' '.join(label_parts)
        # If filename doesn't already exist in dictionary, add filename and label to result dictionary
        if filename not in results_dic:
            results_dic[filename] = [pet_label]
        else:
            # Print an error message if duplicate files exist
            print("** Warning: Duplicate files exist in directory:", filename)
    return results_dic
