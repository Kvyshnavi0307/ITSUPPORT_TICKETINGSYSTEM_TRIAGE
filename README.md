AI-Driven IT Support Orchestrator
Automated Ticket Triaging & Sentiment Analysis Engine

1. Executive Summary
This project automates the manual process of IT support ticket classification. By leveraging Python and Generative AI (GPT-4o), the system analyzes raw support requests, determines urgency, detects user sentiment (frustration/neutrality), and exports actionable business intelligence in a structured format.

2. Technical Architecture
The system follows a three-tier architecture:

Data Ingestion Layer: Reads unstructured data from tickets.txt.

Intelligence Layer: Orchestrates a call to the OpenAI API using a specialized "System Prompt" to perform multi-variable analysis (Priority + Sentiment).

Presentation Layer: Parses the AI response and writes to a .csv file, making the data ready for Microsoft Excel or Power BI.

3. Features
Sentiment Detection: Automatically flags "Angry" or "Frustrated" users to prevent SLA breaches.

Dynamic Prioritization: Assigns High/Medium/Low based on the technical impact described in the ticket.

Business Export: Converts conversational AI output into professional spreadsheet data.

4. Prerequisites & Setup
Language: Python 3.13

Libraries: openai

Environment Variables: Requires an OPENAI_API_KEY.

Bash
# To run this project:
pip install openai
python app.py
5. Roadmap (Phase 2 & 3)
Cloud Migration: Transitioning local file storage to Azure Blob Storage.

Serverless Execution: Deploying the Python logic via Azure Functions for 24/7 automation.

Secure Secrets: Implementing Azure Key Vault to manage API credentials.