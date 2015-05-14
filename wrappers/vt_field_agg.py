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

This module wraps a shell script that performs field aggregation: 
cwsl-ctools/aggregation/cdo_field_agg.sh

Part of the CWSLab Model Analysis Service VisTrails plugin.

"""

import subprocess
from vistrails.core.modules import vistrails_module, basic_modules

from cwsl.configuration import configuration
from cwsl.core.constraint import Constraint
from cwsl.core.process_unit import ProcessUnit
from cwsl.core.pattern_generator import PatternGenerator


class FieldAggregation(vistrails_module.Module):
    """This module performs field aggregation.

    It wraps the cwsl-ctools/aggregation/cdo_field_agg.sh script.

    """

    _input_ports = [('in_dataset', 'csiro.au.cwsl:VtDataSet'),
                    ('agg_method', basic_modules.Float),
                   ]

    _output_ports = [('out_dataset', 'csiro.au.cwsl:VtDataSet')]
    
    _execution_options = {'required_modules': ['cdo',]}

    _data_type = 'default'

    command = '${CWSL_CTOOLS}/aggregation/cdo_sellonlatbox.sh'
    keyword_args = {}

    def __init__(self):

        super(LocateIsotherm, self).__init__()
        self.out_pattern = PatternGenerator('user', self._data_type).pattern

    def compute(self):

        in_dataset = self.getInputFromPort('in_dataset')
        agg_method = self.getInputFromPort('agg_method')

        self.positional_args = [('agg_method', 0), ]
        self.keyword_args = {}

        if len(agg_method.split(',')) > 1:
            agg_constraint = "".join(agg_method.split(','))
        else:
            agg_constraint = agg_method

        new_constraints_for_output = set([Constraint('lonagg_info', [agg_constraint]),
                                          Constraint('latagg_info', [agg_constraint]),
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

