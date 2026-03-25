# 🍳 Smart Recipe Explorer with AI Assistance

## 🌐 Live Demo

**Application URL: [Recipie](https://reci-pie-an-ai-powered-recipe-management-at86ldgnk.vercel.app)**

## 📁 Project Structure

```
/
├── ReciPie/                    # Main application directory
│   ├── config/                 # Database configuration
│   ├── models/                 # Pydantic models
│   ├── routes/                 # API routes
│   ├── schemas/                # Data schemas
│   ├── static/                 # Static files (CSS)
│   ├── templates/              # HTML templates
│   ├── chatbot.py              # AI chatbot logic
│   ├── index.py                # FastAPI main app
│   ├── requirements.txt        # Python dependencies
│   ├── .env                    # Environment variables (not in git)
│   ├── .env.example            # Environment template
│   └── README.md               # Detailed documentation
├── vercel.json                 # Vercel deployment config
├── DEPLOYMENT.md               # Deployment guide
├── DEPLOY_CHECKLIST.md         # Pre-deployment checklist
└── README.md                   # This file
```

## 🚀 Quick Start

### Local Development

```bash
# Navigate to application directory
cd ReciPie

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your credentials

# Run the application
uvicorn index:app --reload
```

Visit http://localhost:8000

### Deploy to Vercel

```bash
# From root directory
vercel
```

Or import via Vercel Dashboard. See [DEPLOYMENT.md](DEPLOYMENT.md) for details.

## ✨ Features

- ✅ **Recipe CRUD Operations** - Create, Read, Update, Delete recipes
- ✅ **Smart Search** - Search by name, ingredients, or method
- ✅ **AI Recipe Assistant** - Groq AI-powered chatbot (Llama 3.1)
- ✅ **MongoDB Database** - Cloud database with MongoDB Atlas
- ✅ **Responsive UI** - Bootstrap 5 interface
- ✅ **Secure Configuration** - Environment-based credential management

## 🛠️ Tech Stack

**Backend:** FastAPI, Python 3.10+
**Database:** MongoDB Atlas
**AI:** Groq Cloud (LangChain)
**Frontend:** Bootstrap 5, Jinja2
**Deployment:** Vercel

## 📚 Documentation

- **[ReciPie/README.md](ReciPie/README.md)** - Complete application documentation
- **[DEPLOYMENT.md](DEPLOYMENT.md)** - Vercel deployment guide
- **[DEPLOY_CHECKLIST.md](DEPLOY_CHECKLIST.md)** - Step-by-step deployment checklist

## 🎯 Assignment Requirements

| Requirement | Status |
|-------------|--------|
| Python backend development | ✅ FastAPI |
| REST API design | ✅ CRUD endpoints |
| Frontend integration | ✅ Bootstrap + Jinja2 |
| Recipe management | ✅ Full CRUD |
| Search and filtering | ✅ MongoDB regex search |
| GenAI integration | ✅ Groq AI (free tier) |
| Environment variables | ✅ .env configuration |
| Deployment | ✅ Vercel-ready |

## 🔒 Environment Variables

Required environment variables (add in Vercel dashboard):

```env
MONGODB_URI=your_mongodb_connection_string
GROQ_API_KEY=your_groq_api_key
```

See `.env.example` in ReciPie folder for template.

## 🧪 Testing

```bash
cd ReciPie

# Test locally
uvicorn index:app --reload

# Test endpoints
curl http://localhost:8000
```

**Manual Testing Checklist:**
- [ ] Create recipe
- [ ] View all recipes
- [ ] Search recipes
- [ ] Edit recipe
- [ ] Delete recipe
- [ ] AI chat functionality

## 📧 Submission

**GitHub Repository:** 
**Live Demo:** 

## 👨‍💻 Author

**Abhinav**


## 📄 License

This project is created for educational and evaluation purposes only.

---

**Need Help?** Check [DEPLOYMENT.md](DEPLOYMENT.md) for deployment instructions or [ReciPie/README.md](ReciPie/README.md) for detailed documentation.
