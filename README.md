# Setup

This code was developed and run on Ubuntu 18.04 using Chrome 73. Basic
instructions for setup are included below. The code is not designed for
resilience in the face of changing browsers, websites, or operating
systems so it is likely that some additional work will be needed when
trying to get things going. Feel free to reach out to me for any help.

## Basic setup instructions

First set up a virtual environment in the top level of this repo and
source it

```
$ virutalenv venv
```
```
$ source venv/bin/activate
```

Next, pip install the requirements.txt

```
$ pip3 install -r requirements.txt
```

Now install a notebook kernel that will use this virtual environment

```
$ python -m ipykernel install --user --name=venv
```

Run the jupyter notebook server, and to use these notebooks select the
kernel named `venv` (or whatever you chose as a name).

## WebDriver

The webdriver we used with selenium is included in this repo under the
`deps` directory. It is compatible with Google Chrome versions 70-73.
Other versions of chromedrivers can be [downloaded here](https://chromedriver.chromium.org/downloads).

# Use

There are two notebooks here. One is used to retrieve and save raw
webpages. The other parses those webpages into data structures and
interacts with the genderize.io API. The notebooks are commented
and with a little inference I hope they are able to explain themselves.
Both notebooks should be able to execute top to bottom, no jumping
around is needed. However, be aware that they reach out to external
sites and can be resource intensive.

# Acknowledgments

The file `gender.py` is copied from [github.com/block8432/gender.py](https://github.com/block8437/gender.py)

# Citation

Please cite as

```
T. Pico, P. Bierman, K. Doyle, S. Richardson, [First authorship gender gap in the geosciences](https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2020EA001203), AGU Earth & Space Sciences, 2020
```

