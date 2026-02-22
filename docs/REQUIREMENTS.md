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
    5.  **e-Filing Sync**: System auto-matches "Filed Cases" (Diary No.) with "Listed Cases" (Case No.) when they appear on board.
    6.  **Intelligence**: Uses Search Bar to query "Similar Judgments".

### C. Core Tracking & Intelligence
*   **Scraper Engine**: Robust extraction from the above portals. **Note: Scrapers only extract available website data; no OCR is performed on documents at this stage. Addition will be done separately laetr and on request**
*   **Scraper Resilience**: Implement **Health Checks** to detect government portal UI changes that cause scraper failure.
*   **IP Proxy Implementation**: Mandatory rotation of Residential IPs to prevent blocking.
*   **Logger Module**: Centralized logging (Error, Info, Warning).

### D. User & Subscription Management
*   **Subscription Manager**: Handle User Lifecycles (Paid -> Expired -> Renewed).
*   **Pricing Structure**: **Unified Paid Tier (₹499/mo) is a baseline sample**. The final model can be tiered based on the volume of requests/cases allowed.
*   **Payment Gateway**: Integration with **Razorpay** (recurring mandate via UPI/Cards).
*   **User Rights**: "Delete Account" button (Right to Erasure) to permanently wipe user data from DB and Backups (Disclaimer: Deletion from system logs is tedious and excluded).

### E. Security & Compliance (DPDP Act 2023)
*   **Data Encryption**: AES-256 for all PII and Case Data at rest.
*   **Data Residency**: Hosting in **India (Mumbai)** region to ensure compliance.
*   **Consent**: "Opt-in" tracking required. **Consent must be explicitly stored in the user data schema along with case data.**
*   **Liability**: Non-compliance carries penalties up to **₹250 Crores**. Strict adherence is mandatory.

### F. Contributor Advocate (Source)
*   **Responsibility**: Provide ground-level intelligence (Crowdsourcing).
*   **Workflow**:
    1.  **Voice Note**: Records "Aaj court 5 mein judge sahab nahi aaye".
    2.  **Verification**: System performs Speech-to-Text on the voice note and verifies it against the data available on the websites.

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
*Note: System must include logic to **prevent duplicate WhatsApp notifications** for the same event.*
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

---

## Appendix: Commercial API Options (Buy vs Build)

While our primary strategy is custom scraping, the following commercial APIs exist as potential fallbacks or "fast-track" options:

### 1. Court Data (Judgments & Case Status)
*   **LegalKart** (`legalkart.com`):
    *   **Features**: Real-time Case Status, Display Board APIs (High Courts), Cause Lists.
    *   **Coverage**: Supreme Court, High Courts, District Courts.
    *   **Cost**: **~₹1 - ₹5 per hit** (Volume based). Enterprise plans available.
    *   **Pros**: Explicit "Display Board API" mentioned. High reliability.
    *   **Cons**: Paid (Per-hit cost).
*   **Surepass** (`surepass.io`):
    *   **Features**: CNR Search, Court Record Check.
    *   **Coverage**: Pan-India.
    *   **Cost**: **~₹2 - ₹5 per verification**.
    *   **Pros**: Good for verification/KYC.
    *   **Cons**: Less focused on real-time "Practice Management" updates.
*   **IDfy** (`idfy.com`):
    *   **Features**: Background Verification.
    *   **Cost**: **~₹50 - ₹100 per full check** (Enterprise only).
    *   **Focus**: Criminal Record Checks (Employment Screening).
*   **Signzy**:
    *   **Focus**: FinTech/Banking KYC.
    *   **Cost**: Enterprise Pricing (High Volume Minimums).

### 2. Land Records (Rajasthan)
*   **Status**: **No Commercial API Exists**.
*   **Reason**: Land records are state subjects. Internal government APIs are not public.
*   **Strategy**: **Custom Scraper** is mandatory for `Apna Khata` and `GCMS`.

### 3. Captcha Strategy (2025 Research)
*   **Primary Provider**: **2Captcha** (Human-based).
    *   **Pros**: Proven reliability with an **approximate 90% success rate**.
    *   **Cons**: Slower (15-45s average). **Caution**: Success rate can drop or downtime increase due to the rising complexity of automated/AI-generated captchas.
*   **Alternative**: **Capsolver** (AI-based).
    *   **Pros**: Fast (3-6s).
    *   **Use Case**: Fallback if 2Captcha latency breaches SLA (>60s) for Real-time alerts.
*   **Verdict**: Start with 2Captcha for **Phase 0** (Accuracy > Speed). Evaluate Capsolver for **Pro Tier** real-time alerts.

### Recommendation
*   **Hybrid Approach**: Build scrapers for Rajasthan-specific portals (Land/Revenue). Consider **LegalKart API** for Court Data if scraper stability becomes a blocker.
