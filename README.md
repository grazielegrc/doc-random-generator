## Introduction

This project was created in order to facilitate the generation of random document numbers to some countries.

## Requirements
- [virtualenv](https://docs.python.org/3.8/library/venv.html) 20.10.0+
- [python](https://www.python.org/downloads/release/python-3810/) 3.8.10+
- [pip](https://pypi.org/project/pip/) 21.3.1+

## Instalation

Creating a virtual environment using python3 location. Remember to retrieve the current python localtion to ensure the correct version.

```bash
virtualenv -p /usr/bin/python3 venv
```

Activating the new virtual environment

```bash
source venv/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the generator.

```bash
pip install -r requirements.txt
```

## Usage

Run the command above and follow the instructions to generate the URL from any country using any environment.

```bash
python generator.py
```

## Contributing

Pull requests are welcome.
