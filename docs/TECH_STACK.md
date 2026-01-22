# Technology Stack Selection

## Core Philosophy
The stack is chosen for **performance** (handling concurrent scraping), **scalability** (multi-tenant), and **velocity** (Python/React ecosystem).

| Layer | Technology | Rationale |
| :--- | :--- | :--- |
| **Frontend** | **React (Vite)** | Industry standard, fast dev server, huge ecosystem of UI components. |
| **Styling** | **TailwindCSS** | Utility-first CSS allows for rapid UI development and implementing "Premium" aesthetics easily. |
| **Backend** | **Python (FastAPI)** | <ul style="margin:0"><li>**Async/Await Native**: Crucial for handling 100+ concurrent Playwright browser data streams.</li><li>**Pydantic**: Excellent data validation for untrusted external data sources.</li><li>**Performance**: One of the fastest Python frameworks.</li></ul> |
| **Database** | **PostgreSQL** | Robust relational model is required for the complex relationships between Tenants (Professionals), End-Clients, and Projects. |
| **Task Queue** | **Celery + Redis** | The "Daily Brief" requires scheduling robust jobs. Redis acts as the broker. Celery is battle-tested. |
| **Scraping** | **Playwright (Python)** | Superior to Selenium. Supports modern web features, auto-waiting, and headless execution reliably. |
| **AI** | **Google Gemini API** | Advanced context window for document summarization. Cost-effective compared to competitors. |
| **Deployment** | **Docker** | Containerization ensures consistent environments between dev and prod (especially important for Playwright dependencies). |

## Detailed Breakdown

### 1. Backend: FastAPI vs Django
While Django provides a lot of out-of-the-box features (Admin, ORM), **FastAPI** was chosen because:
*   The application is heavy on **IO-bound background tasks** (scraping).
*   We need lightweight, high-throughput endpoints for the dashboard.
*   We want granular control over the DB queries (using SQLAlchemy or SQLModel) for multi-tenancy optimization.

### 2. Frontend: Vite vs Next.js
We opted for **Vite (SPA)** over Next.js because:
*   The dashboard is a gated, authenticated app. SEO is not a primary concern.
*   SPA provides a snappier "app-like" feel.
*   Simpler deployment (static files served by Nginx/CDN) compared to managing Node.js server runners.

### 3. Database: Multi-Tenancy Strategy
*   **Approach**: **Shared Database, Shared Schema** (most scalable for <10k tenants).
*   **Implementation**: A `tenant_id` column on every major table (`projects`, `clients`, `reports`), indexed and enforced via the ORM service layer.
