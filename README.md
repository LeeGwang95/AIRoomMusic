# AIRoomMusic
-  4학년 2학기  캡스톤2  프로젝트
-  교내 공과대학 캡스톤 경진대회 금상
-  교내 컴퓨터공학과 캡스톤 경진대회 최우수

Youtube: https://www.youtube.com/watch?v=EO6Gzx4Hw08

<img width="789" alt="스크린샷 2020-03-23 오후 5 36 16" src="https://user-images.githubusercontent.com/62536330/77297604-e1a69200-6d2c-11ea-9a65-b4f83f339dd6.png">
# 환경
 FLASK web 환경의 Python기반 tensorflow,Music21,Keras,numpy 라이브러리 사용
# WHY
 성장하는 음악산업과 4차산업혁명에 있어서 해외에서는 AI작곡 플랫폼이 등장하기 시작 하지만 한국에는 아직 시도가 없어 최대한 쉬운 방식으로 AI작곡 플랫폼 제안을 통하여  영화, 게임, 1인 미디어 산업에 있어서 필요한 음악을 제공.
# How
<img width="414" alt="스크린샷 2020-03-23 오후 5 40 16" src="https://user-images.githubusercontent.com/62536330/77298387-339be780-6d2e-11ea-8be5-7ae1c6564359.png">
1) 수집 : Kaggle, git 등 다양한 매체에서  MIDI파일 저장(classic이 많았음 저작권)

2) 저장 : 프로젝트 파일안에 midi라는 파일을 두고 이를 읽어와서 파싱하는  과정을 거침 그과정속에서 노트와 코드로서 저장을함.
         데이터를 이는 뮤직21라이브러리의 예제들을 이용 

3) 분석 :  LSTM 에 드랍아웃(오버피팅방법),덴스(뉴런과 결합하여 입출력 담당),액티베이션(윤활제)와 같은 좀더 유연하게 만드는 레이어들을 이용하여 LSTM을 구축 케라스            를 선택했고 그 이유는 초보자 수준에서도 단순히 레이어를 쌓는 방식을 이용. (인풋,가중치,연산,활성화함수)

4) 시각화 : HTML환경에서 부투스트랩을 이용하여 빠르고 간결한 템플릿을 구성 + Youtube APi 사용 Get post메소드 이용 인자값을 던져주는 방식 


1. Initial Screen
<img width="1199" alt="스크린샷 2020-03-23 오후 5 42 00" src="https://user-images.githubusercontent.com/62536330/77298395-37c80500-6d2e-11ea-9037-e8fa232f6c94.png">
2. Description
<img width="1217" alt="스크린샷 2020-03-23 오후 5 42 09" src="https://user-images.githubusercontent.com/62536330/77298400-3991c880-6d2e-11ea-94f1-49b18e585c90.png">
3. Music Genre & Contact
<img width="1223" alt="스크린샷 2020-03-23 오후 5 42 16" src="https://user-images.githubusercontent.com/62536330/77298403-3a2a5f00-6d2e-11ea-8446-2c259eef966e.png">
4. Image
<img width="629" alt="스크린샷 2020-03-23 오후 5 35 01" src="https://user-images.githubusercontent.com/62536330/77298407-3ac2f580-6d2e-11ea-8d2f-36eaac5d0f26.png">


