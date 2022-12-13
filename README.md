# memoryVol
A GUI-Based tool based on Volatility CLI-Based memory analysis and forensics tool

As a project, we have built a graphical user interface-based memory analysis tool, which 
is built on top of the CLI-based tool called “Volatility Framework.” This is going to be very user 
friendly to anyone who is using it. 

# how to install

You can get the source code by either downloading a stable release or cloning from github. To do the 
latter, type: 
$ git clone https://github.com/nuwandilsara/memoryVol
This will create a memoryVol folder that contains the source code and you can run memoryVol 
directory from there. 
If you're using the standalone Windows, Linux, or Mac executable, no installation is necessary - just 
run it from a command prompt. No dependencies are required, because they're already packaged 
inside the exe. 
If you're using the Pyinstaller (Windows-only) executable, double click and follow through with the 
installation instructions (which basically consists of clicking Next a few times and then Finish). You 
must already have a working Python 2.7. Also see below for the dependency libraries. 
If you downloaded the zip or tar source code archive (Windows, Linux, OSX) there are two ways to 
"install" the code: 
1. Extract the archive and run setup.py. This will take care of copying files to the right 
locations on your disk. Running setup.py is only necessary if you want to have access to the 
memoryVol namespace from other Python scripts, for example if you plan on importing 
memoryVol as a library. Pros: easy use as a library. Cons: more difficult to upgrade or 
uninstall.
