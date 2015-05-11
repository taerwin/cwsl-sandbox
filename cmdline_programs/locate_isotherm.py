#!/bin/env python

""" 
Description: Locate the desired isotherm
Authors:     Damien Irving irving.damien@gmail.com
Copyright:   2015 CSIRO

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""

import argparse
import numpy
import cdms2
if hasattr(cdms2, 'setNetcdfDeflateFlag'):
    cdms2.setNetcdfShuffleFlag(0)
    cdms2.setNetcdfDeflateFlag(0)
    cdms2.setNetcdfDeflateLevelFlag(0)


def main(variable, isotherm, infile_name, outfile_name):
    """Locate isotherm."""

    infile = cdms2.open(infile_name, 'r')
    input_data = infile(variable, squeeze=1)
    infile.close()

    isotherm_data = input_data

    outfile = cdms2.open(outfile_name, 'w')
    outfile.write(isotherm_data)
    outfile.close()
    

if __name__ == '__main__':

    extra_info =""" 
example:

"""

    description='Locate isotherm'
    parser = argparse.ArgumentParser(description=description,
                                     epilog=extra_info, 
                                     formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument("variable", type=str, help="Input file variable")
    parser.add_argument("infile", type=str, help="Input file name")
    parser.add_argument("outfile", type=str, help="Output file name")

    parser.add_argument("--isotherm", type=float, default=20.0, 
                        help="Isotherm to locate")

    args = parser.parse_args()            

    main(args.variable, args.isotherm, args.infile, args.outfile)
