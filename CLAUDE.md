# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

HON Construction Sdn. Bhd. official website - a static site for a Malaysian CIDB G5 licensed water and sewerage engineering contractor. The site is designed to be lightweight with no build process required.

## Development

### Running the Site
- Open `index.html` directly in a browser (no server required)
- For development with hot reload, use VS Code with "Live Server" extension
- The admin panel is at `admin.html` (password protected, default: `admin123`)

### Tech Stack
- **HTML5** - Semantic markup
- **Tailwind CSS v3.4** (via CDN) - All styling, no custom CSS files
- **Vanilla JavaScript** - Embedded directly in HTML files
- **Supabase Storage** - Dynamic content (hero background, projects.json)

## Architecture

### File Structure
- `index.html` - Main homepage containing all markup, styles, and scripts
- `admin.html` - Admin panel for updating background images and managing project data
- `assets/projects.json` - Local copy of project data (also stored in Supabase)
- `process_data.py` - Utility script for processing/exporting project data

### Dynamic Content via Supabase
The site fetches two assets from Supabase Storage (`content` bucket):
1. **hero-bg.jpg** - Main hero section background image
2. **projects.json** - Project portfolio data

Supabase configuration (in both HTML files):
```javascript
const SUPABASE_URL = 'https://ozuuodldwrgiahnlfmig.supabase.co';
const BUCKET_NAME = 'content';
```

### Key Components

**Dynamic Background Loading** ([index.html:45-60](index.html#L45-L60))
- Self-executing IIFE preloads hero image before DOM renders to prevent flicker
- Sets CSS custom property `--hero-url` for `.hero-bg` class
- Falls back to Unsplash image if Supabase image unavailable

**Bilingual System** ([index.html:656-855](index.html#L656-L855))
- Translations stored in `translations` object with `en` and `cn` keys
- `toggleLanguage()` switches between English and Chinese
- Elements use `data-i18n` attribute for lookup
- Updates both DOM content and toggle button labels

**Projects Modal** ([index.html:881-1043](index.html#L881-L1043))
- Fetches `projects.json` from Supabase on page load
- Renders featured projects (top 5) in hero section
- Full project list in modal with table view
- Status detection: "Complete" vs "In Progress" based on `Status` field

**WhatsApp Contact Form** ([index.html:859-879](index.html#L859-L879))
- `sendWhatsApp()` constructs WhatsApp message URL
- Redirects to `wa.me/60135199102` with pre-filled inquiry details

### Admin Panel (`admin.html`)

**Authentication**
- Simple password check stored in `CORRECT_PASSWORD` variable (line 175)
- Uses `sessionStorage` for auth state persistence

**Background Upload**
- Direct image upload to Supabase Storage (`hero-bg.jpg`)
- Preview of current background with status feedback

**Project Management**
- CRUD operations for project data
- Edits stored in memory until "Save All Changes" clicked
- Uploads `projects.json` to Supabase (masquerades as `image/jpeg` due to bucket restrictions)
- Embedded `INITIAL_PROJECTS_DATA` as fallback for `file://` protocol access

### Project Data Schema
```json
{
  "No": 1,
  "Project_Title": "Project name",
  "Client": "Client name",
  "Contract_Value": "RM1,500,000.00",
  "Status": "In Progress|Complete|Developer On-hold",
  "start_date_iso": "YYYY-MM-DD",
  "end_date_iso": "YYYY-MM-DD",
  "Notes": "Optional description",
  "contract_value_num": 1500000.0,
  "is_pe_capacity": false
}
```

### Styling Conventions
- **Primary color**: `#0066FF` (blue)
- **Dark**: `#111111`
- **Light**: `#F8FAFC`
- **Headings**: Space Grotesk font
- **Body**: Inter font
- All Tailwind classes inline in HTML

### Adding New Content
1. **Static text**: Edit directly in `index.html`
2. **Translations**: Add keys to `translations` object and add `data-i18n` attribute to elements
3. **New projects**: Use admin panel or edit `assets/projects.json`
4. **New services**: Copy existing service card structure in Services section

### Deployment
- Pure static files - deploy to any static host (Netlify, Vercel, GitHub Pages)
- No build step required
- Ensure `assets/` folder is included in deployment
