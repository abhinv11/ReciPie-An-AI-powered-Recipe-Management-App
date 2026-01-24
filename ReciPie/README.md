# 🍳 Smart Recipe Explorer with AI Assistance

A modern recipe management application built with FastAPI, MongoDB, and AI-powered recipe assistance using Groq's LLM API.

## 🌐 Live Demo

**Application URL:** [Deploy to get your URL]

> After deployment, update this link with your Vercel URL

## 📋 Features

### Core Functionality
- **Recipe Management**: Full CRUD operations (Create, Read, Update, Delete)
- **Smart Search**: Search recipes by name, ingredients, or cooking method
- **AI Recipe Assistant**: Interactive chatbot powered by Groq AI (Llama 3.1 model)
- **Responsive UI**: Clean, modern interface built with Bootstrap 5

### Technical Highlights
- **FastAPI Backend**: High-performance async Python framework
- **MongoDB Database**: NoSQL database for flexible recipe storage
- **LangChain Integration**: Advanced AI conversation management
- **Real-time Chat**: AJAX-powered chat interface
- **Environment-based Config**: Secure API key management

## 🛠️ Tech Stack

**Backend:**
- FastAPI (Python web framework)
- PyMongo (MongoDB driver)
- Python-dotenv (Environment variables)

**AI/ML:**
- LangChain Core (AI orchestration)
- LangChain Groq (Groq API integration)
- Groq AI API (Free LLM service)

**Frontend:**
- HTML5 & Jinja2 Templates
- Bootstrap 5
- Vanilla JavaScript (AJAX)

**Database:**
- MongoDB Atlas (Cloud database)

## 📦 Installation

### Prerequisites
- Python 3.10+
- MongoDB Atlas account (free tier)
- Groq API key ([Get it here](https://console.groq.com))

### Setup Steps

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd ReciPie
```

2. **Create virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables**

Create a `.env` file in the root directory:
```env
MONGODB_URI=your_mongodb_connection_string
GROQ_API_KEY=your_groq_api_key
```

5. **Run the application**
```bash
uvicorn index:app --reload
```

The application will be available at `http://localhost:8000`

## 🚀 Usage

### Adding a Recipe
1. Navigate to the homepage
2. Fill in the recipe form with name, ingredients, and method
3. Click "Submit" to save

### Searching Recipes
- Use the search bar in the navigation to find recipes
- Search works across recipe names, ingredients, and cooking methods
- Click "Clear" to reset search results

### Editing/Deleting Recipes
- Each recipe card has "Edit" and "Delete" buttons
- Edit: Modify recipe details and save changes
- Delete: Remove recipe from database

### AI Recipe Assistant
1. Click "🤖 Ask AI Assistant" in the navigation
2. Type your cooking question or recipe request
3. Get instant AI-powered responses
4. Use "Clear Chat" to reset conversation

**Example queries:**
- "How do I make pasta carbonara?"
- "What can I substitute for eggs in baking?"
- "Give me a quick 15-minute dinner recipe"

## 📁 Project Structure

```
ReciPie/
├── config/
│   └── db.py              # Database configuration
├── models/
│   └── models.py          # Pydantic models
├── routes/
│   └── routes.py          # API routes
├── schemas/
│   └── schemas.py         # Data schemas
├── static/
│   └── style.css          # Custom styles
├── templates/
│   ├── index.html         # Homepage
│   ├── edit.html          # Edit recipe page
│   └── chat.html          # AI chat interface
├── chatbot.py             # AI chatbot logic
├── index.py               # Main FastAPI application
├── .env                   # Environment variables (not in git)
├── .gitignore             # Git ignore rules
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

## 🔒 Security

- All sensitive credentials stored in `.env` file
- `.env` file excluded from version control via `.gitignore`
- MongoDB connection uses secure connection string
- API keys never exposed in code

## 🌐 API Endpoints

### Recipe Management
- `GET /` - Homepage with all recipes
- `POST /` - Create new recipe
- `GET /edit/{id}` - Edit recipe page
- `POST /update/{id}` - Update recipe
- `GET /delete/{id}` - Delete recipe

### AI Chat
- `GET /chat` - Chat interface
- `POST /chat/message` - Send message to AI
- `POST /chat/clear` - Clear chat history

## 🎯 Assignment Requirements Checklist

- ✅ Python backend development (FastAPI)
- ✅ REST API design
- ✅ Frontend integration (Bootstrap + Jinja2)
- ✅ CRUD operations for recipes
- ✅ Search and filtering functionality
- ✅ GenAI integration (Groq AI - free tier)
- ✅ Environment variable management
- ✅ Responsive UI design
- ✅ MongoDB database integration
- ✅ Clean code structure

## 🤖 AI Integration Details

**Model Used:** Llama 3.1 8B Instant
**Provider:** Groq Cloud (Free tier)
**Features:**
- Conversational AI with context retention
- Structured recipe generation
- Cooking tips and substitutions
- Dietary restriction adaptations
- Real-time responses (~560 tokens/second)

**Cost:** $0.05 per 1M input tokens, $0.08 per 1M output tokens

## 🐛 Troubleshooting

**Issue: MongoDB connection error**
- Verify `MONGODB_URI` in `.env` file
- Check MongoDB Atlas network access settings
- Ensure IP address is whitelisted

**Issue: Groq API error**
- Verify `GROQ_API_KEY` in `.env` file
- Check API key validity at console.groq.com
- Ensure you haven't exceeded rate limits

**Issue: Chat not working**
- Verify chatbot.py imports correctly
- Check browser console for JavaScript errors
- Ensure FastAPI server is running

## 📝 Development Approach

1. **Planning**: Analyzed requirements and chose optimal tech stack
2. **Backend First**: Implemented FastAPI routes and MongoDB integration
3. **Frontend**: Built responsive UI with Bootstrap
4. **AI Integration**: Added LangChain-powered chatbot
5. **Security**: Moved all credentials to environment variables
6. **Testing**: Manual testing of all features
7. **Documentation**: Comprehensive README and code comments

## 🔮 Future Enhancements

- User authentication and authorization
- Recipe categories and tags
- Image upload for recipes
- Nutrition information
- Recipe ratings and reviews
- Share recipes via social media
- Export recipes to PDF
- Advanced filtering (prep time, difficulty, cuisine)

## � Deployment

### Deploy to Vercel (Recommended)

See [DEPLOYMENT.md](../DEPLOYMENT.md) for detailed deployment instructions.

**Quick Deploy:**
1. Push code to GitHub
2. Import to Vercel
3. Add environment variables (MONGODB_URI, GROQ_API_KEY)
4. Deploy!

**Requirements:**
- Vercel account (free)
- GitHub repository
- MongoDB Atlas with whitelisted IPs (0.0.0.0/0)

## 👨‍💻 Author

**Abhinav**


## 📄 License

This project is created for educational and evaluation purposes only.

---

**Note:** This application uses free-tier services:
- MongoDB Atlas (Free tier - 512MB storage)
- Groq Cloud (Free tier with rate limits)

For production deployment, consider upgrading to paid tiers for better performance and reliability.
