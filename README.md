## Samples for DSPy, Haystack & Bedrock Prompt Flows

This repository contains samples on the basics of DSPy, Haystack and Bedrock Prompt Flows. Each respective topic contains a notebook with a simple RAG application implementation example. View an overview about the concepts and comparison between each framework below:

### DSPy

DSPy is a python based framework specifically tailored towards creating complex, multistep prompt workflows in a reproducible and modular way. It allows users to perform several actions such as chaining prompts, introduce prompt signatures, modular components to handle LM programs. With DSPy, you define the task you want to accomplish and the metrics to measure success. The framework then optimizes the model's behavior for you. It uses easy-to-understand Python syntax, allowing you to concentrate on what your application should do rather than how to prompt the model.

#### Self-improving prompts
One of DSPy's standout features is its ability to automatically improve prompts over time. DSPy continuously refines the prompts, saving you from the hassle of constant manual adjustments. This is achieved using feedback and evaluation, ensuring that the model performs better with each iteration.

#### Modular architecture
DSPy also offers a modular architecture, enabling you to mix and match pre-built modules for different natural language processing (NLP) tasks. This modularity makes it highly customizable to fit your specific needs, promoting flexibility and reusability. The framework includes useful modules like ChainOfThought and ReAct, which can be easily integrated into your applications.

1. **Task Definition**: Once you have defined a task, you can think of a metric of interest to maximize for as a part of your generativeAI application development lifecycle. This is a metric you will use for success (a.k.a your north star metric for your use case). 

1. **Pipeline Construction**: Once the task is defined, you can use several out of the box modules for a specific task. DSPy provides with an option to chain modules together to create complex pipelines. Each module has signatures to define the input and output specifications.

1. **Optimization and Compilation**: Finally, to improve for performance of the metric, you can use DSPy optimizers to use few shot examples, in context learnings and prompt optimizations to get better results. View an example in the notebook provided [here](AWS_DSPy_Examples/dspy_example_bedrock.ipynb).

#### DSPy Use Cases

Use cases that DSPy can help with include: Question answering, Text summarization, Code generation, Translation, etc.

View this [sample notebook](AWS_DSPy_Examples/dspy_example_bedrock.ipynb) to learn more.

### Haystack

Haystack is an open source framework for building production-ready LLM applications, retrieval-augmented generative pipelines and state-of-the-art search systems that work intelligently over large document collections. 

#### Haystack: What does it really entail?

Haystack is composed of two main building blocks for generative AI pipelines: Components and Pipelines

1. **Components**: Components for haystack are building blocks that perform tasks such as document retrieval, text generation, or creating embeddings. A single component is as powerful as to represent a single main part of a generative AI app dev lifecycle. Haystack offers several out of the box Components but you can create your own custom component as well. You can connect components to one another to build _pipelines_.

1. **Pipelines**: Pipelines are powerful abstractions that allow you to define the flow of data through your LLM application. They consist of components.

View this [sample notebook](AWS_Haystack_Examples/sagemaker_haystack_example.ipynb) to learn more.

### Bedrock Prompt Flows

Bedrock prompt flows provides a GUI-based approach to create, test, and evaluate prompt flows, integrating with AWS-hosted models. Prompt Flow is designed for enterprise-scale applications that require reliable, secure, and scalable prompt engineering tools.

View this [sample notebook](Bedrock_Prompt_Flows_Examples/bedrock_prompt_flows_simple_example.ipynb) to learn more. This is a work in progress notebook.
