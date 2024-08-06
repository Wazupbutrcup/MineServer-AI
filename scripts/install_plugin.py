def install_plugin(plugin_name):
    plugins_dir = 'minecraft_server/plugins'
    os.makedirs(plugins_dir, exist_ok=True)
    plugin_url = f"https://api.spigotmc.org/legacy/update.php?resource={plugin_name}"
    plugin_jar = f"{plugins_dir}/{plugin_name}.jar"
    subprocess.run(["curl", "-o", plugin_jar, plugin_url])

install_plugin('EssentialsX')
install_plugin('LuckPerms')
