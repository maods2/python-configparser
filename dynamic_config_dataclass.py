from dataclasses import dataclass
from typing import Any

@dataclass
class Param1Level2Config:
    sub_param1: str
    sub_param2: int

@dataclass
class Param2Level2Config:
    sub_param3: float
    sub_param4: bool

@dataclass
class Param1Level1Config:
    level2: Param1Level2Config

@dataclass
class Param2Level1Config:
    level2: Param2Level2Config

@dataclass
class NestedConfig:
    extra_param: int

@dataclass
class MainConfig:
    param1: Param1Level1Config
    param2: Param2Level1Config
    nested_config: NestedConfig

def generate_config_obj(conf: dict, config_class):
    config_obj = config_class(**{
        key: (
            generate_config_obj(value, config_class.__annotations__[key]) if isinstance(value, dict) 
            else value
        )
        for key, value in conf.items()
    })
    
    return config_obj

# Exemplo de dicionário de configuração com níveis aninhados
config_dict = {
    'param1': {
        'level2': {
            'sub_param1': 'string_value',
            'sub_param2': 20
        }
    },
    'param2': {
        'level2': {
            'sub_param3': 3.14,
            'sub_param4': True
        }
    },
    'nested_config': {
        'extra_param': 100
    }
}

# Gerando o objeto de configuração a partir do dicionário
config_obj = generate_config_obj(config_dict, MainConfig)
print(config_obj)
