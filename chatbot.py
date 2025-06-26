import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

st.title('ChatGosuke')

# 사이드바에 OPENAI 모델 선택 및 대화 요약 기능 추가
with st.sidebar:
    st.header('설정')
    # selectbox => 드롭다운 박스
    st.selectbox(
        'OpenAI 모델을 선택하세요',
        ['gpt-4.1', 'gpt-3.5-turbo'],
        key = 'openai_model'
    )

    # 대화 요약
    if st.button("📝 대화 요약"):
        if "message" in st.session_state and st.session_state.message:
            try:
                summary_response = client.chat.completions.create(
                    model=st.session_state.openai_model,
                    messages=[
                        {"role": "system", "content": "대화를 간결하고 이해하기 쉽게 요약해줘."},
                        *st.session_state.message
                    ]
                )
                summary_text = summary_response.choices[0].message.content
                st.subheader("요약 결과:")
                st.write(summary_text)
            except Exception as e:
                st.error(f"요약 중 오류 발생: {e}")
        else:
            st.info("요약할 대화 내용이 없습니다.")

# st.session_state : 세션에 키-값 형식으로 데이터를 저장하는 변수
# openai_model => str , message => []
if 'openai_model' not in st.session_state:
    st.session_state.openai_model = 'gpt-4.1'

# 메세지 세션 초기화
if 'message' not in st.session_state:
    st.session_state.message = []

# 기존의 메세지가 있다면 출력
for msg in st.session_state.message:
    with st.chat_message(msg['role']):
        st.markdown(msg['content'])

# prompt => 사용자 입력창
if prompt := st.chat_input('메세지를 입력하세요'):
    # messages => [], 대화 내용 추가
    st.session_state.message.append({
        'role': 'user',
        'content': prompt
    })

    with st.chat_message('user'):
        st.markdown(prompt)

    with st.chat_message('assistant'):
        stream = client.chat.completions.create(
            model=st.session_state.openai_model,
            messages=[
                {
                    'role': m['role'],
                    'content': m['content']
                }
                for m in st.session_state.message
            ],
            stream=True
        )
        response = st.write_stream(stream)

    st.session_state.message.append({
        'role': 'assistant',
        'content': response
    })  
