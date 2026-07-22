import streamlit as st


st.set_page_config(page_title="GepAi")



if "messages" not in st.session_state:
    st.session_state.messages = []          # list of all chat messages

if "total_messages" not in st.session_state:
    st.session_state.total_messages = 0     # goes up every message sent yes

# ---- Sidebar ----
st.sidebar.title("GepAi")


st.sidebar.markdown("---")

st.sidebar.subheader("Session Stats")
col1, col2 = st.sidebar.columns(2)


col1.write("Messages")
col1.write(len(st.session_state.messages))

col2.write("Total")
col2.write(st.session_state.total_messages)

st.sidebar.markdown("---")

st.sidebar.subheader("Controls")

accent = st.sidebar.selectbox("Accent", ["Nigeria", "USA", "UK", "India"])

temperature = st.sidebar.slider(
    "Model Temperature",
    min_value=0.0,
    max_value=2.0,
    value=1.20
)

# ---- Main chat area ----
st.title("Chat")

# Show every message that has been sent so far
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ---- Chat input box at the bottom ----
user_input = st.chat_input("Message GePAI")

if user_input:
    # 1. Save and show the user's message
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.session_state.total_messages += 1

    with st.chat_message("user"):
        st.write(user_input)

    # 2. Placeholder reply for now.
    
    bot_reply = "hello."

    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    st.session_state.total_messages += 1

    with st.chat_message("assistant"):
        st.write(bot_reply)