# AIPND-revision
This repository contains _REVISED_ code and associated files for the AI Programming with Python Nanodegree program. This repository consists of a number of tutorial notebooks for various coding exercises and programming labs that will be used to supplement the lessons of the course.

## Table Of Contents

### Tutorial Notebooks
* No revisions

### Programming Project
* [Intro to Python Project - Classifying Pet Images:](https://github.com/udacity/AIPND-revision/tree/master/intropyproject-classify-pet-images "Classifying Pet Images Project") Determine which CNN architecture model works best at classifying images of dogs and their breeds.

### NumPy and Pandas Mini-Projects
* No revisions 

### Matplotlib
* No revisions 

### Quiz Notes
* [Notes:](https://github.com/udacity/AIPND-revision/tree/master/notes "Notes") This directory contains more information about certain quizzes that are testing more challenging concepts. Additionally, one will find the [Frequently Asked Questions](https://github.com/udacity/AIPND-revision/blob/master/notes/project_intro-to-python.md) for the _Intro to Python Project_. Click on the filename to view the contents of the notes on a _quiz_ or the _Intro to Python Project_.

## Dependencies

Each directory has a `requirements.txt` describing the minimal dependencies required to run the notebooks in that directory.

### pip

To install these dependencies with pip, you can issue `pip3 install -r requirements.txt`.

# AI-Programming-Python_P1_ImageClassifierDogBreed
This repo contains the summary of the project description and instruction. 

### Project Instructions

##### Goal:
Use Python to apply an existing image classifier to identify dog breeds and ensure only dogs are registered for the show.

##### Project Overview:

Task: Help register participants by classifying submitted images to confirm they depict dogs.
Challenge: Some participants may submit images of non-dogs. Use the provided classifier to filter them out.
Classifier: You'll use pre-trained deep learning models (AlexNet, VGG, ResNet) that identify objects in images.

##### Your Tasks:

Test the three classifiers to determine:
Which one best identifies images as "dogs" or "not dogs."
Which one most accurately identifies a dog's breed.
Measure the runtime of each classifier. (Trade-off: Higher accuracy may mean slower performance.)
Select the best classifier based on accuracy and runtime.

##### Key Notes:
The provided classifier function leverages CNNs trained on the ImageNet dataset. CNNs excel at detecting image features (e.g., textures, edges).
Some dog breeds look very similar, e.g., Great Pyrenees vs. Kuvasz, German Shepherd vs. Malinois, etc. Accuracy may vary depending on the classifier's training data.
Focus on Python skills to use the classifier effectively, not on creating the classifier itself.
Deliverables:
Determine the best classifier for accuracy and speed, ensuring it works well for identifying dogs and their breeds.

##### Principal Objectives
Correctly identify which pet images are of dogs (even if the breed is misclassified) and which pet images aren't of dogs.  
Correctly classify the breed of dog, for the images that are of dogs.  
Determine which CNN model architecture (ResNet, AlexNet, or VGG), "best" achieve objectives 1 and 2.  
Consider the time resources required to best achieve objectives 1 and 2, and determine if an alternative solution would have given a "good enough" result, given the amount of time each of the algorithms takes to run.

#####  Program Outline
- Time your program (Page 5 & 6)
- Use Time Module to compute program runtime
- Get program Inputs from the user (Page 7 & 8)
- Use command line arguments to get user inputs
- Create Pet Images Labels (Page 9, 10 & 11)
- Use the pet images filenames to create labels
- Store the pet image labels in a data structure (e.g. dictionary)
- Create Classifier Labels and Compare Labels (Page 12 & 13)
- Use the Classifier function to classify the images and create the classifier labels
- Compare Classifier Labels to Pet Image Labels
- Store Pet Labels, Classifier Labels, and their comparison in a complex data structure (e.g. dictionary of lists)
- Classifying Labels as "Dogs" or "Not Dogs" (Page 14 & 15)
- Classify all Labels as "Dogs" or "Not Dogs" using dognames.txt file
- Store new classifications in the complex data structure (e.g. dictionary of lists)
- Calculate the Results (Page 16 & 17)
- Use Labels and their classifications to determine how well the algorithm worked on classifying images
- Print the Results (Page 18 & 19)
- You will need to repeat these tasks for each of the three image classification algorithms that are provided to you.

