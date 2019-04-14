#!/usr/bin/python3
#
# Copyright (c) 2019 Maciej Gorzkowski
#
# This file is licensed under the MIT License.
# Full license text is available in 'LICENSE'.
#

import sys
import xml.etree.ElementTree as ET
import time
from git import Repo


class VhgComponent (object):
        
        def __init__(self, ctype, content = None):
                self.type = ctype
                self.content = content

class VersionHeaderGenerator (object):

        def __init__(self, cfgstring):
                self.cfgroot = ET.fromstring(cfgstring)
                self.name = self.cfgroot.attrib['name']
                self.destination = self.cfgroot.attrib['destination']
                self.path = self.cfgroot.attrib['repository']
                self.repo = Repo(self.path)
                self.vardir = self._getVariables()
                self.recipe = self._parseRecipe()

        def _getVariables(self):
                vardir = {}
                self._parseVariables(vardir)
                self._attachBuildinVariables(vardir)
                return vardir

        def _parseVariables(self, vardir):
                variables = self.cfgroot.find('variables')
                for var in variables:
                        vardir[var.tag] = var.text
                return vardir

        def _attachBuildinVariables(self, vardir):
                if vardir.get('guard_def') == None:
                        vardir['guard_def'] = '_' + self.name.upper() + '_VERSION_H_'
                if vardir.get('name') == None:
                        vardir['name'] = '"' + self.name.upper() + '"'
                if vardir.get('git_revision_hash') == None:
                        vardir['git_revision_hash'] = '"' + self.repo.head.commit.hexsha + '"'
                if vardir.get('git_short_revision_hash') == None:
                        vardir['git_short_revision_hash'] = '"' + self.repo.head.commit.hexsha[0:7] + '"'
                if vardir.get('git_branch') == None:
                        vardir['git_branch'] = '"' + self.repo.active_branch.name + '"'
                if vardir.get('generation_time') == None:
                        vardir['generation_time'] = '"' + time.strftime("%H:%M:%S") + '"'
                if vardir.get('generation_date') == None:
                        vardir['generation_date'] = '"' + time.strftime("%b %d %Y") + '"'
                if vardir.get('compilation_time') == None:
                        vardir['compilation_time'] = '__TIME__'
                if vardir.get('compilation_date') == None:
                        vardir['compilation_date'] = '__DATE__'
                return vardir

        def _parseRecipe(self):
                result = []
                recipe = self.cfgroot.find('recipe')
                for item in recipe:
                        if item.tag == 'line':
                                result.append(VhgComponent('line', item.text))
                        elif item.tag == 'import':
                                result.append(VhgComponent('import', item.attrib['path']))
                        elif item.tag == 'define':
                                result.append(VhgComponent('define', item.attrib['var']))
                        elif item.tag == 'open_guard':
                                result.append(VhgComponent('open_guard'))
                        elif item.tag == 'close_guard':
                                result.append(VhgComponent('close_guard'))
                return result

        def generate(self):
                result = ''
                for item in self.recipe:
                        g_type = item.type
                        g_value = item.content
                        if g_type == 'line':
                                content = ''
                                if g_value != None:
                                        content = g_value
                                result += content + '\n'
                        elif g_type == 'import':
                                content = open(g_value).read()
                                result += content
                        elif g_type == 'define':
                                result += '#define ' + g_value.upper() + '\t' + self.vardir[g_value] + '\n'
                        elif g_type == 'open_guard':
                                result += '#ifndef ' + self.vardir['guard_def'] + '\n#define ' + self.vardir['guard_def'] + '\n'
                        elif g_type == 'close_guard':
                                result += '#endif /* ' + self.vardir['guard_def'] + ' */\n'
                open(self.destination, 'w').write(result)
                return result

def usage():
        return 'Usage: ' + __file__ + ' config.xml'

if __name__ == "__main__":
        if len(sys.argv) != 2:
                print (usage())
                sys.exit(1)
        cfgstring = open(sys.argv[1], 'r').read()
        VersionHeaderGenerator(cfgstring).generate()