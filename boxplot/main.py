#!/usr/bin/env python
#
# Copyright 2013 Evan Wheeler
#
# based on bitly's data_hacks https://github.com/bitly/data_hacks
# and David Golden's https://github.com/dagolden/text-boxplot
#
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

"""
Generate an ascii box-and-whiskers chart for input data

"""
import sys
import itertools
from optparse import OptionParser

from lib import render, Dataset


def str_to_number(s):
    try:
        return int(s)
    except ValueError:
        return float(s)


def load_stream(input_stream):
    for line in input_stream:
        clean_line = line.strip()
        if not clean_line:
            # skip empty lines (ie: newlines)
            continue
        if clean_line[0] in ['"', "'"]:
            clean_line = clean_line.strip('"').strip("'")
        if clean_line:
            yield clean_line


def run(input_stream, options):
    datasets = []
    counter = itertools.count(1)
    for row in input_stream:
        datasets.append(
            Dataset(
                'series-%s' % next(counter),
                [str_to_number(d) for d in row.split(',')]
            )
        )

    if not datasets:
        print("Error: no data")
        sys.exit(1)

    output = render(datasets, options.width, options.box_weight or 1, options.with_scale)
    print(output)


if __name__ == "__main__":
    parser = OptionParser()
    parser.usage = "cat data | %prog [options]"

    parser.add_option("-w", "--width", dest="width", default=72, action="store_true",
                        help="output width")
    parser.add_option("-l", "--label-width", dest="label_width", default=10, action="store_true",
                        help="width of series label")
    parser.add_option("-b", "--box-weight", dest="box_weight", default=1, action="store_true",
                        help="output scale")
    parser.add_option("-s", "--with-scale", dest="with_scale", default=True, action="store_true",
                        help="show min and max values")

    (options, args) = parser.parse_args()

    if sys.stdin.isatty():
        parser.print_usage()
        print("for more help use --help")
        sys.exit(1)
    run(load_stream(sys.stdin), options)
