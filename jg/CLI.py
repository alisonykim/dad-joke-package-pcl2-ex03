#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# CLI.py

# University of Zurich
# Department of Computational Linguistics

# Author 1: Alison Y. Kim
# Author 2: Naomi Bleiker

# Python Version: 3.10.0

# Import modules
from argparse import ArgumentParser, FileType
from jg.joke import Joke, JokeGenerator
import os
import pkg_resources

# Define data directory
DATA_DIR = pkg_resources.resource_filename('jg', 'data/')


def parse_cla() -> ArgumentParser:
    """Creates optional flags for user to call jokes from CLI."""
    parser = ArgumentParser(description='Process and print dad jokes.')
    parser.add_argument('--joke_file',
        type=FileType('r', encoding='utf-8'),
        nargs='?',
        default=os.path.join(DATA_DIR, 'reddit_dadjokes.csv'),
        help='File containing dad jokes with comma-delimited columns containing joke metadata.')
    parser.add_argument('--profanities_file',
        type=FileType('r', encoding='utf-8'),
        nargs='?',
        default=os.path.join(DATA_DIR, 'profanities.txt'),
        help='File containing profanities used to censor jokes.')
    parser.add_argument('--output_file',
        type=FileType('w', encoding='utf-8'),
        help='File to which dad jokes are saved.')
    parser.add_argument('--print',
        action='store_true',
        help='Print jokes in a readable format.')
    parser.add_argument('--split_sent',
        action='store_true',
        help='Print joke sentence-by-sentence.')
    parser.add_argument('--tokenize',
        action='store_true',
        help='Print joke token-by-token.')
    parser.add_argument('--filter',
        action='store_true',
        help='Print filtered version of joke with censored profanities.')
    parser.add_argument('--joke',
        type=str,
        help='Input a joke that the user wants to tell.')
    parser.add_argument('--author',
        type=str,
        help='Select joke from specified author.')
    parser.add_argument('--link',
        type=str,
        help='Select joke from specified link.')
    parser.add_argument('--rating',
        type=int,
        help='Select joke with specified rating.')
    parser.add_argument('--time',
        type=str,
        help='Select joke from specified date and time (format TT.MM.JJJJ SS:MM).')

    return parser


def main():
    # Parse CL arguments
    parser = parse_cla()
    args = parser.parse_args()
    # Define input file names
    joke_file = args.joke_file.name
    profanities_file = args.profanities_file.name
    # Generate joke objects
    if args.joke: # If joke is user-inputted in CL
        if not args.author or not args.link or not args.rating or not args.time:
            raise ValueError('--joke input must be accompanied by nontrivial --author, --link, --rating, AND --time values Please define all necessary flags for custom jokes:\n--joke: Quotation-wrapped string\n--author: Quotation-wrapped string\n--link: String\n--rating: Integer\n--time: Quotation-wrapped string, ideally in the format [DD.MM.YYYY HH:MM]')
        else:
            raw_joke = [args.author, args.link, args.joke, args.rating, args.time]
            joke_objects = JokeGenerator(raw_joke)
    else: # If joke is from .csv file
        joke_objects = JokeGenerator(joke_file)
    # Build output for saving or printing
    output = list()
    for joke_object in joke_objects.make_jokes_objects():
        if args.print or args.joke:
            output.append(joke_object.joke)
            output.append('\n')
        if args.split_sent:
            joke_sent_lines = joke_object.split_into_sentences()
            for line in joke_sent_lines:
                output.append(line)
            output.append('\n')
        if args.tokenize:
            joke_tokens = joke_object._tokenize()
            for line in joke_tokens:
                tokens = ' / '.join(line)
                output.append(tokens)
            output.append('\n')
        if args.filter:
            filtered_lines = joke_object.filter_profanity(filename=profanities_file)[0]
            for filtered_line in filtered_lines:
                filtered_tokens = ' '.join(filtered_line)
                output.append(filtered_tokens)
            output.append('\n')
    # Deliver the joke
    if args.output_file: # Optional
        output_file = args.output_file.name
        with open(output_file, 'w') as f:
            for joke in output:
                for line in joke:
                    f.write(line)
        f.close
    elif (not args.output_file) or args.print: # If --print is specified or nothing is specified
        for line in output:
            print(f'{line}')


if __name__ == '__main__':
    main()