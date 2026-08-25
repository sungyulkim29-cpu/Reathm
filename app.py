import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="The Ol' Jitterbug — Rhythm Game",
    page_icon="🎷",
    layout="centered",
)

st.markdown(
    """
    <style>
        .block-container { padding-top: 1.2rem; padding-bottom: 0; max-width: 560px; }
        header, footer { visibility: hidden; }
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = Path(__file__).parent / "game.html"
game_html = html_path.read_text(encoding="utf-8")

st.components.v1.html(game_html, height=760, scrolling=False)

st.caption(
    "크레이지아케이드 오마주 · 실제 곡의 비트를 분석해서 노트를 배치한 리듬 게임입니다. "
    "D · F · J · K 키로 플레이하세요."
)
