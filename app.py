# launches the g2p API server
import os
import sys
import logging
from g2p.app import APP
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

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
    logger.info("API documentation will be available at http://localhost:{port}/api/v1/docs")
    
    # Run the built-in g2p API server
    uvicorn.run(APP, host="0.0.0.0", port=port)