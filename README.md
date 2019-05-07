# FileUploadPayloadGenerator
Used To Generate A Number Of Payloads Given A file


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
