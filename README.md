# Field Report Extraction RAG System

This project is a Retrieval-Augmented Generation (RAG) system designed to extract structured data from unstructured field reports.

## Project Goals
- Ingest Data Dictionary / Standard Operating Procedures (SOPs) into a vector database.
- Use Semantic Search to retrieve relevant rules when processing a new field report.
- Extract structured data (e.g., Inspection Date, Location Coordinates, Category, and Quantity) using Pydantic and Instructor.
- Store document chunks in a PostgreSQL database with the pgvector extension.
- Provide a user-friendly web interface using Streamlit to input reports and view extracted JSON data.

## Tech Stack
- **Language**: Python 3.11+
- **Database & Vector Store**: PostgreSQL + pgvector
- **Data Validation & Extraction**: Pydantic + Instructor
- **Ingestion Engine**: LlamaIndex
- **UI**: Streamlit

## Directory Structure
- `/src`: Contains the source code for the application.
- `/data`: Used for storing raw reports, SOPs, or data dictionaries.
- `/docs`: Documentation related to the project.

## Setup Instructions
1. Install dependencies: `pip install -r requirements.txt`.
2. Copy `.env.example` to `.env` and fill in your LLM API credentials and Postgres connection string.
3. Further initialization instructions will follow in subsequent phases.

