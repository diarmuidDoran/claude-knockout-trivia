# Railway Deployment - Quick Start

## Files Created for Railway

✅ **Procfile** - Tells Railway how to start your app
✅ **railway.toml** - Railway configuration with health checks
✅ **.env.example** - Template for environment variables
✅ **runtime.txt** - Specifies Python 3.11.6
✅ **requirements.txt** - Root requirements file for Railway builder detection
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

### 4. Database Setup (Automatic! ✨)
**Database is initialized and seeded automatically on every startup!**
- ✅ Creates all database tables
- ✅ 1,000+ trivia questions
- ✅ 500 haunting race questions
- ✅ Runs on every app restart
- ✅ Duplicates automatically skipped

No manual setup needed! Railway runs this on startup:
```bash
cd backend && python init_db.py && python seed_questions.py && python load_haunting_race_questions.py
```

**(Optional) Manual seeding via Railway CLI:**
```bash
npm install -g @railway/cli
railway login && railway link
railway run python backend/seed_questions.py
railway run python backend/load_haunting_race_questions.py
```

### 5. Open Your App
```
https://your-app.railway.app
```

---

## What Railway Does Automatically

✅ Detects Python project
✅ Installs from `backend/requirements.txt`
✅ **Seeds all questions (trivia + haunting race)**
✅ Sets PORT environment variable
✅ Provides PostgreSQL with DATABASE_URL
✅ Runs health checks on `/health`
✅ Serves frontend from `/`
✅ Enables WebSocket support
✅ Provides free HTTPS
✅ Auto-redeploys on git push

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

## Useful Railway Resources

- [Railway Documentation](https://docs.railway.app)
- [Railway CLI Reference](https://docs.railway.app/reference/cli-api)
- [Railway Discord Support](https://discord.gg/railway)
