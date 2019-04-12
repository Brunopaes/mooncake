## TreeShrews - ANN Python modules

Bachelor's final project.

This project is optimised for python 3+

This is an python's future-library for Artificial Neural Networks. This project is aimed on the development and maintenance of an ANN for classification problems. In the final article a classification scenario will be choosen and a benchmark with Keras/Tensorflow will be made.

----------------------------------

### Dependencies

For developers, python requirements could be find in the project's root. For installing the requirements, 
in your ___venv___ or ___anaconda env___, just run the following command:

`pip install -r requirements.txt`

----------------

### Installation

For users, this module could be installed by `pip + git`:

`pip install git+https://github.com/Brunopaes/treeshrews.git`

or, if for some reason the installation fails, downloads this repository and, inside the project's root, run the following command:

`python setup.py install`

----------------

### Project's Structure

```bash 
.
└── treeshrews
    ├── docs
    │   ├── final_article.pdf
    │   ├── reference_articles
    │   ├── ...
    │   └── iris.csv
    ├── treeshrews
    │   ├── __init__.py
    │   └── ANNFitting.py
    ├── tests
    │   └── unittests
    │       ├── data
    │       └── __init__.py
    ├── README.md
    ├── requirements.txt
    └── setup.py
```

-----------------------

### References

- __Activation Functions:__ [link](https://en.wikipedia.org/wiki/Activation_function);

- __ANN in java:__ [Sorting_Hat](https://github.com/Brunopaes/Sorting_Hat)

- __Benchmark's article:__ [Expertise areas](http://www2.espm.br/sites/default/files/pagina/artigo_7o_semic_reformulado_bruno_henrique_paes_8-10-18.pdf)

- __Project's name inspiration:__ [Tree-Shrews](https://www.theawl.com/2014/10/interpreting-the-animal-choices-on-the-worlds-most-popular-programming-books/);

--------------
