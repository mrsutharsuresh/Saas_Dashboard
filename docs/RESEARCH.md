# Research Notes & Similar Projects

## Similar GitHub Projects
*   **FastAPI React MongoDB Boilerplate**: Good reference for the API structure, though we chose PostgreSQL for relational integrity.
*   **SaaS Pegasus (Django)**: Benchmark for multi-tenant user management features. We are adopting a similar "Team/Organization" data model but implemented in FastAPI.

## Architecture Patterns specific to "Scraping-Heavy SaaS"
*   **Decoupled Scrapers**:
    *   It is critical *not* to run Playwright inside the main API process.
    *   **Pattern**: API pushes "Scrape Request" to Redis. Independent "Worker Containers" (scaled based on CPU/RAM) pick up the job.
    *   **Reason**: Playwright is memory hungry. If a browser crashes, it shouldn't take down the Web API.
*   **Proxy Rotation**:
    *   For government portals, simple IPs often get rate-limited.
    *   **Implementation Note**: We may need to integrate a proxy rotation service (like BrightData or similar) if the 1,000 requests come from a single IP.
*   **Captcha Strategy**:
    *   **Primary Provider**: 2Captcha has a proven success rate of approx 90%.
    *   **Risk**: Captchas are becoming more complex with the advancement of AI, which may cause this success rate to drop. Health checks are essential.
*   **No OCR Policy**: Scraper strictly extracts data from the website DOM. OCR for case documents is out of scope to maintain system efficiency.

## WhatsApp Integration Findings
*   **Meta Cloud API** is the modern standard (replacing the old On-Premise API).
*   **Verification**: The "Professional" (Tenant) will likely need to verify their own Business Manager if they want the message to appear *strictly* from them, OR we can use a "Platform" model where messages come from the SaaS generic number with "On behalf of [Professional Name]" in the text.
    *   *Recommendation*: Start with Platform model (Single Sender) for MVP. It is much easier to manage.
