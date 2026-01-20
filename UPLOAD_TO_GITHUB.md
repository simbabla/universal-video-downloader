# How to Upload to GitHub 🚀

Follow these simple steps to upload your video downloader to GitHub!

## 📋 Prerequisites

1. **GitHub account** - Create one at https://github.com/signup if you don't have one
2. **Git installed** - Download from https://git-scm.com/downloads

## 🎯 Step-by-Step Instructions

### Step 1: Create a New Repository on GitHub

1. Go to https://github.com/new
2. Fill in the details:
   - **Repository name**: `universal-video-downloader` (or your preferred name)
   - **Description**: "Download videos from 1000+ websites including YouTube, TikTok, Instagram, and more!"
   - **Visibility**: Choose "Public" to share with everyone
   - **DO NOT** check "Initialize with README" (we already have one)
3. Click "Create repository"

### Step 2: Prepare Your Local Files

Open PowerShell or Command Prompt and navigate to the github folder:

```powershell
cd C:\Users\frenc\Desktop\whop\download\dowln\github
```

### Step 3: Initialize Git Repository

```bash
git init
```

### Step 4: Add All Files

```bash
git add .
```

### Step 5: Create Your First Commit

```bash
git commit -m "Initial commit: Universal video downloader with GUI and CLI"
```

### Step 6: Connect to GitHub

Replace `simbabla` with your GitHub username and `universal-video-downloader` with your repo name:

```bash
git remote add origin https://github.com/simbabla/universal-video-downloader.git
```

### Step 7: Push to GitHub

```bash
git branch -M main
git push -u origin main
```

If prompted, enter your GitHub credentials.

### Step 8: Verify Upload

1. Go to your repository on GitHub: `https://github.com/simbabla/universal-video-downloader`
2. You should see all your files!
3. The README.md will automatically display on the main page

## 🎨 Optional: Make It Look Better

### Add Topics/Tags

On your GitHub repo page:
1. Click the ⚙️ gear icon next to "About"
2. Add topics:
   - `video-downloader`
   - `youtube-downloader`
   - `python`
   - `gui`
   - `tkinter`
   - `yt-dlp`
   - `tiktok-downloader`
   - `instagram-downloader`
3. Add website: `https://github.com/yt-dlp/yt-dlp` (credit the tool we use)
4. Save changes

### Add Screenshots (Optional but Recommended)

1. Take screenshots of your GUI in action
2. Upload them to your repo or use imgur
3. Add them to README.md:
   ```markdown
   ## Screenshots
   
   ![GUI Screenshot](screenshot.png)
   ```

### Create a Release (Optional)

If you build the EXE:
1. Go to "Releases" on your GitHub repo
2. Click "Create a new release"
3. Tag: `v1.0.0`
4. Title: "Universal Video Downloader v1.0.0"
5. Attach the `VideoDownloader.exe` file
6. Click "Publish release"

## 🔧 Future Updates

When you make changes:

```bash
cd C:\Users\frenc\Desktop\whop\download\dowln\github
git add .
git commit -m "Description of your changes"
git push
```

## 🆘 Troubleshooting

### "Permission denied" error

You need to authenticate with GitHub. Options:

1. **Use GitHub Desktop** (easiest): https://desktop.github.com/
2. **Use Personal Access Token**:
   - Go to https://github.com/settings/tokens
   - Generate new token (classic)
   - Use as password when pushing

### "Repository not found" error

Check that:
- You're using the correct GitHub username
- Repository name matches exactly
- Repository exists on GitHub

### Files not showing up

```bash
git status  # Check what's tracked
git add .   # Add everything
git commit -m "Add missing files"
git push
```

## 🎉 You're Done!

Your video downloader is now on GitHub! Share the link:
```
https://github.com/simbabla/universal-video-downloader
```

People can now:
- ⭐ Star your repo
- 🍴 Fork it
- 📥 Clone and use it
- 🐛 Report issues
- 🤝 Contribute improvements

---

**Congratulations on your first open-source project!** 🎊
