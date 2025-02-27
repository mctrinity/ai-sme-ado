# AI SME for Azure DevOps Services

## Overview
This project aims to build an AI-powered **Subject Matter Expert (SME)** for **Azure DevOps Services**. The AI SME will provide intelligent guidance, troubleshoot issues, optimize CI/CD processes, and automate best practices within Azure DevOps.

## Features
- **Pipeline Troubleshooting**: AI-driven analysis and recommendations for Azure DevOps Pipelines.
- **Code Review Automation**: Scan Azure Repos for security, compliance, and quality issues.
- **IaC & Security Compliance**: Ensure Terraform, Bicep, and ARM templates follow best practices.
- **Predictive DevOps Analytics**: Forecast pipeline failures and suggest optimizations.
- **Chatbot Assistant**: AI-powered Q&A support for DevOps engineers.
- **Training & Certification Support**: Assist professionals in preparing for AZ-400 and other certifications.

## Tech Stack
- **Backend**: Python (FastAPI), Node.js
- **AI & NLP**: Azure OpenAI (GPT-4), LangChain
- **DevOps Integration**: Azure DevOps REST API, GitHub Actions
- **Database**: CosmosDB, PostgreSQL
- **Frontend**: React (for dashboards & chatbot)
- **Deployment**: Azure Functions, Kubernetes, Logic Apps

## Setup Instructions
### 1. Clone the Repository
```sh
 git clone https://github.com/mctrinity/ai-sme-ado.git
 cd ai-sme-ado
```

### 2. Install Dependencies
#### Backend
```sh
 cd backend
 pip install -r requirements.txt
```
#### Frontend
```sh
 cd frontend
 npm install
```

### 3. Set Up Azure Resources
- Create an **Azure OpenAI Service** (GPT-4)
- Set up an **Azure DevOps Organization** and generate a **Personal Access Token (PAT)**
- Deploy an **Azure Functions App** for API handling
- Configure **CosmosDB/PostgreSQL** for storing DevOps insights

### 4. Configure Environment Variables
Create a `.env` file in the backend directory:
```sh
AZURE_OPENAI_KEY=your_openai_key
AZURE_DEVOPS_PAT=your_personal_access_token
DATABASE_URL=your_database_url
```

### 5. Run the Application
#### Start Backend
```sh
 cd backend
 uvicorn main:app --reload
```
#### Start Frontend
```sh
 cd frontend
 npm start
```

### 6. Deployment
- Deploy backend using **Azure Functions** or **Kubernetes**
- Deploy frontend on **Azure Static Web Apps**
- Set up **CI/CD Pipelines** for automatic deployments

## Roadmap
- [ ] Build basic AI chatbot for Azure DevOps support
- [ ] Integrate Azure DevOps REST API for pipeline insights
- [ ] Develop ML models for predictive analytics
- [ ] Automate code review and security compliance
- [ ] Deploy and optimize for enterprise usage

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for discussions.

## Contact
Email:  mctrinity24@gmail.com

