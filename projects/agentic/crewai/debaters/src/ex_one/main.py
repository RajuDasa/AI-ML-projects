#!/usr/bin/env python
import sys
import warnings
from dotenv import load_dotenv
from ex_one.crew import Debate
import os

os.environ["LITELLM_SUPPRESS_WARNINGS"] = "1"  #to stop warning - Missing dependency No module named 'fastapi'. Run `pip install 'litellm[proxy]'
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")
load_dotenv()

def run():
    """
    Run the crew.
    """
    inputs = {
        'motion': 'There needs to be strict laws to regulate LLMs',
    }
    
    try:
        result = Debate().crew().kickoff(inputs=inputs)
        print(result.raw)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
