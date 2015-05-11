"""
Authors:  Damien Irving (irving.damien@gmail.com)

Copyright 2015 CSIRO

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

This module wraps a python script that extracts a longitude/latitude box: 
cwsl-ctools/cropping/cdo_sellonlatbox.sh

Part of the CWSLab Model Analysis Service VisTrails plugin.

"""

import subprocess
from vistrails.core.modules import vistrails_module, basic_modules

from cwsl.configuration import configuration
from cwsl.core.constraint import Constraint
from cwsl.core.process_unit import ProcessUnit
from cwsl.core.pattern_generator import PatternGenerator


class LocateIsotherm(vistrails_module.Module):
    """This module extracts a longitude/latitude box.

    It wraps cwsl-ctools/cropping/cdo_sellonlatbox.sh script.

    """

    _input_ports = [('in_dataset', 'csiro.au.cwsl:VtDataSet'),
                    ('west_lon', basic_modules.Float),
                    ('east_lon', basic_modules.Float),
                    ('south_lat', basic_modules.Float),
                    ('north_lat', basic_modules.Float),
                   ]

    _output_ports = [('out_dataset', 'csiro.au.cwsl:VtDataSet')]
    
    _execution_options = {'required_modules': ['cdo',]}

    _data_type = '???????'

    command = '${CWSL_CTOOLS}/cropping/cdo_sellonlatbox.sh'
    keyword_args = {}

    def __init__(self):

        super(LocateIsotherm, self).__init__()
        #tools_base_path = configuration.cwsl_ctools_path
        self.out_pattern = PatternGenerator('user', self._data_type).pattern

    def compute(self):

        in_dataset = self.getInputFromPort('in_dataset')
        west_lon = self.getInputFromPort('west_lon')
        east_lon = self.getInputFromPort('east_lon')
        south_lat = self.getInputFromPort('south_lat')
        north_lat = self.getInputFromPort('north_lat')

        self.positional_args = [('west_lon', 0),
                                ('east_lon', 1),
                                ('south_lat', 2),
                                ('north_lat', 3)]
        self.keyword_args = {}

        new_constraints_for_output = set([Constraint('west_lon', [west_lon]),
                                          Constraint('east_lon', [east_lon]),
                                          Constraint('south_lat', [south_lat],
                                          Constraint('north_lat', [north_lat]))
                                          ])
        
        this_process = ProcessUnit([in_dataset],
                                   self.out_pattern,
                                   self.command,
                                   new_constraints_for_output,
                                   execution_options=self._execution_options,
                                   positional_args=self.positional_args,
                                   cons_keywords=self.keyword_args)

        try:
            this_process.execute(simulate=configuration.simulate_execution)
        except subprocess.CalledProcessError, e:
            raise vistrails_module.ModuleError(self, e.output)
            
        process_output = this_process.file_creator

        self.setResult('out_dataset', process_output)

