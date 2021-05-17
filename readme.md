# Termino

Termino is a discord bot used for fun and moderation.

## NOTE:

This discord bot is still in development, so expect some errors to occur.

## To run this bot:
(You need python 3.5.3 or higher for this.)

The first and second procedures are optional, but I recommend you set up virtual environments so you can install the library needed locally in this repository instead of
installing them globally in your system (Which is bad since it's just going to bloat your system.).

### 1. Setting up the virtual environment:

In windows:

```bash
python -m venv termino
```

In linux/Mac:

```bash
python3 -m venv termino
```

### 2. Activating the virtual environment:

In windows:

```bash
virtualenv.bat
```

In Linux/Mac:

```bash
source virtualenv.sh
```

### 3. Installing discord.py:

In windows:

```bash
python -m pip install -U discord.py
```

In Linux/Mac:

```bash
python3 -m pip install -U discord.py
```

### 4. Running the script:

First, to run the script (bot.py), you will need to create token.txt in scripts/txt files/. Then you will put the token needed for your bot in token.txt.

Second, you will need to create data.json in the scripts directory.

Lastly, all you have to do is to type the following in the command line (Make sure your in the scripts directory):

In windows:

```bash
python bot.py
```

In Linux/Mac:

```bash
python3 bot.py
```

# Alright! Now you're all set and your bot is now ready to go!
