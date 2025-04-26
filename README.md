ServiceMatch: AI-Powered Service Provider Finder
ServiceMatch is a web application that connects users with local service providers by leveraging AI and location-based services. Users input a text description of their problem (e.g., "leaky faucet") and their location (e.g., "New York, NY"). The app uses natural language processing (NLP) to classify the issue into a service category (e.g., plumbing) and queries the Google Maps Places API to suggest nearby providers, displayed with an interactive map. Built in one week using free tools, ServiceMatch showcases full-stack development, AI integration, and API usage, making it a compelling portfolio project for job applications at service-oriented tech companies like Justpaid, Thumbtack, Yelp, Avvo, or Care.com, with potential for a Y Combinator application.

Project Overview
Purpose
ServiceMatch simplifies the process of finding service providers by automating problem classification and provider discovery. It mirrors the functionality of platforms like Thumbtack and Yelp, using AI to enhance user experience, and demonstrates in-demand skills for tech roles.
Why It’s Effective

Relevance: Aligns with service marketplaces by connecting users with professionals, appealing to employers in similar domains.
Technical Showcase: Combines React, Node.js, NLP (Hugging Face), and Google Maps APIs, highlighting full-stack and AI skills.
Job Appeal: Demonstrates domain knowledge and modern tech stack, ideal for fintech (Justpaid) and service platforms.
Startup Potential: Could be pitched to Y Combinator with a commission-based model (e.g., 5% per booking), though the one-week MVP prioritizes job applications.

Target Audience

Job Recruiters: Showcases skills for roles in web development, AI integration, and API-driven applications.
Users: Individuals seeking quick, reliable service provider recommendations.
Y Combinator (Secondary): A prototype for a scalable service marketplace.


Features
Minimum Viable Product (MVP) Features

Problem Description Input:
Form for users to enter a text description (e.g., "my sink is leaking") and location (e.g., "New York, NY").
Responsive design with Tailwind CSS.


AI Classification:
Uses Hugging Face’s zero-shot classification (facebook/bart-large-mnli) to categorize the problem into predefined service categories (e.g., plumbing, electrical).
Displays the detected category to the user.


Service Provider Suggestions:
Geocodes the user’s location using Google Maps Geocoding API.
Queries Google Maps Places API for providers matching the AI-classified category near the user’s location.
Returns provider details (name, address, rating).


Interactive Map Display:
Shows provider locations as markers on a Google Map using the Maps JavaScript API.
Centers the map on the first provider’s location with a default zoom level.



Stretch Goals (Post-MVP, Time Permitting)

Manual category selection dropdown for cases where AI classification is inaccurate.
Provider contact details (e.g., phone, website) via Google Places API.
Basic filtering (e.g., sort by rating or distance).
User feedback form for refining AI classification.


Technical Scope
Tech Stack



Component
Technology
Purpose
Free Deployment



Frontend
React, Tailwind CSS
Responsive UI, form, and map display
Vercel


Backend
Node.js, Express
API endpoints for AI and provider search
Railway


AI
Hugging Face Inference API (facebook/bart-large-mnli)
NLP for problem classification
N/A (free tier)


Location Services
Google Maps APIs (Geocoding, Places, Maps JavaScript)
Geocoding and provider search
N/A ($200 free credit)


Database
JSON file
Store service categories
Local


Architecture

Frontend:
React app with a single-page interface.
Components: Input form, results list, Google Map.
Communicates with backend via Axios for classification and provider data.


Backend:
Express server with two endpoints:
/classify: Takes a problem description and returns the AI-classified category.
/providers: Takes a location and category, geocodes the location, and returns nearby providers.


Uses categories.json to map categories to Google Places types (e.g., plumbing → plumber).


AI:
Hugging Face Inference API handles zero-shot classification.
Predefined categories: plumbing, electrical, cleaning, hvac.


Location Services:
Google Maps Geocoding API converts location strings to coordinates.
Google Maps Places API fetches providers within a 5km radius.
Google Maps JavaScript API renders an interactive map with markers.



Constraints

Time: One-week development for MVP.
Budget: Free tools only (Vercel, Railway, Hugging Face free tier, Google Maps $200 credit).
Scope: Focus on core features; avoid complex additions like user accounts or real-time updates.
API Limits:
Hugging Face: Limited free-tier requests (monitor usage).
Google Maps: $200 monthly credit (sufficient for development and demo).




Detailed Roadmap
The roadmap is structured for a one-week sprint, with daily tasks, deliverables, and contingencies to ensure the MVP is completed on time.
Day 1: Project Setup and Environment Configuration
Objective: Set up development environment, initialize repositories, and acquire API keys.

Tasks:
Install Node.js, VS Code, and Git.
Sign up for Hugging Face, Google Cloud, Vercel, and Railway accounts.
Enable Google Maps APIs (Geocoding, Places, Maps JavaScript) and generate an API key.
Initialize React app in frontend folder:
Run npx create-react-app .
Install dependencies: axios, @react-google-maps/api, tailwindcss, postcss, autoprefixer.
Configure Tailwind CSS.


Initialize Node.js/Express app in backend folder:
Run npm init -y and install express, axios, cors, dotenv.
Create basic server (index.js).


Set up Git repository and push to GitHub.
Create .env files for API keys:
Frontend: REACT_APP_GOOGLE_MAPS_API_KEY
Backend: HUGGING_FACE_API_KEY, GOOGLE_MAPS_API_KEY.




Deliverables:
Functional React and Express apps running locally.
GitHub repository with initial commits.
API keys secured in .env files.


Contingencies:
If Google Cloud setup is delayed, use mock coordinates for initial testing.
If GitHub setup fails, work locally and push later.


Time Estimate: 4-6 hours.

Day 2: Backend Development (AI Classification)
Objective: Implement the /classify endpoint for AI-driven problem classification.

Tasks:
Create categories.json with service categories and Google Places types:[
  { "name": "plumbing", "placesType": "plumber" },
  { "name": "electrical", "placesType": "electrician" },
  { "name": "cleaning", "placesType": "cleaning_service" },
  { "name": "hvac", "placesType": "hvac_contractor" }
]


Implement /classify endpoint in backend/index.js:
Use Axios to call Hugging Face Inference API (facebook/bart-large-mnli).
Pass problem description and candidate labels (categories).
Return the top-scoring category.


Test endpoint with Postman or curl (e.g., curl -X POST http://localhost:5000/classify -d '{"description":"leaky faucet"}').


Deliverables:
Functional /classify endpoint returning AI-classified categories.
categories.json file.


Contingencies:
If Hugging Face API rate limits are hit, use mock classification responses for testing.
If API errors occur, add error handling to return a default category (e.g., plumbing).


Time Estimate: 4-5 hours.

Day 3: Backend Development (Provider Search)
Objective: Implement the /providers endpoint for geocoding and provider search.

Tasks:
Update backend/index.js to include /providers endpoint:
Geocode user’s location using Google Maps Geocoding API.
Map the input category to a Google Places type using categories.json.
Query Google Maps Places API for providers within 5km of the geocoded coordinates.
Return provider details (name, address, rating, location).


Test endpoint with Postman (e.g., curl -X POST http://localhost:5000/providers -d '{"location":"New York, NY","category":"plumbing"}').
Add error handling for invalid locations or API failures.


Deliverables:
Functional /providers endpoint returning provider data.
Backend fully operational for frontend integration.


Contingencies:
If Google Maps API setup fails, return, use mock provider data from categories.json.
If rate limits are hit, cache API responses locally.


Time Estimate: 4-5 hours.

Day 4: Frontend Development (UI and API Integration)
Objective: Build the React frontend with a form, results display, and API integration.

Tasks:
Update frontend/src/App.js to include:
Form for description and location input.
State management for description, location, category, and providers.
Axios calls to /classify and /providers endpoints.
Display for detected category and provider list.


Style form and results using Tailwind CSS for responsiveness.
Test frontend-backend integration locally:
Run backend (node index.js) and frontend (npm start).
Verify category detection and provider display.




Deliverables:
Functional React frontend with form and results.
Styled UI with Tailwind CSS.


Contingencies:
If backend integration fails, use mock API responses.
If styling takes too long, use minimal CSS and refine later.


Time Estimate: 6-8 hours.

Day 5: Frontend Development (Google Maps Integration)
Objective: Add an interactive Google Map to display provider locations.

Tasks:
Update App.js to include Google Map using @react-google-maps/api:
Add LoadScript with Google Maps API key.
Render GoogleMap component with markers for providers.
Set map center to the first provider’s location.


Test map rendering and marker placement.
Ensure responsive map display with Tailwind CSS.


Deliverables:
Interactive map showing provider markers.
Fully functional frontend.


Contingencies:
If map API fails, display provider list only and add map later.
If performance is slow, limit the number of markers (e.g., top 5 providers).


Time Estimate: 4-6 hours.

Day 6: Deployment
Objective: Deploy frontend to Vercel and backend to Railway.

Tasks:
Push code to GitHub:
Frontend: cd frontend && git add . && git commit -m "Complete frontend" && git push
Backend: cd backend && git add . && git commit -m "Complete backend" && git push


Deploy frontend on Vercel:
Import frontend from GitHub.
Set environment variable: REACT_APP_GOOGLE_MAPS_API_KEY.
Note deployed URL (e.g., https://servicematch-frontend.vercel.app).


Deploy backend on Railway:
Import backend from GitHub.
Set environment variables: HUGGING_FACE_API_KEY, GOOGLE_MAPS_API_KEY.
Note deployed URL (e.g., https://servicematch-backend.up.railway.app).


Update App.js to use Railway backend URL.
Test deployed app end-to-end.


Deliverables:
Live demo on Vercel.
Backend API on Railway.


Contingencies:
If deployment fails, use local app for demo and record a screencast.
If CORS issues arise, verify backend CORS settings (cors middleware).


Time Estimate: 4-5 hours.

Day 7: Documentation and Job Application Prep
Objective: Finalize documentation and prepare for job applications.

Tasks:
Update README.md with project details, setup instructions, and screenshots.
Take screenshots of form and results/map, save in screenshots/.
Create a portfolio entry or blog post:
Describe project, challenges, and tech stack.
Include demo and GitHub links.


Update resume with ServiceMatch:ServiceMatch: AI-Powered Service Provider Finder
- Built a web app using React, Node.js, Hugging Face AI, and Google Maps APIs.
- Deployed on Vercel and Railway, showcasing full-stack and AI skills.
- Live Demo: [link] | GitHub: [link]


Draft cover letter snippet:My project, ServiceMatch, aligns with [Company Name]’s mission by using AI to connect users with service providers. Built with React, Node.js, and Google Maps APIs, it demonstrates my full-stack and AI integration skills, which I’m eager to apply at your company.


Identify job postings at Justpaid, Thumbtack, Yelp, Avvo, Care.com, etc.


Deliverables:
Polished README.md with screenshots.
Portfolio entry or blog post.
Updated resume and cover letter.


Contingencies:
If time is short, prioritize README and resume over blog post.
If screenshots are delayed, use placeholder images and update later.


Time Estimate: 4-6 hours.


Challenges and Mitigations



Challenge
Impact
Mitigation



AI Classification Accuracy
Misclassified categories
Add manual category selection dropdown; refine categories in categories.json.


API Rate Limits
Limited requests (Hugging Face, Google Maps)
Monitor usage; cache responses locally; use mock data for testing.


Google Maps API Complexity
Setup delays
Use mock provider data initially; follow Google Cloud setup guides closely.


Time Constraints
Incomplete MVP
Prioritize core features (form, AI, providers, map); defer stretch goals.


CORS Issues
Frontend-backend communication fails
Ensure cors middleware in Express; verify backend URL in frontend.


Deployment Errors
No live demo
Test locally and record screencast; debug Vercel/Railway logs.



Job Application Strategy
Why ServiceMatch Stands Out

Relevance: Mirrors service marketplaces (Thumbtack, Yelp, Care.com) and fintech (Justpaid) by solving real-world problems.
Skills Displayed:
Full-stack development (React, Node.js, Express).
AI integration (Hugging Face NLP).
API usage (Google Maps Geocoding, Places, Maps JavaScript).
Modern tooling (Tailwind CSS, Vercel, Railway).


Portfolio Impact: Live demo and GitHub repo demonstrate end-to-end development and deployment.

How to Present It

Resume:
List ServiceMatch under “Projects” with bullet points on tech stack, deployment, and impact.
Include links to demo and GitHub.


Cover Letter:
Highlight how ServiceMatch aligns with the company’s mission (e.g., user-focused services).
Emphasize AI and web development skills.


Portfolio:
Create a dedicated page or blog post detailing the development process, challenges, and solutions.
Embed screenshots and demo link.


Interviews:
Be prepared to discuss:
Why you chose this project (relevance to service platforms).
Technical challenges (e.g., AI accuracy, API integration).
How you managed time and scope for a one-week MVP.


Walk through the code or demo if requested.



Target Companies

Primary: Justpaid, Thumb  
Secondary: Thumbtack, Yelp, Avvo, Care.com
Others: Tech firms seeking web developers or AI specialists (e.g., startups, fintech, marketplaces).
Application Tips:
Apply via company career pages or LinkedIn.
Tailor cover letters to each company’s mission.
Follow up after 1-2 weeks if no response.



Y Combinator Potential

Business Model: Charge a 5% commission per booking, targeting small service businesses.
YC Pitch (Post-MVP):
Highlight market size (U.S. home services market: ~$600B annually).
Emphasize AI-driven UX and scalability.
Plan user testing and revenue projections for a stronger application.


Note: Focus on job applications first; refine for YC with more polish (e.g., user feedback, advanced features).


Setup Instructions
Prerequisites

Node.js (v16+): nodejs.org
Git: git-scm.com
Accounts:
Hugging Face: huggingface.co (API token)
Google Cloud: cloud.google.com (Geocoding, Places, Maps JavaScript APIs)
Vercel: vercel.com
Railway: railway.app



Installation

Clone the repository:git clone <your-repo-url>


Install frontend dependencies:cd frontend
npm install


Install backend dependencies:cd backend
npm install


Create .env files:
frontend/.env:REACT_APP_GOOGLE_MAPS_API_KEY=your-google-api-key


backend/.env:HUGGING_FACE_API_KEY=your-hugging-face-token
GOOGLE_MAPS_API_KEY=your-google-api-key





Running Locally

Start backend:cd backend
node index.js


Start frontend:cd frontend
npm start


Open http://localhost:3000 in your browser.

Deployment

Frontend (Vercel):
Push frontend to GitHub.
Import to Vercel, set REACT_APP_GOOGLE_MAPS_API_KEY.
Deploy and note URL.


Backend (Railway):
Push backend to GitHub.
Import to Railway, set HUGGING_FACE_API_KEY and GOOGLE_MAPS_API_KEY.
Deploy and update App.js with Railway URL.




Live Demo
ServiceMatch Demo
Screenshots

Input Form: 
Results and Map: 

Future Improvements

Add user authentication for saved searches.
Implement real-time provider updates.
Enhance AI with custom training on service-related texts.
Add advanced filters (e.g., price, availability).

Contact

GitHub: [your-github-profile]
Email: [your-email]
Portfolio: [your-portfolio-url]


Built by [Your Name] as a portfolio project for job applications in web development and AI integration.
