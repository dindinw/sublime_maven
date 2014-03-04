import sublime, sublime_plugin

settings = sublime.load_settings('maven.sublime-build')
mvncmd = settings.get('cmd')
if sublime.platform() == "windows":
    mvncmd = settings.get('windows').get('cmd')

class MavenGoalsCommand(sublime_plugin.WindowCommand):
    wrkDir = None
    cmd = None

    def run(self,working_dir,cmd):
        self.cmd = [cmd]
        self.wrkDir = working_dir
        #print self.wrkDir
        self.window.show_input_panel("mvn",'clean test',self.on_done,None,None)

    def on_done(self, text):
        self.cmd += [u'-B']
        self.cmd += text.split(' ')
        print(self.cmd)
        self.window.run_command("exec",{"cmd":self.cmd, 'working_dir':self.wrkDir})

class MavenCommand(sublime_plugin.WindowCommand):
    def run(self,opts):
        print(opts);
        self.cmd =  [mvncmd] 
        self.cmd += [u'-B']
        self.cmd += opts.split(' ')
        self.window.run_command("exec",{"cmd":self.cmd})