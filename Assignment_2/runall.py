import sys 
import os 
 
 
directory = 'a2test' 
if not os.path.exists(directory): 
     print('There is no directory named {}, giving up...'.format(directory)) 
     sys.exit() 
for filename in os.listdir(directory): 
     if not filename.endswith('.txt'): 
         continue 
     if 'output' in filename: 
         continue 
     print('running {}'.format(filename)) 
     os.system('python maze.py --file {} -print'.format(directory + '/' + filename)) 
     os.system('python maze.py --file {} >{}'.format(directory + '/' + filename, directory + '/' + filename.split('.')[0]+'_my_output.txt')) 
     os.system('fc {} {}'.format(directory + '\\' + filename.split('.')[0]+'_output.txt', directory + '\\' + filename.split('.')[0]+'_my_output.txt')) 
 
 
