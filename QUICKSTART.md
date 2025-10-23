# 🚀 Quick Start Guide

**Bot Management Dashboard - TheRealPourya Team**

---

## For End Users (Using the .EXE)

### Step 1: Run the Application

1. Double-click `BotManager.exe`
2. A console window will open showing the server status
3. Your default web browser will automatically open the dashboard
4. If the browser doesn't open, go to: `http://127.0.0.1:5000`

### Step 2: Add Your First Bot

1. Click the purple **"Add Bot"** button
2. Fill in the form:
   - **Bot Name**: Give your bot a name (e.g., "My Discord Bot")
   - **Folder Path**: The full path where your bot files are located
     - Example: `C:\Users\YourName\Documents\Bots\DiscordBot`
   - **Run Command**: The command to start your bot
     - For Python: `python bot.py` or `python main.py`
     - For Node.js: `node index.js` or `npm start`
     - For other: Any command that works in that folder
   - **Notes**: Add any helpful information (optional)
   - **Pin**: Check this to keep the bot at the top
3. Click **"Add Bot"**

### Step 3: Run Your Bot

1. Find your bot card in the dashboard
2. Click the green **"Run"** button
3. A PowerShell window will open running your bot
4. The bot status will change to "Running"

### Step 4: Manage Your Bots

- **Edit**: Click the yellow pencil icon to change bot details
- **Delete**: Click the red trash icon to remove a bot
- **Open Folder**: Click the blue folder icon to quickly access the bot's files
- **Pin/Unpin**: Click the pin icon to keep important bots at the top
- **Search**: Use the search bar to find bots quickly
- **Reorder**: Drag and drop cards to rearrange them

---

## For Developers (Running from Source)

### Step 1: Install Dependencies

```cmd
cd botManager
python -m pip install -r requirements.txt
```

Or simply run:
```cmd
install.bat
```

### Step 2: Start the Server

```cmd
python app.py
```

Or simply run:
```cmd
run.bat
```

### Step 3: Access the Dashboard

Open your browser and go to: `http://127.0.0.1:5000`

---

## Building Your Own .EXE

### Option 1: Using the Build Script (Easy)

```cmd
build.bat
```

Follow the prompts. Your executable will be in the `dist` folder.

### Option 2: Manual Build

```cmd
pip install pyinstaller
pyinstaller BotManager.spec
```

Find your `.exe` in the `dist` folder.

---

## Common Bot Examples

### Python Bot
- **Path**: `C:\Bots\MyPythonBot`
- **Command**: `python main.py`

### Node.js Bot
- **Path**: `C:\Projects\NodeBot`
- **Command**: `node index.js`

### NPM Project
- **Path**: `C:\Discord\MyBot`
- **Command**: `npm start`

### Batch Script
- **Path**: `C:\Scripts\AutomationBot`
- **Command**: `start.bat`

---

## Tips & Tricks

1. **Keep It Running**: Keep the console window open to keep the dashboard running
2. **Multiple Bots**: Run as many bots as you want simultaneously
3. **Quick Access**: Use the folder button to quickly access bot files
4. **Organization**: Use pins and reordering to organize your bots
5. **Dark Mode**: Toggle dark/light theme with the moon/sun icon
6. **Search Power**: Search works across names, paths, commands, and notes

---

## Troubleshooting

### Dashboard won't start
- Make sure no other program is using port 5000
- Check that Python is installed (for source version)
- Try running as Administrator

### Bot won't run
- Verify the folder path exists
- Check that the command is correct
- Make sure required software (Python, Node.js, etc.) is installed
- Look at the PowerShell window for error messages

### Can't find my bot
- Use the search bar
- Click "Refresh" to reload the list
- Check `C:\Users\YourName\BotManager\data\bots.json`

---

## Need Help?

- Read the full `README.md` for detailed information
- Check that your bot works when run manually first
- Verify all paths are correct and use backslashes (`\`) for Windows

---

**Enjoy managing your bots! 🤖**

*Developed by TheRealPourya Team*