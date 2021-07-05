# EARNINGS CHECK & PR CHECK

## Command usage

| Command         | Description                                                                                |
|:----------------|:-------------------------------------------------------------------------------------------|
| *prcheck @user  | (Alias: *pr) The bot will return power rankings information about the mentioned user.      |
| *earnings @user | (Alias: *earningscheck) The bot will return earnings information about the mentioned user. |

## Adding the bot
**Use the following link**: https://discord.com/oauth2/authorize?client_id=861209215661637642&permissions=84992&scope=bot

## Self-hosting
1. Create a new application in the Discord Developer Portal and add a bot to the application.
2. Create a bot invite link under OAuth2 and join the bot to your server(s).
3. Clone the repository and create a .env file with the required environment variables.
4. Install the required packages using `pip install -r requirements.txt` and run the bot using `python3 main.py`

### Environment variables

| Key         | Value                                                                                  |
|:------------|:---------------------------------------------------------------------------------------|
| FNAPI_URL   | https://fortniteapi.io/v1/                                                             |
| FNR_URL     | https://api.fortniterankings.net/                                                      |
| FNT_URL     | https://api.fortnitetracker.com/v1/                                                    |
| BOT_TOKEN   | Your Discord bot token. You can find this under "bot" in the Discord Developer portal. |
| FNAPI_TOKEN | Create an account at https://fortniteapi.io/                                           |
| FNR_TOKEN   | Message iAgonyii#0232 on Discord to request one.                                       |
| FNT_TOKEN   | Create an app at https://tracker.gg/developers/apps                                    |
