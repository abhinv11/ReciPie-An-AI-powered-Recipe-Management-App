# 📋 Pre-Deployment Checklist

## ✅ Files Ready
- [x] vercel.json (root directory)
- [x] requirements.txt (in ReciPie/)
- [x] .gitignore
- [x] .env.example
- [x] README.md
- [x] DEPLOYMENT.md

## ⚙️ Before You Deploy

### 1. Test Locally
```bash
cd /workspaces/Assignment_durapid/ReciPie
uvicorn index:app --reload
```
Visit http://localhost:8000 and test:
- [ ] Homepage loads
- [ ] Create recipe works
- [ ] Edit recipe works
- [ ] Delete recipe works
- [ ] Search works
- [ ] AI chat responds

### 2. Environment Variables Ready
Make sure you have:
- [ ] MongoDB Atlas URI
- [ ] Groq API Key
- [ ] MongoDB Atlas allows connections from 0.0.0.0/0

### 3. Git Repository
```bash
cd /workspaces/Assignment_durapid
git status  # Check files
git add .
git commit -m "Ready for deployment"
git push origin main
```

## 🚀 Deploy to Vercel

### Method 1: Vercel Dashboard (Easiest)

1. Go to https://vercel.com
2. Sign in with GitHub
3. Click "Add New..." → "Project"
4. Import your repository
5. Add environment variables:
   - MONGODB_URI
   - GROQ_API_KEY
6. Click "Deploy"
7. Wait 1-2 minutes
8. Get your URL!

### Method 2: Vercel CLI

```bash
# Install Vercel CLI
npm i -g vercel

# Login
vercel login

# Deploy
cd /workspaces/Assignment_durapid
vercel

# Add env vars
vercel env add MONGODB_URI
vercel env add GROQ_API_KEY

# Deploy to production
vercel --prod
```

## 🧪 Post-Deployment Testing

Once deployed, test your live URL:

```bash
# Replace with your Vercel URL
export APP_URL="https://your-app.vercel.app"

# Test homepage
curl $APP_URL

# Test in browser
open $APP_URL  # or just visit in browser
```

Test these features:
- [ ] Homepage displays
- [ ] Create new recipe
- [ ] View all recipes
- [ ] Search recipes
- [ ] Edit a recipe
- [ ] Delete a recipe
- [ ] Open AI chat
- [ ] Send message to AI
- [ ] AI responds correctly

## 📧 Final Steps

### 1. Update README
Add your live URL to README.md:
```markdown
## 🌐 Live Demo
**Application URL:** https://your-actual-url.vercel.app
```

### 2. Commit Changes
```bash
git add README.md
git commit -m "Add live demo URL"
git push origin main
```


## 🐛 If Something Goes Wrong

### Check Vercel Logs
1. Go to Vercel Dashboard
2. Select your project
3. Click on latest deployment
4. View "Function Logs" or "Build Logs"

### Common Issues:

**Import errors:**
- Check requirements.txt has all dependencies
- Redeploy after fixing

**MongoDB connection fails:**
- Verify MONGODB_URI in Vercel env vars
- Check MongoDB Atlas network access (allow 0.0.0.0/0)

**AI not responding:**
- Verify GROQ_API_KEY in Vercel env vars
- Check Groq API quota/limits

**404 errors:**
- Verify vercel.json is in root directory
- Check file paths in vercel.json

## ✨ You're Done!

Congratulations! Your application is now live and accessible worldwide! 🎉

Share the links and wait for feedback from Durapid Technologies!
