# Legal SaaS Requirements (Rajasthan + Central Pilot)

## 1. Primary Objective
Building a scalable, AI-powered **Legal Practice Management Platform** for Advocates, specifically targeting **Rajasthan** and **Central Courts**. The system anticipates DPDP Act 2023 compliance and high-reliability scraping.

## 2. Target Portals (Strict Scope)
 The platform will **strictly** focus on the following portals for this phase:

### A. Central / Federal Systems
1.  **Supreme Court of India** (`sci.gov.in`):
    *   **Scope**: Case Status, Orders, Judgments.
2.  **eCourts Services** (`services.ecourts.gov.in`):
    *   **Scope**: All District & Sessions Courts within **Rajasthan**.
3.  **eCourts Judgments** (`https://judgments.ecourts.gov.in/pdfsearch/index.php`):
    *   **Scope**: Search & Download Judgments (PDF) across all district courts.
    *   **Integration**: Ingested into **Vector DB** for private RAG (complementing Indian Kanoon).

### B. Rajasthan State Systems
1.  **Rajasthan High Court** (`hcraj.nic.in`):
    *   **Critical Feature**: Live Display Board (Real-Time Item Number Polling).
2.  **Revenue Board** (`gcms.rajasthan.gov.in`):
    *   **Scope**: Revenue cases, appeals.
3.  **Land Records** (`apnakhata.rajasthan.gov.in`):
    *   **Scope**: Jamabandi, Mutation Status (Requires Captcha Handling).

---

## 3. User Personas, Detailed Workflows, Key Modules & Functional Requirements

### A. Admin (Superuser)
*   **Responsibility**: Monitor system health and revenue.
*   **Key Features**:
    *   **Scraper Dashboard**: View success rates of scraping jobs per state. (e.g., "Rajasthan HC: 98% Success", "UP Bhulekh: 50% Fail - Captcha Issue").
    *   **User Management**: Approve/Ban Advocates.
    *   **Subscription Plans**: **Unified Paid Tier (₹499/mo)**.
        *   Includes **Unlimited Case Tracking**.
        *   **Real-Time Live Board Alerts**.
        *   **Daily WhatsApp Briefs**.
        *   **RAG Search** (Judgments).

### B. Customer Advocate (Subscriber)
*   **Responsibility**: Track their case portfolio.
*   **Workflow**:
    1.  **Onboarding**: Selects State Bar Council ID.
    2.  **Add Case**: Enters CNR Number OR Advocate Name. System auto-populates list.
    3.  **Daily Routine**: Receives "Morning Brief" WhatsApp at 8 AM.
    4.  **Live Tracking**: Receives "Case Incoming" alert when item number is close.
    5.  **Intelligence**: Uses Search Bar to query "Similar Judgments" (Source: eCourts + Indian Kanoon).

### C. Core Tracking & Intelligence
*   **Scraper Engine**: Robust extraction from the above portals.
*   **IP Proxy Implementation**: Mandatory rotation of Residential IPs to prevent blocking.
*   **Logger Module**: Centralized logging (Error, Info, Warning) for debugging scraper failures and system errors.

### D. User & Subscription Management
*   **Subscription Manager**: Handle User Lifecycles (Paid -> Expired -> Renewed).
*   **Payment Gateway**: Integration with **Razorpay** (or similar) for:
    *   Recurring Subscriptions (Auto-debit UPI/Cards).
    *   One-time Top-ups (for Credits/Quota).

### E. Security & Compliance (DPDP Act 2023)
*   **Data Encryption**: All Case Data and PII (Personal Identifiable Information) must be encrypted at rest (AES-256).
*   **Consent**: "Opt-in" tracking for clients.

### F. Contributor Advocate (Source)
*   **Responsibility**: Provide ground-level intelligence (Crowdsourcing).
*   **Workflow**:
    1.  **Voice Note**: Records "Aaj court 5 mein judge sahab nahi aaye" via App.
    2.  **Verification**: System transcribes and cross-verifies with other inputs.

### G. Support & Feedback
*   **Feedback/Ticket Module**:
    *   In-App "Report Issue" button.
    *   Ticketing System for "Scraper Failed" or "Wrong Data" reports.

---

## 4. Automated Notification Workflow (Hinglish)
*Channel: WhatsApp Business API (WABA)*

### A. Morning Brief (8:00 - 9:00 AM)
> **Template**:
> 📌 **NyayaTrack: Aaj ki Cause List ({Date})**
> Namaste Adv. {Name} ji, aaj aapke total {Count} cases scheduled hain:
>
> 1. **{Case_Title}** (Item {Item_No}) - {Court_Name}
> 2. **{Case_Title}** (Item {Item_No}) - {Court_Name}
>
> ⚖️ **Tip**: High Court wala case subah 10:30 par priority par hai.
> — Team NyayaTrack

### B. Real-Time Court Room Alert
> **Template**:
> ⚠️ **NYAYATRACK ALERT: Case Incoming!**
> Adv. {Name} ji, aapka case **Item No. {My_Item}** ({Court_Name}) abhi call hone wala hai.
>
> **Current Running Item: {Current_Item}**
> Kripya court room ke bahar ya andar maujood rahein.

### C. Evening Summary (6:00 - 7:00 PM)
> **Template**:
> ✅ **NyayaTrack: Aaj ka Progress Report**
> Aaj ke cases ka status:
>
> * **{Case_Title}**: Next Date - {Next_Date} ({Purpose})
> * **{Case_Title}**: Order Reserved.
>
> 📅 **Kal ke liye Alert**: Kal aapka ek Filing deadline hai "{Next_Day_Case}" case mein.
> Aapki digital file update kar di gayi hai.
> — Powered by NyayaTrack

---

## 5. Non-Functional Requirements (SLA & Compliance)

### A. Performance & Scalability
*   **Latency**: Real-Time Alerts must be delivered within **60 seconds** of change on the Display Board.
*   **Throughput**: System must handle **100 Concurrent Scrapers** without degradation.
*   **Uptime**: Target **99.5% Availability** during Court Hours (10 AM - 5 PM).

### B. Compliance & Legal
*   **Data Residency**: All Case Data & PII must be stored within **India (Mumbai Region)** servers (DPDP Act 2023).
*   **Consent**: Strict opt-in for tracking engaging parties.
*   **Scraping Ethics**: Respect `robots.txt` rate limits; Identify User-Agent as `NyayaTrack-Bot`.

## 6. Deliverables (Documentation)
1.  **Developer Docs**: Setup guide, API Reference, Architecture Diagram.
2.  **User Manual**: "How to Add Case", "How to Record Voice Note".
