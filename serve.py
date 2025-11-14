#!/usr/bin/env python3
"""
Simple local development server for GraspingAI homepage.

This script serves your static files locally. The auto-reload functionality
is handled by a script tag in your HTML (see index.html).

Usage:
    python3 serve.py
    
Or make it executable and run:
    ./serve.py

Then open: http://localhost:8000

The page will automatically reload when you save changes to HTML/CSS/JS files
(thanks to the auto-reload script in index.html).
"""

import http.server
import socketserver
import os
import webbrowser
from pathlib import Path

PORT = 8000

class DevHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """HTTP Request Handler with development-friendly headers."""
    
    def end_headers(self):
        # Disable caching for development
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()
    
    def log_message(self, format, *args):
        # Custom log format (cleaner output)
        pass


def main():
    os.chdir(Path(__file__).parent)
    
    Handler = DevHTTPRequestHandler
    
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            url = f"http://localhost:{PORT}"
            print(f"\n🚀 Starting development server...")
            print(f"📍 Server running at: {url}")
            print(f"📂 Serving files from: {os.getcwd()}")
            print(f"\n💡 The page will auto-reload when you save changes!")
            print(f"   (Just edit your HTML/CSS/JS files and save)")
            print(f"\n⚠️  Press Ctrl+C to stop the server\n")
            
            # Try to open browser automatically (optional)
            try:
                webbrowser.open(url)
            except:
                pass
            
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n\n👋 Server stopped. Goodbye!")
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"\n❌ Error: Port {PORT} is already in use.")
            print(f"   Try: python3 serve.py")
            print(f"   Or kill the process using port {PORT}")
        else:
            raise


if __name__ == "__main__":
    main()

