import os
import re

# Location of ourselves
self_path = os.path.dirname(os.path.abspath(__file__))
desired_shell = os.getenv('SHELL', 'bash')


# Log to the console in pretty colors
def log(text):
    print(f'\033[1;95;48m 🐟 {text}\033[1;37;0m')


# Return ordered list of scripts found recursively in <path>
def get_ordered_scripts(path):
    script_paths = []

    for root, _, files in os.walk(path):
        for filename in files:
            if re.fullmatch('^[0-9]*-.*.sh$', filename) is None:
                continue
            file_path = os.path.join(root, filename)
            script_paths.append(file_path)
    script_paths.sort(key=lambda script: os.path.basename(script))
    return script_paths


# Execute a shell script given a <path>
def consume_script(script_path):
    script_base_path = os.path.dirname(script_path)
    os.chdir(script_base_path)
    os.system(f'{desired_shell} {script_path}')


def main():
    cwd = os.getcwd()
    script_paths = get_ordered_scripts(cwd)
    for script_path in script_paths:
        log(f'Consuming: {script_path}')
        consume_script(script_path)


if __name__ == "__main__":
    os.chdir(self_path)
    main()
