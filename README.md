# Hide_secret_text_in_a_message (ZeroWidth_Steganography_API_Handler)

## How to run the program:

* Download a Python IDE like Pycharm: https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows&code=PCC

* Once Pycharm is installed open a new file and copy the following code into it:

```python
import requests

while True:

    encodeOrDecoded = input("Encode or Decode: ")

    if encodeOrDecoded == "Encode" or encodeOrDecoded == "encode" or encodeOrDecoded == "E" or encodeOrDecoded == "e":

        hiddenPhrase = input("Enter hidden phrase: ")
        publicPhrase = input("Enter public phrase: ")

        hiddenPhrase = hiddenPhrase.replace(' ', '+')
        publicPhrase = publicPhrase.replace(' ', '+')

        result = requests.get('https://neatnik.net/steganographr/api?public='+ publicPhrase+'&private=' + hiddenPhrase)

        result = result.content
        result = result.decode("utf-8")
        print(result)

    elif encodeOrDecoded == "Decode" or encodeOrDecoded == "decode" or encodeOrDecoded == "D" or encodeOrDecoded == "d":

        decodePhrase = input("Enter phrase to decode: ")
        result2 = requests.get('https://neatnik.net/steganographr/api?decode=' + decodePhrase)
        print(result2.content.decode("utf-8"))

    else:
        print("Error: Input does not match")
        
 ```

* Then right click on the file and selecr the GREEN "Run" arrow.


Steganography_API_Handler


https://neatnik.net/steganographr/


https://neatnik.net/steganographr/api/
