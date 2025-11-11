#!/usr/bin/env python3
"""
Command-line interface for BotManager
"""

import sys
import argparse
from .app import main as run_app


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="BotManager - A modern Windows desktop application for managing and running multiple bots from a beautiful web-based dashboard",
        epilog="Example: botmanager"
    )
    
    parser.add_argument(
        "--version", 
        action="version", 
        version="BotManager 1.0.0"
    )
    
    parser.add_argument(
        "--host", 
        default="127.0.0.1",
        help="Host to bind the server to (default: 127.0.0.1)"
    )
    
    parser.add_argument(
        "--port", 
        type=int, 
        default=5000,
        help="Port to bind the server to (default: 5000)"
    )
    
    args = parser.parse_args()
    
    # For now, we'll use the default host/port from app.py
    # In a future version, we could modify the app to accept these parameters
    print(f"Starting BotManager on {args.host}:{args.port}")
    print("Note: Currently using default settings from app.py")
    
    try:
        run_app()
    except KeyboardInterrupt:
        print("\nBotManager stopped by user")
        sys.exit(0)
    except Exception as e:
        print(f"Error starting BotManager: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
