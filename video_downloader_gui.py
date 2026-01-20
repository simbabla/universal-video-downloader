"""
VIDEO DOWNLOADER - GUI VERSION
Easy-to-use graphical interface for downloading videos from any website!
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
import subprocess
import sys
import threading
from pathlib import Path
import os

class VideoDownloaderGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Downloader - Universal")
        self.root.geometry("800x650")
        self.root.resizable(True, True)
        
        # Variables
        self.output_dir = tk.StringVar(value="video_downloads")
        self.max_quality = tk.StringVar(value="1080")
        self.skip_ads = tk.BooleanVar(value=True)
        self.use_cookies = tk.BooleanVar(value=False)  # Default to False to avoid cookie errors
        self.browser = tk.StringVar(value="chrome")
        self.is_downloading = False
        
        self.setup_ui()
        self.check_dependencies()
    
    def setup_ui(self):
        """Setup the user interface"""
        # Style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Title
        title_frame = tk.Frame(self.root, bg="#2C3E50", height=60)
        title_frame.pack(fill=tk.X)
        title_frame.pack_propagate(False)
        
        title_label = tk.Label(
            title_frame, 
            text="🎬 Video Downloader",
            font=("Arial", 20, "bold"),
            bg="#2C3E50",
            fg="white"
        )
        title_label.pack(pady=15)
        
        # Main container
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # === URL Input Section ===
        url_frame = ttk.LabelFrame(main_frame, text="Video URLs", padding="10")
        url_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        url_label_frame = tk.Frame(url_frame)
        url_label_frame.pack(fill=tk.X, pady=(0, 5))
        
        tk.Label(
            url_label_frame,
            text="Paste your video URLs here (one per line):",
            font=("Arial", 10)
        ).pack(side=tk.LEFT)
        
        tk.Label(
            url_label_frame,
            text="  💡 Tip: Most sites don't need cookies!",
            font=("Arial", 9),
            fg="gray"
        ).pack(side=tk.LEFT, padx=(10, 0))
        
        self.url_text = scrolledtext.ScrolledText(
            url_frame,
            height=8,
            font=("Consolas", 10),
            wrap=tk.WORD
        )
        self.url_text.pack(fill=tk.BOTH, expand=True)
        self.url_text.insert("1.0", "# Paste video URLs here, one per line\n# Examples:\n# https://www.youtube.com/watch?v=dQw4w9WgXcQ\n# https://www.tiktok.com/@user/video/123456\n")
        
        # === Settings Section ===
        settings_frame = ttk.LabelFrame(main_frame, text="Settings", padding="10")
        settings_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Settings grid
        settings_grid = ttk.Frame(settings_frame)
        settings_grid.pack(fill=tk.X)
        
        # Row 1: Output directory
        ttk.Label(settings_grid, text="Save to:").grid(row=0, column=0, sticky=tk.W, padx=(0, 10))
        ttk.Entry(settings_grid, textvariable=self.output_dir, width=40).grid(row=0, column=1, sticky=tk.W, padx=(0, 5))
        ttk.Button(settings_grid, text="Browse", command=self.browse_folder).grid(row=0, column=2, sticky=tk.W)
        
        # Row 2: Quality
        ttk.Label(settings_grid, text="Max Quality:").grid(row=1, column=0, sticky=tk.W, padx=(0, 10), pady=(10, 0))
        quality_combo = ttk.Combobox(
            settings_grid, 
            textvariable=self.max_quality, 
            values=["480", "720", "1080", "1440", "2160"],
            width=10,
            state="readonly"
        )
        quality_combo.grid(row=1, column=1, sticky=tk.W, pady=(10, 0))
        
        # Row 3: Browser for cookies
        ttk.Label(settings_grid, text="Browser:").grid(row=2, column=0, sticky=tk.W, padx=(0, 10), pady=(10, 0))
        browser_combo = ttk.Combobox(
            settings_grid,
            textvariable=self.browser,
            values=["chrome", "firefox", "edge", "brave", "opera"],
            width=15,
            state="readonly"
        )
        browser_combo.grid(row=2, column=1, sticky=tk.W, pady=(10, 0))
        
        # Checkboxes
        checkbox_frame = ttk.Frame(settings_frame)
        checkbox_frame.pack(fill=tk.X, pady=(10, 0))
        
        ttk.Checkbutton(
            checkbox_frame,
            text="Skip ads & sponsors",
            variable=self.skip_ads
        ).pack(side=tk.LEFT, padx=(0, 20))
        
        cookies_check = ttk.Checkbutton(
            checkbox_frame,
            text="Use browser cookies (only for sites requiring login - close browser first!)",
            variable=self.use_cookies
        )
        cookies_check.pack(side=tk.LEFT)
        
        # === Action Buttons ===
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.download_btn = tk.Button(
            button_frame,
            text="📥 Download Videos",
            font=("Arial", 12, "bold"),
            bg="#27AE60",
            fg="white",
            activebackground="#229954",
            activeforeground="white",
            cursor="hand2",
            command=self.start_download,
            height=2
        )
        self.download_btn.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        
        clear_btn = tk.Button(
            button_frame,
            text="🗑️ Clear",
            font=("Arial", 10),
            bg="#E74C3C",
            fg="white",
            activebackground="#C0392B",
            activeforeground="white",
            cursor="hand2",
            command=self.clear_urls,
            width=10
        )
        clear_btn.pack(side=tk.LEFT, padx=(5, 0))
        
        # === Progress/Log Section ===
        log_frame = ttk.LabelFrame(main_frame, text="Progress", padding="10")
        log_frame.pack(fill=tk.BOTH, expand=True)
        
        self.log_text = scrolledtext.ScrolledText(
            log_frame,
            height=10,
            font=("Consolas", 9),
            bg="#1E1E1E",
            fg="#00FF00",
            wrap=tk.WORD,
            state=tk.DISABLED
        )
        self.log_text.pack(fill=tk.BOTH, expand=True)
        
        # Progress bar
        self.progress = ttk.Progressbar(
            log_frame,
            mode='indeterminate'
        )
        self.progress.pack(fill=tk.X, pady=(10, 0))
    
    def browse_folder(self):
        """Open folder browser dialog"""
        folder = filedialog.askdirectory(initialdir=self.output_dir.get())
        if folder:
            self.output_dir.set(folder)
    
    def clear_urls(self):
        """Clear the URL input box"""
        self.url_text.delete("1.0", tk.END)
        self.log("URL list cleared", "INFO")
    
    def log(self, message, level="INFO"):
        """Add message to log display"""
        self.log_text.config(state=tk.NORMAL)
        
        # Color coding
        if level == "ERROR":
            color_tag = "error"
            prefix = "❌"
        elif level == "SUCCESS":
            color_tag = "success"
            prefix = "✅"
        elif level == "WARNING":
            color_tag = "warning"
            prefix = "⚠️"
        else:
            color_tag = "info"
            prefix = "ℹ️"
        
        self.log_text.tag_config("error", foreground="#FF5555")
        self.log_text.tag_config("success", foreground="#50FA7B")
        self.log_text.tag_config("warning", foreground="#FFB86C")
        self.log_text.tag_config("info", foreground="#8BE9FD")
        
        self.log_text.insert(tk.END, f"{prefix} {message}\n", color_tag)
        self.log_text.see(tk.END)
        self.log_text.config(state=tk.DISABLED)
        self.root.update_idletasks()
    
    def check_dependencies(self):
        """Check if yt-dlp and ffmpeg are installed"""
        self.log("Checking dependencies...", "INFO")
        
        # Check yt-dlp
        try:
            result = subprocess.run(
                ['yt-dlp', '--version'],
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                version = result.stdout.strip()
                self.log(f"yt-dlp {version} is installed", "SUCCESS")
            else:
                self.install_ytdlp()
        except (subprocess.TimeoutExpired, FileNotFoundError):
            self.install_ytdlp()
        
        # Check ffmpeg
        try:
            result = subprocess.run(
                ['ffmpeg', '-version'],
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                self.log("ffmpeg is installed", "SUCCESS")
            else:
                self.log("⚠️ ffmpeg not found - required for high-quality videos!", "WARNING")
                self.log("Run AUTO_INSTALL_FFMPEG.bat to install it", "WARNING")
        except (subprocess.TimeoutExpired, FileNotFoundError):
            self.log("⚠️ ffmpeg not found - required for high-quality videos!", "WARNING")
            self.log("Double-click AUTO_INSTALL_FFMPEG.bat to install it", "WARNING")
    
    def install_ytdlp(self):
        """Install yt-dlp"""
        self.log("Installing yt-dlp... This may take a moment.", "WARNING")
        try:
            subprocess.run(
                [sys.executable, '-m', 'pip', 'install', '--upgrade', 'yt-dlp'],
                capture_output=True,
                check=True
            )
            self.log("yt-dlp installed successfully!", "SUCCESS")
        except subprocess.CalledProcessError:
            self.log("Failed to install yt-dlp. Please install manually: pip install yt-dlp", "ERROR")
    
    def get_urls(self):
        """Extract URLs from text box"""
        text = self.url_text.get("1.0", tk.END)
        urls = []
        for line in text.split('\n'):
            line = line.strip()
            # Skip comments and empty lines
            if line and not line.startswith('#') and line.startswith('http'):
                urls.append(line)
        return urls
    
    def start_download(self):
        """Start the download process in a separate thread"""
        if self.is_downloading:
            messagebox.showwarning("Download in Progress", "A download is already in progress!")
            return
        
        urls = self.get_urls()
        
        if not urls:
            messagebox.showwarning("No URLs", "Please add at least one video URL!")
            return
        
        # Disable download button
        self.download_btn.config(state=tk.DISABLED, text="⏳ Downloading...")
        self.progress.start()
        self.is_downloading = True
        
        # Clear previous logs
        self.log_text.config(state=tk.NORMAL)
        self.log_text.delete("1.0", tk.END)
        self.log_text.config(state=tk.DISABLED)
        
        # Start download in separate thread
        thread = threading.Thread(target=self.download_videos, args=(urls,))
        thread.daemon = True
        thread.start()
    
    def download_videos(self, urls):
        """Download videos using yt-dlp"""
        self.log(f"Starting download of {len(urls)} video(s)...", "INFO")
        self.log(f"Output directory: {Path(self.output_dir.get()).absolute()}", "INFO")
        self.log(f"Max quality: {self.max_quality.get()}p", "INFO")
        self.log("-" * 60, "INFO")
        
        # Create output directory
        output_path = Path(self.output_dir.get())
        output_path.mkdir(parents=True, exist_ok=True)
        
        success_count = 0
        failed_count = 0
        
        for idx, url in enumerate(urls, 1):
            self.log(f"[{idx}/{len(urls)}] Downloading: {url}", "INFO")
            
            # Build yt-dlp command
            cmd = self.build_command(url)
            
            try:
                # Run yt-dlp
                process = subprocess.Popen(
                    cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    bufsize=1,
                    universal_newlines=True
                )
                
                # Stream output
                for line in process.stdout:
                    line = line.strip()
                    if line:
                        # Check for cookie errors and provide helpful message
                        if 'could not copy' in line.lower() and 'cookie' in line.lower():
                            self.log(f"  ⚠️ Cookie access error - Close your browser or disable 'Use browser cookies'", "WARNING")
                        # Check for ffmpeg errors
                        elif 'ffmpeg not found' in line.lower():
                            self.log(f"  ❌ FFmpeg is required but not installed!", "ERROR")
                            self.log(f"  💡 Run AUTO_INSTALL_FFMPEG.bat to fix this", "WARNING")
                        # Only show important lines
                        elif any(keyword in line.lower() for keyword in ['download', 'merge', 'destination', 'error', 'already']):
                            self.log(f"  {line}", "INFO")
                
                process.wait()
                
                if process.returncode == 0:
                    self.log(f"✅ Successfully downloaded!", "SUCCESS")
                    success_count += 1
                else:
                    self.log(f"❌ Download failed", "ERROR")
                    failed_count += 1
                    
            except Exception as e:
                self.log(f"❌ Error: {str(e)}", "ERROR")
                failed_count += 1
            
            self.log("-" * 60, "INFO")
        
        # Summary
        self.log("", "INFO")
        self.log("=" * 60, "INFO")
        self.log("DOWNLOAD COMPLETE!", "SUCCESS")
        self.log(f"✅ Successful: {success_count}/{len(urls)}", "SUCCESS")
        if failed_count > 0:
            self.log(f"❌ Failed: {failed_count}/{len(urls)}", "ERROR")
        self.log(f"📁 Files saved to: {output_path.absolute()}", "INFO")
        self.log("=" * 60, "INFO")
        
        # Re-enable download button
        self.download_btn.config(state=tk.NORMAL, text="📥 Download Videos")
        self.progress.stop()
        self.is_downloading = False
        
        # Show completion message
        if success_count > 0:
            messagebox.showinfo(
                "Download Complete",
                f"Successfully downloaded {success_count}/{len(urls)} video(s)!\n\n"
                f"Saved to: {output_path.absolute()}"
            )
    
    def build_command(self, url):
        """Build yt-dlp command"""
        output_template = str(Path(self.output_dir.get()) / '%(title)s.%(ext)s')
        
        cmd = [
            'yt-dlp',
            url,
            '-o', output_template,
            '--merge-output-format', 'mp4',
            '--no-warnings',
            '--ignore-errors',
            '--no-check-certificate',
            '--add-metadata',
            '--concurrent-fragments', '4',
            '--retries', '10',
            '--fragment-retries', '10',
        ]
        
        # Format/Quality
        max_q = self.max_quality.get()
        cmd.extend(['-f', f'bestvideo[height<={max_q}]+bestaudio/best[height<={max_q}]/best'])
        
        # Skip ads
        if self.skip_ads.get():
            cmd.extend([
                '--sponsorblock-remove', 'sponsor,intro,outro,selfpromo,interaction',
                '--no-playlist'
            ])
        
        # Browser cookies (only if enabled)
        # Note: Most sites like YouTube, TikTok, etc. don't need cookies
        # Only enable for sites requiring login
        if self.use_cookies.get():
            try:
                cmd.extend(['--cookies-from-browser', self.browser.get()])
            except:
                pass  # Skip if cookies can't be accessed
        
        # HLS support
        cmd.extend([
            '--hls-prefer-native',
            '--external-downloader', 'ffmpeg'
        ])
        
        # Bypass restrictions
        cmd.extend(['--geo-bypass', '--age-limit', '99'])
        
        # Try to locate ffmpeg if not in PATH (works with common install locations)
        ffmpeg_paths = [
            r'C:\ffmpeg\bin\ffmpeg.exe',
            r'C:\Program Files\ffmpeg\bin\ffmpeg.exe',
        ]
        for ffmpeg_path in ffmpeg_paths:
            if os.path.exists(ffmpeg_path):
                cmd.extend(['--ffmpeg-location', ffmpeg_path])
                break
        
        return cmd

def main():
    root = tk.Tk()
    app = VideoDownloaderGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
