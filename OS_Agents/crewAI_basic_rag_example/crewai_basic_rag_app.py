#!/usr/bin/env python
# coding: utf-8

import os
import logging
import requests
from crewai import LLM, Task, Agent, Crew, Process
from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource

# Set logger
logging.basicConfig(format='[%(asctime)s] %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Global variables
DATA_DIR = "data"
PDF_FILE_NAME_LOCAL = "aws_overview.pdf"
AWS_SERVICES_PDF_URL = "https://docs.aws.amazon.com/pdfs/whitepapers/latest/aws-overview/aws-overview.pdf"
BEDROCK_CLAUDE_3_HAIKU = "anthropic.claude-3-haiku-20240307-v1:0"
TITAN_TEXT_EMBED_V2 = 'amazon.titan-embed-text-v2:0'

# Embedder configuration
embedder_config = {
    "provider": "bedrock",
    "config": {
        "model": TITAN_TEXT_EMBED_V2,
    },
}

# Download and prepare knowledge source
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

try:
    response = requests.get(AWS_SERVICES_PDF_URL)
    response.raise_for_status()
    with open(PDF_FILE_NAME_LOCAL, 'wb') as f:
        f.write(response.content)
    logger.info(f"PDF downloaded: {PDF_FILE_NAME_LOCAL}")
    pdf_source = PDFKnowledgeSource(file_paths=[PDF_FILE_NAME_LOCAL], embedder=embedder_config)
except Exception as e:
    logger.error(f"Error downloading PDF: {e}")
    pdf_source = None

# Define LLMs
llm = LLM(
    model=f"bedrock/{BEDROCK_CLAUDE_3_HAIKU}",
    temperature=0.1,
    timeout=120,
    max_tokens=256,
    top_p=0.9,
)

# Define agents
aws_agent = Agent(
    role="AWS Solutions Architect",
    goal="Answer AWS-related questions.",
    backstory="Expert in AWS solutions architecture with 10 years of experience.",
    llm=llm,
    knowledge_source=[pdf_source],
)

dev_agent = Agent(
    role="Python Developer",
    goal="Generate Python code for coding-related questions.",
    backstory="Expert Python developer with 10 years of experience.",
    llm=llm,
    allow_code_execution=True,
    code_execution_mode="safe",
)

manager_llm = LLM(
    model=f"bedrock/{BEDROCK_CLAUDE_3_HAIKU}",
    temperature=0.1,
    timeout=120,
    max_tokens=256,
    top_p=0.9,
)

manager_agent = Agent(
    llm=manager_llm,
    role="Project Manager",
    goal="Route tasks to the appropriate agent.",
)

# Define tasks
aws_task = Task(
    description="Conduct a research on {topic}.",
    expected_output="Detailed report about {topic}.",
    agent=aws_agent,
)

dev_task = Task(
    description="Generate Python code for the user task: {topic}.",
    expected_output="Executable Python code for {topic}.",
    agent=dev_agent,
    output_file=f"{DATA_DIR}/code.py",
)

# Create and configure Crew
crew = Crew(
    manager_agent=manager_agent,
    agents=[aws_agent, dev_agent],
    tasks=[aws_task, dev_task],
    verbose=True,
    process=Process.hierarchical,
)

def crewai_handler(event, context):
    """
    AWS Lambda handler to execute CrewAI process
    """
    try:
        inputs = event.get("inputs", {})
        result = crew.kickoff(inputs=inputs)
        return {
            "statusCode": 200,
            "body": result,
        }
    except Exception as e:
        logger.error(f"Error executing Crew: {e}")
        return {
            "statusCode": 500,
            "body": str(e),
        }
