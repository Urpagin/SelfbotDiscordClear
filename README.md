# SelfbotDiscordClear

A neat Discord selfbot that allows the deletion of own messages.

## Table of contents

- [Installation](#installation)
- [Usage](#usage)
- [Common Errors](#common-errors)
- [Legal](#legal)

## Installation

### 🪟 Windows

1. Download the latest release [here](https://github.com/Urpagin/SelfbotDiscordClear/releases/latest)
2. Get your Discord token
    <details>
      <summary>How to get your Discord token</summary>
   <p><a href="https://www.youtube.com/watch?v=YEgFvgg7ZPI">https://www.youtube.com/watch?v=YEgFvgg7ZPI</a><br>
   <a href="https://www.youtube.com/watch?v=LnBnm_tZlyU">(mirror) https://www.youtube.com/watch?v=LnBnm_tZlyU</a></p>
    </details>
3. Paste your Discord token into the app's terminal
4. See [usage](#Usage)

### 🐧 Linux/Mac/Source 🍎

You'll need to build from source

1. Install [Python](https://www.python.org/downloads/) (at the time Python 3.10 is required)
2. Clone the repository <br>
   ```shell
   git clone https://github.com/Urpagin/SelfbotDiscordClear.git
   ```
3. Go in the directory SelfbotDiscordClear and install dependencies
   ```shell
   pip install -r requirements.txt
   ```
4. Launch the app
   ```shell
   python main.py
   ```
5. Get your token in the [Windows](#-windows) section then see [Usage](#usage)

## Usage

🛑 **`!clearr` not `!clear`, don't forget the 2 RR**


### ⚒️ How to use ⚒️

- `!clearr <amount> <links>`
    - `<amount>`: (integer) the amount of own messages to delete
    - `<links>`: (boolean) if true, deletes only messages containing links

### 📜 Examples 📜

- `!clearr 10 1` will delete 10 of your messages containing links
- `!clearr -1` will delete ALL of your messages (may take a long time)
- `!clearr -1 1` will delete ALL of you messages that contain links (may take a long time)

## Common errors

1. `WARNING  discord.gateway Gateway is ratelimited, waiting 57.50 seconds.`<br>
   You may not be able to delete any messages during the timespan specified, wait and it will pass.
2. `WARNING  discord.http We are being rate limited. DELETE https://discord.com/api/v9/channels/<id>/messages/<id> responded with 429. Retrying in 1.53 seconds.`<br>
   This is a non issue as mass deleting messages isn't the normal behavior of a user, wait and it will pass.

## Legal
Selfbots are against Discord's Terms of Service.<br>
> **Automating normal user accounts (generally called "self-bots") outside of the OAuth2/bot API is forbidden, and can result in an account termination if found.**<br>
> https://support.discord.com/hc/en-us/articles/115002192352-Automated-user-accounts-self-bots-
