# Mooncake: Improving predictors for fraudulent transactions

Bachelor's final project.

This project is optimised for python 3+

This Data Science-like project is aimed on analyzing a bunch of techniques for 
False Negatives (Frauds classified as Non-Frauds) in a extreme imbalanced 
dataset - Financial Fraud and improving the predictors performance.

----------------------------------

## Dependencies

For developers, python requirements could be find in the project's root. 
For installing the requirements, 
in your ___venv___ or ___anaconda env___, just run the following command:

`pip install -r requirements.txt`

----------------

## Project's Structure

```bash 
.
└── mooncake
    ├── data
    │   ├── entropy
    │   │   ├── tree_entropy_2020-03-04.png
    │   │   └── tree_entropy_2020-03-05.png
    │   ├── datasource.csv
    │   ├── validation-2020-02-27.csv
    │   └── validation-2020-03-24.csv
    ├── docs
    │   ├── confusion-matrix.xlsx
    │   ├── Ficha.pdf
    │   ├── PGT 04.17.docx
    │   ├── PGT 05.11.docx
    │   ├── PGT 05.23.docx
    │   ├── PGT 05.26.docx
    │   ├── PGT 05.28.docx
    │   ├── PGT 05.29.docx
    │   └── PGT 05.29.pdf
    ├── mooncake
    │   ├── __init__.py
    │   ├── helpers.py
    │   ├── models.py
    │   ├── plotting.ipynb
    │   ├── ros.py
    │   ├── smote.ipynb
    │   └── smote.py
    ├── tests
    │   └── unittests
    │       ├── __init__.py
    │       ├── ...
    │       └── test_helpers.py
    ├── .gitignore
    ├── LICENSE
    ├── README.md
    ├── requirements.txt
    └── setup.py
```

-----------------------

## References

- __Activation Functions:__ [link](https://en.wikipedia.org/wiki/Activation_function);

- __ANN in java:__ [Sorting_Hat](https://github.com/Brunopaes/Sorting_Hat)

- __Benchmark's article:__ [Expertise areas](http://bibliotecas.espm.br:8080/pergamumweb/vinculos/0000aa/0000aa9d.pdf)

- __Old Project's name inspiration:__ [Tree-Shrews](https://www.theawl.com/2014/10/interpreting-the-animal-choices-on-the-worlds-most-popular-programming-books/);

--------------
