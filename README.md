# Shark Tank

## Prerequisites

- Python (3.13 or later)
- uv
- A Slack workspace where you have permissions to install apps

## Setting up the Slack App

1. Go to [https://api.slack.com/apps](https://api.slack.com/apps) and click "Create New App".
2. Choose "From an app manifest" and select your workspace.
3. Copy and paste the manifest in `manifest.yml`
4. Review and create the app.
5. In the "Basic Information" section, note down the `App Id`, `Client Id`, `Client Secret`, `Signing Secret` .
6. Go to "OAuth & Permissions" and install the app to your workspace. Note down the "Bot User OAuth Token".

## Setting up the Project

1. Install dependencies:

   ```
   uv sync
   source .venv/bin/activate # for bash/zsh
   source .venv/bin/activate.fish # for fish
   source .venv/bin/activate.csh # for csh
   source .venv/bin/activate.ps1 # for powershell
   ```

4. Copy the `.env.sample` file to `.env`:

   ```
   cp .env.sample .env
   ```

5. Edit the `.env` file and fill in the values.


## Running the Application

1. Start your tunneling tool and expose the local server. (Not needed in socket mode with `SLACK_APP_TOKEN` set)

   Note the HTTPS URL you get.

2. Update your Slack app's request URLs:

   - Go to your Slack app's settings.
   - In "Event Subscriptions" and "Interactivity & Shortcuts", update the request URL to your HTTPS URL followed by `/slack/events`.
   - In "OAuth & Permissions", update `Redirect URLs` to your HTTPS URL followed by `/slack/oauth_redirect`.

3. Start the application:
   ```
   app
   ```

Your Slack app should now be running and connected to your Slack workspace!
If you're adding commands, your commands in development will be prefixed with `/dev-COMMAND`. When deploying your app, you *must* set the `ENVIRONMENT` env var to `production`.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

# Shark

## Moods

- Abused
- Happy
- Neutral
- Sad
- Abandonment
    - Sends DMs to the last person that talked to it begging to come back because shark misses you :c

## Mechanisms

- Hunger
  - Int 1-100
  - If it gets too hungry it eats you and you have to start again
- Health
  - Int 1-100
  - Hygene, you have to clean it every
