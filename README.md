# Hide_secret_text_in_a_message (ZeroWidth_Steganography_API_Handler)

## How to run the program:

* Download a Python IDE like Tonny: https://thonny.org/

* Once Tonny is installed open a new file and copy the following code into it:

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

        print("Here is your encrypted message:")
        print("###############################\n")
        print(result)
        print("\n###############################")

    elif encodeOrDecoded == "Decode" or encodeOrDecoded == "decode" or encodeOrDecoded == "D" or encodeOrDecoded == "d":

        decodePhrase = input("Enter phrase to decode: ")
        result2 = requests.get('https://neatnik.net/steganographr/api?decode=' + decodePhrase)

        print("Here is your decrypted message:")
        print("###############################\n")
        print(result2.content.decode("utf-8"))
        print("\n###############################")


    else:
        print("Error: Input does not match")
        
 ```

* Then click on the the GREEN "Run" arrow to run the program.

## How the program works


Steganography_API_Handler


https://neatnik.net/steganographr/


https://neatnik.net/steganographr/api/
