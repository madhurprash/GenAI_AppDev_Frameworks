# This is the agent file. It uses llama_index to draw a workflow with several different steps.
# This file contains the main agent workflow that contains several steps. As a part of preparing the workflow, 
# the agent identifies the task using an intent classifier agent. The intent classifying agent checks for if
# the task is a data analysis task or a text translation task. If the user is about text translation, the 
# text translation agent workflow will be called which will have a separate set of steps within itself.
# It will prepare the prompt, invoke the model and call tools to translate the text, change the sentiment
# and return the final output to the agent. This is a simple agent workflow example using llama_index.

# Import necessary libraries
# Amazon SDK
import boto3
import logging
# LlamaIndex
from llama_index.core.workflow import (
    StartEvent,
    StopEvent,
    Workflow,
    step,
    # There are two new components that are added here in the workflow below: Event & Context
    Event,
    Context,
)
from llama_index.core.llms import LLM
from llama_index.llms.bedrock import Bedrock
from llama_index.core.llms import MessageRole
from llama_index.core.memory import ChatMemoryBuffer
from llama_index.llms.bedrock_converse import BedrockConverse
from llama_index.utils.workflow import draw_all_possible_flows

# These are the different agents that are used in the workflow. These are the intent workflow agent to identify what the 
# user query is asking for, a data analysis agent to analyze the data and a text translation agent to translate the text.
from agent_workflow.workflow.events import *
from agent_workflow.workflow.schemas import *
from agent_workflow.session import create_boto_session
from agent_workflow.workflow.intent import IntentAgentWorkflow
from agent_workflow.workflow.data_analysis import DataAnalysisAgentWorkflow
from agent_workflow.workflow.text_translation import TextTranslationAgentWorkflow

# These are the tools that are used in the workflow. These are the tools that are used to analyze the data and translate the text.
from audio_chatbot.tools.data_analysis_tool import DataAnalysisToolSpec
from audio_chatbot.tools.text_translation_tool import TextTranslationToolSpec

# Set up the logger
logging.basicConfig(format='[%(asctime)s] p%(process)s {%(filename)s:%(lineno)d} %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

class MainAgentWorkflow(Workflow):
    