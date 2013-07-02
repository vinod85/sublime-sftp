# sftp.py - sublime text sftp package
# Vinod <vinod at segfault dot in>
# Fri Jun 28 08:19:57 IST 2013

import sublime, sublime_plugin

class sftpsetupCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, 0, "Hello, World!")
