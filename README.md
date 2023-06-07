# Misc
Misc Programs

#For the python script:

This script is a Python script that looks at backing up large chunks of data and getting an idea of files, directories and roots that are being backed up monthly. 
There are Linux commands included within the script - Make sure that a linux environment is available. 

**Linux**
Following linux commands will be included in this python script: 
  `  du -h --max-depth=N`
   ` ls -slh `
    Note: It maybe necessary to include infront of the commands as they coudld fail otherwise

The commands will be ran the following way: 
    `cmd = '''sudo ls -slh %s'''%('/path/to/directory/tobeanalyzed')`
