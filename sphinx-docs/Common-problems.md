# Common problems

### I'm getting an error starting the application!

1. You likely have a misalignment between the core code and the plugin repositories. This is typically caused by doing a "git pull" on one of the repositories and not the others. If you see this error, you should re-clone the latest stable version of CALDERA (recursively, of course).
2. Another common reason for this is running CALDERA from < Python 3.6.1.

### I start an agent but cannot see it from the server!

1. Check that the firewall is open, allowing network connections, between the remote computer running the agent and the server itself. 
2. Ensure you are serving CALDERA on all interfaces (0.0.0.0). 
3. If you are running the agent on Windows, our default agent assumes it is a 64-bit system. If you are running 32-bit, you'll need to recompile the Windows agent to use it. 

### I'm seeing issues in the browser - things don't seem right!

1. Are you using Chrome or Safari? These are the only supported/tested browsers. All other ones are use-at-your-own-risk.

### I see a 404 when I try to download conf.yml!

1. The conf.yml file is only relevant to pre-CALDERA 2.0. You should go to the README page and follow the instructions to run one of the missions. 

### I ran an adversary and it didn't do everything!

1. Check each ability on the adversary profile. It should show an icon for which operating system it runs on. Match this up with the operating systems of your agents. These are the only abilities an operation will attempt to run.
2. Look at each ability command. If there is a variable inside - shown by #{} syntax - the ability will need to be ["unlocked" by another ability](Learning-the-terminology.html#what-is-an-ability), in a prior step, before it can run. 

### I can't open files on the server
1. Files are encrypted by default and can be decrypted with the following utility: <https://github.com/mitre/caldera/blob/master/app/utility/file_decryptor.py> 

### I'm getting this GO error when I run my server!
```
can't load package: package github.com/google/go-github/github: cannot find package "github.com/google/go-github/github" in any of:
	/usr/local/go/src/github.com/google/go-github/github (from $GOROOT)
	/home/debian/go/src/github.com/google/go-github/github (from $GOPATH)
```

1. Check to see if GO is properly installed on your system.
2. Make sure the go environment variables are properly set. Add the following line to your `/etc/profile`:
```
export PATH=$PATH:/usr/local/go/bin
````
3. Run the following GO commands:
```
go get -u github.com/google/go-github/github
go get -u golang.org/x/oauth2
```
