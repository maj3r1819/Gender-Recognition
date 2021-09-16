# Gender Recognition App
This is a Desktop App I developed that identifies the gender of a person (Male or Female only) after clicking a picture. 
* For the gender recognition part I have trained a **Convolutional Neural Network (CNN)** that classifies an image either as a male or female.
* The App is developed using the **QT** framework which is a library that is flexible with different programming languages. 

## Gender Recognition Part
###  Convolutional Neural Network
I preferred to use this neural network since it works best with classification of image problems. Since I only had to classify two things, CNN was the best choice.
* **train_model.ipynb**  is the notebook in which I have trained the model. Going through its architecture will be helpful if anyone wants to go deeper in this network
* If someone wants to directly use my model I would suggest directly use '**gender_detector.data-000000-of-000001**', '**gender_detector.meta** ',**gender_detector.index** files. Just download and load these files separately. 
* If you have trouble loading the data files on your own please check out '**eye.ipynb**' where I have loaded the models for a separate task. 

### Eye Extraction 
To extract only eyes from the entire image, I have used **haarcascade_eye.xml**  from [anaustinbeing/haar-cascade-files: A complete collection of Haar-Cascade files. Every Haar-Cascades here! (github.com)](https://github.com/anaustinbeing/haar-cascade-files) repository. 
Please go through the **eye.ipynb** notebook first, where I can given a plain image as an input. Then
* The program first loads the data files of the trained model.
* Then, we extract only the eyes from the entire image.
* This image is then fed to the neural network and the output is predicted.
 
I have used this format in the App deployment.
