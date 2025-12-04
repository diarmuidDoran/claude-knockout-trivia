# Railway Deployment - Quick Start

## Files Created for Railway

✅ **Procfile** - Tells Railway how to start your app
✅ **railway.toml** - Railway configuration with health checks
✅ **.env.example** - Template for environment variables
✅ **runtime.txt** - Specifies Python 3.11.6
✅ **RAILWAY_DEPLOYMENT.md** - Complete deployment guide
✅ **main.py** - Updated to serve frontend and use PORT env var

---

## Quick Deploy Steps

### 1. Push to GitHub (Already Done! ✓)
```bash
git add .
git commit -m "Add Railway deployment configuration"
git push origin main
```

### 2. Deploy on Railway
1. Go to https://railway.app
2. Click "New Project" → "Deploy from GitHub repo"
3. Select `claude-knockout-trivia`
4. Railway auto-deploys!

### 3. Add PostgreSQL
1. In project, click "+ New" → "Database" → "PostgreSQL"
2. DATABASE_URL automatically configured

### 4. Seed Database
```bash
# Install Railway CLI
npm install -g @railway/cli

# Login and link
railway login
railway link

# Run seeding
railway run python backend/seed_questions.py
```

### 5. Open Your App
```
https://your-app.railway.app
```

---

## What Railway Does Automatically

✅ Detects Python project
✅ Installs from `backend/requirements.txt`
✅ Sets PORT environment variable
✅ Provides PostgreSQL with DATABASE_URL
✅ Runs health checks on `/health`
✅ Serves frontend from `/`
✅ Enables WebSocket support
✅ Provides free HTTPS

---

## Environment Variables

Railway auto-sets:
- `DATABASE_URL` - PostgreSQL connection
- `PORT` - App port (Railway assigns)

Optional (you can add in Railway dashboard):
- `ENVIRONMENT=production`
- `FRONTEND_URL=https://your-app.railway.app`

---

## URLs After Deployment

- **Homepage**: `https://your-app.railway.app/`
- **TV Screen**: `https://your-app.railway.app/tv.html`
- **Mobile**: `https://your-app.railway.app/mobile.html`
- **API**: `https://your-app.railway.app/api/`
- **Health**: `https://your-app.railway.app/health`

---

## Frontend Auto-Configuration

Your `frontend/js/config.js` already detects the environment:
- **Development**: Uses `localhost:8001`
- **Production**: Uses current domain automatically

No changes needed! 🎉

---

## Troubleshooting

**Build Failed?**
- Check Railway logs for errors
- Verify `backend/requirements.txt` is correct

**Database Connection Error?**
- Ensure PostgreSQL service is running
- Check DATABASE_URL is set

**404 on Frontend?**
- Verify `frontend/` directory exists
- Check Railway logs for static file serving

**WebSocket Issues?**
- Railway supports WebSockets by default
- Check CORS settings in `main.py`

---

## Cost

**Free Tier:**
- $5 credit per month
- Enough for development/testing
- Scales automatically

**Hobby Plan:**
- $5/month after free credit
- Perfect for production

---

## Next Steps

1. ✅ Deploy to Railway
2. ✅ Test all features
3. ✅ Add custom domain (optional)
4. ✅ Set up monitoring
5. ✅ Share with players!

---

For detailed instructions, see: [RAILWAY_DEPLOYMENT.md](RAILWAY_DEPLOYMENT.md)
