# This globals file contains different LLMs that will be called as a part of the
# multi step agentic workflow. 
from enum import Enum


# Example model IDs as an Enum for convenience
class BedrockModelIds(str, Enum):
    CLAUDE_3_SONNET: str = "anthropic.claude-3-sonnet-20240229-v1:0"
    CLAUDE_3_HAIKU: str = "anthropic.claude-3-haiku-20240307-v1:0"
    TITAN_TEXT = "amazon.titan-text-express-v1"