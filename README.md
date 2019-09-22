# CSV to TXT 

[![PyPI](https://img.shields.io/pypi/v/csv2txt?color=blue&style=flat-square)](https://pypi.org/project/csv2txt/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/csv2txt?style=flat-square)
![PyPI - Downloads](https://img.shields.io/pypi/dm/csv2txt?style=flat-square)
[![GitHub](https://img.shields.io/github/license/gyk001/csv2txt?style=flat-square)](https://github.com/gyk001/csv2txt)

A python util package for convert a csv file to token separator txt file.

* HomePage: https://pypi.org/project/csv2txt/
* SourceCode: https://github.com/gyk001/csv2txt

# Usage

## In command line

Just install the package by pip, then enjoy it!

```bash
pip install csv2txt
csv2txt input.csv out.txt
```

## In source code 

```python
import csv2txt

# for File Path
csv2txt.convertByPath(csvFilePathString, txtFilePathString, '\t');

# for File Object
csv2txt.convertByFile(csvFile, txtFile, '\t');
```


