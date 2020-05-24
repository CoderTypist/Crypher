# Crypher

Crypher is a series of Python packages that can encode and decode various ciphers

## Supported Ciphers
- Tap Code (tap.py)
- Ceasar Cipher (ceasar.py)

## Packages

### tap

Functions for encoding/decoding tap code

### ceasar

CeasarCoder class that has functions for encoding/decoding ceasar ciphers.

### cryparse

Functions for adding arguments to an ArgumentParser.

Functions for analyzing the dictionary of arguments.

### lman

Functions for list creation and manipulation.

## Command Line Examples

### tap.py

Encode and decode tap code. Tap code was commonly used by prisoners during the Vietnam War. 

#### Encode String and Output to Console

./tap.py -e -t \<string\>

#### Encode String and Output to File

./tap.py -e -t \<string\> -o \<output_file\>

#### Decode String and Output to Console

./tap.py -d -t \<string\>

#### Decode String and Output to File

./tap.py -d -t \<string\> -o \<output_file\>

#### Encode File and Output to Console

./tap.py -e -i \<input_file\>

#### Encode File and Output to File

./tap.py -e -i \<input_file\> -o \<output_file\>

#### Decode File and Output to Console

./tap.py -d -i \<input_file\>

#### Decode File and Output to File

./tap.py -d -i \<input_file\> -o \<output_file\>

#### Help

./tap.py -h

### ceasar.py

Encode and decode messages using the classic ceasar cipher. 

#### Encode String and Output to Console

./ceasar.py -e -t \<string\> -s \<num_shifts\>

#### Encode String and Output to File

./ceasar.py -e -t \<string\> -s \<num_shifts\> -o \<output_file\>

#### Decode String and Output to Console

./ceasar.py -d -t \<string\> -s \<num_shifts\>

#### Decode String and Output to File

./ceasar.py -d -t \<string\> -s \<num_shifts\> -o \<output_file\>

#### Encode File and Output to Console

./ceasar.py -e -i \<input_file\> -s \<num_shifts\>

#### Encode File and Output to File

./ceasar.py -e -i \<input_file\> -s \<num_shifts\> -o \<output_file\>

#### Decode File and Output to Console

./ceasar.py -d -i \<input_file\> -s \<num_shifts\>

#### Decode File and Output to File

./ceasar.py -d -i \<input_file\> -s \<num_shifts\> -o \<output_file\>

#### Decode String (Bruteforce) and Output to Console

./ceasar.py -d -t \<string\> -b

#### Decode String (Bruteforce) and Output to File

./ceasar.py -d -t \<string\> -b -o \<output_file\>

#### Decode File (Bruteforce) and Output to Console

./ceasar.py -d -i \<input_file\> -b

#### Decode File (Bruteforce) and Output to File

./ceasar.py -d -i \<input_file\> -b -o \<output_file\>

#### Help

./ceasar.py -h