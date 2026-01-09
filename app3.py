import streamlit as st
import pandas as pd
from datetime import datetime
import os

REGISTER_FILE = "test.csv"

if st.button("Save"):
    now = datetime.now().strftime("%d/%m/%y %H:%M:%S")

    new_row = {
        "Date Time (UTC)": now,   # <-- THIS is the only thing that matters
        "Value": 123
    }

    if os.path.exists(REGISTER_FILE):
        df = pd.read_csv(REGISTER_FILE)
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    else:
        df = pd.DataFrame([new_row])

    df.to_csv(REGISTER_FILE, index=False)
    st.write(df)
