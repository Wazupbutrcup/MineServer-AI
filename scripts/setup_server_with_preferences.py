def setup_server_with_preferences():
    # Get user preferences
    server_name = input("Enter server name: ")
    max_players = int(input("Enter max players: "))
    gamemode = input("Enter gamemode (survival/creative): ")
    difficulty = input("Enter difficulty (peaceful/easy/normal/hard): ")
    seed = input("Enter world seed (leave blank for random): ")

    # Apply preferences
    configure_server_properties(server_name, max_players, gamemode, difficulty, seed) # type: ignore
    install_plugin('EssentialsX') # type: ignore
    install_plugin('LuckPerms') # type: ignore
    # Start the server
    subprocess.run(["./start.sh"], cwd='minecraft_server') # type: ignore

setup_server_with_preferences()
