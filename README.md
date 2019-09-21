# CSV to TXT 

A python util package for convert a csv file to token separator txt file.

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

