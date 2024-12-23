import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from ipywidgets import interact, Dropdown
from scipy.optimize import curve_fit
import matplotlib.ticker as ticker

# 페이지 스타일 설정
page_style = """
<style>
/* 사이드바 배경색 */
[data-testid="stSidebar"] {
    background-color: #d9f0ff; /* 밝은 하늘색 */
    padding: 15px;
}

/* 사이드바 텍스트 스타일 */
[data-testid="stSidebar"] .css-1aumxhk {
    font-size: 18px; /* 텍스트 크기 */
    font-weight: bold; /* 텍스트 굵게 */
}

/* 라디오 버튼 스타일 */
.css-10trblm {
    font-size: 16px !important; /* 라디오 버튼 텍스트 크기 */
    color: #0056b3 !important; /* 라디오 버튼 텍스트 색 */
}
</style>
"""
st.markdown(page_style, unsafe_allow_html=True)

# 제목 설정
st.title("💡 회귀분석 및 수학적 모델링")

# CSS 스타일 추가
sidebar_style = """
<style>
/* 사이드바 제목 가운데 정렬 */
[data-testid="stSidebar"] h1 {
    text-align: center;
    font-weight: bold;
}

/* HOME 버튼 굵게 표시 */
.css-1aumxhk div:first-child div[data-baseweb="radio"] > div:first-child label {
    font-weight: bold !important;
}
</style>
"""
st.markdown(sidebar_style, unsafe_allow_html=True)

# 사이드바 네비게이터
st.sidebar.title("📌 수업 차시 안내")
page = st.sidebar.radio(
    "",
    [
        "🏠 HOME",
        "1차시: 회귀분석 알아보기",
        "2차시: 최적 모델 선택하기",
        "3차시: 주도적으로 데이터 분석하기",
    ],
)


# 페이지별 화면

if page == "🏠 HOME":
    st.subheader("🌟 환영합니다!")
    st.info("""
    이 애플리케이션은 **반송고 2학년 회귀분석 탐구 프로젝트 수업**을 위해 설계되었습니다.  
    왼쪽 메뉴에서 수업 차시를 선택하여 시작하세요. 🚀  
    """)
    
    # 로그인 후 콘텐츠 표시
    st.markdown("---")
    st.markdown("""
        ### 📋 애플리케이션의 목적
        - 📊 **데이터 분석 능력 함양**: 데이터를 기반으로 회귀분석 모델을 이해하고 적용합니다.  
        - 🧠 **수학적 사고력 향상**: 함수의 개념과 수학적 모델링을 활용하여 문제를 해결합니다.  
        - 🤝 **협력적 학습**: 모둠 활동을 통해 의견을 공유하고 문제를 해결합니다.  
        """)
        
    st.markdown("""
        ### 🗺️ 탐구 활동 순서
        1️⃣ **1차시: 회귀분석 알아보기**  
        👉 회귀분석의 개념과 다양한 모델 유형에 대해 학습합니다.  
        <br>
        2️⃣ **2차시: 최적 모델 선택하기**  
        👉 데이터를 분석하여 적합한 회귀 모델을 선택합니다.  
        <br>
        3️⃣ **3차시: 주도적으로 데이터 분석하기**  
        👉 모둠별로 데이터를 분석하고, 결과를 발표합니다.  
        """, unsafe_allow_html=True)
        
    st.markdown("""
        ### 📦 활동 준비 사항
        - **팀원과 협력**: 모둠별로 활동하며 결과를 공유하세요.  
        - **호기심과 열정**: 데이터를 탐구하며 질문하고 답을 찾아봅시다!  
        """)
        
    st.markdown("""
        ### 🎯 기대 효과
        본 수업을 통해 데이터 분석 능력을 키우고, 수학적 사고력을 배양하며, 협력적 문제 해결 경험을 쌓을 수 있습니다. 즐거운 탐구 시간이 되길 바랍니다! 😊
        """)


            


    
elif page == "1차시: 회귀분석 알아보기":
    st.subheader("📌1차시: 회귀분석 알아보기")
    st.markdown("""
    오늘은 **회귀분석**이 무엇인지 알아봅시다! 😊  
    아래 순서에 따라 **Step 1부터 Step 3까지** 차근차근 나아가보아요! 🚀
    """)
    
    # Step1: 회귀분석 이해하기
    st.markdown("<h3 style='font-size:20px; font-weight:bold;'>✅Step1) 회귀분석 이해하기</h3>", unsafe_allow_html=True)
    with st.expander("📘 회귀분석이란?"):
        st.markdown("""
        - **회귀분석**이란 두 변수(또는 여러 변수) 사이의 관계를 **수학적 식**으로 나타내고, 그 관계를 통해 결과를 예측하는 방법입니다.  
        - **예시**:  
          - 하루 공부 시간이 많아질수록 시험 점수도 높아질까?  
          - 광고를 많이 하면 물건 판매량이 늘어날까?  
        - 결과 예측을 통해 _"매일 하루에 6시간 이상 공부하면 내 점수는 80점 이상이겠군!"_ 하고 계획을 세울 수 있습니다.  
        - 데이터를 분석하여 **미래를 예측**하고, 우리가 배운 함수 개념을 토대로 **수학적으로 사고**해 봅시다! 🔎
        """)

    # Step2: 회귀분석의 종류
    st.markdown("<h3 style='font-size:20px; font-weight:bold;'>✅Step2) 회귀분석의 종류</h3>", unsafe_allow_html=True)
    with st.expander("📘 회귀분석의 다양한 유형을 살펴봅시다!"):
        st.markdown("""
        <style>
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 10px 0;
        }
        th, td {
            border: 1px solid black;
            padding: 10px;
            text-align: left;
        }
        th {
            background-color: #f9f9f9;
        }
        </style>

        <table>
            <tr>
                <th>회귀 유형</th>
                <th>설명</th>
            </tr>
            <tr>
                <td>📊 선형 회귀</td>
                <td>- 일차함수 \( y = ax + b \)로 관계를 설명<br>- 두 변수의 관계가 직선으로 나타나는 상황</td>
            </tr>
            <tr>
                <td>📈 다항 회귀</td>
                <td>- 다항함수 \( y = ax^2 + bx + c \)로 설명<br>- 두 변수의 관계가 곡선(예: 포물선)으로 나타나는 상황</td>
            </tr>
            <tr>
                <td>📉 지수 회귀</td>
                <td>- 지수함수 \( y = ae^{bx} \)로 설명<br>- 기하급수적으로 증가하거나 감소하는 상황</td>
            </tr>
            <tr>
                <td>📂 로그 회귀</td>
                <td>- 로그함수 \( y = a \log x + b \)로 설명<br>- 독립 변수가 증가하면 종속 변수가 점점 완만해지는 패턴</td>
            </tr>
        </table>
        """, unsafe_allow_html=True)
        
    # Step3: 일상적인 주제 떠올리기
    st.markdown("<h3 style='font-size:20px; font-weight:bold;'>✅Step3) 일상적인 주제 떠올리기</h3>", unsafe_allow_html=True)
    with st.expander("📘 회귀분석으로 설명할 수 있는 일상적인 주제를 떠올려봅시다."):
        st.info("💬 모둠원과 함께 토의하여 각 회귀 유형에 맞는 예시를 작성하고 제출 버튼을 눌러주세요!")

        # 제출 버튼 스타일
        button_style = """
        <style>
        div.stButton > button {
            background-color: #007BFF !important; /* 버튼 배경색 */
            color: white !important; /* 텍스트 색 */
            border-radius: 5px !important; /* 둥근 모서리 */
            padding: 8px 15px !important; /* 버튼 여백 */
            font-size: 16px !important; /* 텍스트 크기 */
        }
        div.stButton > button:hover {
            background-color: #0056b3 !important; /* 호버 배경색 */
        }
        </style>
        """
        st.markdown(button_style, unsafe_allow_html=True)

        # 각 회귀 유형에 대한 작성 및 제출
        topics = {
            "linear_topic": "✍ 두 변수의 관계가 직선으로 나타나는 주제는 무엇일까요?",
            "para_topic": "✍ 두 변수의 관계가 포물선으로 나타나는 주제는 무엇일까요?",
            "exp_topic": "✍ 두 변수의 관계가 기하급수적으로 증가하거나 감소하는 주제는 무엇일까요?",
            "log_topic": "✍ 두 변수의 관계가 로그 함수 패턴으로 나타나는 주제는 무엇일까요?",
        }

        for key, prompt in topics.items():
            st.text_area(prompt, key=key, placeholder="예: ○○○○과 △△△△의 관계")

        # 버튼과 메시지를 같은 줄에 배치 (1:9 비율)
        col1, col2 = st.columns([1, 8])
        with col1:
            submitted = st.button("제출", key=f"submit_{key}")  # 제출 버튼
        with col2:
            if submitted:
                if not st.session_state[key].strip():
                    st.error("⚠ 답안을 작성해주세요!")
                else:
                    st.success("✅ 제출이 완료되었습니다! 잘 작성하였습니다. 😊")
 
 
 
                            
elif page == "2차시: 최적 모델 선택하기":
    st.subheader("📌2차시: 최적 모델 선택하기")
    st.markdown("""
        Step1 부터 Step4 까지 순서대로 다양한 데이터를 분석하고 최적의 모델을 선택해봅시다.
        """)
    
    # 회귀 함수 정의
    def linear_regression(x, y):
        slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
        return slope * x + intercept

    def polynomial_regression(x, y, degree=2):
        coeffs = np.polyfit(x, y, degree)
        poly = np.poly1d(coeffs)
        return poly(x)

    def exponential_regression(x, y):
        x_scaled = x - np.min(x)     # x 값 스케일링 (최소값 기준으로 0부터 시작)

        # 지수 함수 정의
        def exp_func(x, a, b):
            return a * np.exp(b * x)

        # 초기값 조정 및 예외 처리
        try:
            # 초기값 (a: y의 초기값 추정, b: 증가율 추정)
            params, _ = curve_fit(exp_func, x_scaled, y, p0=(1e6, 0.001))  
            return exp_func(x_scaled, *params)
        except RuntimeError:
            st.error("지수 회귀 모델이 데이터에 적합하지 않습니다!")
            return np.zeros_like(x)  # 더미 데이터 반환

    def logarithmic_regression(x, y):
        def log_func(x, a, b):
            return a * np.log(b * x)

        # x 값이 0 이하인지 확인
        if np.any(x <= 0):
            st.error("로그 회귀 모델이 데이터에 적합하지 않습니다.")
            return np.zeros_like(x)  # 모든 값을 0으로 반환 (더미 데이터)

        try:
            # curve_fit 함수로 매개변수 추정
            params, _ = curve_fit(log_func, x, y, p0=(1, 1), maxfev=2000)
            return log_func(x, *params)
        except RuntimeError:
            st.error("로그 회귀 모델이 데이터에 적합하지 않습니다!")
            return np.zeros_like(x)  # 모든 값을 0으로 반환


    

    # Step1: GDP와 실업자 수
    st.markdown("<h3 style='font-size:20px; font-weight:bold;'>✅Step1) GDP와 청년 실업자 수</h3>", unsafe_allow_html=True)
    
    # 파일 경로 설정
    GDP_file_path = "./국내총생산.csv"  # 코드와 같은 디렉토리에 파일이 있는 경우
    unemployed_file_path = "./실업자수.csv"

    # 데이터 읽기
    GDP_data = pd.read_csv(GDP_file_path, encoding='cp949')  
    unemployed_data = pd.read_csv(unemployed_file_path, encoding='cp949')  

    # 데이터 병합 (월 기준으로 결합)
    merged_data = pd.merge(GDP_data, unemployed_data, on="연도")  # '연도' 열 기준으로 병합

    # 평균기온과 전력사용량을 각각 x, y로 설정
    x4 = merged_data["GDP"]
    y4 = merged_data["실업자수"]
        
    with st.expander("1-1) 우리나라 GDP와 실업자 수 사이의 관계를 살펴볼까요?"):
        
        st.markdown("""
        - 가로축은 1인당 국내총생산(GDP), 세로축은 실업자 수(명)입니다.
        - 25년 간의 GDP와 실업자 수의 데이터를 시각화한 산점도는 다음과 같습니다.
        """)

        # 기본 산점도 그리기
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.scatter(x4, y4, c='blue', alpha=0.7, label='Data')
        ax.set_xlabel("GDP")
        ax.set_ylabel("Number of unemployed")
        ax.legend()
        st.pyplot(fig)
    
    with st.expander("1-2) 위의 데이터에 다양한 회귀 모델을 적용해볼까요?"):
       
        # 회귀 모델 업데이트 함수
        def update_regression(model):
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.scatter(x4, y4, c='blue', alpha=0.7)
            ax.set_xlabel("GDP")
            ax.set_ylabel("Number of unemployed youth")

            if model == '선형 회귀':
                y_pred = linear_regression(x4, y4)
                ax.plot(x4, y_pred, color='red', label='Linear Fit')
            elif model == '다항 회귀':
                y_pred = polynomial_regression(x4, y4, degree=2)
                ax.plot(x4, y_pred, color='green', label='Polynomial Fit')
            elif model == '지수 회귀':
                y_pred = exponential_regression(x4, y4)
                ax.plot(x4, y_pred, color='purple', label='Exponential Fit')
            elif model == '로그 회귀':
                y_pred = logarithmic_regression(x4, y4)
                ax.plot(x4, y_pred, color='orange', label='Logarithmic Fit')

            ax.legend()
            st.pyplot(fig)
            
        # 회귀 모델 선택 및 시각화 - 드롭다운 메뉴 (Streamlit의 selectbox 사용)
        model = st.selectbox(
            "📍회귀 분석 모델을 직접 선택해보세요:",
            ["선택하세요", "선형 회귀", "다항 회귀", "지수 회귀", "로그 회귀"],
            key="regression_model_4"
        )

        # 선택한 회귀 모델로 그래프 업데이트
        if model != "선택하세요":
            update_regression(model)  
            
    with st.expander("1-3) 최적의 모델을 선택해볼까요?"):
        # 답변 입력란
        answer4 = st.text_area(
            "**✍해당 데이터를 분석하기 위한 최적의 모델을 선택하고, 그 이유를 작성하세요.**", 
            key="answer4",
            placeholder="예시: 최적의 모델은 ㅇㅇ 회귀입니다. 이유는 데이터가 ㅇㅇ 형태로 분포되어 있기 때문입니다."
            )
        
        # 제출 버튼 추가 
        button_style = """
        <style>
        div.stButton > button {
            background-color: white !important; /* 버튼 배경색: 흰색 강제 적용 */
            color: black !important; /* 텍스트 색: 검정 강제 적용 */
            border: 1px solid gray !important; /* 테두리 색: 회색 강제 적용 */
            border-radius: 5px !important; /* 버튼 모서리 둥글게 */
            padding: 5px 10px !important; /* 버튼 내부 여백 */
        }
        div.stButton > button:hover {
            background-color: lightgray !important; /* 마우스 올렸을 때: 연한 회색 */
            border: 1px solid darkgray !important; /* 테두리 색 진한 회색 */
        }
        </style>
        """
        st.markdown(button_style, unsafe_allow_html=True)

        # 제출 버튼과 메시지 레이아웃
        col1, col2 = st.columns([1, 9])  # 제출 버튼과 메시지 칸 비율 설정

        with col1:  # 첫 번째 칸: 제출 버튼
            if st.button("제출", key="submit_answer_4"):
                if not answer4.strip():  # 답안이 공란인지 확인
                    st.session_state["submit_message"] = "⚠ 답안을 작성해주세요!"  # 에러 메시지 저장
                    st.session_state["submit_message_style"] = "error"
                else:
                    st.session_state["submit_message"] = "😊 제출이 완료되었습니다! 잘 작성하였습니다."  # 성공 메시지 저장
                    st.session_state["submit_message_style"] = "success"

        with col2:  # 두 번째 칸: 제출 결과 메시지
            if "submit_message" in st.session_state:
                if st.session_state["submit_message_style"] == "error":
                    st.error(st.session_state["submit_message"])  # 에러 메시지 출력
                elif st.session_state["submit_message_style"] == "success":
                    st.success(st.session_state["submit_message"])  # 성공 메시지 출력





    # Step2: 월 평균 기온과 월 전력 사용량
    st.markdown("<h3 style='font-size:20px; font-weight:bold;'>✅Step2) 월 평균 기온과 월 전력 사용량</h3>", unsafe_allow_html=True)
    
    # 파일 경로 설정
    temp_file_path = "./월 평균 기온.csv"  # 코드와 같은 디렉토리에 파일이 있는 경우
    power_file_path = "./월 전력 사용량.csv"

    # 데이터 읽기
    temp_data = pd.read_csv(temp_file_path, encoding='cp949')  # 월 평균 기온 데이터
    power_data = pd.read_csv(power_file_path, encoding='cp949')  # 월 전력 사용량 데이터

    # 데이터 병합 (월 기준으로 결합)
    merged_data = pd.merge(temp_data, power_data, on="월")  # '월' 열 기준으로 병합

    # 평균기온과 전력사용량을 각각 x, y로 설정
    x2 = merged_data["평균기온"]
    y2 = merged_data["전력사용량"]
        
    with st.expander("2-1) 월 평균 기온과 월 전력 사용량 사이의 관계를 살펴볼까요?"):
        
        st.markdown("""
        - 가로축은 서울의 월 평균 기온(°C), 세로축은 월 평균 전력 사용량 (18시 기준)입니다.
        - 2008년 1월부터 2023년 12월까지의 매월 데이터를 시각화한 산점도는 다음과 같습니다.
        """)

        # 기본 산점도 그리기
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.scatter(x2, y2, c='blue', alpha=0.7, label='Data')
        ax.set_xlabel("Monthly Temperature (°C)")
        ax.set_ylabel("Monthly Electricity Consumption (kWh)")
        ax.legend()
        st.pyplot(fig)
    
    with st.expander("2-2) 위의 데이터에 다양한 회귀 모델을 적용해볼까요?"):
       
        # 회귀 모델 업데이트 함수
        def update_regression(model):
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.scatter(x2, y2, c='blue', alpha=0.7)
            ax.set_xlabel("Monthly Temperature (°C)")
            ax.set_ylabel("Monthly Electricity Consumption (kWh)")

            if model == '선형 회귀':
                y_pred = linear_regression(x2, y2)
                ax.plot(x2, y_pred, color='red', label='Linear Fit')
            elif model == '다항 회귀':
                y_pred = polynomial_regression(x2, y2, degree=2)
                ax.plot(x2, y_pred, color='green', label='Polynomial Fit')
            elif model == '지수 회귀':
                y_pred = exponential_regression(x2, y2)
                ax.plot(x2, y_pred, color='purple', label='Exponential Fit')
            elif model == '로그 회귀':
                y_pred = logarithmic_regression(x2, y2)
                ax.plot(x2, y_pred, color='orange', label='Logarithmic Fit')

            ax.legend()
            st.pyplot(fig)
            
        # 회귀 모델 선택 및 시각화 - 드롭다운 메뉴 (Streamlit의 selectbox 사용)
        model = st.selectbox(
            "📍회귀 분석 모델을 직접 선택해보세요:",
            ["선택하세요", "선형 회귀", "다항 회귀", "지수 회귀", "로그 회귀"],
            key="regression_model_2"
        )

        # 선택한 회귀 모델로 그래프 업데이트
        if model != "선택하세요":
            update_regression(model)  
            
    with st.expander("2-3) 최적의 모델을 선택해볼까요?"):
        # 답변 입력란
        inappropriate_model = st.text_area(
            "**✍데이터를 분석하기에 가장 부적절한 모델은 무엇이고 그 이유는 무엇인지 작성하세요.**", 
            key="inappropriate_model_2",
            placeholder="예시: 가장 부적절한 모델은 ㅇㅇ 회귀입니다. 이유는 ~~~ 때문입니다."
            )
        
        # 제출 버튼 스타일 적용
        button_style = """
        <style>
        div.stButton > button {
            background-color: white !important; /* 버튼 배경색: 흰색 */
            color: black !important; /* 텍스트 색: 검정 */
            border: 1px solid gray !important; /* 테두리 색: 회색 */
            border-radius: 5px !important; /* 모서리 둥글게 */
            padding: 5px 10px !important; /* 내부 여백 */
        }
        div.stButton > button:hover {
            background-color: lightgray !important; /* 마우스 올렸을 때: 연한 회색 */
            border: 1px solid darkgray !important; /* 테두리 색 진한 회색 */
        }
        </style>
        """
        st.markdown(button_style, unsafe_allow_html=True)

        # 제출 버튼과 메시지 레이아웃
        col1, col2 = st.columns([1, 9])  # 제출 버튼과 메시지 칸 비율 설정

        with col1:  # 첫 번째 칸: 제출 버튼
            if st.button("제출", key="submit_inappropriate_model_2"):
                if not inappropriate_model.strip():  # 답안이 공란인지 확인
                    st.session_state["submit_message"] = "⚠ 답안을 작성해주세요!"  # 에러 메시지
                    st.session_state["submit_message_style"] = "error"
                else:
                    st.session_state["submit_message"] = "😊 제출이 완료되었습니다! 잘 작성하였습니다."  # 성공 메시지
                    st.session_state["submit_message_style"] = "success"

        with col2:  # 두 번째 칸: 제출 결과 메시지
            if "submit_message" in st.session_state:
                if st.session_state["submit_message_style"] == "error":
                    st.error(st.session_state["submit_message"])
                elif st.session_state["submit_message_style"] == "success":
                    st.success(st.session_state["submit_message"])

        # 힌트 버튼과 메시지 레이아웃
        col3, col4 = st.columns([1, 9])  # 힌트 버튼과 메시지 칸 비율 설정

        with col3:  # 첫 번째 칸: 힌트 버튼
            if st.button("힌트", key="hint_inappropriate_model_2"):
                st.session_state["show_hint"] = True  # 세션 상태를 활용해 힌트 표시 여부 제어

        with col4:  # 두 번째 칸: 힌트 메시지
            if st.session_state.get("show_hint", False):  # 힌트 버튼 클릭 시 메시지 표시
                st.markdown(
                    """
                    <div style="background-color: #ffe6e6; padding: 10px; border-radius: 5px;">
                        <strong style="color: red;">⚠힌트:</strong>
                        <span style="color: red;">x 변량에 0 또는 음수가 있나요? 로그 함수의 정의역을 생각해봅시다.</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
    





    # Step3: 우리나라 대학교 진학률 변화
    st.markdown("<h3 style='font-size:20px; font-weight:bold;'>✅Step3) 우리나라 연도별 대학교 진학률</h3>", unsafe_allow_html=True)

    # 파일 경로 설정
    univ_path = "./대학교 취학률.csv"  # 코드와 같은 디렉토리에 파일이 있는 경우

    # 데이터 읽기
    data = pd.read_csv(univ_path, encoding='cp949')  # 연도별 인구 수 데이터

    # 데이터 준비 x,y 로 설정
    x3 = np.array(data["연도"]) 
    y3 = np.array(data["취학률"]) 

    with st.expander("3-1) 대학교 진학률 변화를 살펴볼까요?"):
        
        st.markdown("""
        - 가로축은 연도(년), 세로축은 대학교 진학률(%)입니다.
        - 1925년부터 2010년까지 5년 주기의 데이터와 2015년부터 현재까지의 1년 주기 데이터를 시각화한 산점도는 다음과 같습니다.
        """)

        # 기본 산점도 그리기
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.scatter(x3, y3, c='blue', alpha=0.7, label='Data')
        ax.set_xlabel("Year")
        ax.set_ylabel("University Enrollment Rates")
        ax.legend()
        ax.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))  # y축 포맷 설정: StrMethodFormatter 사용

        st.pyplot(fig)

        
    with st.expander("3-2) 위의 데이터에 다양한 회귀 모델을 적용해볼까요?"):
       
        # 회귀 모델 업데이트 함수
        def update_regression(model):
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.scatter(x3, y3, c='blue', alpha=0.7)
            ax.set_xlabel("Year")
            ax.set_ylabel("University Enrollment Rates")
            ax.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))  # y축 포맷 설정: StrMethodFormatter 사용

            if model == '선형 회귀':
                y_pred = linear_regression(x3, y3)
                ax.plot(x3, y_pred, color='red', label='Linear Fit')
            elif model == '다항 회귀':
                y_pred = polynomial_regression(x3, y3, degree=2)
                ax.plot(x3, y_pred, color='green', label='Polynomial Fit')
            elif model == '지수 회귀':
                y_pred = exponential_regression(x3, y3)
                ax.plot(x3, y_pred, color='purple', label='Exponential Fit')
            elif model == '로그 회귀':
                y_pred = logarithmic_regression(x3, y3)
                ax.plot(x3, y_pred, color='orange', label='Logarithmic Fit')

            ax.legend()
            st.pyplot(fig)
            
        # 회귀 모델 선택 및 시각화 - 드롭다운 메뉴 (Streamlit의 selectbox 사용)
        model = st.selectbox(
            "📍회귀 분석 모델을 직접 선택해보세요:",
            ["선택하세요", "선형 회귀", "다항 회귀", "지수 회귀", "로그 회귀"],
            key="regression_model_3"
        )

        # 선택한 회귀 모델로 그래프 업데이트
        if model != "선택하세요":
            update_regression(model)  

            
    with st.expander("3-3) 최적의 모델을 선택해볼까요?"):
        # 답변 입력란
        answer3 = st.text_area(
            "**✍해당 데이터를 분석하기 위한 최적의 모델을 선택하고, 데이터를 분석하는 글을 작성해보세요.**", 
            key="answer3",
            placeholder="예시: 최적의 모델은 ㅇㅇ 회귀입니다. 연도별 데이터 진학률은 ~~하게 변화하고 있습니다."
            )
        
        # 제출 버튼 추가 
        button_style = """
        <style>
        div.stButton > button {
            background-color: white !important; /* 버튼 배경색: 흰색 강제 적용 */
            color: black !important; /* 텍스트 색: 검정 강제 적용 */
            border: 1px solid gray !important; /* 테두리 색: 회색 강제 적용 */
            border-radius: 5px !important; /* 버튼 모서리 둥글게 */
            padding: 5px 10px !important; /* 버튼 내부 여백 */
        }
        div.stButton > button:hover {
            background-color: lightgray !important; /* 마우스 올렸을 때: 연한 회색 */
            border: 1px solid darkgray !important; /* 테두리 색 진한 회색 */
        }
        </style>
        """
        st.markdown(button_style, unsafe_allow_html=True)

        # 제출 버튼과 메시지 레이아웃
        col1, col2 = st.columns([1, 9])  # 제출 버튼과 메시지 칸 비율 설정

        with col1:  # 첫 번째 칸: 제출 버튼
            if st.button("제출", key="submit_answer_3"):
                if not answer3.strip():  # 답안이 공란인지 확인
                    st.session_state["submit_message"] = "⚠ 답안을 작성해주세요!"  # 에러 메시지 저장
                    st.session_state["submit_message_style"] = "error"
                else:
                    st.session_state["submit_message"] = "😊 제출이 완료되었습니다! 잘 작성하였습니다."  # 성공 메시지 저장
                    st.session_state["submit_message_style"] = "success"

        with col2:  # 두 번째 칸: 제출 결과 메시지
            if "submit_message" in st.session_state:
                if st.session_state["submit_message_style"] == "error":
                    st.error(st.session_state["submit_message"])  # 에러 메시지 출력
                elif st.session_state["submit_message_style"] == "success":
                    st.success(st.session_state["submit_message"])  # 성공 메시지 출력
        
    

    
    
    
    # Step4: 연도별 인구 수
    st.markdown("<h3 style='font-size:20px; font-weight:bold;'>✅Step4) 연도별 인구 수</h3>", unsafe_allow_html=True)

    # 파일 경로 설정
    population_path = "./연도별 인구 수.csv"  # 코드와 같은 디렉토리에 파일이 있는 경우

    # 데이터 읽기
    data = pd.read_csv(population_path, encoding='cp949')  # 연도별 인구 수 데이터

    # 데이터 준비 x,y 로 설정
    x1 = np.array(data["연도"])  # 독립 변수 (연도)
    y1 = np.array(data["인구"])  # 종속 변수 (인구수)


    with st.expander("4-1) 인구 변화율을 살펴볼까요?"):
        
        st.markdown("""
        - 가로축은 연도(년), 세로축은 대한민국 총 인구 수(명)입니다.
        - 1920년부터 2010년까지 5년 주기의 데이터와 2015년부터 현재까지의 1년 주기 데이터를 시각화한 산점도는 다음과 같습니다.
        """)

        # 기본 산점도 그리기
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.scatter(x1, y1, c='blue', alpha=0.7, label='Data')
        ax.set_xlabel("Year")
        ax.set_ylabel("Population")
        ax.legend()
        ax.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))  # y축 포맷 설정: StrMethodFormatter 사용

        st.pyplot(fig)

        
    with st.expander("4-2) 위의 데이터에 다양한 회귀 모델을 적용해볼까요?"):
       
        # 회귀 모델 업데이트 함수
        def update_regression(model):
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.scatter(x1, y1, c='blue', alpha=0.7)
            ax.set_xlabel("Year")
            ax.set_ylabel("Population")
            ax.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))  # y축 포맷 설정: StrMethodFormatter 사용

            if model == '선형 회귀':
                y_pred = linear_regression(x1, y1)
                ax.plot(x1, y_pred, color='red', label='Linear Fit')
            elif model == '다항 회귀':
                y_pred = polynomial_regression(x1, y1, degree=2)
                ax.plot(x1, y_pred, color='green', label='Polynomial Fit')
            elif model == '지수 회귀':
                y_pred = exponential_regression(x1, y1)
                ax.plot(x1, y_pred, color='purple', label='Exponential Fit')
            elif model == '로그 회귀':
                y_pred = logarithmic_regression(x1, y1)
                ax.plot(x1, y_pred, color='orange', label='Logarithmic Fit')

            ax.legend()
            st.pyplot(fig)
            
        # 회귀 모델 선택 및 시각화 - 드롭다운 메뉴 (Streamlit의 selectbox 사용)
        model = st.selectbox(
            "📍회귀 분석 모델을 직접 선택해보세요:",
            ["선택하세요", "선형 회귀", "다항 회귀", "지수 회귀", "로그 회귀"],
            key="regression_model_1"
        )

        # 선택한 회귀 모델로 그래프 업데이트
        if model != "선택하세요":
            update_regression(model)  


    with st.expander("4-3) 최적의 모델을 선택해볼까요?"):

        # 답변 입력란
        optimal_model = st.text_area(
            "**✍해당 데이터를 분석하기 위한 최적의 모델을 선택하고, 2080년 인구 수가 어떻게 될 지 예측해봅시다.**", 
            key="optimal_model_1",
            placeholder="예시: 최적의 모델은 ㅇㅇ 회귀이며 데이터는 ~~하게 변화하고 있으므로 2080년 인구 수는...."
            )
        
        # 제출 버튼 추가 
        button_style = """
        <style>
        div.stButton > button {
            background-color: white !important; /* 버튼 배경색: 흰색 강제 적용 */
            color: black !important; /* 텍스트 색: 검정 강제 적용 */
            border: 1px solid gray !important; /* 테두리 색: 회색 강제 적용 */
            border-radius: 5px !important; /* 버튼 모서리 둥글게 */
            padding: 5px 10px !important; /* 버튼 내부 여백 */
        }
        div.stButton > button:hover {
            background-color: lightgray !important; /* 마우스 올렸을 때: 연한 회색 */
            border: 1px solid darkgray !important; /* 테두리 색 진한 회색 */
        }
        </style>
        """
        st.markdown(button_style, unsafe_allow_html=True)

        # 제출 버튼과 메시지 레이아웃
        col1, col2 = st.columns([1, 9])  # 제출 버튼과 메시지 칸 비율 설정

        with col1:  # 첫 번째 칸: 제출 버튼
            if st.button("제출", key="submit_optimal_model_1"):
                if not optimal_model.strip():  # 답안이 공란인지 확인
                    st.session_state["submit_message"] = "⚠ 답안을 작성해주세요!"  # 에러 메시지 저장
                    st.session_state["submit_message_style"] = "error"
                else:
                    st.session_state["submit_message"] = "😊 제출이 완료되었습니다! 잘 작성하였습니다."  # 성공 메시지 저장
                    st.session_state["submit_message_style"] = "success"

        with col2:  # 두 번째 칸: 제출 결과 메시지
            if "submit_message" in st.session_state:
                if st.session_state["submit_message_style"] == "error":
                    st.error(st.session_state["submit_message"])  # 에러 메시지 출력
                elif st.session_state["submit_message_style"] == "success":
                    st.success(st.session_state["submit_message"])  # 성공 메시지 출력



    
elif page == "3차시: 주도적으로 데이터 분석하기":
    
    st.subheader("📌3차시: 주도적으로 데이터 분석하기")
    st.info("😊 지금부터 여러분은 데이터 전문가입니다. 모둠별로 토의하여 KOSIS에서 데이터를 직접 선정하고, 해당 데이터를 시각화하여 적절한 회귀분석을 선택하여 분석해봅시다. (Step1~Step6)")
            
    # 데이터 전처리 안내
    st.markdown("<h3 style='font-size:20px; font-weight:bold;'>Step1) 📂 데이터 전처리</h3>", unsafe_allow_html=True)
    with st.expander("선정한 데이터를 다음과 조건에 맞추어 정리하세요.", expanded = True):
        st.write("""
        - 모든 데이터는 숫자 데이터여야 합니다. (예: 연도, 인구 수, 참여율 등)
        - 불필요한 열 또는 행은 모두 삭제합니다.
        - x, y축에 들어갈 2개의 데이터를 2개의 열로 정리합니다.
        - 첫번째 행은 데이터의 정보(x축 이름, y축 이름)가 들어갑니다.
        - 데이터는 CSV 형식의 파일이어야 합니다. (예: 연도별 인구수.csv)
        """)                
    
    # 데이터 업로드
    st.markdown("<h3 style='font-size:20px; font-weight:bold;'>Step2) 📤데이터 업로드</h3>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("CSV 파일 형식으로 업로드하세요:", type=["csv"])
    
    if uploaded_file is not None:
        # 데이터 읽기
        try:
            # ANSI(CP1252/CP949) 인코딩 시도
            data = pd.read_csv(uploaded_file, encoding="cp949")
        except UnicodeDecodeError:
            try:
                # UTF-8로 재시도
                data = pd.read_csv(uploaded_file, encoding="utf-8")
            except UnicodeDecodeError:
                st.error("⚠️ 지원되지 않는 파일 인코딩 형식입니다. ANSI, UTF-8, 또는 CP949 형식의 파일을 업로드해주세요.")
                data = None

        if data is not None:
            
            # 데이터를 표로 출력 
            st.markdown("<h3 style='font-size:20px; font-weight:bold;'>Step3) 📑데이터 전체 보기</h3>", unsafe_allow_html=True)
            st.dataframe(data, height=200, use_container_width=True)  # 전체 데이터를 스크롤 가능한 표로 출력
            
            st.markdown("<h3 style='font-size:20px; font-weight:bold;'>Step4) 📈산점도 그리기</h3>", unsafe_allow_html=True)

            # X, Y 변수 선택 탭
            col1, col2 = st.columns(2)
            with col1:
                x_col = st.selectbox(
                    "📊 X축 데이터를 선택하세요.:", 
                    ["선택하세요"] + list(data.columns),  # "선택하세요"를 옵션에 추가
                    index=0  # 기본값으로 "선택하세요" 설정
                )
            with col2:
                y_col = st.selectbox(
                    "📊 Y축 데이터를 선택하세요.:", 
                    ["선택하세요"] + list(data.columns),  # "선택하세요"를 옵션에 추가
                    index=0  # 기본값으로 "선택하세요" 설정
                )

            # 학생이 선택해야만 다음 단계를 진행할 수 있도록 조건 설정
            if x_col != "선택하세요" and y_col != "선택하세요":
                
                # X, Y 데이터를 숫자로 변환 (필요할 경우 소수점 유지)
                x = pd.to_numeric(data[x_col], errors='coerce')
                y = pd.to_numeric(data[y_col], errors='coerce')

                # NaN 값 제거
                valid_mask = ~np.isnan(x) & ~np.isnan(y)
                x = x[valid_mask]
                y = y[valid_mask]

                # 산점도 그리기
                fig, ax = plt.subplots(figsize=(10, 6))
                ax.scatter(x, y, c='blue', alpha=0.7, label='Data')
                ax.legend()
                st.pyplot(fig)

                # 회귀 모델 적용
                st.markdown("<h3 style='font-size:20px; font-weight:bold;'>Step5) 📐 회귀 모델 적용</h3>", unsafe_allow_html=True)
                model = st.selectbox(
                    "📍 회귀 분석 모델을 선택하세요:",
                    ["선택하세요", "선형 회귀", "다항 회귀", "지수 회귀", "로그 회귀"],
                    key="regression_model_upload"
                )
                
                # 로그 회귀 함수 정의
                def logarithmic_regression(x, y):
                    def log_func(x, a, b):
                        return a * np.log(b * x)

                    # x 값이 0 이하인지 확인
                    if np.any(x <= 0):
                        st.error("로그 회귀 모델이 데이터에 적합하지 않습니다. X 값은 0보다 커야 합니다.")
                        return np.zeros_like(x)  # 모든 값을 0으로 반환 (더미 데이터)

                    try:
                        # curve_fit 함수로 매개변수 추정
                        params, _ = curve_fit(log_func, x, y, p0=(1, 1), maxfev=2000)
                        return log_func(x, *params), params  # 예측 값과 매개변수 반환
                    except RuntimeError:
                        st.error("로그 회귀 모델이 데이터에 적합하지 않습니다! 최적화를 실패했습니다.")
                        return np.zeros_like(x), None  # 모든 값을 0으로 반환

                def apply_regression(model, x, y):
                    fig, ax = plt.subplots(figsize=(10, 6))
                    ax.scatter(x, y, c='blue', alpha=0.7, label='Data')

                    if model == '선형 회귀':
                        slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
                        y_pred = slope * x + intercept
                        ax.plot(x, y_pred, color='red', label='Linear Fit')
                    elif model == '다항 회귀':
                        coeffs = np.polyfit(x, y, 2)
                        poly = np.poly1d(coeffs)
                        y_pred = poly(x)
                        ax.plot(x, y_pred, color='green', label='Polynomial Fit')
                    elif model == '지수 회귀':
                        x_scaled = x - np.min(x)  # x 값 스케일링
                        def exp_func(x, a, b): return a * np.exp(b * x)
                        params, _ = curve_fit(exp_func, x_scaled, y, p0=(1, 0.1))
                        y_pred = exp_func(x_scaled, *params)
                        ax.plot(x, y_pred, color='purple', label='Exponential Fit')
                    elif model == '로그 회귀':
                        # 로그 회귀 함수 호출
                        y_pred, params = logarithmic_regression(x, y)

                        if params is not None:  # 최적화 성공 시만 그래프 그리기
                            ax.plot(x, y_pred, color='orange', label='Logarithmic Fit')

                    ax.legend()
                    st.pyplot(fig)

                # 선택된 모델로 회귀 분석 적용
                if model != "선택하세요":
                    apply_regression(model, x, y)
                    
                    # Step6: 데이터 분석하기 추가
                    st.markdown("<h3 style='font-size:20px; font-weight:bold;'>Step6) 📋 데이터 분석하기</h3>", unsafe_allow_html=True)

                    # 데이터 분석 안내 메시지
                    st.info("🔍 적절한 회귀 모델을 선택한 이유를 설명하고, 데이터를 분석한 내용을 작성하세요. 모둠원의 의견도 함께 정리하세요.")

                    # 답안 작성 텍스트 박스
                    analysis_text = st.text_area(
                        "✏️ 분석 내용을 작성하세요:",
                        placeholder="예시: 선택한 회귀 모델은 데이터를 가장 잘 설명한다고 판단한 이유는...\n모둠원 의견: ..."
                    )

                    # 제출 버튼과 메시지를 같은 줄에 배치 (비율: 1:9)
                    col1, col2 = st.columns([1, 9])

                    with col1:
                        # 제출 버튼
                        if st.button("제출"):
                            if analysis_text.strip():  # 작성 내용이 있는 경우
                                with col2:
                                    st.success("✅ 분석 내용이 성공적으로 제출되었습니다. 좋은 분석 기대할게요!")
                            else:  # 작성 내용이 비어 있는 경우
                                with col2:
                                    st.error("⚠️ 분석 내용을 작성한 후 제출해주세요.")
                    

                
            else:
                st.warning("⚠️ X축과 Y축 데이터를 모두 선택하세요.")



        