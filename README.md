# Cowin Discord Bot

This Discord bot is designed to help users check COVID-19 vaccine availability in a specific area using the Cowin API. The bot provides real-time information about vaccine centers, slots, and other relevant details, allowing users to stay informed about vaccination opportunities.

## Setup

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/SoulDev07/Cowin-Bot.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Create a .env file having TOKEN of bot:
    ```markdown 
    TOKEN = 'your_bot_token'
    ```

4. Run the bot:

    ```bash
    python bot.py
    ```

## Usage
Simply type the command `cowin start pincode` or `/start pincode` in any text channel to get list of centres every 5 minutes.

## Built With

* [Python 3.12](https://www.python.org/)
* [discord.py](https://github.com/Rapptz/discord.py)

## License
See [LICENSE](LICENSE) for details.