test_settings = {
    'theme': 'dark',
    'notfications': 'enabeled',
    'volume': 'high'
}

# 1- Definir uma funcao add_setting: 
#   2 parametros = dicionario de configuracoes e uma tupla de (chave, valor) 
def add_setting(settings:dict, config: tuple):
    if not isinstance(settings, dict):
        return print("Error: settings must be a dict type")

    if not isinstance(config, tuple):
        return print("Error: config must be a tuple type")
    
    key, value = config
    if isinstance(key,str):
        key = key.lower()
    if isinstance(value, str):
        value = value.lower()

    if settings.get(key, None) != None:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings: dict, config: tuple):
    # Verifiac se eh dicionario
    if not isinstance(settings, dict):
        return print("Error: settings must be a dict type")
    # Verifica se eh tupla
    if not isinstance(config, tuple):
        return print("Error: config must be a tuple type")
    
    #transforma em letra minuscula se for str
    key, value = config
    if isinstance(key,str):
        key = key.lower()
    if isinstance(value, str):
        value = value.lower()
    
    if settings.get(key, None) == None:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
    else:
        settings.update([(key, value)])
        return f"Setting '{key}' updated to '{value}' successfully!"


def delete_setting(settings:dict,key):
    if not isinstance(settings, dict):
        return print("Error: settings must be a dict type")
    
    if not key:
        return print("Error: key must have a value")
    
    if isinstance(key,str):
        key = key.lower()

    result = settings.pop(key, None)
    if result == None:
        return f"Setting not found!"
    else:
        return f"Setting '{key}' deleted successfully!"

def view_settings(settings:dict):
    if not isinstance(settings, dict):
        return print("Error: settings must be a dict type")

    if not settings:
        return f"No settings available."
    
    else:
        message = ''
        for key, value in settings.items():
            if isinstance(key,str):
                key = key.title()
            if isinstance(value, str):
                value = value.lower()
            message += f"{key}: {value}\n"
        return "Current User Settings:\n"+message



print(add_setting(test_settings, ('bright', 75)))
print(test_settings)

print(update_setting(test_settings, ('bright', 20)))
print(test_settings)

print(delete_setting(test_settings, 'bright'))
print(test_settings)

print(view_settings(test_settings))