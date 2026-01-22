# Functional Requirements & Build List

## 1. User Roles & Permissions

### Super Admin
*   [ ] Dashboard to view total active tenants, API usage metrics, and system error logs.
*   [ ] Ability to disable/suspend a Professional account.
*   [ ] Configuration management for global API keys (e.g., WhatsApp, Gemini).

### Professional (The Subscriber)
*   [ ] **Onboarding**: Sign up, profile setup, WhatsApp Business verification status.
*   [ ] **Project Management**:
    *   Add new Project (Input: Application Number / ID).
    *   View grid of all tracked projects with current status.
    *   Manual "Refresh" button for specific projects.
*   [ ] **Client Management**:
    *   Add End-Clients (Name, Phone Number).
    *   Link Projects to End-Clients (One-to-Many).
*   [ ] **Settings**: Configure automated message templates.

### End-Client
*   [ ] **Passive Interaction**: Does not log in. Receives WhatsApp updates.
*   [ ] **content**: "Your project [ID] has moved to status [STATUS]. Summary: [AI_SUMMARY]."

## 2. Core Modules

### A. Data Integration Layer
*   **API Client**:
    *   [ ] Implement rate-limited client for `JSON-based 3rd Party Provider`.
    *   [ ] Map external JSON fields to internal `Project` schema.
*   **Web Scraper (Playwright)**:
    *   [ ] `Input`: Government Portal URL + Record ID.
    *   [ ] `Action`: Navigate, Solve Captcha (if present), Scrape Table Data, Download PDFs.
    *   [ ] `Output`: Structured JSON + PDF Files.
    *   [ ] **Constraint**: Must handle network timeouts and retries gracefully.

### B. The "Daily Brief" Engine
*   **Scheduler**:
    *   [ ] Cron job set for 06:00 AM Local Time.
*   **Change Detection Logic**:
    *   [ ] Fetch current state from DB (`old_state`).
    *   [ ] Fetch new state from Scraper/API (`new_state`).
    *   [ ] Compare fields. If different -> Trigger `Event: UpdateDetected`.

### C. AI Summary Module
*   **Input**: PDF Document (buffer/stream) or lengthy text description.
*   **Process**:
    *   [ ] Send to Google Gemini API with prompt: *"Summarize this technical status update into 3 bullet points for a non-technical client."*
*   **Output**: Clean text string.

### D. Notification Pipeline
*   **Channel**: WhatsApp Business API.
*   **Logic**:
    *   [ ] Queue notification when `Event: UpdateDetected` occurs.
    *   [ ] Check `Professional.subscription_status` before sending.
    *   [ ] Replace placeholders in template: `Hello {client_name}, Update on {project_id}...`
    *   [ ] **Security**: Encrypt PII (Phone Numbers) in logs. Do not log message body if it contains sensitive info.

## 3. Non-Functional Requirements
*   **Latency**: Dashboard load time < 2s.
*   **Throughput**: "Daily Brief" must process 1,000 records within 1 hour (Requires ~17 records/min processing speed).
*   **Reliability**: 99.9% uptime for the Dashboard.
*   **Security**: 
    *   Fernet Encryption for Client Phones.
    *   HTTPS everywhere.
    *   Secure HTTP-only cookies for Auth tokens.
