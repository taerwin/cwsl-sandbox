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

This module wraps a python script that locates an isotherm of interest: 
cwsl-ctools/utils/locate_isotherm.py

Part of the CWSLab Model Analysis Service VisTrails plugin.

"""

import subprocess
from vistrails.core.modules import vistrails_module, basic_modules

from cwsl.configuration import configuration
from cwsl.core.constraint import Constraint
from cwsl.core.process_unit import ProcessUnit
from cwsl.core.pattern_generator import PatternGenerator


class LocateIsotherm(vistrails_module.Module):
    """This module locates an isotherm of interest from an input monthly timeseries.

    It wraps cwsl-ctools/utils/locate_isotherm.py script.

    """

    _input_ports = [('in_dataset', 'csiro.au.cwsl:VtDataSet'),
                    ('variable_name', basic_modules.String),
                    ('isotherm', basic_modules.String, {'labels': str(['Isotherm'])})]

    _output_ports = [('out_dataset', 'csiro.au.cwsl:VtDataSet')]
    
    _execution_options = {'required_modules': ['python/2.7.5', 'python-cdat-lite/6.0rc2-py2.7.5']}

    _data_type = 'monthly_isotherms'

    command = '${CWSL_CTOOLS}/indices/locate_isotherm.py'
    keyword_args = {}

    def __init__(self):

        super(LocateIsotherm, self).__init__()
        #tools_base_path = configuration.cwsl_ctools_path
        self.out_pattern = PatternGenerator('user', self._data_type).pattern

    def compute(self):

        in_dataset = self.getInputFromPort('in_dataset')
        variable_name = self.getInputFromPort('variable_name')
        isotherm = self.getInputFromPort('isotherm')
        self.positional_args = [('variable', 0),]
        self.keyword_args = {'isotherm': 'isotherm'}

        new_constraints_for_output = set([Constraint('isotherm', [isotherm]),
                                          Constraint('variable', [variable_name]),
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
