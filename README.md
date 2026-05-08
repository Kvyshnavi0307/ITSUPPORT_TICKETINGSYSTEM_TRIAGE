 Enterprise IT Service Automation Engine 
*** Strategic Triage Automation & Operational Efficiency Framework ***

1. Executive Summary
This project automates the manual process of IT support ticket classification. By leveraging Python and Generative AI (GPT-4o), the system analyzes raw support requests, determines urgency, detects user sentiment (frustration/neutrality), and exports actionable business intelligence in a structured format.

2.Strategic Capabilities 
Automated Workflow Orchestration:  Replaces manual sorting with a Python-based logic engine that processes incoming support requests in real-time.

Data-Driven Reporting: Generates structured CSV and Text-based analytics to provide leadership with visibility into ticket trends and system health.

Scalable Architecture: Built with a modular design to allow for seamless integration with Cloud environments (Azure) and enterprise API layers.

Risk Mitigation: Standardizes the triage process to eliminate human error and ensure critical high-priority incidents are flagged immediately.

3. Technical Architecture
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

Libraries: OpenAI

Environment Variables: Requires an OPENAI_API_KEY.

5. Roadmap (Phases 2 & 3)
Cloud Migration: Transitioning local file storage to Azure Blob Storage.

Serverless Execution: Deploying the Python logic via Azure Functions for 24/7 automation.

Secure Secrets: Implementing Azure Key Vault to manage API credentials.

6.Business Impact
Cost Reduction: Minimizes the overhead associated with Level 1 support triage.
Increased Accuracy: Ensures 100% compliance with business routing rules.
Operational Scalability: Designed to handle increasing ticket volumes without requiring additional headcount.

---
**Architected by:** Vyshnavi Kurapati  
