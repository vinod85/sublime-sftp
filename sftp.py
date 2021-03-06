# sftp.py - sublime text sftp package
# Vinod <vinod at segfault dot in>
# Fri Jun 28 08:19:57 IST 2013

import sublime, sublime_plugin
import os

SETTINGS_PATH = sublime.packages_path() + '/User/sftp_servers'

class Settings:
	@staticmethod
	def getDefaultSettings():
			return """{
	"user":"${1:username}",
	"password":"${2:secret}",
	"default_path":"${3:path}"
}"""

class sftpsetupCommand(sublime_plugin.WindowCommand):
	def __init__(self, win):
		self.window = win
	def run(self):
		new_view = self.window.new_file()
		new_view.set_name('untitled')
		edit = new_view.begin_edit()
		new_view.run_command("insert_snippet", { "contents": "%s" %  Settings.getDefaultSettings() } )

class sftpeditCommand(sublime_plugin.WindowCommand):
	def __init__(self, win):
		self.window = win
		self.servers = []

	def find_server_settings(self):
		folder = sublime.packages_path() + '/User/sftp_servers'
		for filename in os.listdir (folder):
			self.servers.append(filename)

	def on_select(self,picked):
		if picked == -1:
			return

		filename = ''.join([sublime.packages_path(), '/User/sftp_servers/', self.servers[picked]])
		self.window.open_file(filename)

	def run(self):
		self.find_server_settings()
		self.window.show_quick_panel(self.servers, self.on_select)

class sftpdeleteCommand(sublime_plugin.WindowCommand):
	def __init__(self, win):
		self.window = win
		self.servers = []

	def find_server_settings(self):
		folder = sublime.packages_path() + '/User/sftp_servers'
		for filename in os.listdir (folder):
			self.servers.append(filename)

	def on_select(self,picked):
		if picked == -1:
			return

		filename = ''.join([sublime.packages_path(), '/User/sftp_servers/', self.servers[picked]])
		os.remove(filename)

	def run(self):
		self.find_server_settings()
		self.window.show_quick_panel(self.servers, self.on_select)

if __name__ == 'sftp':

	# Create settings directory
	if not os.path.isdir(SETTINGS_PATH):
		os.mkdir(SETTINGS_PATH)



