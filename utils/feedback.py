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

import gspread
import datetime
import streamlit as st

def add_row_to_sheet(values):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    gc = gspread.service_account(filename="service.json")

    sh = gc.open_by_url("https://docs.google.com/spreadsheets/d/1XgKCxp2qMASO3bwhPBJQBOavY1Fnqd6ZFZ3rnxLP9Nk/edit/")

    worksheet = sh.get_worksheet(0)

    worksheet.append_row(values)

def submit_feedback(feedback, query, response):
    face = feedback['score']
    # score = {"😀": 5, "🙂": 4, "😐": 3, "🙁": 2, "😞": 1}[face]
    score = {"👍":1,"👎":0}[face]
    comment = "Score: " + str(score) + " Feedback: " + feedback['text'] or "none"
    feedback_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    feedback_data = (feedback_time, score, query, response, comment)
    st.toast("Thank you for your feedback!")
    # add to Google Sheet here
    try:
        add_row_to_sheet(feedback_data)
    except Exception as e:
        st.write(e)
        st.toast(f"Failed to add to Google Sheet. Exception: {e}")

def simple_feedback(rating, query, response):
    # score = {"😀": 5, "🙂": 4, "😐": 3, "🙁": 2, "😞": 1}[face]
    score = {"👍":1,"👎":0}
    comment = "Score: " + str(score) + " Feedback: " + feedback['text'] or "none"
    feedback_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    feedback_data = (feedback_time, score, query, response, comment)
    st.toast("Thank you for your feedback!")
    # add to Google Sheet here
    try:
        add_row_to_sheet(feedback_data)
    except Exception as e:
        st.write(e)
        st.toast(f"Failed to add to Google Sheet. Exception: {e}")

feedback_kwargs = {
        "feedback_type": "thumbs",
        "optional_text_label": "Please provide feedback",
        "on_submit": submit_feedback,
    }