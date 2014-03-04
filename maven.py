import os, sublime, sublime_plugin

settings = None
mvncmd = None 
workdir = None

def plugin_loaded():
    global settings
    global mvncmd
    settings = sublime.load_settings('maven.sublime-build')
    mvncmd = settings.get('cmd')
    # print(mvncmd)
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
        global workdir 
        workdir = None
        view_file_name = self.window.active_view().file_name()
        print("view_file:",view_file_name)
        if view_file_name :
            path, filename = os.path.split(self.window.active_view().file_name())
            if filename.lower() == "pom.xml" :
                workdir = path
                print("workdir current:",path)
            else :
                search_pom_file(path)
            if not workdir :
                sublime.status_message("No pom.xml find.")
                return
            self.cmd =  [mvncmd] 
            self.cmd += [u'-B']
            self.cmd += opts.split(' ')
            print("cmd:",self.cmd)
            print("work_dir:",workdir)
            self.window.run_command("exec",{"cmd":self.cmd, 'working_dir':workdir})

def search_pom_file(path):
    global workdir
    print("seach_file_in:",path)
    _path, _filename = os.path.split(path)
    if _path == os.path.realpath(path) : #it root
        return
    if os.path.isfile(_path+os.sep+"pom.xml") :
        workdir = _path
        print("workdir set to",_path)
        return
    search_pom_file(_path)