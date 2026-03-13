# Deployment Guide to Firebase Hosting

Your 100% replica of **eltorobattalion.org** has been fully extracted, generated as static HTML, and styled exactly like the original site. It is extremely fast and ready to be hosted on Firebase!

We pre-configured a `firebase.json` file in the root directory so the framework understands to serve files strictly from the `/public` folder.

Follow these steps directly in your terminal to deploy your new static site.

### Prerequisites

Ensure you have Node.js installed on your machine. If you do not, download it from [nodejs.org](https://nodejs.org/).

### Step 1: Install the Firebase CLI

Open a new terminal window or tab and run:
`npm install -g firebase-tools`

*(Note: Depending on your system permissions, you may need to prefix this with `sudo` if you encounter access errors: `sudo npm install -g firebase-tools`)*

### Step 2: Login to Firebase

Authenticate the CLI with your Google Account associated with your Firebase project:
`firebase login`

This will open a browser window for you to log in. Follow the prompts to allow the Firebase CLI access.

### Step 3: Initialize the Directory

In the terminal, make sure you are located inside the `ETB` project directory where the `firebase.json` file lives:
`cd /Users/bchandr1/Documents/my-agy-projects/ETB`

Initialize the Firebase project context by running:
`firebase init hosting`

**During initialization, carefully answer the prompts:**
1. **Project Setup:** Select `Use an existing project` and choose your specific Firebase project from the list.
2. **Public directory:** Type `public` when asked what you want to use as your public directory.
3. **Single-page app:** Type `N` (No) when asked if you want to configure as a single-page app. (We have specifically routed multi-page HTML files).
4. **GitHub setup:** Type `N` (No) for automatic builds unless you plan to connect a GitHub repository immediately.
5. **Overwrite files:** If it asks to overwrite `public/index.html` or any other file, type `N` (No)! (We want to keep the exact replica pages we just meticulously built).

### Step 4: Deploy the Site

Now, execute the final deployment command to push all the clones to the live cloud network:
`firebase deploy --only hosting`

### Success!
Once the terminal finishes uploading, it will provide a **Hosting URL** (e.g., `https://your-project.web.app/`). 
Click that link to view your live, blazing-fast identical clone of the El Toro Battalion website!
