# Gender Recognition App
This is a Desktop App I developed that identifies the gender of a person (Male or Female only) after clicking a picture. 
* For the gender recognition part I have trained a **Convolutional Neural Network (CNN)** that classifies an image either as a male or female.
* The App is developed using the **QT** framework which is a library that is flexible with different programming languages. 

##  Convolutional Neural Network
I preferred to use this neural network since it works best with classification of image problems. Since I only had to classify two things, CNN was the best choice.
* **train_model.ipynb**  is the notebook in which I have trained the model. Going through its architecture will be helpful if anyone wants to go deeper in this network
* If someone wants to directly use my model I would suggest directly use '**gender_detector.data-000000-of-000001**', '**gender_detector.meta** ',**gender_detector.index** files. Just download and load these files separately. 
* If you have trouble loading the data files on your own please check out '**eye.ipynb**' where I have loaded the models for a separate task. 
 

