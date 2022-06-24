# jg: **J**oke processing and **g**eneration package
This package processes and generates jokes from a .csv file or from a command line input. The processing contains different functionalities: splitting the jokes into sentences, tokenization, filtering and censoring profanities and printing the jokes in a readable manner. The package can also be used to generate random jokes and print them with build up before the punchline.

## How to run the package
The package can be run on the command line simply by calling ```jg``` plus one or more of the flags listed below in **Optional flags**.

### Optional flags
The following optional flags can be specified in the function call:
* ```--joke_file```: Specifies the joke file from which you would like to inherit the jokes. If this is not specified, then the program will default to ```reddit_dadjokes.csv```, located in the ```data``` folder.
* ```--profanities_file```: Specifies the profanities file that ```Joke.filter_profanity``` will use to censor profanities in jokes. If this is not specified, then the program will default to ```profanities.txt```, located in the ```data``` folder.
* ```--output_file```: Specifies the name of the output file to which processed jokes will be written and saved. If this is not specified, then the program will print the processed jokes to the console.
* ```--print```: Prints out each joke string in a readable manner.
* ```--split_sent```[^1] [^2]: Prints out each joke sentence-by-sentence.
* ```--tokenize```[^1] [^2]: Tokenizes the jokes and prints out the tokens separated by a forward slash '/'.
* ```--filter```[^1] [^2]: Filters and censors profanities in the jokes before printing the joke sentence-by-sentence.
* ```--joke```[^1] [^2]: Allows user to input their own joke via the command line. The joke should be passed as a *quotation-wrapped* string. In order for the joke to be properly converted to a ```Joke```-Object, this flag MUST be accompanied by the following flags:
    * ```--author```: Who came up with the joke (format: *str*, unless it is more than 1 word, in which case it should be quotation-wrapped)
    * ```--link```: URL to the joke (format: *quotation-wrapped str*)
    * ```--rating```: Rating of the joke (format: *int*)
    * ```--time```: Date and time of the joke (format: *str*, ideally TT.MM.JJJJ SS:MM)

[^1]: If called without specifying ```--output_file```, i.e. if you only want to print the joke to the console, then this flag is unnecessary. The program won't break if ```--print``` is additionally called, but both the joke string *and* the processed joke will be printed, which might be superfluous.
[^2]: Can be called with ```--output_file``` in order to save the output to a separate file.

### Example function calls
```sh
$ python3 jg --print
It\'s okay if your phone autocorrects fuck to duck. You\'re still using fowl language.

$ python3 jg --split_sent
It\'s okay if your phone autocorrects fuck to duck.
You\'re still using fowl language.

$ python3 jg --tokenize
It\'s / okay / if / your / phone / autocorrects / fuck / to / duck / .
You\'re / still / using / fowl / language / .

$ python3 jg --filter
It\'s okay if your phone autocorrects \#\#\#\# to duck.
You\'re still using fowl language.

$ python3 jg --output_file my_output.txt --tokenize
# New file my_output.txt will appear in working directory with tokenized jokes from default reddit_dadjokes.csv

$ python3 jg --joke_file twitter_dadjokes.csv --profanity_file new_profanities_file.txt --filter
# Jokes from twitter_dadjokes.csv will be filtered using new_profanities_file.txt and printed to the console

$ python3 jg --joke "This is a joke. Unfortunately, it is not funny" --author Me --link www.this_is_a_url.ch --rating 1 --time "14.03.2002 03:00"
This is a joke. Unfortunately, it is not funny

$ python3 jg --joke "This is a joke. Unfortunately, it is not funny"
ValueError: --joke input must be accompanied by nontrivial --author, --link, --rating, AND --time values Please define all necessary flags for custom jokes:
--joke: Quotation-wrapped string
--author: Quotation-wrapped string
--link: String
--rating: Integer
--time: Quotation-wrapped string, ideally in the format [DD.MM.YYYY HH:MM]
```

## CLI.py
This module handles the argument parsing and outputting (print and/or save to an output file). Its methods are:
* ```parse_cla()```: Defines the arguments that can be passed in the command line.
* ```main()```: Processes the passed arguments, raises exceptions when arguments are not passed properly, and handles the outputting.

## joke.py
This module handles the under-the-hood work of processing the files used to generate jokes, as well as the generation itself.

### Class ```Joke```
The ```Joke``` class handles the *instantiation* of a joke. Its methods are:
* ```__init__```: Stores instance attributes ```self.raw_joke```, ```self.author```, ```self.link```, ```self.joke```, ```self.rating``` and ```self.time```.
* ```split_into_sentences```: Splits a joke line into a list of individual sentences.
* ```_tokenize```: Tokenizes a list of sentences.
* ```filter_profanity```: Checks tokens against a file containing profanities and returns a tuple of a list of tokens per line and the number of profanities found in the joke.
* ```tell_joke```: Prints the joke to the console in a suspenseful way.
* ```pretty_print```: Handles the printing used in ```tell_joke```.

### Class ```JokeGenerator```
The ```JokeGenerator``` class handles the *delivery* of a joke. Its methods are:
* ```__init__```: Stores instance attributes ```self.data``` and ```self.jokes```.
* ```make_jokes_objects```: Processes the joke source (either multiple jokes in a .csv file or user-inputted string) and stores the jokes as Joke-Objects in a list.
* ```generate_jokes```: Prints the joke to the console if it is longer than 1 line. (Sorry, no one-liners!)
* ```random_joke```: Selects and prints a random joke from the joke source.

## License
This package is distributed under the MIT License. We selected this license type in the spirit of open-source development, allowing users to modify and add modules for their own purposes and re-license such derivative works. It also has the benefit of compatibility across almost all operating systems. The only condition that must be satisfied is that the same copyright notice must be included in all copies of the software.

## Footnotes