A demonstration of a multimodal RAG agent with:  
* [x] Reranking Features
* [x] Live Search Agent

The implementation is inspired from the NVIDIA GenAI [examples](https://github.com/NVIDIA/GenerativeAIExamples) with some more enhancements on the lines to handle multiple configurations for different stakeholders and using reranking and agent functionalites in order to get more relevant and correct results from the RAG application.

## Steps Implemented:  
1. Retrieval from user provided knowledge base.
2. Ranking for retreived documents to only pass the relevant documents in LLM API call.
3. Incorporation of positve/negative binary feedack, that saves the feedback data in a [Google Sheet](https://docs.google.com/spreadsheets/d/1XgKCxp2qMASO3bwhPBJQBOavY1Fnqd6ZFZ3rnxLP9Nk/edit?usp=sharing).
4. Addition of a search agent which comes into picture if the user gives negative feedback on the RAG response.
5. Guardrail Implementation using LLM as a Judge (code is commented.)  
