# Define the global variables: AWS Region, Model IDs for different models that are used in different 
# parts of the haystack pipeline and DSPy workflow
AWS_REGION: str = "us-west-2"
BEDROCK_HAIKU_MODELID: str = "anthropic.claude-3-haiku-20240307-v1:0"
SONNET_3_5_MODELID: str = "anthropic.claude-3-5-sonnet-20240620-v1:0"
SONNET_MODELID: str = "anthropic.claude-3-sonnet-20240229-v1:0"
TITAN_TEXT_EMBED_MODELID: str = "amazon.titan-embed-text-v2:0"
PUBMED_QA_CSV_FNAME: str = "PubMedQA_instruction.csv"
# Number of rows that need to be extracted that will be written in 
# the in memory document store.
NUM_ROWS: int = 1000

# Data directory where the HF dataset will be loaded
DATA_DIR: str = "data"

# This is the bucket where your haystack pipeline will be stored.
# This bucket will be created if it does not exist.
HAYSTACK_PIPELINE_BUCKET: str = "sagemaker-us-east-2-015469603702"

# This is the file key for the haystack pipeline.
HAYSTACK_PIPELINE_KEY: str = "pipelines/basic_rag_pipeline.yml"