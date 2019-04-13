#!/usr/bin/python3
#
# Copyright (c) 2019 Maciej Gorzkowski
#
# This file is licensed under the MIT License.
# Full license text is available in 'LICENSE'.
#

import sys
import xml.etree.ElementTree as ET

# from git import Repo

class VhgComponenet (object):

	def __init__(self, ctype, content = None):
		self.type = ctype
		self.content = content

class VersionHeaderGenerator (object):

	def __init__(self, cfgstring):
		self.cfgroot = ET.fromstring(cfgstring)
		self.path = self.cfgroot.attrib['path']
		self.vardir = self.parsevariables()
		self.recipe = self.parserecipe()
		if self.vardir.get('guard-def') == None:
			self.vardir['guard-def'] = '_' + self.path.split('/')[-1].upper() + '_VERSION_H_'

	def parsevariables(self):
		result = {}
		variables = self.cfgroot.find('variables')
		for var in variables:
			result[var.tag] = var.text
		return result

	def parserecipe(self):
		result = []
		recipe = self.cfgroot.find('recipe')
		for item in recipe:
			if item.tag == 'line':
				result.append(VhgComponenet('line', item.text))
			elif item.tag == 'import':
				result.append(VhgComponenet('import', item.attrib['path']))
			elif item.tag == 'define':
				result.append(VhgComponenet('define', item.attrib['var']))
			elif item.tag == 'open-guard':
				result.append(VhgComponenet('open-guard'))
			elif item.tag == 'close-guard':
				result.append(VhgComponenet('close-guard'))
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
			elif g_type == 'open-guard':
				result += '#ifndef ' + self.vardir['guard-def'] + '\n#define ' + self.vardir['guard-def'] + '\n'
			elif g_type == 'close-guard':
				result += '#endif /* ' + self.vardir['guard-def'] + ' */\n'
		return result

def help():
	return 'Usage: ' + __file__ + ' config.xml output.h'

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print (help())
		sys.exit(1)
	else:
		cfgstring = open(sys.argv[1], 'r').read()
		output = open(sys.argv[2], 'w')
	vhg = VersionHeaderGenerator(cfgstring)
	content = vhg.generate()
	output.write(content)