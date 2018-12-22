# Thermal-AI

## Project Description
 
Detection of Mental Health diseases with accuracy by means of generating a body heat map of the patient with the help of a thermal camera and applying techniques of image processing and Deep Learning image classification models to measure the magnitude of the detected disease

For working photos and videos [click here](https://github.com/Sai-Adarsh/ThermalAI/tree/master/WorkingPhotos)

![Architecture](https://github.com/Sai-Adarsh/ThermalAI/blob/master/Architecture%20.jpg)

## Dataset !!

* [Dataset](http://vcipl-okstate.org/pbvs/bench/Data/04/download.html)
* [Sample Dataset](http://vcipl-okstate.org/pbvs/bench/Data/04/face01.zip) 

## Primay TechStacks

![TechStacks](https://github.com/Sai-Adarsh/ThermalAI/blob/master/Tech%20Stacks.jpg)
## Install

### Training & Testing

How to train:
Place your own thermal dataset in training_data and testing_data folders,

```sh

   $ cd tutorial-2-image-classifier

   $ python train.py
   ```

### How to run:  

```sh
   $ git clone https://github.com/sai-adarsh/ThermalAI.git

   $ cd ThermalAI

   $ pip install -r requirements.txt
   ```
### After installing all requirements, to run in cmd:
   ```sh
   $ cd tutorial-2-image-classifier

   $ python predict.py <imageInputFileName.extension>
   ```

### To run the WebApp:
   ```sh
   $ cd project\thermalai

   $ python manage.py runserver
   ```   

### To run through RaspberryPi (with cam):
   Open a new cmd terminal(Make sure Raspbian OS is installed in RaspberryPi
   ```sh
   $ cd project\thermalai\thermalai
   ```
   Add desired host and it's ports in **ALLOWED_HOSTS** of **settings.py**
   ```sh
   $ cd project\thermalai
   ```
   ```sh
   $ python manage.py runserver
   ```
   ```sh
   $ cd RaspberryPi
   ```
   For Windows
   ```sh
   $ runthisstress.sh
   ```
   For Linux
   ```sh
   $ ./runthisstress.sh
   ```

### Author

[Sai Adarsh](https://github.com/sai-adarsh),
[Rajasekar](https://github.com/rajasekar1999),
[Sibi Bose](https://www.linkedin.com/in/sibi-bose-8683b6150/).

[<img src="https://image.flaticon.com/icons/svg/185/185961.svg" width="35" padding="10">](https://twitter.com/dialstudios)
[<img src="https://image.flaticon.com/icons/svg/185/185964.svg" width="35" padding="10">](linkedin.com/in/sai-adarsh/)
[<img src="https://image.flaticon.com/icons/svg/185/185981.svg" width="35" padding="10">](https://www.facebook.com/saiadarsh99)
[<img src="https://image.flaticon.com/icons/svg/185/185985.svg" width="35" padding="10">](https://www.instagram.com/adarsh_theories/)

<p align="center"> Made with ❤ by <a href="https://github.com/sai-adarsh">Sai Adarsh</a></p>


### Research papers & sources

[Paper 1](https://www.semanticscholar.org/paper/Facial-Thermal-Image-Analysis-for-Stress-Detection-Hong-Liu/2e8ccf7156629bcf14d43b946397eb04a14b9d78)
[Paper 2](http://www.pnas.org/content/pnas/suppl/2013/12/26/1321664111.DCSupplemental/pnas.201321664SI.pdf)
[Source 1](https://www.businesstoday.in/lifestyle/off-track/indians-suffer-from-stress-depression/story/280119.html)
[Source 2](https://economictimes.indiatimes.com/magazines/panache/89-per-cent-of-indias-population-suffering-from-stress-most-dont-feel-comfortable-talking-to-medical-professionals/articleshow/64926633.cms)
[Source 3](https://www.mentalhealth.org.uk/statistics/mental-health-statistics-stress)
[Paper 4](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3968009/)
[Paper 5](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0090782)
[Paper 6](https://www.researchgate.net/publication/261206963_Modeling_Stress_Using_Thermal_Facial_Patterns_A_Spatio-Temporal_Approach)

