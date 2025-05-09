# launches the g2p API server
import os
import sys
import logging
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from starlette.routing import Route

from g2p import app as g2p_app

async def fixed_home(request):
    return g2p_app.TEMPLATES.TemplateResponse("index.html", {"request": request})

g2p_app.home = fixed_home

from g2p.app import APP

async def root(request):
    return RedirectResponse(url="/api/v1/docs")

APP.routes.append(Route("/", endpoint=root, include_in_schema=False))

APP.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    logger.info(f"Starting G2P API server on port {port}")
    logger.info(f"API documentation will be available at http://localhost:{port}/api/v1/docs")
    
    uvicorn.run(APP, host="0.0.0.0", port=port)