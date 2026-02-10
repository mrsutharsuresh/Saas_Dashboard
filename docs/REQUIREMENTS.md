# Functional Requirements & Build List

## 1. Project Overview
A specialized B2B SaaS platform designed to bridge data gaps between government portals and professional users.
**Core Value**: Real-time data aggregation, AI-driven voice processing, and controlled client communication via a Mobile-First PWA experience.

## 2. User Roles & Dashboards

### Super Admin (System Owner)
*   **Platform**: Desktop Web Dashboard.
*   **Capabilities**: View total active tenants, API usage metrics (Gemini/WhatsApp), system error logs, and disable/suspend accounts.
*   **Dashboard**: View total active tenants, API usage metrics, and system error logs.
*   **Management**: Ability to disable/suspend a Professional account.
*   **Global Config**: Manage API keys (WhatsApp, Gemini).

### Professional (The Subscriber - Mobile User)
*   **Platform**: **Mobile PWA** (Optimized for Phone).
*   **Capabilities**:
    *   **Voice Workflow**: Instantly create records by speaking.
    *   **Project Management**: Add/Edit Projects, Clients, and view status.
        *   **Add Projects**: Voice Input or Manual ID Entry.
        *   **Manage Projects**: View "My Projects" list with real-time status. Manual "Refresh" trigger.
        *   **Manage Clients**: Add End-Clients (Name, Phone) and link to projects.
    *   **Reviewer**: Validate scraped data and approve WhatsApp drafts.
    *   **Searcher**: Access E-Library for documents/GIS records.

### End-Client (Passive Receiver)
*   **Platform**: None (WhatsApp Only).
*   **Interaction**: Receives updates only after Professional approval.

## 3. Core Modules & Logic

### A. Data Integration & AI Layer
*   **Web Scraper (Playwright)**:
    *   Targets: Two distinct Government Web Portals.
    *   Actions: Navigate, Solve Captcha, Scrape Table Data, Download PDFs.
    *   **Conflict Logic**: Compare `Portal Data` vs `User Manual Data`. Prioritize distinct recent updates.
    *   **Predefined Rules**:
        1.  **Freshness**: If Portal Date > Local Date -> Update Record.
        2.  **Status Change**: If `Status` changes (e.g., Pending -> Approved) -> Trigger Alert.
        3.  **New Record**: If new ID found -> Create Record.
*   **AI Voice Engine**:
    *   **Input**: Mobile Voice Note (Supports Mixed Language/Hinglish).
        *   *Note*: Model handles language switching automatically.
    *   **Process**: Transcribe (Whisper) -> Extract Data (Gemini JSON).
    *   **Output Data**: Structured JSON used to **Pre-fill the "Add Project" Form**.
        *   Example: `{ "client_name": "Ramesh", "survey_number": "123", "village": "Rampur" }`.
    *   **Action**: User reviews the pre-filled form and clicks "Save" to commit to DB.

### B. The "Daily Brief" Engine
*   **Scheduler**: Cron job at 06:00 AM Local Time.
*   **Change Detection**: Compare `new_scrape` vs `old_db_state`.
*   **Trigger**: If change detected -> Queue Draft Notification.

### C. Managed Notification Bridge (Drafts Queue)
*   **Workflow**:
    *   System generates "Draft Message".
    *   **Dashboard/App**: Shows "Pending Approvals".
    *   User Actions: `Approve` (Send), `Edit` (Modify Text), `Delete` (Discard).
*   **Channel**: WhatsApp Business API.
*   **AI Summary**: PDF Docs -> Gemini -> 3-bullet summary included in draft.

### D. Knowledge Repository (E-Library)
*   **Content**: PDF and Text documents.
*   **Features**:
    *   **Fast Search**: Full-text search engine (Postgres `tsvector`).
    *   **Filtering**: By Category, Tags, Year.
    *   **GIS/ID Integration**: Specific search for Government Record IDs.

## 4. Non-Functional Requirements
*   **Database Strategy**:
    *   **Development**: Localhost (Docker).
    *   **Production**: Cloud Managed Database (AWS RDS / DigitalOcean) for 24/7 availability.
*   **Mobile Experience**: **Mobile-First Web App (PWA)** using React.
*   **Data Security**: High-level encryption for Professional's client data (PII).
*   **Accuracy**: Voice processing must handle Indian accents/mixed-language (Hinglish).
