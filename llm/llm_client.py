# SPDX-FileCopyrightText: Copyright (c) 2023-2024 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import requests
import os
from llm.llm import create_llm
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage

class LLMClient:
    def __init__(self, model_name="mixtral_8x7b", model_type="NVIDIA"):
        self.llm = create_llm(model_name, model_type)

    def chat_with_prompt(self, system_prompt, prompt):
        langchain_prompt = ChatPromptTemplate.from_messages([("system", system_prompt), ("user", "{input}")])
        chain = langchain_prompt | self.llm | StrOutputParser()
        response = chain.stream({"input": prompt})

        return response

    def multimodal_invoke(self, b64_string, steer=False, creativity=0, quality=9, complexity=0, verbosity=8):
        message = HumanMessage(content=[{"type": "text", "text": "Describe this image in detail:"},
                                        {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{b64_string}"},}])
        if steer:
            return self.llm.invoke([message], labels={"creativity": creativity, "quality": quality, "complexity": complexity, "verbosity": verbosity})
        else:
            return self.llm.invoke([message])
        
    def ranking_model(self, payload,top_r=2):
        assert len(payload['passages'])>=top_r

        invoke_url = "https://ai.api.nvidia.com/v1/retrieval/nvidia/reranking"

        headers = {
            "Authorization": f"Bearer {os.environ['NVIDIA_API_KEY']}",
            "Accept": "application/json",
        }

        print("Printing Payload \n",payload,"\n Payload Over \n")
        session = requests.Session()

        response = session.post(invoke_url, headers=headers, json=payload)

        response.raise_for_status()
        response_body = response.json()
        return [entry['index'] for entry in response_body['rankings'][:top_r]]
