#!/usr/bin/env bash

##############################################################################
#
# Description: Select a latitude/longitude box from an input netCDF file.
#              
# Modules Required: cdo
#
# Authors:     Damien Irving
#
# Copyright:   2015 CSIRO
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#############################################################################

function usage {
    echo "Select a longitude/latitude box from an input netCDF file."
    echo " "
    echo "USAGE: bash $0 west_lon east_lon south_lat north_lat infile outfile"
    echo "   west_lon:   Western boundary of the region (in degrees longitude)"
    echo "   east_lon:   Eastern boundary of the region (in degrees longitude)"
    echo "   south_lat:  Southern boundary of the region (in degrees latitude)"
    echo "   north_lat:  Northern boundary of the region (in degrees latitude)"
    echo "   infile:     Input file name"
    echo "   outfile:    Output file name"

    echo "   e.g. bash $0 190 240 -30 30 indata.nc outdata.nc"
    exit 1
}

nargs=6

if [ $nargs -ne $# ] ; then
  usage
fi

west_lon=$1
east_lon=$2
south_lat=$3
north_lat=$4
infile=$5
outfile=$6


cdo sellonlatbox,${west_lon},${east_lon},${south_lat},${north_lat} $infile $outfile

