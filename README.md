# PyVcardParser (Python VCard Parser)

It is a small python3 script written for extraction of the VCF data files, and arrange the data into a programmable data type or even a designed / structured text format. The tool is a single script with a function named __extractor__ which does all the work.

## Usage

Move the entire folder to the project directory of yours. Now, just type this code to import the extractor() function.
```
from PyVcardParser import extractor
```
Now, we read the data of the _.vcf_ file to a variable "data" and pass it as an argument to the extractor() function. The function by default returns filtered data in a list of dict objects like [{"name" : "Ryjein Yakuz", "contact" : "+666 111 000"}, ...]. Example code for the process is
```
extractor(data)
```
