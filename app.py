from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from starlette.routing import Route
from g2p.app import APP as G2P_APP

app = FastAPI()

@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/api/v1/docs")

# Add CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount the G2P app under /api/v1
app.mount("/api/v1", G2P_APP)

if __name__ == "__main__":
    import uvicorn
    import os
    import logging

    port = int(os.environ.get("PORT", 5000))
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info(f"Starting G2P API server on port {port}")
    logger.info(f"API docs at http://localhost:{port}/api/v1/docs")

    uvicorn.run(app, host="0.0.0.0", port=port)
