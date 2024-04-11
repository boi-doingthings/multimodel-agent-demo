#!/bin/bash

# Create and Activate environment
cd ..
python3 -m virtualenv genai
source genai/bin/activate

cd multimodel-agent-demo
pip install -r requirements.txt

export NVIDIA_API_KEY="provide_your_key"


wget https://raw.githubusercontent.com/milvus-io/milvus/master/scripts/standalone_embed.sh
bash standalone_embed.sh start

sleep 3
streamlit run Rank_+_Search.py