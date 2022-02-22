# About

**NOTE**: If you are using Mac with M1 chip, you cannot use autogluon - because autogluon does not support M1 yet!! - you have to use `requirements-m1.txt` to install packages, which does not include autogluon - you can run the autogluon tutorial using Kaggle link below instead.

This repo contains the code for my minimalist end-to-end machine learning tutorial.

- `mini-ml.ipynb`: basic full pipeline with EDA, preprocessing, model tuning/evaluation/selection/persistence
- `titanic-streamlit-app.py`: machine learning web app via Streamlit
- `rapidminer`: no-code version using Rapidminer
- `mini-ml-automl.ipynb`: AutoEDA and AutoML (AutoGluon)
- `mini-ml-clearml.ipynb` and `pytorch_mnist_clearml.py`: MLOps (ClearML)

## Local Setup

Python 3 required, see my tutorial to setup Python 3: https://bit.ly/2uX6wAX

Clone the repo, go to the repo folder in Terminal, setup the virtual environment and install the required packages as follows:

```shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run `jupyter lab` or `code .` (if use VSCode) to go over the notebooks.

## Kaggle Notebooks

You can also directly run notebooks using Kaggle: 
- `mini-ml.ipynb`: [https://www.kaggle.com/harrywang/minimalist-machine-learning-tutorial](https://www.kaggle.com/harrywang/minimalist-machine-learning-tutorial)
- `mini-ml-automl.ipynb`: [https://www.kaggle.com/harrywang/autoeda-and-automl](https://www.kaggle.com/harrywang/autoeda-and-automl)

## Machine Learning Web App

Steps to get the streamlit app running (make sure to use the Terminal and the virtual environment is activated):

1. Get the data and model files ready
2. Create a notebook to do analysis and prediction
3. Create an app python file based on the notebook, such as `titanic-streamlit-app.py`
4. Run the app locally (Local URL: http://localhost:8501) using terminal: `streamlit run titanic-streamlit-app.py` 
5. Stop the app by using ctrl + C or closing the terminal
6. Deploy the app to the cloud for public access via services such as streamlit share, heroku, aws by following my tutorial at https://github.com/harrywang/streamlit-basics. you can see an example at: https://st-demo-harrywang.herokuapp.com/
