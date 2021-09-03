import yaml
import os

global config

def open_yaml(file):
    global config
    with open(file, 'r') as stream:
        try:
            config = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)


open_yaml('config.yml')

for step in config['steps']:
    for action in step['actions']:
        os.system(action['command'])