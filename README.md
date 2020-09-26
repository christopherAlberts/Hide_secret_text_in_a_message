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

* Now for this program to work you'll first need to install the `requests` package. To do this look for the "Search icon" (It should be top right). Search for the following : `project interpreter`. This should open your project's interpreter. Then click on the "+", search for `requests` and click "Install Package". Once the package is installed you should be good to go.

* Right click on the file and select the GREEN "Run" arrow to run the program. You should see the output in the terminal window below.

## How the program works

When the program runs you'll be presented with the following output:

 ```
Encode or Decode:
 ```

Here you can either write `encode` or `e` to encode a message. Or you could write `decode` or `d` to decode a message.

For instance: 

 ```
 Encode or Decode: encode
 ```
 
 You'll then be propted to firstly enter your hidden message:
 
 ```
 Enter hidden phrase:
 
 ```
 Following this you'll be prompted to 
 
 

# IF YOU CAN'T GET THE CODE TO WORK YOU CAN ALWAY'S JUST USE THE WEBSITE


Go to this link to use the website: https://neatnik.net/steganographr/


For developers. The following link will take you to the api page. https://neatnik.net/steganographr/api/
