![Stage](https://img.shields.io/badge/Stage-BETA-yellow)
[![PyPI](https://img.shields.io/pypi/v/gspread2)](https://pypi.org/project/gspread2)
[![gspread](https://img.shields.io/badge/gspread-3.2.0-blue)](https://github.com/burnash/gspread)
[![Documentation Status](https://readthedocs.org/projects/gspread2/badge/?version=latest)](https://gspread2.readthedocs.io/en/latest/?badge=latest)


# Gspread2

A wrapper around [gspread](https://github.com/burnash/gspread) for easier usage.
Intended to provide features and syntax similar to [OpenPyXL](https://bitbucket.org/openpyxl/openpyxl).

> DISCLAIMER: This library is still under development!\
> Until v1.0.0 is released, assume everything is subject to change.

## Features

- Cell Formatting such as Fonts, Colors and Borders
- OpenPyXL functions such as `iter_rows()` and `iter_cols()`
- ~~Values are automatically applied to the sheet when updated~~ See Issue #1

## Roadmap/TODO

- Documentation (WIP)
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

2. Navigate to "API & Services", "Credentials".

3. Click on "CREATE CREDENTIALS", "Service account" and follow through the prompts.
On the last page, create a JSON key and save it locally. You will need to import this into the library to authenticate
to the API.

4. Once you hit "Done", you will see the email address under "Service Accounts", make note of that email.

5. On your Google Sheet, hit "Share" and add the email above.

6. You should now have the credentials and permissions to view and edit your Google Sheet.

#### Load Workbook

To access a Workbook, you'll need the Google Sheet URL and the credentials file as shown above.
The following code example will return a Workbook object:

```python
import gspread2

URL = 'https://docs.google.com/spreadsheets/d/spreadsheetID'
CREDENTIALS = 'path/to/json.file'

workbook = gspread2.load_workbook(URL, CREDENTIALS)
```

You can also import the Workbook class and initialise it with the same parameters:

```python
from gspread2.models import Workbook

URL = 'https://docs.google.com/spreadsheets/d/spreadsheetID'
CREDENTIALS = 'path/to/json.file'

workbook = Workbook(URL, CREDENTIALS)
```

#### Load Worksheet

Once you have a Workbook loaded, you can access worksheets in a number of ways:

```python
workbook = gspread2.load_workbook(URL, CREDENTIALS)
worksheet = workbook['Sheet 1']
```

OR

```python
workbook = gspread2.load_workbook(URL, CREDENTIALS)
worksheet = workbook.get_sheet_by_name('Sheet 1')
```

To get the first sheet (usually the active one):

```python
workbook = gspread2.load_workbook(URL, CREDENTIALS)
worksheet = workbook.active
```

#### Select Cell

You can select cells individually or iterate through columns and rows (other gspread functions are still available such
 as `worksheet.range()`)

##### Worksheet.cell()

Select an individual cell in the worksheet

```python
cell = worksheet.cell(1, 2)  # 1st row, 2nd column
```
OR
```python
cell = worksheet.cell('B1')
```

##### Worksheet.iter_rows()

Returns a list of lists of cells for each row. This function is the same as found on OpenPyXL. \
Arguments are as follows:
- start_row (default: First row)
- end_row (default: Last row)
- start_col (default: First column)
- end_col (default: Last column)

```python
worksheet.iter_rows(2, 4, 3, 5)
```

The example above will return:

```python
[
    [Cell(C2), Cell(D2), Cell(E2)],
    [Cell(C3), Cell(D3), Cell(E3)],
    [Cell(C4), Cell(D4), Cell(E4)],
]
```

##### Worksheet.iter_cols()

Returns a list of lists of cells for each column. This function is the same as found on OpenPyXL. \
Arguments are as follows:
- start_row (default: First row)
- end_row (default: Last row)
- start_col (default: First column)
- end_col (default: Last column)

```python
worksheet.iter_cols(2, 4, 3, 5)
```
The example above will return:

```python
[
    [Cell(C2), Cell(C3), Cell(C4)],
    [Cell(D2), Cell(D3), Cell(D4)],
    [Cell(E2), Cell(E3), Cell(E4)],
]
```

#### Edit Cells

##### Cell Values

Once you have retrieved your desired cells as shown above, you'll want to update the value.
On the original `gspread` library, you have to keep track of all the cells you modified and pass them on to 
`worksheet.update_cells()`. \
In `gspread2` you do not have to pass on the cells to the function, the library will know what you modified.

```python
cell = worksheet.cell(1, 1)
cell.value = 'New Value'
worksheet.update_cells()
```

##### Cell Fonts

`gspread` does not provide any formatting features. To apply formatting to a cell, you must initialise a Font instance
(`gspread2.styles.Font`)

```python
from gspread2.styles import Font

cell = worksheet.cell(1, 1)
new_font = Font(
    name='Arial',
    size=12,
    bold=True,
    italic=True,
    strikethrough=True,
    underline=True,
    color='#FF000000',
)
cell.font = new_font
worksheet.update_cells()
```

All arguments for `Font` are optional and default to `None`. \
Arguments with `None` as a value will be untouched on update.


##### Cell Fill

To apply a background color to a cell, you must initialise `gspread2.styles.colors.Color`
and set it to `cell.fill`

```python
from gspread2.styles.colors import Color
cell = worksheet.cell(1, 1)
bg_color Color('#FF000000')
cell.fill = bg_color
worksheet.update_cells()
```
