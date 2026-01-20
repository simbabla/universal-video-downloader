"""
VIDEO DOWNLOADER - Download from ANY website!

This script can download videos from:
- YouTube, Vimeo, Twitter/X, Facebook, Instagram, TikTok, Reddit, Twitch
- Sites with right-click disabled or protected video players
- Direct video URLs (.mp4, .webm, .mkv, etc.)
- HLS streams (.m3u8) - commonly used on protected streaming sites
- Sites requiring login (uses your browser cookies automatically)
- 1000+ other websites!

HOW TO USE:
1. Add video URLs to VIDEO_URLS list below
2. Adjust settings if needed (quality, output folder, etc.)
3. Run the script or double-click RUN_VIDEO_DOWNLOADER.bat

TIPS FOR PROTECTED SITES:
- If a site requires login, make sure you're logged in on your browser first
- The script will automatically use your browser cookies
- For direct video URLs, right-click on the page > "Inspect" > "Network" tab
  > Reload page > Look for .m3u8 or .mp4 files
- Some sites use HLS (.m3u8) - just paste the URL and it will work!
"""

import os
import sys
from pathlib import Path
import subprocess
import re

# Configuration
VIDEO_URLS = [
    # Add your video URLs here, one per line
    # Examples:
    # "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    # "https://example.com/video.mp4",
    # "https://example.com/stream/playlist.m3u8",
]

OUTPUT_DIR = "video_downloads"  # Folder where videos will be saved
VIDEO_FORMAT = "best"  # Options: "best", "bestvideo+bestaudio", "worst", "mp4", etc.
MAX_QUALITY = "1080"  # Maximum video quality (e.g., "480", "720", "1080", "1440", "2160")

# Advanced options
SKIP_ADS = True  # Skip advertisements
EMBED_SUBS = True  # Embed subtitles if available
DOWNLOAD_PLAYLIST = False  # Download entire playlist if URL is a playlist

# Options for protected/difficult websites
USE_BROWSER_COOKIES = False  # Extract cookies from your browser (for logged-in content)
BROWSER_FOR_COOKIES = "chrome"  # Options: "chrome", "firefox", "edge", "brave", "opera"
EXTRACT_M3U8_HLS = True  # Download HLS streams (m3u8 files) - common on protected sites
BYPASS_RESTRICTIONS = True  # Try to bypass geo-restrictions and other blocks

class VideoDownloader:
    def __init__(self):
        self.output_dir = Path(OUTPUT_DIR)
        self.downloaded_count = 0
        self.failed_urls = []
    
    @staticmethod
    def print_help_for_protected_sites():
        """Print instructions for finding video URLs on protected sites"""
        print("\n" + "="*60)
        print("🔍 HOW TO FIND VIDEO URLs ON PROTECTED SITES")
        print("="*60)
        print("\nIf the site has right-click disabled or custom video player:")
        print("\n1. Open the website in Chrome/Edge/Firefox")
        print("2. Press F12 to open Developer Tools")
        print("3. Click on the 'Network' tab")
        print("4. In the filter box, type: m3u8 OR mp4 OR webm")
        print("5. Play the video on the website")
        print("6. Look for entries with .m3u8, .mp4, or .mpd extensions")
        print("7. Right-click the entry > Copy > Copy URL")
        print("8. Paste that URL into VIDEO_URLS list in this script")
        print("\nCommon patterns to look for:")
        print("   • master.m3u8 or playlist.m3u8 (HLS streams)")
        print("   • .mp4?token=... (direct video with auth)")
        print("   • manifest.mpd (DASH streams)")
        print("="*60 + "\n")
        
    def check_dependencies(self):
        """Check if yt-dlp is installed, if not, install it"""
        print("🔍 Checking dependencies...")
        try:
            subprocess.run(['yt-dlp', '--version'], 
                         capture_output=True, check=True)
            print("✅ yt-dlp is already installed\n")
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("📦 yt-dlp not found. Installing...")
            try:
                subprocess.run([sys.executable, '-m', 'pip', 'install', 
                              '--upgrade', 'yt-dlp'], check=True)
                print("✅ yt-dlp installed successfully\n")
                return True
            except subprocess.CalledProcessError as e:
                print(f"❌ Failed to install yt-dlp: {e}")
                print("💡 Try installing manually: pip install yt-dlp")
                return False
    
    def build_yt_dlp_command(self, url):
        """Build the yt-dlp command with all options"""
        # Create output directory if it doesn't exist
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Output template: Save as video title with safe filename
        output_template = str(self.output_dir / '%(title)s.%(ext)s')
        
        # Base command
        cmd = [
            'yt-dlp',
            url,
            '-o', output_template,
        ]
        
        # Format selection (quality)
        if VIDEO_FORMAT == "best":
            cmd.extend(['-f', f'bestvideo[height<={MAX_QUALITY}]+bestaudio/best[height<={MAX_QUALITY}]/best'])
        elif VIDEO_FORMAT == "mp4":
            cmd.extend(['-f', f'bestvideo[height<={MAX_QUALITY}][ext=mp4]+bestaudio[ext=m4a]/best[height<={MAX_QUALITY}][ext=mp4]/best'])
        else:
            cmd.extend(['-f', VIDEO_FORMAT])
        
        # Merge to mp4 container
        cmd.extend(['--merge-output-format', 'mp4'])
        
        # Skip ads and sponsors (SponsorBlock integration)
        if SKIP_ADS:
            cmd.extend([
                '--sponsorblock-remove', 'sponsor,intro,outro,selfpromo,interaction',
                '--no-playlist',  # Don't download playlists by default
            ])
        
        # Playlist handling
        if DOWNLOAD_PLAYLIST:
            cmd.remove('--no-playlist') if '--no-playlist' in cmd else None
            cmd.extend(['--yes-playlist'])
        
        # Subtitle options
        if EMBED_SUBS:
            cmd.extend([
                '--write-auto-subs',  # Download auto-generated subtitles
                '--embed-subs',  # Embed subtitles in video
                '--sub-lang', 'en',  # Prefer English subtitles
            ])
        
        # === ADVANCED OPTIONS FOR PROTECTED SITES ===
        
        # Use browser cookies (for sites requiring login)
        if USE_BROWSER_COOKIES:
            cmd.extend(['--cookies-from-browser', BROWSER_FOR_COOKIES])
        
        # HLS stream support (m3u8 files)
        if EXTRACT_M3U8_HLS:
            cmd.extend([
                '--hls-prefer-native',  # Use native HLS downloader
                '--hls-use-mpegts',  # Better compatibility with some streams
                '--external-downloader', 'ffmpeg',  # Use ffmpeg for downloading
                '--external-downloader-args', 'ffmpeg:-movflags +faststart',  # Optimize for streaming
            ])
        
        # Bypass geo-restrictions and other blocks
        if BYPASS_RESTRICTIONS:
            cmd.extend([
                '--geo-bypass',  # Try to bypass geo-restrictions
                '--age-limit', '99',  # Bypass age restrictions
            ])
        
        # Additional useful options
        cmd.extend([
            '--no-warnings',  # Suppress warnings
            '--ignore-errors',  # Continue on download errors
            '--no-check-certificate',  # Skip SSL verification (for some sites)
            '--prefer-free-formats',  # Prefer free video formats
            '--add-metadata',  # Add metadata to file
            '--concurrent-fragments', '4',  # Download multiple fragments in parallel (faster)
            '--retries', '10',  # Retry failed downloads
            '--fragment-retries', '10',  # Retry failed fragments
            '--user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        ])
        
        return cmd
    
    def download_video(self, url):
        """Download a single video"""
        # Detect video type
        video_type = "webpage"
        if '.m3u8' in url.lower():
            video_type = "HLS stream (.m3u8)"
        elif '.mpd' in url.lower():
            video_type = "DASH stream (.mpd)"
        elif any(ext in url.lower() for ext in ['.mp4', '.webm', '.mkv', '.avi', '.mov']):
            video_type = "direct video"
        
        print(f"📥 Downloading: {url}")
        print(f"   Type: {video_type}")
        
        try:
            cmd = self.build_yt_dlp_command(url)
            result = subprocess.run(cmd, capture_output=False, text=True)
            
            if result.returncode == 0:
                print(f"✅ Successfully downloaded!\n")
                self.downloaded_count += 1
                return True
            else:
                print(f"❌ Download failed for: {url}")
                print(f"💡 Tip: If this is a protected site, try:")
                print(f"   1. Make sure you're logged in on your browser")
                print(f"   2. Check if browser cookies are enabled (USE_BROWSER_COOKIES=True)")
                print(f"   3. Try finding the direct video URL (see help below)\n")
                self.failed_urls.append(url)
                return False
                
        except Exception as e:
            print(f"❌ Error downloading {url}: {e}\n")
            self.failed_urls.append(url)
            return False
    
    def download_all(self):
        """Download all videos in the list"""
        if not VIDEO_URLS:
            print("⚠️  No video URLs found!")
            print("💡 Edit the script and add URLs to the VIDEO_URLS list at the top.")
            print("\n📚 Supported sites:")
            print("   • YouTube, Vimeo, Dailymotion")
            print("   • Twitter/X, Facebook, Instagram, TikTok")
            print("   • Reddit, Twitch, Streamable")
            print("   • Direct video links (.mp4, .webm, .m3u8, etc.)")
            print("   • Sites with protected content (using browser cookies)")
            print("   • 1000+ other sites!")
            return
        
        print("="*60)
        print("🎬 VIDEO DOWNLOADER - ADVANCED MODE")
        print("="*60)
        print(f"📁 Output directory: {self.output_dir.absolute()}")
        print(f"🎥 Videos to download: {len(VIDEO_URLS)}")
        print(f"🎯 Max quality: {MAX_QUALITY}p")
        print(f"🚫 Skip ads: {'Yes' if SKIP_ADS else 'No'}")
        print(f"🍪 Browser cookies: {'Yes (' + BROWSER_FOR_COOKIES + ')' if USE_BROWSER_COOKIES else 'No'}")
        print(f"🔓 HLS/m3u8 support: {'Yes' if EXTRACT_M3U8_HLS else 'No'}")
        print(f"🌍 Bypass restrictions: {'Yes' if BYPASS_RESTRICTIONS else 'No'}")
        print("="*60)
        print()
        
        # Check dependencies
        if not self.check_dependencies():
            return
        
        # Download each video
        for idx, url in enumerate(VIDEO_URLS, 1):
            print(f"[{idx}/{len(VIDEO_URLS)}] ", end="")
            self.download_video(url)
        
        # Summary
        print("="*60)
        print("✨ DOWNLOAD COMPLETE!")
        print("="*60)
        print(f"✅ Successfully downloaded: {self.downloaded_count}/{len(VIDEO_URLS)}")
        
        if self.failed_urls:
            print(f"\n⚠️  Failed downloads ({len(self.failed_urls)}):")
            for url in self.failed_urls:
                print(f"   - {url}")
            
            # Show help for finding direct URLs
            self.print_help_for_protected_sites()
        
        print(f"\n📁 Files saved to: {self.output_dir.absolute()}")
        print("="*60)

def main():
    """Main entry point"""
    downloader = VideoDownloader()
    downloader.download_all()

if __name__ == "__main__":
    main()
