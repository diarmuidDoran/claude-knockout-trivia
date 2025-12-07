# Railway Deployment Guide

## Prerequisites

- GitHub account with your repository pushed
- Railway account (sign up at https://railway.app)
- PostgreSQL database (Railway provides this)

---

## Step 1: Create Railway Project

1. Go to https://railway.app
2. Click **"New Project"**
3. Select **"Deploy from GitHub repo"**
4. Authorize Railway to access your GitHub
5. Select **`claude-knockout-trivia`** repository

---

## Step 2: Add PostgreSQL Database

1. In your Railway project, click **"+ New"**
2. Select **"Database"** → **"PostgreSQL"**
3. Railway will automatically create a PostgreSQL instance
4. The `DATABASE_URL` environment variable will be automatically set

---

## Step 3: Configure Environment Variables

Railway auto-detects some variables, but you should verify:

### Automatically Set (by Railway):
- `DATABASE_URL` - PostgreSQL connection string
- `PORT` - Port to bind to (Railway assigns this)

### Optional Variables (you can add):
Go to your service → **Variables** tab:

```bash
ENVIRONMENT=production
FRONTEND_URL=https://your-frontend-url.railway.app
```

---

## Step 4: Deploy Backend

Railway will automatically:
1. ✅ Detect Python project
2. ✅ Install dependencies from `backend/requirements.txt`
3. ✅ Run health checks on `/health` endpoint
4. ✅ Start the app using `Procfile` or `railway.toml`

**Build Process:**
```bash
cd backend
pip install -r requirements.txt
```

**Start Command:**
```bash
cd backend
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

---

## Step 5: Initialize Database

After deployment, you need to seed the database with questions:

### Option A: Using Railway CLI

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login to Railway
railway login

# Link to your project
railway link

# Run database initialization
railway run python backend/seed_questions.py
```

### Option B: Using Railway Dashboard

1. Go to your service
2. Click **"Settings"** → **"Deployments"**
3. Find a successful deployment
4. Click **"View Logs"**
5. Use the shell option (if available) to run:
   ```bash
   cd backend && python seed_questions.py
   ```

### Option C: Add to build command

Update `railway.toml`:
```toml
[build]
builder = "nixpacks"
buildCommand = "cd backend && pip install -r requirements.txt && python init_db.py && python seed_questions.py"
```

---

## Step 6: Deploy Frontend (Static Files)

Railway automatically serves your frontend if configured properly.

### Update `main.py` to serve frontend:

The app should already be configured to serve static files. Ensure this is in `backend/app/main.py`:

```python
# Serve frontend static files
frontend_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "..", "frontend")
if os.path.exists(frontend_path):
    app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")
```

---

## Step 7: Get Your Deployment URL

1. Go to your Railway project
2. Click on your service
3. Go to **"Settings"** → **"Domains"**
4. Railway provides a default domain: `your-app.railway.app`
5. (Optional) Add custom domain

---

## Step 8: Update Frontend Configuration

Update `frontend/js/config.js` with your Railway URL:

```javascript
const CONFIG = {
    // Use Railway URL in production
    API_BASE_URL: window.location.origin,
    WS_BASE_URL: window.location.origin.replace('http', 'ws'),
    // ... rest of config
};
```

Or use environment-based detection:
```javascript
const CONFIG = {
    API_BASE_URL: window.location.hostname === 'localhost'
        ? 'http://localhost:8001'
        : window.location.origin,
    WS_BASE_URL: window.location.hostname === 'localhost'
        ? 'ws://localhost:8001'
        : window.location.origin.replace('http', 'ws'),
};
```

---

## Step 9: Test Your Deployment

1. Open your Railway URL: `https://your-app.railway.app`
2. Check health endpoint: `https://your-app.railway.app/health`
3. Test API: `https://your-app.railway.app/api/rooms/`
4. Open TV screen: `https://your-app.railway.app/tv.html`
5. Open mobile: `https://your-app.railway.app/index.html` or `mobile.html`

---

## Monitoring & Logs

### View Logs:
1. Go to your Railway project
2. Click on your service
3. Click **"Deployments"**
4. View real-time logs

### Check Metrics:
1. Go to **"Metrics"** tab
2. Monitor CPU, Memory, Network usage

---

## Troubleshooting

### Database Connection Issues

**Error:** `could not connect to server`

**Solution:**
```bash
# Verify DATABASE_URL is set
railway variables

# Check PostgreSQL service is running
railway status
```

### Port Binding Issues

**Error:** `Address already in use`

**Solution:** Ensure your app uses `$PORT` from environment:
```python
# In backend/app/main.py
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("app.main:app", host="0.0.0.0", port=port)
```

### Build Failures

**Error:** `pip install failed`

**Solution:** Check `backend/requirements.txt` dependencies are compatible

### CORS Issues

**Error:** `blocked by CORS policy`

**Solution:** Update CORS in `main.py`:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specific Railway URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## Continuous Deployment

Railway automatically redeploys on git push:

```bash
# Make changes locally
git add .
git commit -m "Update feature"
git push origin main

# Railway automatically detects and deploys
```

---

## Cost Optimization

### Free Tier Limits:
- $5 credit per month
- One project with multiple services
- Hobby plan: $5/month after free credit

### Tips:
1. Use single PostgreSQL instance for all environments
2. Monitor usage in Railway dashboard
3. Scale down when not in use (Railway pauses inactive apps)

---

## Environment-Specific Deployments

### Production Branch:
```bash
# Deploy only from main branch
railway up --branch main
```

### Staging Environment:
1. Create new Railway project
2. Link to `develop` branch
3. Use separate database

---

## Security Checklist

- ✅ Use environment variables for secrets
- ✅ Enable HTTPS (automatic on Railway)
- ✅ Restrict CORS origins in production
- ✅ Use strong PostgreSQL passwords
- ✅ Keep dependencies updated
- ✅ Monitor logs for suspicious activity

---

## Next Steps

1. ✅ Set up custom domain
2. ✅ Configure SSL certificate (automatic)
3. ✅ Set up monitoring and alerts
4. ✅ Configure backup strategy for database
5. ✅ Set up CI/CD pipeline (optional)

---

## Useful Commands

```bash
# Railway CLI commands
railway login                  # Login to Railway
railway link                   # Link to project
railway status                 # Check service status
railway logs                   # View logs
railway run <command>          # Run command in Railway environment
railway variables              # List environment variables
railway variables set KEY=value # Set environment variable
railway open                   # Open project in browser
```

---

## Support

- Railway Documentation: https://docs.railway.app
- Railway Discord: https://discord.gg/railway
- Project GitHub: https://github.com/diarmuidDoran/claude-knockout-trivia
- Issues: https://github.com/diarmuidDoran/claude-knockout-trivia/issues

---

---

## Deployment Status

✅ **Successfully Deployed!**

**Live URL:** https://claude-knockout-trivia-production.up.railway.app

**Verified Working:**
- ✅ Frontend served correctly (index, TV, mobile screens)
- ✅ Backend API responding
- ✅ PostgreSQL database connected
- ✅ Questions seeded automatically on startup
- ✅ WebSocket connections functioning
- ✅ Cross-device testing successful (desktop + mobile)

**Deployment Date:** December 4, 2025

Happy deploying! 🚀
