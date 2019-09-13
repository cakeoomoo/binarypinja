binarypinja
==============================

This project is to make dataset for sevearal machine learnning program and model of the natural processng language.


HOW TO INSTALL:

$ pip3 install -e .  
$ pip3 install -r requirements.txt  


HOW TO USE:
$ pinja [input-directory]
$ pinja --help


Project Organization
------------

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    └── pinja              <- Source code for use in this project.
        ├── __init__.py    <- Makes src a Python module
        │
        ├── data           <- Scripts to download or generate data
        │   └── make_dataset.py
        │
        ├── features       <- Scripts to turn raw data into features for modeling
        │   └── build_features.py
        │
        ├── models         <- Scripts to train models and then use trained models to make
        │   │                 predictions
        │   ├── predict_model.py
        │   └── train_model.py
        │
        └── visualization  <- Scripts to create exploratory and results oriented visualizations
            └── visualize.py

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
