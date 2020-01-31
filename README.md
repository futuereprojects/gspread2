![Stage](https://img.shields.io/badge/Stage-ALPHA-red)
[![PyPI](https://img.shields.io/pypi/v/gspread2)](https://pypi.org/project/gspread2)
[![gspread](https://img.shields.io/badge/gspread-3.1.0-blue)](https://github.com/burnash/gspread)
[![Documentation Status](https://readthedocs.org/projects/gspread2/badge/?version=latest)](https://gspread2.readthedocs.io/en/latest/?badge=latest)


# Gspread2

A wrapper around [gspread](https://github.com/burnash/gspread) for easier usage.
Intended to provide features and syntax similar to [OpenPyXL](https://bitbucket.org/openpyxl/openpyxl).

> DISCLAIMER: This library is still under development!

## Features

- Cell Formatting such as Fonts, Colors and Borders
- OpenPyXL functions such as `iter_rows()` and `iter_cols()`
- Values are automatically applied to the sheet when updated

## Roadmap/TODO

- Documentation (WIP)
- Colors and Borders
- Formulas
- Filters and Pivot Tables

## Installation

### Requirements:
- Python3.6+

### Install via Pip
```
$ pip install gspread2
```

## Basic Usage

### Getting Started

#### Create API credentials

Before using this library, you must log into Google Developers page and set up a Service Account,
allowing read/write access to your Google Sheets.

1. Head to [Google Developers Console](https://console.developers.google.com/project) 
and create a new project (or select the one you have.)

2. Navigate to "API & Services", "Credentials"

3. Click on "CREATE CREDENTIALS", "Service account"