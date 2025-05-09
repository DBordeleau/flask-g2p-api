# launches the g2p API server
import os
import sys
import logging
from g2p.app import APP
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from starlette.routing import Route

# For Starlette apps, we need to use routes differently
# Remove the previous decorator approach and add routes directly
async def root(request):
    return RedirectResponse(url="/api/v1/docs")

# Add the route to the APP's routes list
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
    
    # Run the built-in g2p API server
    uvicorn.run(APP, host="0.0.0.0", port=port)