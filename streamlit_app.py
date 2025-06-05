"""A minimal Streamlit app."""

try:
    import streamlit as st
except ModuleNotFoundError as exc:
    raise SystemExit(
        "Streamlit is required to run this app."
    ) from exc


st.write(
    """# My first app
Hello *world!*"""
)
