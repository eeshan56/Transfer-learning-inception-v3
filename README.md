
# Transfer learning with Inception-V3

## Instructions for execution:

### 1) Install Python3.7

### 2) Install Python3.7-venv:

Linux:
```
sudo apt install python3.7-venv
python3.7 -m venv env # creates new environment
source env/bin/activate # activates the environment
```

Windows:

Refer to https://mothergeo-py.readthedocs.io/en/latest/development/how-to/venv-win.html

### 3) Install Packages:

```
pip install -r requirements.txt
```

## To use the model:
```
python app.py
```
## Dataset:

The dataset is of 10 types of animals: butterflies, cats, chickens, cows, dogs, elephants, horses, sheep, squirrels and spiders. The dataset can be downloaded from the following link: https://www.kaggle.com/alessiocorrado99/animals10

### Once downloaded, extract the dataset

For splitting the dataset into train, validation and test sets:
```
python DataSplit.py
```
