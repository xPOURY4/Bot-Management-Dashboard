
# Bot Management Dashboard
**Developed by TheRealPourya Team**
A modern, production-ready Windows desktop application for managing and running multiple bots (Python, Node.js, or any command-line based bots) from a beautiful web-based dashboard.

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Platform](https://img.shields.io/badge/platform-Windows%2010%2F11-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)
![Winget](https://img.shields.io/badge/winget-available-0078D4)
![PyPI](https://img.shields.io/badge/pypi-1.0.0-blue)

---

## ✨ Features
- 🤖 **Manage Multiple Bots** – Add, edit, delete, and organize unlimited bots
- ▶️ **Run in PowerShell** – Execute bots in separate PowerShell windows
- 📁 **Quick Folder Access** – Open bot directories directly from the dashboard
- 📌 **Pin Important Bots** – Keep frequently used bots at the top
- 🔍 **Search & Filter** – Quickly find bots by name, path, command, or notes
- 🎨 **Modern UI** – Beautiful, responsive interface with dark/light theme
- 🖱️ **Drag & Drop** – Reorder bots with intuitive drag and drop
- 💾 **Persistent Storage** – All settings saved locally in JSON format
- 🚀 **Run All Bots** – Start multiple bots simultaneously with one click
- 📊 **Status Tracking** – See which bots are running or stopped
- 🎯 **Zero Configuration** – Works out of the box after installation

---

## 📋 Requirements
- **Windows 10 or Windows 11**
- **Python 3.8 or higher** (for running from source)
- **PowerShell** (pre-installed on Windows)

---

## 🚀 Installation

### **Option 1: Install via Winget (Recommended for Windows Users)** coming soon
The easiest way to install **Bot Management Dashboard** on Windows is using **Winget**, the Windows Package Manager.

1. Open **Command Prompt** or **PowerShell**.
2. Run the following command:
   ```bash
   winget install TheRealPourya.BotManager
   ```
3. The application will be installed automatically, and you can launch it from the Start Menu.

---

### **Option 2: Install via PyPI (For Python Users)**
You can also install the application globally using **pip**:

1. Open **Command Prompt** or **PowerShell**.
2. Run the following command:
   ```bash
   pip install botmanager
   ```
3. After installation, launch the application by running:
   ```bash
   botmanager
   ```
   The dashboard will open in your default web browser at `http://127.0.0.1:5000`.

---

### **Option 3: Running from Source**
If you prefer to run the application from the source code:

#### 1. Install Dependencies
```bash
cd botManager
pip install -r requirements.txt
```

#### 2. Run the Application
**Option A: Using Python directly**
```bash
python app.py
```
**Option B: Using the batch file**
```bash
run.bat
```
The dashboard will automatically open in your default web browser at `http://127.0.0.1:5000`.

---

### **Option 4: Building as a Standalone .EXE**
To create a single `.exe` file for distribution:

#### 1. Install PyInstaller
```bash
pip install pyinstaller
```

#### 2. Build the Executable
**Option A: Using the spec file (Recommended)**
```bash
pyinstaller BotManager.spec
```
**Option B: Using command line**
```bash
pyinstaller --onefile --name BotManager --add-data "templates;templates" --add-data "static;static" --hidden-import flask --hidden-import flask_cors --console app.py
```

#### 3. Locate Your Executable
After building, find your executable at:
```
botManager\dist\BotManager.exe
```

#### 4. Distribution
You can now distribute `BotManager.exe` to any Windows 10/11 computer. No Python installation is required on the target machine!
**Note:** The data folder will be automatically created at:
```
C:\Users\<USERNAME>\BotManager\data\
```

---

## 📖 User Guide
### Adding a New Bot
1. Click the **"Add Bot"** button.
2. Fill in the required fields:
   - **Bot Name**: A descriptive name for your bot.
   - **Folder Path**: Full path to the bot's directory (e.g., `C:\Bots\MyBot`).
   - **Run Command**: Command to execute (e.g., `python main.py`, `node index.js`, `npm start`).
   - **Notes**: Optional description or important information.
   - **Pin**: Check to keep this bot at the top.
3. Click **"Add Bot"** to save.

### Running Bots
- **Single Bot**: Click the green **"Run"** button on any bot card.
- **All Bots**: Click the **"Run All"** button in the action bar.
- Each bot opens in its own PowerShell window.
- The bot status will update to show **"Running"**.

### Managing Bots
- **Edit**: Click the yellow edit icon (✏️) to modify bot details.
- **Delete**: Click the red trash icon (🗑️) to remove a bot.
- **Open Folder**: Click the blue folder icon (📂) to open the bot's directory.
- **Pin/Unpin**: Click the pin icon (📌) to toggle pinned status.
- **Reorder**: Drag and drop bot cards to rearrange them.

### Search and Filter
Use the search bar to quickly find bots by:
- Bot name
- Folder path
- Run command
- Notes content

### Theme
Toggle between light and dark mode using the sun/moon icon in the header.

---

## 🗂️ Project Structure
```
botManager/
├── app.py                  # Flask backend server
├── requirements.txt        # Python dependencies
├── run.bat                 # Windows batch launcher
├── BotManager.spec         # PyInstaller configuration
├── README.md               # This file
├── templates/
│   └── index.html          # Main dashboard UI
├── static/
│   ├── css/                # (Reserved for custom CSS)
│   └── js/                 # (Reserved for custom JS)
└── data/
    └── bots.json           # Bot configuration storage
```

---

## 💾 Data Storage
Bot configurations are stored in:
```
C:\Users\<USERNAME>\BotManager\data\bots.json
```
The file is automatically created on first run with example bots. You can manually edit this JSON file if needed.

### Bot JSON Structure
```json
{
  "id": "unique-uuid",
  "name": "Bot Name",
  "path": "C:\\Path\\To\\Bot",
  "command": "python main.py",
  "notes": "Optional description",
  "pinned": false,
  "order": 0
}
```

---

## 🔧 Configuration
### Changing the Server Port
Edit `app.py`, line at the bottom:
```python
app.run(host="127.0.0.1", port=5000, debug=False)
```
Change `5000` to your desired port.

### Disabling Auto-Browser Launch
Comment out or remove this line in `app.py`:
```python
threading.Thread(target=open_browser, daemon=True).start()
```

---

## 🐛 Troubleshooting
### "Python not found" Error
Make sure Python is installed and added to your system PATH:
1. Download Python from [python.org](https://www.python.org/).
2. During installation, check **"Add Python to PATH"**.
3. Restart your terminal/command prompt.

### Bot Won't Run
- Verify the **Folder Path** exists and is correct.
- Check that the **Run Command** is valid for that directory.
- Ensure necessary dependencies are installed in the bot's environment.
- Check the PowerShell window for error messages.

### Port Already in Use
If port 5000 is occupied:
1. Close the application using that port.
2. Or change the port in `app.py` (see Configuration section).

### .EXE Build Fails
- Ensure all dependencies are installed: `pip install -r requirements.txt`.
- Try upgrading PyInstaller: `pip install --upgrade pyinstaller`.
- Check that `templates` and `static` folders exist.

### Browser Doesn't Open Automatically
Manually navigate to: `http://127.0.0.1:5000` in your web browser.

---

## 🛠️ Development
### Tech Stack
- **Backend**: Python 3, Flask, Flask-CORS
- **Frontend**: HTML5, TailwindCSS, Alpine.js
- **Drag & Drop**: SortableJS
- **Icons**: Font Awesome 6
- **Packaging**: PyInstaller

### Running in Development Mode
To enable Flask debug mode, edit `app.py`:
```python
app.run(host="127.0.0.1", port=5000, debug=True)
```

### Adding Custom Styles
Add CSS files to `static/css/` and link them in `templates/index.html`.

### Adding Custom JavaScript
Add JS files to `static/js/` and include them in `templates/index.html`.

---

## 🔐 Security Notes
- This application is designed for **local use only**.
- The Flask server binds to `127.0.0.1` (localhost) by default.
- Do **NOT** expose this server to the internet without proper security measures.
- Bot commands are executed directly in PowerShell—only add trusted bots.

---

## 📝 API Endpoints
The dashboard uses the following REST API:

| Method | Endpoint          | Description                     |
|--------|-------------------|---------------------------------|
| GET    | `/api/bots`       | Get all bots                    |
| POST   | `/api/bots`       | Add a new bot                   |
| PUT    | `/api/bots/:id`   | Update a bot                    |
| DELETE | `/api/bots/:id`   | Delete a bot                    |
| POST   | `/api/bots/:id/run` | Run a specific bot            |
| POST   | `/api/bots/:id/stop` | Stop a running bot           |
| POST   | `/api/bots/:id/open-folder` | Open bot folder |
| POST   | `/api/bots/run-all` | Run all bots                |
| POST   | `/api/bots/reorder` | Reorder bots               |

---

## 🤝 Contributing
This is a complete, production-ready application. Feel free to:
- Fork and modify for your needs.
- Add new features.
- Improve the UI/UX.
- Submit pull requests.

---

## 📄 License
MIT License – Feel free to use, modify, and distribute.

---

## 👨‍💻 Developer
**TheRealPourya Team**
Built with ❤️ for the bot management community.

---

## 🎯 Version History
### v1.0.0 (Current)
- ✅ Initial release
- ✅ Full CRUD operations for bots
- ✅ PowerShell execution support
- ✅ Dark/Light theme
- ✅ Drag & drop reordering
- ✅ Search and filter
- ✅ Pin/Unpin functionality
- ✅ Run all bots feature
- ✅ Status tracking
- ✅ Modern responsive UI

---

## 🚀 Future Enhancements (Ideas)
- [ ] Bot scheduling (run at specific times)
- [ ] Log viewer for bot output
- [ ] Custom bot icons
- [ ] Import/Export bot configurations
- [ ] Multi-language support
- [ ] System tray integration
- [ ] Auto-restart on crash
- [ ] Resource monitoring (CPU, RAM)
- [ ] Bot grouping/categories

---
**Enjoy managing your bots! 🤖**
```
