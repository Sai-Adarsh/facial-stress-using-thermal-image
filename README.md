## Facial Stress Detection using Thermal Imaging

### Project Description
* Accurate detection of mental health diseases is achieved by generating a body heat map of the patient using a thermal camera and applying techniques of image processing and Deep Learning image classification models to measure the disease's magnitude.
* Working photos/videos [here](https://github.com/Sai-Adarsh/ThermalAI/tree/master/WorkingPhotos)
* Know more about Problem & Solution [here](https://github.com/Sai-Adarsh/ThermalAI/blob/master/Phase1/Team%20Appendly%20-%20Shaastra%20AI%20Challenge%202018%20Phase%20I%20Ideation.pdf)

### Dataset
* [Dataset - Visual Computing and Image Processing Lab 
Oklahoma State University](http://vcipl-okstate.org/pbvs/bench/Data/04/download.html)
* [Sample Dataset - Visual Computing and Image Processing Lab 
Oklahoma State University](http://vcipl-okstate.org/pbvs/bench/Data/04/face01.zip) 

## Getting Started

### Run:  
 ```bash
 $ git clone https://github.com/Sai-Adarsh/facial-stress-using-thermal-image.git
 
 $ cd facial-stress-using-thermal-image
 
 $ pip install -r requirements.txt
 ```
### Open and replace the project path with the respective path inside the below mentioned files:
 ```bash
 project\thermalai\predictor\predict.py

 tutorial-2-image-classifier\predict.py

 tutorial-2-image-classifier\train.py
 ```

### Activate virtualenv
 ```bash
 # Linux
 $ source ./venv/bin/activate
 
 # Windows
 $ cd venv/Scripts/
 
 $ activate
 ```
### Train/Test
Place your thermal dataset in the training_data and testing_data folders.

 ```bash
 $ cd tutorial-2-image-classifier

 $ python train.py
 ```

### Predict
 ```bash
 $ cd tutorial-2-image-classifier
 
 $ python predict.py sample.jpg (any extension works)
 ```
### Run web app:
 ```bash
 $ cd project\thermalai
 
 $ python manage.py runserver
 ```   
### Run through Raspberry Pi (with a camera):
 Open a new CMD terminal (Ensure that Raspbian OS is installed on the Raspberry Pi).
 ```bash
 $ cd project\thermalai\thermalai
 
 # Add the desired host and its ports to the ALLOWED_HOSTS section of settings.py
 $ cd project\thermalai
 
 $ python manage.py runserver
 
 $ cd RaspberryPi
 
 # Windows
 $ runthisstress.sh
 
 # Linux
 $ ./runthisstress.sh
 ```
### References
* [Facial Thermal Image Analysis for Stress Detection](https://www.semanticscholar.org/paper/Facial-Thermal-Image-Analysis-for-Stress-Detection-Hong-Liu/2e8ccf7156629bcf14d43b946397eb04a14b9d78)
* [Stress as a Mediator of Socioeconomic Disparities in Health: The Role of Race](http://www.pnas.org/content/pnas/suppl/2013/12/26/1321664111.DCSupplemental/pnas.201321664SI.pdf)
* [Indians Suffer from Stress and Depression](https://www.businesstoday.in/lifestyle/off-track/indians-suffer-from-stress-depression/story/280119.html)
* [89% of India's Population Suffers from Stress; Most Don't Feel Comfortable Talking to Medical Professionals](https://economictimes.indiatimes.com/magazines/panache/89-per-cent-of-indias-population-suffering-from-stress-most-dont-feel-comfortable-talking-to-medical-professionals/articleshow/64926633.cms)
* [Mental Health Statistics - Stress](https://www.mentalhealth.org.uk/statistics/mental-health-statistics-stress)
* [ncbi.nlm.nih.gov](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3968009/)
* [journals.plos.org](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0090782)
* [Modeling Stress Using Thermal Facial Patterns: A Spatio-Temporal Approach](https://www.researchgate.net/publication/261206963_Modeling_Stress_Using_Thermal_Facial_Patterns_A_Spatio-Temporal_Approach)
