# 🚀 Complete Setup Guide - Bot Management Dashboard

**One Document to Rule Them All**

*TheRealPourya Team - Version 1.0.0*

---

## 📋 Table of Contents

1. [Introduction](#introduction)
2. [Installation Options](#installation-options)
3. [For End Users - Using the EXE](#for-end-users)
4. [For Developers - Running from Source](#for-developers)
5. [Building the Executable](#building-the-executable)
6. [Using the Dashboard](#using-the-dashboard)
7. [Troubleshooting](#troubleshooting)
8. [Advanced Topics](#advanced-topics)
9. [FAQ](#faq)

---

## Introduction

### What is Bot Management Dashboard?

A modern Windows application that lets you manage and run multiple bots from one beautiful interface.

**Key Features:**
- ✅ Manage unlimited bots (Python, Node.js, etc.)
- ✅ Run bots in PowerShell with one click
- ✅ Beautiful modern web interface
- ✅ Dark/Light theme support
- ✅ Search, filter, and organize bots
- ✅ Pin important bots
- ✅ Drag & drop reordering

### Who is This For?

- **Bot Developers** - Manage Discord, Telegram, Twitter bots
- **Automation Engineers** - Control automation scripts
- **Developers** - Manage any command-line applications
- **Anyone** - Who runs multiple scripts/programs

---

## Installation Options

### Option A: Use Pre-built EXE (Recommended for Users)
- Download `BotManager.exe`
- No Python required
- No installation needed
- Just double-click and go!

### Option B: Run from Source (For Developers)
- Requires Python 3.8+
- Full control over code
- Can modify and customize
- See development section below

### Option C: Build Your Own EXE (For Distributors)
- Build from source
- Create custom versions
- Package for distribution
- See building section below

---

## For End Users

### Step 1: Get the Application

**If you have BotManager.exe:**
- You're ready to go! Skip to Step 2.

**If you have the source code:**
- Continue to "For Developers" section

### Step 2: First Run

1. **Double-click** `BotManager.exe`
2. **Wait** for the console window to open (shows "Starting Flask server...")
3. **Browser opens automatically** to the dashboard
4. If browser doesn't open, go to: `http://127.0.0.1:5000`

### Step 3: Add Your First Bot

1. Click the purple **"+ Add Bot"** button (top left)

2. Fill in the form:
   - **Bot Name**: Give it a memorable name
     - Example: "My Discord Bot"
   
   - **Folder Path**: Full path to your bot's folder
     - Example: `C:\Users\YourName\Bots\DiscordBot`
     - Must be a valid Windows path
     - Use backslashes `\`
   
   - **Run Command**: Command to start your bot
     - For Python: `python bot.py` or `python main.py`
     - For Node.js: `node index.js` or `npm start`
     - For npm: `npm run dev` or `npm start`
     - Any command that works in that folder
   
   - **Notes**: (Optional) Add helpful information
     - Example: "Production Discord bot - requires .env file"
   
   - **Pin this bot**: Check to keep it at the top

3. Click **"Add Bot"**

### Step 4: Run Your Bot

1. Find your bot in the dashboard
2. Click the green **"Run"** button
3. A PowerShell window opens running your bot
4. Keep the PowerShell window open to keep bot running
5. Status changes to "Running" (green indicator)

### Step 5: Explore Features

**Search:** Type in the search bar to filter bots

**Open Folder:** Click the blue folder icon to access bot files

**Edit:** Click the yellow pencil icon to modify bot details

**Delete:** Click the red trash icon to remove a bot

**Pin/Unpin:** Click the pin icon to toggle pinned status

**Reorder:** Drag and drop cards to rearrange

**Theme:** Click moon/sun icon to toggle dark/light mode

**Run All:** Click "Run All" to start multiple bots at once

---

## For Developers

### Prerequisites

- Windows 10 or Windows 11
- Python 3.8 or higher
- Internet connection (for package installation)

### Step 1: Check Python Installation

Open Command Prompt and run:
```cmd
python --version
```

Should show: `Python 3.8.x` or higher

If not installed:
1. Download from https://www.python.org/
2. During installation, CHECK "Add Python to PATH"
3. Restart computer
4. Try again

### Step 2: Navigate to Project

Open Command Prompt:
```cmd
cd C:\path\to\botManager
```

### Step 3: Install Dependencies

**Automated (Recommended):**
```cmd
install.bat
```

**Manual:**
```cmd
pip install -r requirements.txt
```

This installs:
- Flask 3.0.0 (Web framework)
- Flask-CORS 4.0.0 (Cross-origin support)
- Werkzeug 3.0.1 (WSGI utilities)

### Step 4: Run the Application

**Option A - Automated:**
```cmd
run.bat
```

**Option B - Manual:**
```cmd
python app.py
```

**Option C - Alternative Python command:**
```cmd
py app.py
```

### Step 5: Access the Dashboard

Your browser should open automatically to:
```
http://127.0.0.1:5000
```

If not, manually open your browser and go to that address.

### Step 6: Stop the Application

Press `Ctrl+C` in the console window to stop the server.

---

## Building the Executable

### Why Build an EXE?

- Share with others who don't have Python
- Create standalone application
- Professional distribution
- No dependencies needed on target machine

### Prerequisites for Building

- Python 3.8+ installed
- All dependencies installed (`install.bat`)
- PyInstaller (`pip install pyinstaller`)

### Method 1: Automated Build (Easy!)

```cmd
build.bat
```

This script will:
1. Check Python installation
2. Install PyInstaller if needed
3. Clean previous builds
4. Build the executable
5. Prompt to copy EXE to current folder

**Result:** `dist\BotManager.exe` (20-30 MB)

### Method 2: Manual Build

**Step 1:** Install PyInstaller
```cmd
pip install pyinstaller
```

**Step 2:** Build with spec file
```cmd
pyinstaller --clean BotManager.spec
```

**Step 3:** Find your EXE
```
botManager\dist\BotManager.exe
```

### Method 3: Command Line Build

```cmd
pyinstaller --onefile ^
    --name BotManager ^
    --add-data "templates;templates" ^
    --add-data "static;static" ^
    --hidden-import flask ^
    --hidden-import flask_cors ^
    --hidden-import werkzeug ^
    --console ^
    app.py
```

### Testing Your Build

1. Navigate to `dist` folder
2. Double-click `BotManager.exe`
3. Verify:
   - Console opens
   - Server starts
   - Browser opens
   - Dashboard loads
   - Can add/edit/delete bots
   - Can run bots
   - Data persists after restart

### Distribution

Your `BotManager.exe` is now ready to distribute!

**Single File Distribution:**
- Just copy `BotManager.exe`
- Send via email, cloud storage, USB, etc.
- No other files needed!

**With Documentation:**
- Create a ZIP with:
  - `BotManager.exe`
  - `QUICKSTART.md`
  - `README.md` (optional)

---

## Using the Dashboard

### Dashboard Layout

```
┌──────────────────────────────────────────────┐
│  🤖 Bot Management Dashboard    ☀️  [X Bots] │
│     TheRealPourya Team                       │
├──────────────────────────────────────────────┤
│  [+ Add] [▶️ Run All] [🔄 Refresh]  [🔍___] │
├──────────────────────────────────────────────┤
│                                               │
│  ┌───────────┐  ┌───────────┐  ┌──────────┐ │
│  │ Bot Card  │  │ Bot Card  │  │ Bot Card │ │
│  └───────────┘  └───────────┘  └──────────┘ │
│                                               │
└──────────────────────────────────────────────┘
```

### Bot Card Explained

```
┌─────────────────────────────┐
│ 📌 Bot Name           [Pin] │  ← Name & Pin status
│ ● Running                   │  ← Status indicator
├─────────────────────────────┤
│ Path: C:\Bots\MyBot        │  ← Folder location
│ Command: python main.py    │  ← Run command
│ Notes: My awesome bot      │  ← Description
├─────────────────────────────┤
│ [▶️ Run] [📂 Folder]        │  ← Actions
│ [✏️ Edit] [🗑️ Delete]       │
└─────────────────────────────┘
```

### Common Actions

#### Add a Bot
1. Click **"+ Add Bot"**
2. Fill form
3. Click **"Add Bot"**

#### Edit a Bot
1. Click **yellow pencil icon** on bot card
2. Modify fields
3. Click **"Save Changes"**

#### Delete a Bot
1. Click **red trash icon**
2. Confirm deletion
3. Bot is removed (data deleted)

#### Run a Bot
1. Click **green "Run"** button
2. PowerShell window opens
3. Bot starts executing
4. Status changes to "Running"

#### Stop a Bot
- Close the PowerShell window manually
- Or click Stop button (if implemented)

#### Open Bot Folder
1. Click **blue folder icon**
2. Windows Explorer opens to bot's directory

#### Pin/Unpin Bot
1. Click **pin icon** (top right of card)
2. Pinned bots stay at top
3. Click again to unpin

#### Search for Bots
1. Type in search bar (top right)
2. Results filter in real-time
3. Searches: name, path, command, notes

#### Reorder Bots
1. Click and hold **grip icon** (⋮⋮)
2. Drag to new position
3. Release to drop
4. Order is saved automatically

#### Toggle Theme
1. Click **moon/sun icon** (top right)
2. Switches between dark/light mode
3. Preference saved in browser

#### Run All Bots
1. Click **"Run All"** button
2. Confirm action
3. All bots start in separate PowerShell windows

---

## Troubleshooting

### Application Issues

#### Problem: "Python is not recognized"
**Symptom:** Error when running scripts

**Solution:**
1. Install Python from https://python.org
2. During install, CHECK "Add Python to PATH"
3. Restart computer
4. Open new Command Prompt
5. Try: `python --version`

#### Problem: "Port 5000 already in use"
**Symptom:** Server won't start, port conflict

**Solution:**
1. Close other applications using port 5000
2. Or kill the process:
   ```cmd
   netstat -ano | findstr :5000
   taskkill /PID <PID> /F
   ```
3. Or change port in `app.py`:
   ```python
   app.run(host="127.0.0.1", port=5001, debug=False)
   ```

#### Problem: Browser doesn't open automatically
**Symptom:** Server starts but no browser

**Solution:**
- Manually open browser
- Go to: `http://127.0.0.1:5000`
- Check if default browser is set

#### Problem: Dashboard loads but shows errors
**Symptom:** 404 errors, missing templates

**Solution:**
1. Verify `templates` folder exists
2. Verify `templates/index.html` exists
3. Rebuild if using EXE
4. Check console for specific errors

### Bot Execution Issues

#### Problem: Bot won't run
**Symptom:** Click Run, nothing happens or error

**Solution:**
1. Verify **Folder Path** exists and is correct
2. Check **Run Command** is valid
3. Test command manually in PowerShell:
   - Open PowerShell
   - `cd "C:\Path\To\Bot"`
   - Run your command
4. Check bot's dependencies are installed
5. Verify Python/Node.js is installed if needed

#### Problem: Bot starts but closes immediately
**Symptom:** PowerShell window flashes and closes

**Solution:**
1. Check bot for errors
2. Run manually to see error messages
3. Verify all required files exist
4. Check environment variables
5. Ensure dependencies installed

#### Problem: Multiple PowerShell windows
**Symptom:** Too many windows open

**Solution:**
- Each bot runs in its own window (by design)
- Close windows to stop bots
- Consider consolidating bots

### Build Issues

#### Problem: PyInstaller not found
**Symptom:** Command not recognized

**Solution:**
```cmd
pip install pyinstaller
```

#### Problem: Build fails with "Module not found"
**Symptom:** Import errors during build

**Solution:**
1. Install all dependencies:
   ```cmd
   pip install -r requirements.txt
   ```
2. Add to hidden imports in `BotManager.spec`:
   ```python
   hiddenimports=['missing_module'],
   ```

#### Problem: EXE built but won't run
**Symptom:** EXE exists but crashes

**Solution:**
1. Run from Command Prompt to see errors:
   ```cmd
   dist\BotManager.exe
   ```
2. Check `templates` folder included
3. Check `static` folder included
4. Rebuild with `--clean`:
   ```cmd
   pyinstaller --clean BotManager.spec
   ```

#### Problem: Antivirus blocks/deletes EXE
**Symptom:** File disappears or won't run

**Solution:**
1. Add exception in antivirus
2. This is common with PyInstaller EXEs
3. For distribution, consider code signing
4. Build on clean VM

### Data Issues

#### Problem: Bots disappear after restart
**Symptom:** Data not persisting

**Solution:**
1. Check data folder exists:
   `C:\Users\<YourName>\BotManager\data\`
2. Check write permissions
3. Look for `bots.json` file
4. Check file isn't corrupted (valid JSON)

#### Problem: Can't edit or delete bots
**Symptom:** Actions don't work

**Solution:**
1. Check browser console for errors (F12)
2. Verify API endpoints working
3. Check file permissions
4. Restart application

---

## Advanced Topics

### Customization

#### Change Server Port
Edit `app.py`, find:
```python
app.run(host="127.0.0.1", port=5000, debug=False)
```
Change `5000` to your preferred port.

#### Add Custom Icon to EXE
1. Get a `.ico` file
2. Save as `icon.ico` in project folder
3. Edit `BotManager.spec`:
   ```python
   icon='icon.ico',
   ```
4. Rebuild

#### Modify Theme Colors
Edit `templates/index.html`, find CSS variables:
```css
.gradient-bg {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}
```

### Security Considerations

**Current Security Model:**
- Localhost-only (127.0.0.1)
- No authentication
- Direct command execution
- User-space file operations

**Recommendations:**
- ⚠️ Do NOT expose to internet
- ⚠️ Only add trusted bot commands
- ⚠️ Run with standard user account (no admin)
- ⚠️ Keep on local network only

**For Network Deployment:**
- Add authentication system
- Use HTTPS
- Implement command whitelisting
- Add user permissions

### Performance Optimization

**Reduce EXE Size:**
1. Enable UPX compression (already in spec)
2. Exclude unused packages
3. Strip debug symbols

**Improve Startup Time:**
1. Use `--onefile` (already default)
2. Exclude unnecessary imports
3. Optimize Python code

### Creating an Installer

**Option 1: Inno Setup (Free)**
1. Download from https://jrsoftware.org/isinfo.php
2. Create script for:
   - Installing EXE
   - Creating shortcuts
   - Adding to Start Menu
   - Uninstaller

**Option 2: NSIS (Free)**
1. Download from https://nsis.sourceforge.io/
2. Similar to Inno Setup
3. More customizable

### Environment Variables

To use environment variables in bot commands:
```
Command: set TOKEN=xxx && python bot.py
```

Or use a batch file:
```
Command: start.bat
```

---

## FAQ

### General Questions

**Q: Do end users need Python installed?**
A: No! The EXE includes everything needed.

**Q: What Windows versions are supported?**
A: Windows 10 and Windows 11 (64-bit).

**Q: Can I use this on Mac or Linux?**
A: Not currently. This is Windows-specific due to PowerShell integration.

**Q: Is this free?**
A: Yes! MIT License - free to use and modify.

**Q: Can I sell/distribute this?**
A: Yes, under MIT License terms.

### Usage Questions

**Q: How many bots can I manage?**
A: Unlimited! Performance depends on your system.

**Q: Can I run bots on startup?**
A: Not automatically, but you can add BotManager.exe to Windows startup.

**Q: Where is my data stored?**
A: `C:\Users\<YourName>\BotManager\data\bots.json`

**Q: Can I backup my bots?**
A: Yes, just copy the `bots.json` file.

**Q: Can I import/export bot configurations?**
A: Currently manual (copy JSON), feature planned for future.

### Technical Questions

**Q: Why does each bot open a new window?**
A: By design - allows you to see bot output and close individually.

**Q: Can I run bots in background?**
A: Not currently. PowerShell windows are visible by design.

**Q: Does this work with virtual environments?**
A: Yes! Use full path to venv Python:
```
Command: C:\Bots\MyBot\venv\Scripts\python.exe main.py
```

**Q: Can I pass arguments to bots?**
A: Yes! Include in command:
```
Command: python bot.py --arg value
```

**Q: How do I update the dashboard?**
A: Download new version, replace old EXE. Data is preserved.

---

## Summary Checklist

### For End Users
- [ ] Download or receive `BotManager.exe`
- [ ] Double-click to run
- [ ] Add your bots
- [ ] Run and manage bots
- [ ] Enjoy! 🎉

### For Developers
- [ ] Install Python 3.8+
- [ ] Run `install.bat`
- [ ] Run `run.bat` or `python app.py`
- [ ] Customize if needed
- [ ] Build EXE with `build.bat`

### For Distributors
- [ ] Build EXE successfully
- [ ] Test on clean Windows machine
- [ ] Create documentation package
- [ ] Consider creating installer
- [ ] Distribute!

---

## Resources

### Included Files
- `app.py` - Backend server
- `templates/index.html` - Frontend UI
- `requirements.txt` - Dependencies
- `run.bat` - Quick launcher
- `install.bat` - Dependency installer
- `build.bat` - EXE builder
- `BotManager.spec` - Build configuration

### Documentation
- `START_HERE.md` - Entry point
- `QUICKSTART.md` - Quick guide
- `README.md` - Full documentation
- `STEP_BY_STEP_PACKAGING.md` - Build guide
- `PACKAGING_GUIDE.md` - Advanced packaging
- `PROJECT_SUMMARY.md` - Overview
- `CHANGELOG.md` - Version history

### External Resources
- Python: https://www.python.org/
- Flask: https://flask.palletsprojects.com/
- PyInstaller: https://pyinstaller.org/
- TailwindCSS: https://tailwindcss.com/
- Alpine.js: https://alpinejs.dev/

---

## Support

**Need Help?**
1. Check this guide first
2. Read relevant documentation
3. Check troubleshooting section
4. Verify all files are present
5. Try rebuilding from scratch

**Found a Bug?**
- Document the issue
- Include error messages
- Note steps to reproduce
- Check if others have same issue

---

## Final Notes

**This is a complete, production-ready application!**

Everything you need is included:
✅ Full-featured backend
✅ Beautiful modern UI
✅ Comprehensive documentation
✅ Easy packaging
✅ Ready to use or distribute

**No additional setup or configuration required!**

---

**Thank you for using Bot Management Dashboard!** 🤖

**Developed with ❤️ by TheRealPourya Team**

---

*Version 1.0.0 - Windows 10/11 - MIT License*
*Last Updated: 2025*

**Happy Bot Managing! 🚀**