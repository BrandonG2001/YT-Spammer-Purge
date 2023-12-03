from subprocess import Popen
from shutil import rmtree, copyfile
from os import path, environ, remove, getcwd

from warnings import filterwarnings
filterwarnings("ignore", category=UserWarning)

# Create function #
def create_exe(script_name, exe_name, log_level='FATAL', make_admin=False):
    command_list = [
                  "pyinstaller" ,
                  '-F',
                  f'{script_name}',
                  f'--paths="{environ["VIRTUAL_ENV"]}\\Lib\\site_packages"',
                  f'--log-level {log_level}',
                  '--clean',
                  f'--name="{exe_name}"',
                  ]
    if make_admin:
        command_list.insert(3, '--uac-admin')
        
        
    command = ''
    for command_part in command_list:
        command = command + command_part + ' '
    
    print(f'\nCreating {exe_name} executable\n')
    result = Popen(command)
    result.wait()
    print()
    print(f'Finished Creating {exe_name} EXE')
    print()
    
    
    # cleanup
    spec_file = exe_name + '.spec'
    if path.isfile(spec_file):
        remove(spec_file)
    
    # delete temporary build files
    if path.isdir('build'):
        rmtree('build')
    
    current_file = path.join(getcwd(), 'dist', exe_name + '.exe')    
    #desktop_path = path.join(environ['UserProfile'], 'Desktop')
    #copyfile(src=current_file, dst=path.join(desktop_path, exe_name+'.exe'))

if __name__ == '__main__':

    create_exe(script_name='"YTSpammerPurge multiple_channels.py"', exe_name='FULL YT Spam Purger', make_admin=False)
    

    