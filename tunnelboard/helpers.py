import time

def get_os():
    import platform
    return platform.system()

def get_browser_driver(browser):

    osname = get_os()

    if osname == 'Darwin':

        browsers = {'firefox' : "open -a /Applications/Firefox.app %s",
                    'chrome' : 'open -a /Applications/Google\ Chrome.app %s',
                    'edge': 'open -a /Applications/Microsoft\ Edge.app %s',
                    'safari': 'open -a /Applications/Safari.app %s'}
 
        return browsers[browser]

def close_instance(client):
    try:
        response = client.run('tmux kill-session -t tmuxboard')
    except: 
        pass

def start_session(client, executable, dictionary):
    string = ''
    for key, value in dictionary.items():
        string += f' --{key}={value}'
    command = '''tmux new-session -d -s tmuxboard {} {}'''.format(executable, string)
    result = client.run(command); time.sleep(2)
    return result


