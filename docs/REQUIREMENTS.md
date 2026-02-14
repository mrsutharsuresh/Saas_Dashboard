# Legal SaaS Requirements (Rajasthan + Central Pilot)

## 1. Primary Objective
Building a scalable, AI-powered **Legal Practice Management Platform** for Advocates, specifically targeting **Rajasthan** and **Central Courts**. The system anticipates DPDP Act 2023 compliance and high-reliability scraping.

## 2. Target Portals (Strict Scope)
 The platform will **strictly** focus on the following portals for this phase:

### A. Central / Federal Systems
1.  **Supreme Court of India** (`sci.gov.in`):
    *   **Scope**: Case Status, Orders, Judgments.
    *   **Access**: Scraper (Captcha: Image).
2.  **eCourts Services** (`services.ecourts.gov.in`):
    *   **Scope**: Unified Case History for Rajasthan Districts.
    *   **Access**: Scraper (Captcha: 5-char Alphanumeric).
    *   **Note**: No native public API; Mobile App endpoints may be explored for stability.
3.  **eCourts Judgments** (`judgments.ecourts.gov.in`):
    *   **Scope**: Judgment PDF Search & Download.
    *   **Access**: Scraper (Captcha: 5-char Alphanumeric).

### B. Rajasthan State Systems
3.  **Rajasthan High Court** (`hcraj.nic.in`):
    *   **Scope**: Live Display Board (Jaipur/Jodhpur Benches).
    *   **Access**: High-Frequency Polling (10s interval) of JSON/HTML endpoint.
4.  **Revenue Board** (`gcms.rajasthan.gov.in`):
    *   **Scope**: Revenue Case Status.
    *   **Access**: Scraper (Standard Form Post).
5.  **Land Records** (`apnakhata.rajasthan.gov.in`):
    *   **Scope**: Jamabandi, Mutation.
    *   **Access**: Scraper (Captcha: Image/Audio).

---

## 3. User Personas, Detailed Workflows, Key Modules & Functional Requirements

### A. Admin (Superuser)
*   **Responsibility**: Monitor system health and revenue.
*   **Key Features**:
    *   **Scraper Dashboard**: View success rates.
    *   **User Management**: Approve/Ban Advocates.
    *   **Subscription Plans**: **Unified Paid Tier (₹499/mo)**.
        *   Includes **Unlimited Case Tracking**.
        *   **Real-Time Live Board Alerts**.
        *   **Daily WhatsApp Briefs**.
        *   **RAG Search** (Source: eCourts Judgments + Indian Kanoon).

### B. Customer Advocate (Subscriber)
*   **Responsibility**: Track their case portfolio.
*   **Workflow**:
    1.  **Onboarding**: Selects State Bar Council ID.
    2.  **Add Case**: Enters CNR Number OR Advocate Name. System auto-populates list.
    3.  **Daily Routine**: Receives "Morning Brief" WhatsApp at 8 AM.
    4.  **Live Tracking**: Receives "Case Incoming" alert when item number is close.
    5.  **Intelligence**: Uses Search Bar to query "Similar Judgments".

### C. Core Tracking & Intelligence
*   **Scraper Engine**: Robust extraction from the above portals.
*   **IP Proxy Implementation**: Mandatory rotation of Residential IPs to prevent blocking.
*   **Logger Module**: Centralized logging (Error, Info, Warning).

### D. User & Subscription Management
*   **Subscription Manager**: Handle User Lifecycles (Paid -> Expired -> Renewed).
*   **Payment Gateway**: Integration with **Razorpay** (recurring mandate via UPI/Cards).
*   **User Rights**: "Delete Account" button (Right to Erasure) to permanently wipe user data from DB.

### E. Security & Compliance (DPDP Act 2023)
*   **Data Encryption**: AES-256 for all PII and Case Data at rest.
*   **Data Residency**: Hosting in **India (Mumbai)** region to ensure compliance.
*   **Consent**: "Opt-in" tracking for clients with clear Notice.
*   **Liability**: Non-compliance carries penalties up to **₹250 Crores**. Strict adherence is mandatory.

### F. Contributor Advocate (Source)
*   **Responsibility**: Provide ground-level intelligence (Crowdsourcing).
*   **Workflow**:
    1.  **Voice Note**: Records "Aaj court 5 mein judge sahab nahi aaye".
    2.  **Verification**: System transcribes and verified against live board data.

### G. Support & Feedback
*   **Feedback/Ticket Module**:
    *   In-App "Report Issue" button.

---

## 4. Automated Notification Workflow (Hinglish)
*Channel: WhatsApp Business API (WABA)*

### Pricing Note (2025 Update)
*   **Utility Messages**: ~₹0.12 - ₹0.15 per delivered message (Business Initiated).
*   **Cost Implication**: 
    *   Daily Brief + Real-Time Alert = ~2 msgs/day.
    *   Monthly Cost: 60 * ₹0.15 = **₹9.00/user**.
    *   This is well within the **₹499** subscription margin.

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
