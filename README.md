# About

This repo contains the code for my minimalist end-to-end data science project tutorial.

## Local Setup

Python 3 required, see my tutorial to setup Python 3: https://bit.ly/2uX6wAX

Clone the repo, go to the repo folder, setup the virtual environment, and install the required packages:


```shell
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Run `$ jupyter lab` to go over the notebooks.

## Google Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1hh7X2ycEcOmuX5LhsB2ZdpM2N5RQRx06)

Note that I use OpenML to get the dataset (the dataset is slightly different from the Kaggle version) so that there won't be separate data files to handle. 

## Data Science App

Steps to get the streamlit app running (make sure to use the Terminal and the virtual environment is activated):

1. Get the data and model files ready
2. Create a notebook to do analysis and prediction
3. Create an app python file based on the notebook, such as `titanic-streamlit-app.py`
4. Run the app locally (Local URL: http://localhost:8501) using terminal: `streamlit run titanic-streamlit-app.py` 
5. Stop the app by using ctrl + C or closing the terminal
6. Deploy the app to the cloud for public access via services such as streamlit share, heroku, aws by following my tutorial at https://github.com/harrywang/streamlit-basics. you can see an example at: https://st-demo-harrywang.herokuapp.com/
