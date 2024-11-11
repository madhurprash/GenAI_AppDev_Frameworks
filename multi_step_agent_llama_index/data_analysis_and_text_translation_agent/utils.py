# This is the utils.py file containing utility functions to create the boto3 session
# as well as creating and initializing the bedrock converse llm for llama_index
import os
import boto3
import logging
from enum import Enum
from pathlib import Path
from typing import Optional, Dict
from llama_index.llms.bedrock import Bedrock

# Initialize the boto3 session
session = boto3.session.Session()
region_name = session.region_name

# Set up the logger
logging.basicConfig(format='[%(asctime)s] p%(process)s {%(filename)s:%(lineno)d} %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def get_bedrock_llm(model_id: str = "anthropic.claude-3-sonnet-20240229-v1:0") -> Optional[Bedrock]:
    """
    Initialize a Bedrock LLM using the existing session credentials
    
    Args:
        model_id: The Bedrock model identifier to use
        
    Returns:
        Bedrock: Configured Bedrock LLM instance
    """
    try:
        llm: Optional[Bedrock] = None
        # Get credentials from the existing session
        credentials = session.get_credentials()
        frozen_credentials = credentials.get_frozen_credentials()
        
        # Initialize the Bedrock LLM
        llm = Bedrock(
            model=model_id,
            aws_access_key_id=frozen_credentials.access_key,
            aws_secret_access_key=frozen_credentials.secret_key,
            aws_session_token=frozen_credentials.token,
            region_name=region_name
        )
    except Exception as e:
        logger.error(f"Error initializing Bedrock LLM: {e}")
        llm = None
    return llm
