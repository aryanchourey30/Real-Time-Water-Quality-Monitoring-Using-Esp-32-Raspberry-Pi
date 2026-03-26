# Water Quality Monitoring System

A full-stack smart water monitoring platform that combines IoT sensor readings, community reviews, weather context, and AI-assisted analysis to help users understand water conditions in a location.

This project was built to demonstrate practical software engineering across frontend development, backend API design, real-time systems, AI integration, and data-driven user experiences.

## Why This Project Stands Out

- Solves a real problem with a clear social impact: safer and more transparent water quality reporting.
- Blends multiple data sources instead of relying on a single static dataset.
- Demonstrates full-stack ownership across React, Node.js, MongoDB, Python, and AI workflows.
- Includes both real-time monitoring and community-driven review intelligence.
- Shows engineering tradeoffs such as fallback handling, API redundancy, modular routing, and service-based backend design.

## Core Features

- Real-time water quality monitoring for location-based analysis
- ESP32-ready backend endpoints for IoT sensor ingestion
- Community review submission and review-based quality insights
- AI-powered summaries and analysis for water quality interpretation
- Weather and rainfall context for environmental correlation
- Location-aware API flows for district or coordinate-based queries
- Chatbot support with Python/HuggingFace integration and Node.js fallback handling
- Modular backend architecture with route, middleware, model, and service separation

## Tech Stack

### Frontend

- React 18
- TypeScript
- Vite
- Tailwind CSS

### Backend

- Node.js
- Express.js
- MongoDB with Mongoose
- Socket.IO
- JWT authentication
- Winston logging

### AI and Data Intelligence

- OpenAI API for analysis endpoints
- Python LLM bridge for chatbot support
- HuggingFace integration with fallback responses

### External Integrations

- OpenWeatherMap
- WeatherAPI
- AccuWeather
- Google Maps APIs
- Twilio
- Nodemailer

## System Architecture

1. ESP32 devices or user-generated reviews send water-related inputs to the backend.
2. The Express API validates, processes, and stores data in MongoDB.
3. Weather and location services enrich the collected records.
4. AI modules generate summaries, interpretations, and chatbot responses.
5. The React frontend visualizes insights for users in an accessible dashboard experience.

## Project Structure

```text
project water main - Final/
|-- backend/
|   |-- middleware/       # Auth, validation, caching, error handling
|   |-- models/           # MongoDB schemas and AI helper modules
|   |-- routes/           # API route modules
|   |-- scripts/          # Seed and utility scripts
|   |-- services/         # Socket, Redis placeholder, LLM integration services
|   |-- utils/            # Logger and shared helpers
|   |-- package.json
|   |-- README.md
|   `-- server.js
|-- frontend/
|   |-- src/
|   |   |-- components/   # Dashboard, monitoring, chatbot, analysis UI
|   |   |-- utils/        # API helpers
|   |   |-- App.tsx
|   |   `-- main.tsx
|   |-- package.json
|   `-- vite.config.ts
|-- README.md
|-- README_CHATBOT_SETUP.md
|-- requirements.txt
`-- start_backend.bat
```

## Key Engineering Highlights

### Full-Stack Integration

The frontend and backend are separated cleanly, with Vite proxy support for local development and modular API routing on the backend.

### AI with Practical Fallback Design

The chatbot flow is designed with layered resilience:

- Python-based LLM execution
- Node.js fallback handling
- Built-in domain-specific fallback responses

This makes the system more robust than a single fragile AI dependency chain.

### Recruiter-Relevant Strengths

- Real-world problem framing
- End-to-end product thinking
- Multi-service integration
- Clean modular backend organization
- Blend of software engineering and applied AI

## Local Setup

### 1. Clone and open the project

```bash
cd "Auronyx/project water main - Final"
```

### 2. Install frontend dependencies

```bash
cd frontend
npm install
```

### 3. Install backend dependencies

```bash
cd ../backend
npm install
```

### 4. Configure environment variables

Create a `backend/.env` file from `backend/.env.example` and fill in the required values.

### 5. Start the backend

```bash
cd backend
npm run dev
```

The API runs on `http://localhost:5001`.

### 6. Start the frontend

Open another terminal:

```bash
cd frontend
npm run dev
```

The frontend runs on Vite's local dev server and proxies `/api` requests to the backend.

## Environment Variables

The backend uses the following categories of environment variables:

- Server config: `PORT`, `NODE_ENV`, `ALLOWED_ORIGINS`
- Database: `MONGODB_URI`, `MONGODB_URI_PROD`
- Auth: `JWT_SECRET`, `JWT_EXPIRES_IN`, `BCRYPT_ROUNDS`
- AI: `OPENAI_API_KEY`, `HUGGINGFACEHUB_API_TOKEN`
- Weather: `OPENWEATHER_API_KEY`, `WEATHERAPI_KEY`, `ACCUWEATHER_API_KEY`
- Location: `GOOGLE_MAPS_API_KEY`
- Notifications: `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_USER`, `EMAIL_PASS`, `TWILIO_*`
- Optional cache config: `REDIS_URL`

## Example API Areas

- `/health`
- `/api/auth`
- `/api/water-quality`
- `/api/esp32`
- `/api/weather`
- `/api/location`
- `/api/reviews`
- `/api/ai`
- `/api/ai-enhanced/chatbot`
- `/api/notifications`

## Suggested Resume / Portfolio Framing

If you are presenting this project to recruiters, highlight it as:

`Built a full-stack water quality monitoring platform using React, Node.js, MongoDB, AI APIs, and IoT-ready backend services to combine sensor telemetry, community reviews, weather data, and intelligent analysis in a single system.`

## Future Improvements

- Add automated tests for critical API flows
- Introduce Docker-based local setup
- Add deployment documentation for cloud hosting
- Replace placeholder Redis integration with a production cache layer
- Add screenshots or a short demo video to strengthen portfolio presentation

## Project Notes

- The backend startup script has been made portable for local use.
- The chatbot setup details remain available in `README_CHATBOT_SETUP.md`.
- The backend has its own technical README for API-level details, while this file serves as the main recruiter-facing project overview.
