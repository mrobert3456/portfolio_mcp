import logging
from contextlib import contextmanager
from dotenv import load_dotenv
from langchain_core.documents import Document as LangDocument
from langchain_aws.retrievers import AmazonKnowledgeBasesRetriever
#from langchain_aws.retrievers.bedrock import SearchFilter
from typing import Generator
from typing import List
import os
import boto3

load_dotenv()
KB_ID =os.getenv("AWS_KNOWLEDGEBASE_ID", None)

if KB_ID is None:
    raise ImportError("ENV variable AWS_KNOWLEDGEBASE_ID does not exists")

class RetrievalTool():
    def __init__(self) -> None:
        self.logger = logging.getLogger("retriever_logger")
        self.client = boto3.client(
                            'bedrock-agent-runtime', 
                            region_name='eu-central-1'
                        )

    @contextmanager
    def get_retriever(self) -> Generator[AmazonKnowledgeBasesRetriever, None, None]:
        retriever = AmazonKnowledgeBasesRetriever(
            knowledge_base_id=KB_ID,
            retrieval_config={"vectorSearchConfiguration": {"numberOfResults": 4,
            # "filter":{
            #             "in":{
            #                 "key":"source",
            #                 "value":["baseknowledge",id]
            #             }
            # }
            }},
            
            client=self.client
        )
        try:
            yield retriever
        finally:
            del retriever
    
    def run(self, question: str) -> List[LangDocument]:
        with self.get_retriever() as retriever:
            documents = retriever.invoke(input = question)
            self.logger.info(f"{len(documents)} documents were fetched")
            self.logger.info(f"DOCUMENTS: {documents}")
            
            return documents