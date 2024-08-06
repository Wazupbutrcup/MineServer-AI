# MineServerAI

MineServerAI is an AI-driven solution to set up a Minecraft server from scratch. This project automates the server setup process, including installing server software, managing plugins, configuring settings, and providing a web interface for user customization.

## Features

- Automated Minecraft server installation (Spigot, Paper, or Fabric)
- Plugin installation and management
- Server configuration based on user preferences
- Web interface for easy configuration
- Customizable server properties
- Simple and easy-to-use setup process

## Project Structure

```
minecraft-server-setup/
├── README.md
├── scripts/
│   ├── install_server.py
│   ├── install_plugin.py
│   ├── configure_server_properties.py
│   ├── setup_server_with_preferences.py
│   └── start_server.sh
├── config/
│   ├── server_defaults.json
│   └── plugins.json
├── web/
│   ├── app.py
│   ├── templates/
│   │   └── index.html
│   └── static/
│       └── css/
│           └── style.css
├── requirements.txt
└── setup.sh
```

## Getting Started

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)
- curl (command-line tool for transferring data)
- jq (command-line JSON processor)

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/minecraft-server-setup.git
    cd minecraft-server-setup
    ```

2. Install Python dependencies:

    ```sh
    pip install -r requirements.txt
    ```

3. Run the setup script:

    ```sh
    ./setup.sh
    ```

4. Access the web interface:

    Open your browser and navigate to `http://127.0.0.1:5000`.

### Configuration

#### Web Interface

1. Fill out the form on the web interface with your server preferences:
    - Server Name
    - Max Players
    - Gamemode (Survival/Creative)
    - Difficulty (Peaceful/Easy/Normal/Hard)
    - Level Seed (optional)

2. Click the "Setup Server" button to start the setup process.

#### Manually Editing Configuration Files

1. Edit `config/server_defaults.json` to set default server properties.

    ```json
    {
        "server_name": "My Minecraft Server",
        "max_players": 20,
        "gamemode": "survival",
        "difficulty": "easy",
        "level_seed": "mycustomseed"
    }
    ```

2. Edit `config/plugins.json` to manage plugins.

    ```json
    {
        "plugins": [
            {
                "name": "EssentialsX",
                "url": "https://api.spigotmc.org/legacy/update.php?resource=9089"
            },
            {
                "name": "LuckPerms",
                "url": "https://api.spigotmc.org/legacy/update.php?resource=28140"
            }
        ]
    }
    ```

## Scripts

### install_server.py

Script to download and set up the Minecraft server.

### install_plugin.py

Script to download and install plugins.

### configure_server_properties.py

Script to configure the `server.properties` file based on user preferences or defaults.

### setup_server_with_preferences.py

Script to collect user preferences, configure the server, install plugins, and start the server.

### start_server.sh

Script to start the Minecraft server using the `start.sh` script.

## Web Interface

The web interface is built using Flask and provides a simple form for configuring the server. It includes the following files:

- `app.py`: Main Flask application.
- `templates/index.html`: HTML form for user input.
- `static/css/style.css`: CSS styles for the web interface.

## Requirements

List of required Python packages specified in `requirements.txt`:

```
Flask
requests
```

## Contributing

We welcome contributions! If you'd like to help improve MineServer-AI, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request on GitHub.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [SpigotMC](https://www.spigotmc.org/)
- [PaperMC](https://papermc.io/)
- [EssentialsX](https://github.com/EssentialsX/Essentials)
- [LuckPerms](https://github.com/lucko/LuckPerms)
- [Flask](https://flask.palletsprojects.com/)

## Support

For support, please open an issue on the GitHub repository.

## Donations

If you find MineServer-AI useful and would like to support its development, consider making a donation. Your support helps us improve and maintain the project.
[Donate on Ko-fi](https://ko-fi.com/wazupbutrcup)
[Donate on PayPal](https://www.paypal.com/donate/?business=6TUCF33LPY9K2&no_recurring=0&item_name=Development+and+Coding+Features&currency_code=USD)

## Contact

For any inquiries or feedback, please reach out to [your email](mailto:wazupbutrcup@gmail.com).