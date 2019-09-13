binarypinja
==============================

[![status](https://img.shields.io/badge/test-v0.0.1-ff7964.svg?style=for-the-badge)](https://github.com/cakeoomoo/binarypinja/blob/master/LICENSE)

[![GitHub license](https://img.shields.io/github/license/cakeoomoo/binarypinja)](https://github.com/cakeoomoo/binarypinja/blob/master/LICENSE)

[![GitHub stars](https://img.shields.io/github/stars/cakeoomoo/binarypinja)](https://github.com/cakeoomoo/binarypinja/stargazers)


This project is to make dataset for sevearal machine learnning program and model of the natural processng language.


HOW TO INSTALL:

```
pip3 install -r requirements.txt  
pip3 install -e .  
```


HOW TO USE:

```
pinja [input-directory]
pinja --help
```


![pinjaTree](http://github.com/cakeoomoo/binarypinja/image.jpg "pinja tree")



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
        ├── main.py        <- Scripts to download or generate data
        │
        ├── exec2asm.py    <- Scripts to turn raw data into features for modeling
        │
        └── visualization  <- Scripts to create exploratory and results oriented visualizations
            └── visualize.py

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
