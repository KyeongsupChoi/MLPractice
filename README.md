# ML/AI Portfolio

A Collection of Data Science Projects created for academic, self learning, and hobby purposes in the form of Jupyter notebooks, also available on Kaggle.

[![](https://img.shields.io/badge/ML/AI_Algorithms-20BEFF?style=for-the-badge&logo=Kaggle&logoColor=white)](https://www.kaggle.com/kyeongsupchoi/code?scroll=true)

## Contents

- ### [Supervised Learning]

    _Libraries: Scikit-learn, Pandas, Matplotlib, Numpy_ 

	- [Decision Tree Regressor](https://www.kaggle.com/code/kyeongsupchoi/decisiontreeregressor-randomforestregressor): Predicting insurance charges based on age, sex, bmi, smoking data utilizing a Decision Tree Regression model. 
	
    - [Random Forest Regressor](https://www.kaggle.com/code/kyeongsupchoi/decisiontreeregressor-randomforestregressor): Testing comparative performance of a Random Forest Regressor model with previous example based on max leaf nodes and mean absolute error
	
    - [Linear Regression](https://www.kaggle.com/code/kyeongsupchoi/linearregression): Prediction of home prices based on square foot area, number of bedrooms, renovated year utilizing a linear regression model. 

	- [Titanic Competition](https://www.kaggle.com/code/kyeongsupchoi/titanic): Kaggle Titanic competition notebook utilizing a XGBoost Classifier and an Ordinal Encoding data processing technique

- ### [Unsupervised Learning]

	_Libraries: Scikit-learn, Pandas, Matplotlib, Numpy_ 

	- [Local Outlier Factor](https://www.kaggle.com/code/kyeongsupchoi/local-outlier-factor): Utilizing the Local Outlier Factor algorithm to identify anomalies in the insurance dataset. 

	- [Isolation Forest](https://www.kaggle.com/code/kyeongsupchoi/time-series-anomaly): Discovering anomalies in the NYC Taxi charges dataset utilizing the Isolation Forest algorithm.

	- [One Class Support Vector Machine](https://www.kaggle.com/code/kyeongsupchoi/one-class-support-vector-machine): Gauging performance of a One Class Support Vector Machine to detect outliers on generated, experimental data. 

- ### [Deep Learning]

	_Libraries: Tensorflow, Numpy_ 

	- [Image Classification](https://www.kaggle.com/code/kyeongsupchoi/tensorflowbasicimageclassification): This project creates a deep learning model using TensorFlow and tf.keras on the Fashion MNIST dataset. The trained model achieves a certain level of accuracy on the test set, and predictions are made on individual images from the dataset. The project also includes visualizations of the predicted labels and their associated probabilities.

	- [Text Classification](https://www.kaggle.com/code/kyeongsupchoi/textclassificationtensorflowhub): This project trains a text classification model using TensorFlow and TensorFlow Hub. The IMDb Reviews dataset is used, and a pre-trained embedding layer is employed to process the text data. The model is trained and evaluated on the dataset, and the performance metrics are reported.

- ### [한국어]

	_라이브러리: 싸이키트런, 판다스, 넘파이, 매트플롯_ 

 	- [1 종류 지원 백터 머신](https://www.kaggle.com/code/kyeongsupchoi/model2-1): 이 프로젝트는 1 종류 지원 백터 머신을 사용하여 생성된 실험 데이터에서 이상치를 감지하는 작업을 수행합니다. 데이터프레임을 로드한 후, 분류 모델을 초기화하고 훈련 데이터로 모델을 훈련합니다. 이후, 테스트 데이터에 대한 예측을 수행하고 예측 결과를 초기 데이터프레임에 연결합니다. 이상치를 시각화하여 확인하고, 데이터프레임에 시간과 요일 열을 추가합니다

	- [결정트리회귀](https://www.kaggle.com/code/kyeongsupchoi/model): 이 프로젝트는 보험 데이터를 분석하여 데이터프레임으로 변환합니다. 데이터프레임의 기본적인 통계 요약과 정보를 출력합니다. 이후, 결정트리와 램덤포레스트를 사용하여 회귀 모델을 학습하고 검증 데이터에 대한 예측을 생성합니다. 예측 결과와 실제값 사이의 평균 절대 오차(MAE)를 계산하여 모델의 성능을 평가합니다. 최대 잎 노드 수를 다양하게 변경하면서 MAE 값을 비교합니다.

	- [시계열 이상감지](https://www.kaggle.com/code/kyeongsupchoi/model1): 이 프로젝트는 NYC 택시 데이터셋을 활용하여 이상치를 감지하는 작업을 수행합니다. 먼저, 데이터셋을 데이터프레임으로 로드하고 기본적인 탐색적 데이터 분석을 수행합니다. 다음으로, 격리 포리스트를 사용하여 이상치를 감지하는 분류자 객체를 초기화하고 훈련 데이터에 적합시킵니다. 그 후, 테스트 데이터에 대한 예측 결과를 생성하고 초기 데이터프레임에 연결합니다. 마지막으로, 이상치를 시각화하여 확인하고 데이터프레임에 시간과 요일 열을 추가합니다.

    - [로컬 이상값 요인](https://github.com/): 이 프로젝트는 보험 데이터를 로드하고, 데이터프레임으로 변환합니다. 이후, 특정 피처들을 선택하고, 로컬 이상값 요인를 사용하여 이상치를 감지하는 모델을 학습시킵니다. 학습된 모델을 사용하여 이상치를 예측하고 예측 결과를 데이터프레임에 추가합니다. 마지막으로, 이상치를 검증하기 위해 이상치로 분류된 데이터를 출력합니다. 
