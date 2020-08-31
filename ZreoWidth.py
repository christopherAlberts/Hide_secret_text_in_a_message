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