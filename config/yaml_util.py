import yaml
import os


def load_yaml(file_name:str='config.yaml'):
    file_name=os.path.join(os.path.dirname(__file__),file_name)
    with open(file_name, 'r') as file:
        data=yaml.safe_load(file)
    return data


def dump_yaml(data:yaml, file_name:str='config.yaml'):
    file_name=os.path.join(os.path.dirname(__file__),file_name)
    with open(file_name,'w') as file:
        yaml.dump(data,file)

if __name__=='__main__':
    data=load_yaml()
    data['vivek']='kumar'
    dump_yaml(data)