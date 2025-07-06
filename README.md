# DataAgent Lite - AI-Powered Database Analytics Agent

---

A lightweight AI agent built with Python FastAPI that connects to PostgreSQL databases and provides intelligent business analytics through natural language queries. The agent leverages Google's Gemini API to understand user questions, generate SQL queries, and provide human-readable explanations of the results.

## 🚀 Features

- **Natural Language Processing**: Ask questions in plain English about your database
- **Intelligent SQL Generation**: Automatically generates optimized PostgreSQL queries
- **Schema-Aware**: Dynamically retrieves and understands your database structure
- **Business Intelligence**: Converts raw data into meaningful business insights
- **RESTful API**: Easy-to-use FastAPI endpoints for integration
- **Dockerized Database**: Containerized PostgreSQL setup for easy deployment

## 🛠️ Tech Stack

- **Backend**: Python FastAPI
- **AI/ML**: Google Gemini API
- **Database**: PostgreSQL (Dockerized)
- **ORM**: SQLAlchemy
- **HTTP Client**: HTTPX
- **Validation**: Pydantic

## 📋 Prerequisites

- Python 3.8+
- Docker and Docker Compose
- Google Gemini API key

## 🔧 Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd DataAgent
   ```
2. **Set up virtual environment**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```
3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```
4. **Set up environment variables**
   Create a `.env` file in the root directory:

   ```env
   DATABASE_URL=postgresql://user:password@localhost:5432/analyticsdb
   GEMINI_API_KEY=your_gemini_api_key_here
   ```
5. **Start the PostgreSQL database**

   ```bash
   docker-compose up -d
   ```

## 🚀 Usage

### Starting the Application

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

### API Documentation

Once the server is running, visit:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

### Making Queries

Send POST requests to `/ask` endpoint:

```bash
curl -X POST "http://localhost:8000/ask" \
     -H "Content-Type: application/json" \
     -d '{"question": "How was today'\''s sales compared to yesterday?"}'
```

### Example Response

```json
{
  "sql_query": "SELECT DATE(created_at) as date, SUM(amount) as total_sales FROM sales WHERE DATE(created_at) IN (CURRENT_DATE, CURRENT_DATE - 1) GROUP BY DATE(created_at) ORDER BY date;",
  "result": [
    {"date": "2025-07-05", "total_sales": 15000.50},
    {"date": "2025-07-06", "total_sales": 18500.75}
  ],
  "explanation": "Today's sales ($18,500.75) increased by $3,500.25 compared to yesterday ($15,000.50), representing a 23.3% improvement in daily revenue."
}
```

## 🏗️ Project Structure

```
DataAgent/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application and endpoints
│   ├── agent.py         # AI agent logic and Gemini integration
│   └── db.py            # Database connection and schema utilities
├── Data-Agent/          # API testing files (Bruno)
│   ├── bruno.json
│   └── Query.bru
├── env/                 # Virtual environment
├── docker-compose.yml   # PostgreSQL container configuration
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (create this)
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## 🔍 How It Works

1. **User Input**: User sends a natural language question via API
2. **Schema Analysis**: Agent retrieves current database schema structure
3. **SQL Generation**: Gemini API generates appropriate PostgreSQL query
4. **Query Execution**: Generated SQL is executed against the database
5. **Result Processing**: Raw results are processed through Gemini for human-readable explanation
6. **Response**: User receives SQL query, raw results, and business explanation

## 📊 Example Use Cases

- **Sales Analytics**: "What were our best-selling products last month?"
- **Performance Tracking**: "Show me the revenue trend for the past quarter"
- **Customer Insights**: "Which customers have the highest lifetime value?"
- **Operational Metrics**: "How many orders were processed this week?"

## 🔒 Environment Variables

| Variable           | Description                  | Required |
| ------------------ | ---------------------------- | -------- |
| `DATABASE_URL`   | PostgreSQL connection string | Yes      |
| `GEMINI_API_KEY` | Google Gemini API key        | Yes      |

## 🐳 Docker Setup

The project includes a PostgreSQL container configured with:

- **Username**: `user`
- **Password**: `password`
- **Database**: `analyticsdb`
- **Port**: `5432`

To start the database:

```bash
docker-compose up -d
```

To stop the database:

```bash
docker-compose down
```

## 🧪 Testing

The project includes Bruno API collection for testing:

```bash
# Navigate to Data-Agent directory and use Bruno client
# or import the collection into your preferred API testing tool
```

## 🛡️ Security Considerations

- Store API keys securely in environment variables
- Use connection pooling for database connections
- Implement rate limiting for production use
- Validate and sanitize user inputs
- Use HTTPS in production environments

## 🚀 Deployment

### Production Deployment

1. **Update environment variables** for production database
2. **Set up reverse proxy** (nginx recommended)
3. **Configure SSL certificates**
4. **Set up monitoring and logging**
5. **Use a production WSGI server** like Gunicorn

### Docker Deployment

```bash
# Build and run the application
docker-compose up --build
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🙏 Acknowledgments

- Google Gemini API for AI capabilities
- FastAPI for the excellent web framework
- PostgreSQL for robust database functionality
- SQLAlchemy for ORM capabilities

## 📞 Support

For questions or support, please open an issue in the GitHub repository.

---

**Note**: Make sure to populate your database with relevant tables and data before testing the agent. The agent works best with well-structured business data including sales, customer, product, and order information.
