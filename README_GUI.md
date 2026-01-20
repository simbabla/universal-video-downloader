# Video Downloader - GUI Version 🎬

A beautiful, easy-to-use graphical interface for downloading videos from any website!

## 🚀 Quick Start

### Option 1: Run with Python (No installation needed)
1. Double-click `RUN_GUI.bat`
2. The GUI window will open
3. Start downloading!

### Option 2: Create a Standalone EXE
1. Double-click `CREATE_EXE.bat`
2. Wait for the build to complete (2-3 minutes)
3. Find your EXE in the `dist` folder: `VideoDownloader.exe`
4. You can now run it anywhere without Python!

## 📖 How to Use

### Step 1: Add Video URLs
- Paste your video URLs in the text box (one per line)
- Supports YouTube, TikTok, Instagram, Twitter, Facebook, Reddit, and 1000+ more sites
- Works with protected sites too!

### Step 2: Configure Settings
- **Save to**: Choose where to save your videos
- **Max Quality**: Select 480p, 720p, 1080p, 1440p, or 2160p
- **Browser**: Choose your browser for cookie support
- **Skip ads & sponsors**: Auto-skip YouTube ads
- **Use browser cookies**: Download from sites you're logged into

### Step 3: Download
- Click the **"📥 Download Videos"** button
- Watch the progress in real-time
- Files will be saved to your chosen folder!

## ✨ Features

- 🎯 **Simple Interface** - No command line needed!
- 🚀 **Fast Downloads** - Multiple fragments downloaded in parallel
- 📊 **Real-time Progress** - See exactly what's happening
- 🔓 **Protected Sites** - Uses browser cookies for login-required content
- 🎨 **Beautiful Design** - Modern, easy-to-read interface
- 💾 **Batch Downloads** - Add multiple URLs and download them all at once
- 🚫 **Ad Skipping** - Automatically removes ads and sponsors from YouTube videos

## 🌐 Supported Websites

Works with 1000+ sites including:
- YouTube, Vimeo, Dailymotion
- TikTok, Instagram, Twitter/X, Facebook
- Reddit, Twitch, Streamable
- Direct video files (.mp4, .webm, .m3u8, etc.)
- Protected streaming sites (using browser cookies)

## 📝 Tips

### For Protected Sites:
1. Make sure you're logged in on your browser (Chrome, Firefox, Edge, etc.)
2. Enable "Use browser cookies" in settings
3. Select the correct browser from the dropdown
4. The script will use your login session

### For HLS Streams (.m3u8):
- Just paste the .m3u8 URL directly
- The downloader handles it automatically
- Common on protected streaming sites

### Finding Hidden Video URLs:
1. Press F12 in your browser
2. Go to Network tab
3. Play the video
4. Look for .m3u8 or .mp4 files
5. Copy the URL and paste it in the GUI

## 🔧 Creating an EXE File

The EXE file lets you:
- ✅ Run without Python installed
- ✅ Share with friends/family
- ✅ Use on any Windows computer
- ✅ Keep it portable on a USB drive

**To create:**
1. Double-click `CREATE_EXE.bat`
2. Wait 2-3 minutes
3. Find `VideoDownloader.exe` in the `dist` folder
4. Done! You can now delete everything except the EXE

**Note:** The first time you run the EXE, Windows might show a warning. Click "More info" then "Run anyway". This is normal for unsigned apps.

## 🆘 Troubleshooting

### "yt-dlp not installed" error
- Click the Download button anyway - it will auto-install
- Or run: `pip install yt-dlp`

### "Download failed" error
- Make sure you're logged in on your browser (if needed)
- Enable "Use browser cookies"
- Try finding the direct video URL (F12 > Network tab)

### EXE creation fails
- Make sure you have Python installed
- Run: `pip install pyinstaller`
- Try running `CREATE_EXE.bat` again

### Videos won't download from a specific site
- The site might use DRM protection (can't be bypassed)
- Try using browser cookies
- Look for the direct .m3u8 or .mp4 URL

## 📁 File Structure

```
dowln/
├── video_downloader_gui.py    # Main GUI application
├── RUN_GUI.bat                # Quick launcher
├── CREATE_EXE.bat             # EXE builder
├── README_GUI.md              # This file
└── dist/                      # Created after building EXE
    └── VideoDownloader.exe    # Standalone executable
```

## 🎯 Examples

### Example 1: YouTube Video
```
https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

### Example 2: Multiple Videos
```
https://www.youtube.com/watch?v=video1
https://www.tiktok.com/@user/video/123456
https://vimeo.com/123456789
```

### Example 3: Protected Site
```
https://example.com/members/video-lesson-1
```
(Make sure "Use browser cookies" is enabled and you're logged in)

### Example 4: Direct HLS Stream
```
https://cdn.example.com/streams/master.m3u8?token=abc123
```

---

**Enjoy downloading!** 🎬

If you have any issues, check the troubleshooting section or refer to the main README.md file.
