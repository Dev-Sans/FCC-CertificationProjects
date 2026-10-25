#User Configuration Manager: Source Code
def add_setting(dict1, tup):
    tup1 = tuple(i.lower() for i in tup)
    if tup1[0] in dict1.keys():
        return f"Setting '{tup1[0]}' already exists! Cannot add a new setting with this name."
    else:
        dict1[tup1[0]] = tup1[1]
        return f"Setting '{tup1[0]}' added with value '{tup1[1]}' successfully!"

def update_setting(dict1, tup2):
    tup1 = ()
    for i in tup2:
        tup1 += (i.lower(),)
    if tup1[0] in dict1:
        dict1[tup1[0]] = tup1[1]
        return f"Setting '{tup1[0]}' updated to '{tup1[1]}' successfully!"
    else:
        return f"Setting '{tup1[0]}' does not exist! Cannot update a non-existing setting."

def delete_setting(dict1, key):
    key = key.lower()
    if key in dict1.keys():
        dict1.pop(key)
        return f"Setting '{key}' deleted successfully!"
    else:
        return 'Setting not found!'

def view_settings(dict1):
    if len(dict1) == 0:
        return 'No settings available.'
    else:
        text = 'Current User Settings:\n'
        for key, val in dict1.items():
            text = text + key.capitalize() + ': ' + val + '\n'
        return text

test_settings = {'theme':'dark', 'notifications':'enabled', 'volume':'high'}
ts1 = {}

print(add_setting({'theme': 'light', 'language': 'English'}, ('THEME', 'dark')))

print(add_setting({'theme': 'light'}, ('volume', 'high')))

print(update_setting({'theme': 'light', 'language': 'English'}, ('theme', 'dark')))

print(update_setting({'theme': 'light'}, ('volume', 'high')))

print(delete_setting({'theme': 'light', 'language': 'English'}, 'theme'))

print(delete_setting({'theme': 'light', 'language': 'English'}, 'volume'))

print(view_settings(ts1))
print(view_settings(test_settings))
