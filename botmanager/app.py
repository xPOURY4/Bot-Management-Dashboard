import os
import json
import subprocess
import uuid
import webbrowser
import threading
import time
from pathlib import Path
from flask import Flask, render_template, jsonify, request, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Get user's home directory and create BotManager data folder
USER_HOME = os.path.expanduser("~")
DATA_DIR = os.path.join(USER_HOME, "BotManager", "data")
BOTS_FILE = os.path.join(DATA_DIR, "bots.json")

# Ensure data directory exists
os.makedirs(DATA_DIR, exist_ok=True)

# Store running processes
running_processes = {}


def load_bots():
    """Load bots from JSON file"""
    if not os.path.exists(BOTS_FILE):
        # Create empty bots file - user must add bots manually
        empty_bots = []
        save_bots(empty_bots)
        return empty_bots

    try:
        with open(BOTS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading bots: {e}")
        return []


def save_bots(bots):
    """Save bots to JSON file"""
    try:
        with open(BOTS_FILE, "w", encoding="utf-8") as f:
            json.dump(bots, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error saving bots: {e}")
        return False


@app.route("/")
def index():
    """Serve the main dashboard"""
    return render_template("index.html")


@app.route("/icon/<path:filename>")
def serve_icon(filename):
    """Serve icon files"""
    icon_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon")
    return send_from_directory(icon_dir, filename)


@app.route("/favicon.ico")
def favicon():
    """Serve favicon as fallback"""
    icon_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon")
    return send_from_directory(
        icon_dir, "icon.ico", mimetype="image/vnd.microsoft.icon"
    )


@app.route("/api/bots", methods=["GET"])
def get_bots():
    """Get all bots"""
    try:
        bots = load_bots()
        # Sort by order, then by pinned status
        bots.sort(key=lambda x: (not x.get("pinned", False), x.get("order", 0)))

        # Add status information
        for bot in bots:
            bot["status"] = "running" if bot["id"] in running_processes else "stopped"

        return jsonify({"success": True, "bots": bots})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route("/api/bots", methods=["POST"])
def add_bot():
    """Add a new bot"""
    try:
        data = request.json

        # Validate required fields
        if not data.get("name") or not data.get("path") or not data.get("command"):
            return jsonify({"success": False, "error": "Missing required fields"}), 400

        bots = load_bots()

        # Create new bot
        new_bot = {
            "id": str(uuid.uuid4()),
            "name": data["name"],
            "path": data["path"],
            "command": data["command"],
            "notes": data.get("notes", ""),
            "pinned": data.get("pinned", False),
            "order": len(bots),
        }

        bots.append(new_bot)

        if save_bots(bots):
            return jsonify({"success": True, "bot": new_bot})
        else:
            return jsonify({"success": False, "error": "Failed to save bot"}), 500

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route("/api/bots/<bot_id>", methods=["PUT"])
def update_bot(bot_id):
    """Update an existing bot"""
    try:
        data = request.json
        bots = load_bots()

        # Find bot by ID
        bot_index = next((i for i, b in enumerate(bots) if b["id"] == bot_id), None)

        if bot_index is None:
            return jsonify({"success": False, "error": "Bot not found"}), 404

        # Update bot fields
        if "name" in data:
            bots[bot_index]["name"] = data["name"]
        if "path" in data:
            bots[bot_index]["path"] = data["path"]
        if "command" in data:
            bots[bot_index]["command"] = data["command"]
        if "notes" in data:
            bots[bot_index]["notes"] = data["notes"]
        if "pinned" in data:
            bots[bot_index]["pinned"] = data["pinned"]
        if "order" in data:
            bots[bot_index]["order"] = data["order"]

        if save_bots(bots):
            return jsonify({"success": True, "bot": bots[bot_index]})
        else:
            return jsonify({"success": False, "error": "Failed to save bot"}), 500

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route("/api/bots/<bot_id>", methods=["DELETE"])
def delete_bot(bot_id):
    """Delete a bot"""
    try:
        bots = load_bots()

        # Filter out the bot
        original_length = len(bots)
        bots = [b for b in bots if b["id"] != bot_id]

        if len(bots) == original_length:
            return jsonify({"success": False, "error": "Bot not found"}), 404

        # Stop the bot if it's running
        if bot_id in running_processes:
            try:
                running_processes[bot_id].terminate()
                del running_processes[bot_id]
            except:
                pass

        if save_bots(bots):
            return jsonify({"success": True})
        else:
            return jsonify({"success": False, "error": "Failed to save bots"}), 500

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route("/api/bots/<bot_id>/run", methods=["POST"])
def run_bot(bot_id):
    """Run a bot in PowerShell"""
    try:
        bots = load_bots()
        bot = next((b for b in bots if b["id"] == bot_id), None)

        if not bot:
            return jsonify({"success": False, "error": "Bot not found"}), 404

        # Check if path exists
        if not os.path.exists(bot["path"]):
            return jsonify(
                {"success": False, "error": f"Path does not exist: {bot['path']}"}
            ), 400

        # Prepare PowerShell command
        # Run the command in the bot's directory in a new PowerShell window
        ps_command = f'cd "{bot["path"]}"; {bot["command"]}; Write-Host "`nPress any key to exit..."; $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")'

        # Start PowerShell in a new window
        process = subprocess.Popen(
            ["powershell.exe", "-NoExit", "-Command", ps_command],
            creationflags=subprocess.CREATE_NEW_CONSOLE,
            cwd=bot["path"],
        )

        # Store the process
        running_processes[bot_id] = process

        return jsonify(
            {
                "success": True,
                "message": f"Bot '{bot['name']}' started in PowerShell",
                "pid": process.pid,
            }
        )

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route("/api/bots/run-all", methods=["POST"])
def run_all_bots():
    """Run all bots"""
    try:
        bots = load_bots()
        results = []

        for bot in bots:
            try:
                if not os.path.exists(bot["path"]):
                    results.append(
                        {
                            "bot_id": bot["id"],
                            "name": bot["name"],
                            "success": False,
                            "error": "Path does not exist",
                        }
                    )
                    continue

                ps_command = f'cd "{bot["path"]}"; {bot["command"]}; Write-Host "`nPress any key to exit..."; $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")'

                process = subprocess.Popen(
                    ["powershell.exe", "-NoExit", "-Command", ps_command],
                    creationflags=subprocess.CREATE_NEW_CONSOLE,
                    cwd=bot["path"],
                )

                running_processes[bot["id"]] = process

                results.append(
                    {
                        "bot_id": bot["id"],
                        "name": bot["name"],
                        "success": True,
                        "pid": process.pid,
                    }
                )

                # Small delay between starts
                time.sleep(0.5)

            except Exception as e:
                results.append(
                    {
                        "bot_id": bot["id"],
                        "name": bot["name"],
                        "success": False,
                        "error": str(e),
                    }
                )

        return jsonify({"success": True, "results": results})

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route("/api/bots/<bot_id>/stop", methods=["POST"])
def stop_bot(bot_id):
    """Stop a running bot"""
    try:
        if bot_id not in running_processes:
            return jsonify({"success": False, "error": "Bot is not running"}), 400

        process = running_processes[bot_id]
        process.terminate()
        del running_processes[bot_id]

        return jsonify({"success": True, "message": "Bot stopped"})

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route("/api/bots/<bot_id>/open-folder", methods=["POST"])
def open_folder(bot_id):
    """Open bot folder in Windows Explorer"""
    try:
        bots = load_bots()
        bot = next((b for b in bots if b["id"] == bot_id), None)

        if not bot:
            return jsonify({"success": False, "error": "Bot not found"}), 404

        path = bot["path"]

        # Check if path exists
        if not os.path.exists(path):
            return jsonify(
                {"success": False, "error": f"Path does not exist: {path}"}
            ), 400

        # Open in Explorer
        os.startfile(path)

        return jsonify({"success": True, "message": f"Opened folder: {path}"})

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route("/api/bots/reorder", methods=["POST"])
def reorder_bots():
    """Reorder bots"""
    try:
        data = request.json
        bot_ids = data.get("bot_ids", [])

        bots = load_bots()

        # Create a mapping of id to bot
        bot_map = {bot["id"]: bot for bot in bots}

        # Reorder and update order field
        reordered_bots = []
        for i, bot_id in enumerate(bot_ids):
            if bot_id in bot_map:
                bot = bot_map[bot_id]
                bot["order"] = i
                reordered_bots.append(bot)

        # Add any bots that weren't in the reorder list
        for bot in bots:
            if bot["id"] not in bot_ids:
                bot["order"] = len(reordered_bots)
                reordered_bots.append(bot)

        if save_bots(reordered_bots):
            return jsonify({"success": True})
        else:
            return jsonify({"success": False, "error": "Failed to save bots"}), 500

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


def open_browser():
    """Open browser after a short delay"""
    time.sleep(1.5)
    webbrowser.open("http://127.0.0.1:5000")


def main():
    """Main entry point for the application"""
    # Start browser in a separate thread
    threading.Thread(target=open_browser, daemon=True).start()

    print("=" * 60)
    print("Bot Management Dashboard - TheRealPourya Team")
    print("=" * 60)
    print(f"Data stored at: {DATA_DIR}")
    print("Server starting at: http://127.0.0.1:5000")
    print("Opening browser automatically...")
    print("=" * 60)
    print("\nPress CTRL+C to stop the server\n")

    # Run Flask app
    app.run(host="127.0.0.1", port=5000, debug=False)


if __name__ == "__main__":
    main()
