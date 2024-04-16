# ML/AI Portfolio

A Collection of Data Science Projects in the form of Jupyter notebooks, also available on Kaggle.

[![](https://img.shields.io/badge/ML/AI_Algorithms-20BEFF?style=for-the-badge&logo=Kaggle&logoColor=white)](https://www.kaggle.com/kyeongsupchoi/code?scroll=true)

## Contents

- ### [Supervised Learning]

    _Libraries: Scikit-learn, Pandas, Matplotlib, Numpy_ 

	- [Titanic Competition](https://www.kaggle.com/code/kyeongsupchoi/titanic): Kaggle Titanic competition notebook utilizing a XGBoost Classifier and an Ordinal Encoding data processing technique

- ### [Unsupervised Learning]

	_Libraries: Scikit-learn, Pandas, Matplotlib, Numpy_ 

	- [Local Outlier Factor](https://www.kaggle.com/code/kyeongsupchoi/local-outlier-factor): Utilizing the Local Outlier Factor algorithm to identify anomalies in the insurance dataset. 

	- [One Class Support Vector Machine](https://www.kaggle.com/code/kyeongsupchoi/one-class-support-vector-machine): Gauging performance of a One Class Support Vector Machine to detect outliers on generated, experimental data. 

- ### [Deep Learning]

	_Libraries: Tensorflow, Numpy_ 

	- [Text Classification](https://www.kaggle.com/code/kyeongsupchoi/textclassificationtensorflowhub): This project trains a text classification model using TensorFlow and TensorFlow Hub. The IMDb Reviews dataset is used, and a pre-trained embedding layer is employed to process the text data. The model is trained and evaluated on the dataset, and the performance metrics are reported.

- ### [한국어]

	_라이브러리: 싸이키트런, 판다스, 넘파이, 매트플롯_ 

 	- [1 종류 지원 백터 머신](https://www.kaggle.com/code/kyeongsupchoi/model2-1): 이 프로젝트는 1 종류 지원 백터 머신을 사용하여 생성된 실험 데이터에서 이상치를 감지하는 작업을 수행합니다. 데이터프레임을 로드한 후, 분류 모델을 초기화하고 훈련 데이터로 모델을 훈련합니다. 이후, 테스트 데이터에 대한 예측을 수행하고 예측 결과를 초기 데이터프레임에 연결합니다. 이상치를 시각화하여 확인하고, 데이터프레임에 시간과 요일 열을 추가합니다

    - [로컬 이상값 요인](https://www.kaggle.com/code/kyeongsupchoi/model3): 이 프로젝트는 보험 데이터를 로드하고, 데이터프레임으로 변환합니다. 이후, 특정 피처들을 선택하고, 로컬 이상값 요인를 사용하여 이상치를 감지하는 모델을 학습시킵니다. 학습된 모델을 사용하여 이상치를 예측하고 예측 결과를 데이터프레임에 추가합니다. 마지막으로, 이상치를 검증하기 위해 이상치로 분류된 데이터를 출력합니다. 
