sublime_maven
=============

A sublime 3 plugin for maven.


Installation
------------

In sublime click on Preferences/Browse Packages. Copy `sublime_maven` folder into this folder.


Requirements
------------

The plugin assume that you have maven installed and is in your path.

Configuration
-------------

```
[
    { 
        "caption": "maven: clean",
        "command": "maven",
        "args": {
            "opts":"clean"
        }
    },
    { 
        "caption": "maven: install",
        "command": "maven",
        "args": {
            "opts":"clean install"
        }
    },
    { 
        "caption": "maven: test",
        "command": "maven",
        "args": {
            "opts":"clean test"
        }
    },
]
```

Inspired by 
-----------

 - hangar88's [Hangar88ST2Plugins]
 - moore0n's [sublimemavenplugin]
 - nlloyd's [SublimeMaven]


[Hangar88ST2Plugins]:https://github.com/hangar88/Hangar88ST2Plugins/tree/master/Maven

[sublimemavenplugin]:https://bitbucket.org/moore0n/sublimemavenplugin

[SublimeMaven]:https://github.com/nlloyd/SublimeMaven

