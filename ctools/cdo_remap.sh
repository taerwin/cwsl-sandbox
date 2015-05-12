#!/usr/bin/env bash

##############################################################################
#
# Description: Remap to new horizontal grid.
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
    echo "Remap to new horizontal grid."
    echo " "
    echo "USAGE: bash $0 [method] grid infile outfile"
    echo "   method:     Method for remapping to new horizontal grid [default = remapcon2]"
    echo "               Choices: remapbil, remapbic, remapdis, remapnn, remapcon, remapcon2, remaplaf"
    echo "   grid:       Name of cdo target grid or interpolation weights file. Grid names are at: " 
    echo "               https://code.zmaw.de/projects/cdo/embedded/index.html#x1-150001.3.2  "
    echo "   infile:     Input file name"
    echo "   outfile:    Output file name"

    echo "   e.g. bash $0 remapcon2 r360x180 indata.nc outdata.nc"
    exit 1
}


if [ $# -eq 3 ] ; then
    gridname=$1
    infile=$2
    outfile=$3
    method=remapcon2
elif [ $# -eq 4 ] ; then
    method=$1
    gridname=$2
    infile=$3
    outfile=$4
else
    usage
fi

if [ ! -f $infile ] ; then
    echo "Input file doesn't exist: " $infile
    usage
fi


# Check if input is an XML file
inbase=`basename $infile`
extn=`expr match "${inbase}" '.*\.\(.*\)'`
if [ $extn = 'xml' ] ; then
  tmp_in=$TMPDIR/xml_concat.$$.nc
  python ${CWSL_CTOOLS}/utils/xml_to_nc.py None $infile $tmp_in
  infile=$tmp_in
fi


# process gridname
case $gridname in
    r*x* )
      cdogrid=$gridname
      ;;
    lon*_lat* )
      cdogrid=$gridname
      ;;
    t*grid )
      cdogrid=$gridname
      ;;
    gme* )
      cdogrid=$gridname
      ;;
    * )
      if [ -f $gridname ] ; then  # Could add an extra option here to a directory of saved grid files
        cdogrid=$gridname
      else
        echo "Can't recognise or find grid definition: " $griname
        exit 1
      fi
esac
        
cdo ${method},$cdogrid $infile $outfile

