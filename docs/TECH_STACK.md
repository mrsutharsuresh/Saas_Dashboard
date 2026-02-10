# Technology Stack Selection

## Core Philosophy
The stack is chosen for **performance** (handling concurrent scraping), **scalability** (multi-tenant), and **velocity** (Python/React ecosystem).

| Layer | Technology | Rationale |
| :--- | :--- | :--- |
| **Frontend** | **React (Vite) + Chakra UI / ShadCN** | Mobile-First Responsive Design (PWA). ShadCN provides accessible, high-quality mobile components. |
| **Backend** | **Python (FastAPI)** | Async support for AI processing and Scraping. |
| **Database** | **PostgreSQL (pgvector)** | Relational data + Vector Embeddings for E-Library Search. |
| **AI Processing** | **Google Gemini 1.5 Flash** | Cost-effective, high-speed LLM for Voice-to-JSON extraction. |
| **Voice** | **Web Audio API + OpenAI Whisper** | Browser-based recording -> Server-side transcription. |
| **Task Queue** | **Celery + Redis** | Managing scrape jobs and AI processing pipelines. |
| **Scraping** | **Playwright (Python)** | Headless browsing for government portals. |

## Detailed Breakdown

### 1. Frontend: Mobile-First PWA
*   **Why React?**: Huge ecosystem. We will use a "Mobile First" CSS framework (Tailwind) to ensure it acts like an App.
*   **PWA Features**: Manifest.json for "Add to Home Screen", Service Workers for offline capabilities.

### 2. Backend: AI & Voice Pipeline
*   **Voice**: Mobile uploads `.webm` or `.mp3`.
*   **Processing**:
    1.  `FastAPI` receives file.
    2.  `Whisper` (or Gemini) transcodes Speech-to-Text.
    3.  `Gemini 1.5` parses text to JSON.


### 3. Database: Multi-Tenancy Strategy
*   **Approach**: **Shared Database, Shared Schema** (most scalable for <10k tenants).
*   **Hosting**:
    *   **Dev**: Docker Desktop (Localhost).
    *   **Prod**: AWS RDS / DigitalOcean Managed DB (Cloud).
*   **Implementation**: A `tenant_id` column on every major table (`projects`, `clients`, `reports`), indexed and enforced via the ORM service layer.
