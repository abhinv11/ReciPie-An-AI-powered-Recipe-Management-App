# 🚀 Vercel Deployment Guide

## Prerequisites
- GitHub account
- Vercel account (sign up at [vercel.com](https://vercel.com))
- Your code pushed to GitHub repository

## Step-by-Step Deployment

### 1. Push Code to GitHub

```bash
cd /workspaces/Assignment_durapid
git add .
git commit -m "Ready for Vercel deployment"
git push origin main
```

### 2. Deploy to Vercel

#### Option A: Via Vercel Dashboard (Recommended)

1. **Go to Vercel**
   - Visit https://vercel.com
   - Click "Sign Up" or "Login"
   - Sign in with GitHub

2. **Import Project**
   - Click "Add New..." → "Project"
   - Select your GitHub repository: `Assignment_durapid`
   - Click "Import"

3. **Configure Project**
   - **Framework Preset:** Other
   - **Root Directory:** Leave as is (or select `ReciPie` if needed)
   - **Build Command:** Leave empty or use `pip install -r ReciPie/requirements.txt`
   - **Output Directory:** Leave empty
   - **Install Command:** `pip install -r ReciPie/requirements.txt`

4. **Add Environment Variables**
   Click "Environment Variables" and add:
   
   ```
   MONGODB_URI = your_mongodb_connection_string
   GROQ_API_KEY = your_groq_api_key
   ```
   
   Make sure to add them for all environments (Production, Preview, Development)

5. **Deploy**
   - Click "Deploy"
   - Wait 1-2 minutes for deployment
   - You'll get a URL like: `https://assignment-durapid.vercel.app`

#### Option B: Via Vercel CLI

```bash
# Install Vercel CLI
npm i -g vercel

# Login to Vercel
vercel login

# Deploy
cd /workspaces/Assignment_durapid
vercel

# Follow prompts:
# - Set up and deploy? Y
# - Which scope? (your account)
# - Link to existing project? N
# - Project name? assignment-durapid
# - Directory? ./
# - Override settings? N

# Add environment variables
vercel env add MONGODB_URI
vercel env add GROQ_API_KEY

# Deploy to production
vercel --prod
```

### 3. Verify Deployment

1. Visit your Vercel URL
2. Test all features:
   - ✅ Homepage loads
   - ✅ Create recipe
   - ✅ Search recipes
   - ✅ Edit recipe
   - ✅ Delete recipe
   - ✅ AI Chat works

### 4. Update README

Add your live demo link to README.md:

```markdown
## 🌐 Live Demo

**Application URL:** https://your-app.vercel.app

Test the live application with full functionality!
```

## ⚠️ Important Notes

### MongoDB Atlas Configuration

**Whitelist Vercel IPs:**
1. Go to MongoDB Atlas Dashboard
2. Network Access → IP Access List
3. Click "Add IP Address"
4. Select "Allow Access from Anywhere" (0.0.0.0/0)
   - For production, use specific Vercel IPs

### Potential Issues & Solutions

**Issue 1: Static files not loading**
- Solution: Vercel doesn't support static file mounting the same way
- Alternative: Use a CDN or external storage for static assets

**Issue 2: MongoDB connection timeout**
- Solution: Check MongoDB Atlas network access
- Ensure connection string in Vercel environment variables is correct

**Issue 3: AI Chat not working**
- Solution: Verify GROQ_API_KEY is set in Vercel dashboard
- Check function timeout limits (Vercel free tier: 10s)

**Issue 4: 404 on routes**
- Solution: Verify `vercel.json` is in root directory
- Check that routes are correctly configured

### Vercel Limitations (Free Tier)

- ⏱️ **Function Timeout:** 10 seconds
- 💾 **Function Size:** 50 MB
- 🔄 **Deployments:** 100 per day
- 📊 **Bandwidth:** 100 GB per month

For AI responses that take longer, consider:
- Using streaming responses
- Optimizing prompts
- Upgrading to Pro plan ($20/month)

## 📱 Testing Production

Test these scenarios:
```bash
# Test homepage
curl https://your-app.vercel.app

# Test API endpoints
curl https://your-app.vercel.app/chat

# Test health
curl https://your-app.vercel.app/
```

## 🔄 Continuous Deployment

Once connected, every push to `main` branch automatically deploys!

```bash
git add .
git commit -m "Update feature"
git push origin main
# Vercel auto-deploys! 🚀
```

## 🎯 Post-Deployment Checklist

- [ ] Application loads successfully
- [ ] All recipes display correctly
- [ ] Search functionality works
- [ ] CRUD operations work
- [ ] AI chat responds correctly
- [ ] No console errors
- [ ] MongoDB connection works
- [ ] Environment variables loaded
- [ ] README updated with live URL
- [ ] Shared live URL with recruiter

## 🌟 Pro Tips

1. **Custom Domain:** Add a custom domain in Vercel dashboard (free on all plans)
2. **Analytics:** Enable Vercel Analytics for usage insights
3. **Preview Deployments:** Every branch gets a preview URL
4. **Logs:** Check deployment logs in Vercel dashboard for errors
5. **Rollback:** Easy rollback to previous deployments if needed







---

**Need Help?**
- Vercel Docs: https://vercel.com/docs
- FastAPI on Vercel: https://vercel.com/guides/using-fastapi-with-vercel
- Support: https://vercel.com/support
