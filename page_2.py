import streamlit as st

st.title("page 2") 

st.header("여기는 챗봇 페이지 입니다.")
import streamlit as st
import pandas as pd

st.title("엑셀 데이터 업로드하기")

uploaded_file = st.file_uploader(
    "엑셀 파일을 업로드하세요",
    type=["xlsx", "xls"]
)

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)

    st.success("파일 업로드 완료!")

    st.subheader("업로드한 데이터")
    st.dataframe(df)

    st.subheader("데이터 기본 정보")
    st.write("행 개수:", df.shape[0])
    st.write("열 개수:", df.shape[1])

    st.subheader("컬럼 목록")
    st.write(df.columns.tolist())
else:
    st.info("엑셀 파일을 업로드해 주세요.")