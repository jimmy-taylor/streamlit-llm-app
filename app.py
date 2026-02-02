import os
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
from openai import OpenAI


# st.secrets ではなく os.environ を使う
api_key = os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)



st.title("専門家質問フォーム")

st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことで質問に回答します。")
st.write("##### 専門家①: プロレス評論家")
st.write("##### 専門家②: K-POP評論家")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["プロレス評論家", "K-POP評論家"]
)

st.divider()


#プロレス評論家モード：入力された内容に対してopenAIのAPIを使用して回答を生成

if selected_item == "プロレス評論家":
    st.header("プロレス評論家に質問する")
    user_input = st.text_area("質問を入力してください。", height=200)
    if st.button("実行"):
        # OpenAI APIを呼び出して回答を生成
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "あなたはプロレス評論家です。"},
                {"role": "user", "content": user_input}
            ]
        )
        answer = response.choices[0].message.content
        st.write(f"プロレス評論家の回答: {answer}")
#K-POP評論家モード：入力された内容に対してopenAIのAPIを使用して回答を生成
else:
    st.header("K-POP評論家に質問する")
    user_input = st.text_area("質問を入力してください。", height=200)
    if st.button("実行"):
        # OpenAI APIを呼び出して回答を生成
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "あなたはK-POP評論家です。"},
                {"role": "user", "content": user_input}
            ]
        )
        answer = response.choices[0].message.content
        st.write(f"K-POP評論家の回答: {answer}")