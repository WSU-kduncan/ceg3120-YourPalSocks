## Discord Bot CEG3120 Project 1
### Ethan Heinlein
A simple discord bot that posts various text and image messages via different commands. Built on the discord python library v2.0.1
(btw the branch made for this project is the "discord-bot-v1" branch.

---
## Dependencies
- Python3
- Pip
- discord.py (v2.0.1)

> python3 pip -U install discord.py
- dotenv

> python3 pip -U install python-dotenv

---
## Setup
1. Open your [bot's page](https://discord.com/developers/applications) in the Discord developer portal
2. Navigate to the **Bot** tab and copy your token. This token will need to be reset after changing the bot settings.
3. In the project directory, create a new file named **.env**. Inside, paste this code and include your bot's token:

`DISCORD_TOKEN: <YOUR TOKEN HERE>`

---
## Usage
Below are the different commands the bot responds to once connected to a server:

> **!help** -- Lists all possible commands

> **!joke** -- Creates two text messages: a joke setup and punchline

> **!myreaction** -- Creates an image message from an array of possible reactions

> **!kill** -- Stops the bot instance (only used to get control of my console back)
---
## R&D
This bot is hosted locally, so when the machine running it shuts down the bot shuts down as well. Most discord bots are always on though, so how do developers do this without just leaving their machine on 24/7?

Like websites or other resources that must be on at all times, discord bots can be hosted on online platforms to keep them running without the machine being on. Below are some different platforms:

- [Google Cloud](https://cloud.google.com/blog/topics/developers-practitioners/build-and-run-discord-bot-top-google-cloud): The cloud can run a VM of linux that can clone and  the repository.
- [AWS](https://brianmorrison.me/blog/deploy-your-discord-bot-to-aws): This platform can be used nearly identically to Google Cloud, but now use AWS instead.
- [XGamingServer](https://xgamingserver.com/discord-bot-hosting): While I usually detest anything with "gaming" in the title as a sales gimmick, this platform is build with video game server hosting in mind. That said they do have a pretty cheap discord bot hosting option as well. This option also has some special tools made for managing discord bots.
- [Heroku](https://www.heroku.com/): A neat option I found that can deploy a bot straight from a Github repository!

Servers are computers, and thus have storage. Considering most servers use linux in some form, the dependencies and repository can theoretically be installed and the Bot can be run from the server.
