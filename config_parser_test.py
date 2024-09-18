from ast import literal_eval
import configparser


file = """
[section]
name = test

"""
config = configparser.ConfigParser()
config.read_string(file)   

print(config['section']['name'])
print(config._sections)

                
class DynamicConfig:
    def __init__(self):
        pass

def generate_config_obj(conf:dict, config_obj: DynamicConfig = DynamicConfig()):
        if not isinstance(conf, dict):
            raise TypeError(f'dict expected, found {type(conf).__name__}')
    
        for key, value in conf.items():
            if isinstance(value, dict):
                obj = generate_config_obj(value)
                setattr(config_obj, key, obj)
            else:
                setattr(config_obj, key, value)
                
        return config_obj
    
    
        
config = generate_config_obj(config._sections)
print(config.section.name)
