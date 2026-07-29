import streamlit as st
import requests
from gtts import gTTS
import io
import uuid
import base64
from streamlit.components.v1 import html as st_html


st.set_page_config(page_title="GePAI")

st.markdown("""
<style>
div[data-testid="stChatMessage"] {
    width: fit-content;
    max-width: 80%;
}
div[data-testid="stChatMessage"]:has(div[data-testid="stChatMessageAvatarUser"]) {
    margin-left: auto;
    margin-right: 0;
    flex-direction: row-reverse;
}
div[data-testid="stChatMessage"]:has(div[data-testid="stChatMessageAvatarUser"]) div[data-testid="stMarkdownContainer"] {
    text-align: right;
}
div[data-testid="stChatMessage"]:has(div[data-testid="stChatMessageAvatarAssistant"]) {
    margin-right: auto;
    margin-left: 0;
}
</style>
""", unsafe_allow_html=True)


ACCENT_TO_TLD = {
    "Nigeria": "com.ng",
    "USA": "us",
    "UK": "co.uk",
    "India": "co.in",
    "Cameroon": "com.ng"
}

if "messages" not in st.session_state:
    st.session_state.messages = []          # list of all chat messages

if "total_messages" not in st.session_state:
    st.session_state.total_messages = 0     # goes up every message sent yes

# ---- Sidebar ----
st.sidebar.title("🌱 GePAI")
st.sidebar.caption("one step at a time")

st.sidebar.markdown("---")

st.sidebar.subheader("📊 Session Stats")
col1, col2 = st.sidebar.columns(2)

col1.write("Messages")
col1.write(len(st.session_state.messages))

col2.write("Total")
col2.write(st.session_state.total_messages)

st.sidebar.markdown("---")

st.sidebar.subheader("⚙️ Controls")

accent = st.sidebar.selectbox("Accent", ["Cameroon", "Nigeria", "USA", "UK", "India"])

temperature = st.sidebar.slider(
    "Model Temperature",
    min_value=0.0,
    max_value=2.0,
    value=1.20
)

# ---- Main chat area ----
st.title("💬 Chat with GePAI")

# Show every message that has been sent so far
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])


user_input = st.chat_input("Message GePAI")

if user_input:
    # 1. Save and show the user's message
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.session_state.total_messages += 1

    with st.chat_message("user"):
        st.write(user_input)


    with st.chat_message("assistant"):
        placeholder = st.empty()
        bot_reply = ""
        try:
            response = requests.post(
                "http://127.0.0.1:8000/ai",
                json={
                    "messages": st.session_state.messages,
                    "accent": accent,
                    "temperature": temperature
                },
                stream=True
            )
            for chunk in response.iter_content(chunk_size=None, decode_unicode=True):
                if chunk:
                    bot_reply += chunk
                    placeholder.write(bot_reply)
        except requests.exceptions.RequestException:
            bot_reply = "Couldn't reach the AI server. Is `uvicorn AI:app --reload` running?"
            placeholder.write(bot_reply)

        st.session_state.messages.append({"role": "assistant", "content": bot_reply})
        st.session_state.total_messages += 1


        try:
            tld = ACCENT_TO_TLD.get(accent, "us")
            tts = gTTS(text=bot_reply, lang="en", tld=tld)
            audio_buffer = io.BytesIO()
            tts.write_to_fp(audio_buffer)
            audio_buffer.seek(0)
            audio_b64 = base64.b64encode(audio_buffer.read()).decode()
            audio_id = f"audio_{uuid.uuid4().hex}"

            st_html(f"""
                <div style="margin:0;padding:0;">
                    <audio id="{audio_id}" src="data:audio/mp3;base64,{audio_b64}"></audio>
                    <button onclick="var a=document.getElementById('{audio_id}'); a.playbackRate=1.25; a.play()"
                        style="background:none;border:none;cursor:pointer;padding:4px;color:#555;">
                        🔊
                    </button>
                </div>
            """, height=36)
        except Exception as e:
            st.warning(f"Couldn't generate audio: {e}")