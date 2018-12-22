# Thermal-AI

## Project Description
 
Detection of Mental Health diseases with accuracy by means of generating a body heat map of the patient with the help of a thermal camera and applying techniques of image processing and Deep Learning image classification models to measure the magnitude of the detected disease

## Dataset !!

* [Dataset](http://vcipl-okstate.org/pbvs/bench/Data/04/download.html)
* [Sample Dataset](http://vcipl-okstate.org/pbvs/bench/Data/04/face01.zip) 

### Training & Testing

How to train:
Place your own thermal dataset in training_data and testing_data folders,

```sh

   $ cd tutorial-2-image-classifier

   $ python train.py
   ```

## Install

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

[Sai Adarsh](https://github.com/sai-adarsh)
[Rajasekar](https://github.com/rajasekar1999)
[Sibi Bose](https://www.linkedin.com/in/sibi-bose-8683b6150/)

[<img src="https://image.flaticon.com/icons/svg/185/185961.svg" width="35" padding="10">](https://twitter.com/dialstudios)
[<img src="https://image.flaticon.com/icons/svg/185/185964.svg" width="35" padding="10">](linkedin.com/in/sai-adarsh/)
[<img src="https://image.flaticon.com/icons/svg/185/185981.svg" width="35" padding="10">](https://www.facebook.com/saiadarsh99)
[<img src="https://image.flaticon.com/icons/svg/185/185985.svg" width="35" padding="10">](https://www.instagram.com/adarsh_theories/)

<p align="center"> Made with ❤ by <a href="https://github.com/sai-adarsh">Sai Adarsh</a></p>


### Research sources

[Paper 1](https://www.semanticscholar.org/paper/Facial-Thermal-Image-Analysis-for-Stress-Detection-Hong-Liu/2e8ccf7156629bcf14d43b946397eb04a14b9d78)
