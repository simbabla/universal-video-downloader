# Universal Video Downloader 🎬

A powerful and user-friendly video downloader with both GUI and CLI interfaces. Download videos from 1000+ websites including YouTube, TikTok, Instagram, Twitter, Facebook, and more!

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.7+-blue.svg)

## ✨ Features

- 🎯 **Easy-to-Use GUI** - Beautiful interface, no command line needed
- 🚀 **1000+ Supported Sites** - YouTube, TikTok, Instagram, Twitter, Facebook, Reddit, Vimeo, and more
- 🔓 **Protected Site Support** - Download from sites with right-click disabled or login requirements
- 🎥 **Quality Selection** - Choose from 480p to 4K (2160p)
- 🚫 **Ad Skipping** - Automatically removes YouTube ads and sponsors
- 📦 **Batch Downloads** - Download multiple videos at once
- 💾 **Multiple Formats** - Supports MP4, WebM, HLS (.m3u8), DASH (.mpd)
- 🔄 **Real-time Progress** - See download status with colored output
- 🖥️ **Standalone EXE** - Create a portable executable (no Python needed!)

## 🖼️ Screenshots

### GUI Version
Beautiful, modern interface with real-time progress display:
- Paste multiple URLs
- Select quality and settings
- Watch downloads in real-time
- Colored progress logs

### CLI Version
Simple command-line interface for power users

## 🚀 Quick Start

### Option 1: GUI (Recommended for beginners)

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/video-downloader.git
cd video-downloader
```

2. **Run the GUI:**
```bash
python video_downloader_gui.py
```
Or double-click `RUN_GUI.bat` (Windows)

3. **Start downloading:**
   - Paste video URLs in the text box
   - Configure settings (quality, output folder, etc.)
   - Click "Download Videos"
   - Done!

### Option 2: CLI (For advanced users)

1. Edit `video_downloader.py` and add your URLs:
```python
VIDEO_URLS = [
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "https://www.tiktok.com/@user/video/123456",
]
```

2. Run the script:
```bash
python video_downloader.py
```
Or double-click `RUN_DOWNLOADER.bat` (Windows)

## 📦 Installation

### Requirements
- Python 3.7 or higher
- pip (Python package manager)

### Dependencies
The script will automatically install required packages:
- `yt-dlp` - Video download engine (auto-installed)
- `ffmpeg` - Video/audio merger (required for high-quality videos)
- `tkinter` - GUI framework (usually included with Python)

**Installing FFmpeg:**

**Option 1 (Easiest):** Double-click `INSTALL_FFMPEG.bat`

**Option 2 (Chocolatey):**
```bash
choco install ffmpeg
```

**Option 3 (Manual):**
1. Download from https://www.gyan.dev/ffmpeg/builds/
2. Extract and add `bin` folder to PATH
3. Restart your terminal/app

Manual yt-dlp installation (if needed):
```bash
pip install yt-dlp
```

## 🔧 Building Standalone EXE

Want to share with non-technical users? Create a standalone executable:

1. Double-click `CREATE_EXE.bat` (Windows)
2. Wait 2-3 minutes for the build
3. Find `VideoDownloader.exe` in the `dist` folder
4. Share the EXE - works without Python!

Or manually:
```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name "VideoDownloader" video_downloader_gui.py
```

## 🌐 Supported Websites

Works with **1000+ websites** including:

### Popular Platforms
- **YouTube** - Videos, playlists, live streams, shorts
- **TikTok** - Videos without watermark
- **Instagram** - Posts, reels, IGTV, stories
- **Twitter/X** - Videos and GIFs
- **Facebook** - Videos and live streams
- **Reddit** - Video posts
- **Vimeo** - All content types
- **Twitch** - VODs and clips

### Streaming & Media
- Dailymotion, Streamable, Mixcloud
- SoundCloud, Bandcamp
- Archive.org, Giphy, Imgur

### Direct Links
- MP4, WebM, MKV, AVI, MOV files
- HLS streams (.m3u8) - common on protected sites
- DASH streams (.mpd)

[See full list of supported sites](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)

## 🔓 Downloading Protected Content

### For Sites with Right-Click Disabled

**Method 1: Browser Cookies (Easiest)**
1. Log in to the website on your browser
2. Enable "Use browser cookies" in the GUI
3. Select your browser from the dropdown
4. **Close your browser completely**
5. Download!

**Method 2: Find Direct Video URL**
1. Press `F12` in your browser (Developer Tools)
2. Go to "Network" tab
3. Play the video on the website
4. Look for `.m3u8`, `.mp4`, or `.mpd` files
5. Right-click → Copy → Copy URL
6. Paste the URL in the downloader

Common patterns:
- `https://cdn.example.com/master.m3u8?token=abc123`
- `https://videos.example.com/video.mp4?auth=xyz`

## ⚙️ Configuration

### GUI Settings
- **Save to**: Choose output directory
- **Max Quality**: 480p, 720p, 1080p, 1440p, or 2160p
- **Browser**: Chrome, Firefox, Edge, Brave, or Opera
- **Skip ads & sponsors**: Auto-remove YouTube ads
- **Use browser cookies**: For login-required content

### CLI Settings
Edit these variables in `video_downloader.py`:
```python
OUTPUT_DIR = "video_downloads"
MAX_QUALITY = "1080"
SKIP_ADS = True
USE_BROWSER_COOKIES = False  # Only enable if needed
BROWSER_FOR_COOKIES = "chrome"
```

## 💡 Usage Examples

### Example 1: Single YouTube Video
```
https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

### Example 2: Multiple Videos from Different Sites
```
https://www.youtube.com/watch?v=video1
https://www.tiktok.com/@user/video/123456
https://vimeo.com/123456789
https://www.reddit.com/r/videos/comments/abc123/
```

### Example 3: Protected Site (with login)
```
https://education-site.com/course/video-lesson-1
```
Enable "Use browser cookies" and make sure you're logged in!

### Example 4: Direct HLS Stream
```
https://cdn.example.com/streams/master.m3u8?token=abc123
```

## 🐛 Troubleshooting

### "ffmpeg not found" error
**This is the most common issue!** FFmpeg is required to merge video and audio streams.

**Quick fix:**
1. Double-click `INSTALL_FFMPEG.bat` in the script folder
2. Restart your GUI/terminal after installation
3. Try downloading again

Or install manually:
- **Chocolatey**: `choco install ffmpeg`
- **winget**: `winget install Gyan.FFmpeg`
- **Manual**: Download from https://www.gyan.dev/ffmpeg/builds/

### "yt-dlp not installed" error
- The script will auto-install it on first run
- Or manually: `pip install yt-dlp`

### "Cookie access error"
- Close your browser completely before downloading
- Or disable "Use browser cookies" (most sites don't need it)

### "Download failed" error
1. Check if the URL works in your browser
2. For protected sites, enable browser cookies
3. Try finding the direct video URL (F12 → Network tab)

### Videos play but won't download
- Some sites use DRM protection (can't be bypassed legally)
- Try looking for the direct .m3u8 or .mp4 URL

### EXE creation fails
```bash
pip install --upgrade pyinstaller
```

## 📁 Project Structure

```
video-downloader/
├── video_downloader_gui.py    # GUI application
├── video_downloader.py        # CLI application
├── RUN_GUI.bat               # Quick launcher (GUI)
├── RUN_DOWNLOADER.bat        # Quick launcher (CLI)
├── CREATE_EXE.bat            # EXE builder
├── README.md                 # Main documentation
├── README_GUI.md             # GUI-specific guide
├── LICENSE                   # MIT License
└── dist/                     # Generated EXE files
    └── VideoDownloader.exe
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [yt-dlp](https://github.com/yt-dlp/yt-dlp) - The amazing video download engine
- GUI created with Python's tkinter
- Created with assistance from Claude AI

## ⚠️ Legal Disclaimer

This tool is for personal use only. Please respect copyright laws and website terms of service. Only download videos you have permission to download. The authors are not responsible for any misuse of this software.

## 📞 Support

If you encounter any issues or have questions:
- Open an [Issue](https://github.com/simbabla/video-downloader/issues)
- Check the [Troubleshooting](#-troubleshooting) section
- Read the detailed [GUI Guide](README_GUI.md)

## ⭐ Star this repo if you find it useful!

---

**Made with ❤️ and Python**
