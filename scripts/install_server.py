import os
import subprocess

def install_server(server_type='paper', version='latest'):
    if server_type == 'paper':
        os.makedirs('minecraft_server', exist_ok=True)
        os.chdir('minecraft_server')
        if version == 'latest':
            version = subprocess.getoutput("curl -s https://papermc.io/api/v2/projects/paper | jq -r '.versions[-1]'")
        build = subprocess.getoutput(f"curl -s https://papermc.io/api/v2/projects/paper/versions/{version} | jq -r '.builds[-1]'")
        download_url = f"https://papermc.io/api/v2/projects/paper/versions/{version}/builds/{build}/downloads/paper-{version}-{build}.jar"
        subprocess.run(["curl", "-o", "paper.jar", download_url])
        with open('eula.txt', 'w') as f:
            f.write('eula=true\n')
        with open('start.sh', 'w') as f:
            f.write('java -Xmx1024M -Xms1024M -jar paper.jar nogui\n')
        subprocess.run(["chmod", "+x", "start.sh"])

install_server()
