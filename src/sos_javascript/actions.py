#!/usr/bin/env python3
#
# This file is part of Script of Scripts (sos), a workflow system
# for the execution of commands and scripts in different languages.
# Please visit https://github.com/vatlab/SOS for more information.
#
# Copyright (C) 2016 Bo Peng (bpeng@mdanderson.org)
##
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

from sos.actions import SoS_Action, SoS_ExecuteScript

@SoS_Action(acceptable_args=['script', 'args'])
def node(script, args='', **kwargs):
    '''Execute specified script with command node. This action accepts common action arguments
    such as input, active, workdir, docker_image and args. In particular, content of one or
    more files  specified by option input would be prepended before the specified script.
    '''
    return SoS_ExecuteScript(
        script, 'node', '.js', args).run(**kwargs)

