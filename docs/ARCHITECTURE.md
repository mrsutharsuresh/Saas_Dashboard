# Legal SaaS Architecture (Rajasthan + Central Pilot)

## 1. System Overview
A robust, secure platform designed for **Rajasthan Advocates** (Pilot) but built on a **Universal Architecture** capable of Pan-India scale. 
*   **Scalability**: Supports **100+ Concurrent Scrapers** via Celery.
*   **Security**: **AES-256 Encryption** (DPDP Compliant) & Residential Proxy rotation.
*   **Reliability**: Targeted **99.5% Uptime** with auto-healing scraper logic.

---

## 2. High-Level Workflow
```mermaid
graph TD
    User[Advocate Mobile PWA] -->|Auth/Inputs| API[FastAPI Gateway]
    API -->|Read/Write (Encrypted)| DB[(PostgreSQL + pgvector)]
    
    subgraph "Core Modules"
        Logger[Central Logger] -->|Captures| API
        Logger -->|Captures| ScraperWorker
        Reasoning[AI Engine] -->|Process| Voice/RAG
        Payment[Razorpay/Stripe] -->|Subscription| User
        Feedback[Support Ticket] -->|Issue Report| Admin
    end

    subgraph "Scraper Engine (The Worker Nodes)"
        ProxyMgr[Proxy Manager] -->|Rotate IPs| ScraperWorker
        ScraperWorker -->|Polls| HCRaj[HC Raj Display Board]
        ScraperWorker -->|Scrapes| Central[Supreme Court/eCourts]
        ScraperWorker -->|Scrapes| State[Revenue/Land Records]
    end
    
    subgraph "Intelligence Layer"
        Audio[Voice Notes] -->|Whisper API| Transcriber[Text Engine]
        Transcriber -->|LLM Extraction| StructuredData[JSON Case Entity]
        RAG[Legal Search] -->|Indian Kanoon API| Precedents[Judgments]
    end
    
    subgraph "Notification Hub"
        AlertEngine[Alert Logic] -->|Trigger| WhatsAppGateway[Meta/Twilio API]
        WhatsAppGateway -->|Hinglish Msg| EndUser[Advocate]
    end

    ScraperWorker -->|Update Status| DB
    DB -->|State Change| AlertEngine
```

---

## 3. Component Details (Deep Dive)

### A. Scraper Engine & Proxy Management
*   **Proxy Strategy**: 
    *   **Residential IPs**: Mandatory for accessing `apnakhata` and `hcraj` to avoid blocking.
    *   **Rotation Logic**: Rotate IP every `N` requests or on `429/403` error.
    *   **Implementation**: `ProxyManager` class handles IP pool health checks.
    *   **Captcha Solving**: 
        *   **Tier 1**: Local OCR (Tesseract) for simple captchas (Cost: ₹0).
        *   **Tier 2**: 2Captcha/Anti-Captcha API for complex challenges (Cost: ~₹0.10/solve).
*   **Target Portals**:
    *   **Central**: Supreme Court (`sci.gov.in`), eCourts Services (`services.ecourts`), eCourts Judgments (`judgments.ecourts`).
    *   **Rajasthan**: High Court (`hcraj`), Revenue (`gcms`), Land (`apnakhata`).

### B. Live Board Poller (Real-Time)
*   **Specific Challenge**: `hcraj.nic.in` and other HCs have "Display Boards" that update every 10-30 seconds.
*   **Implementation**: Lightweight `aiohttp` poller (No Headless Browser) fetching JSON/HTML every 30s.
*   **Alert Logic**:
    *   Cache `Current_Item_No` in **Redis** (TTL: 60s).
    *   Compare with `User_Case_Item_No`.
    *   If `(User_Item - Current_Item) <= 3` -> Trigger High Priority **"Case Incoming"** Alert.

### C. Legal Intelligence (The Brain)
*   **Voice Pipeline**:
    *   **Input**: MP3/WAV/AAC from WhatsApp or App.
    *   **Process**: `OpenAI Whisper` (Model: `tiny` or `base` for speed) -> Transcribes Hinglish -> `Gemini Flash` extracts {CaseNo, NextDate, Judge}.
*   **RAG (Retrieval Augmented Generation)**:
    *   **Vector DB**: `pgvector` extension in Postgres.
    *   **Data Sources**: **Indian Kanoon API** + **eCourts Judgments** (PDFs).
    *   **Flow**: User Query -> Embedding (OpenAI `text-embedding-3-small`) -> Vector Search -> Context Retrieval -> LLM Summary.

### D. Security & Compliance (DPDP Act 2023)
*   **Encryption at Rest**:
    *   **PII & Case Data**: Encrypted using **AES-256-GCM** before storing in PostgreSQL.
    *   **Keys**: Managed via Environment Variables / AWS KMS.
*   **Data Masking**: Logs must NOT contain full case details or user PII.
*   **Consent**: Explicit opt-in audit trail for tracking client cases.

### D. Notification Hub
*   **Queue System**: Priority Queues in Celery (`high_prio` for Real-time alerts, `low_prio` for Daily Briefs).
*   **Channel**: **WhatsApp Business API** (WABA).
*   **Pricing Optimization**: 
    *   Utilize **24-hour Free Window** for user-initiated conversations.
    *   Batch "Daily Brief" and "Next Date" alerts to minimize paid template usage context.
    *   Est. Cost: **₹0.13 - ₹0.15** per Utility Message.

### E. Ethical Scraping Policy
*   **Robots.txt**: Scrapers must parse and respect `Allow/Disallow` directives where technically feasible.
*   **Rate Limiting**: Hard limit of **1 Request / Minute** per IP per Domain to prevent DoS.
*   **Identity**: User-Agent string will identify as `Bot/LegalTech-Research` to be transparent to admins.

### F. Payment & Subscription Module
*   **Gateway**: **Razorpay** (Primary for India) / Stripe (Global Backup).
*   **Features**:
    *   **Recurring Billing**: Subscriptions (Monthly/Yearly).
    *   **Top-ups**: Credits for extra Court Syncs or Voice Notes.
    *   **Invoicing**: Auto-generation of GST-compliant invoices.

### G. Logging & Monitoring
*   **Logger Module**: 
    *   **Standard**: Structured JSON logging (`structlog`).
    *   **Levels**: `INFO` (Flow), `WARNING` (Retry), `ERROR` (Failure), `CRITICAL` (System Down).
    *   **Storage**: File rotation (Dev) / ELK Stack or CloudWatch (Prod).
*   **Alerting**: Slack/Email alerts to Admin on `CRITICAL` scraper failures.

### H. Infrastructure Scalability
*   **Database**: Managed PostgreSQL with Read Replicas for high-read (Dashboard) traffic.
*   **Worker Nodes**: Auto-scaling Group (ASG) for Scrapers based on Queue Depth.
*   **Monitoring**: Prometheus + Grafana for scraping success rates and error spikes.

### I. Support & Feedback
*   **Ticketing System**: Internal module for users to report "Data Mismatch" or "Feature Request".
*   **Admin View**: Dashboard to triage and resolve reported issues.

---

## 4. Database Schema (Conceptual)

### Entities
*   **Advocate**: `id`, `name`, `phone`, `subscription_status`, `payment_id`.
*   **Court**: `id`, `type` (HC/District/Revenue), `state`, `adapter_code` (e.g., `RAJ_HC`, `RAJ_DIST`, `SUPREME_COURT`).
*   **Case**: `id`, `cnr_number`, `encrypted_data`, `court_id`, `petitioner`, `respondent`, `current_stage`, `next_date`.
*   **Hearing**: `id`, `case_id`, `date`, `business` (Proceeding), `judge_name`.
*   **LiveTracking**: `id`, `advocate_id`, `case_id`, `today_item_no`, `status` (Pending/Called).
*   **Subscription**: `id`, `user_id`, `plan_id`, `start_date`, `end_date`, `status`.
*   **Payment**: `id`, `transaction_id`, `amount`, `gateway_ref`, `status`.
*   **Feedback**: `id`, `user_id`, `category`, `message`, `status`.
