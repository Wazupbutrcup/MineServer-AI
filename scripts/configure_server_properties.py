def configure_server_properties():
    properties = {
        'server-name': 'My Minecraft Server',
        'max-players': 20,
        'gamemode': 'survival',
        'difficulty': 'easy',
        'level-seed': 'mycustomseed'
    }
    with open('minecraft_server/server.properties', 'w') as f:
        for key, value in properties.items():
            f.write(f"{key}={value}\n")

configure_server_properties()
