## 의사결정트리를 이용한 유방함 판독 구현


# 필요 패키지 선언
from sklearn.tree import DecisionTreeClassifier # 결정트리를 위한 라이브러리 선언
from sklearn.tree import export_graphviz # 결정 트리를 그림으로 출력하기 위한 라이브러리 선언
from sklearn.datasets import load_breast_cancer # 유방암 데이터를 사용하기 위한 라이브러리 선언
from sklearn.model_selection import train_test_split # 데이터 셋을 나누기 위한 라이브러리 선언
import pydot # 트리를 그림으로 저장하기 위한 차이브러리 선언


# 데이터 선언
cancer = load_breast_cancer()


# 훈련, 테스트 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, stratify=cancer.target, random_state=42)


# 의사결정트리 생성 : 가지치기를 안한 결정트리모델 사용
dTreeAll = DecisionTreeClassifier(random_state=0) # 난수시드 설정

# 의사결정트리 적합 : 가지치기를 안한 결정트리모델 사용
dTreeAll.fit(X_train, y_train)

# 의사결정트리 적합 점수 출력 : 가지치기를 안한 결정트리모델 사용
print("Trian set score1 : {:.2f}".format(dTreeAll.score(X_train, y_train))) # 훈련 데이터에 대한 적합 점수 출력
print("Trian set score1 : {:.2f}".format(dTreeAll.score(X_test, y_test))) # 테스트 데이터에 대한 적합 점수 출력 


# 의사결정트리 생성 : 가지치기를 한 결정트리모델 사용
dTreeLimit = DecisionTreeClassifier(max_depth=3, random_state=0) # 깊이를 제한하여 가지 치기 실행


# 의사결정트리 적합 : 가지치기를 한 결정트리모델 사용
dTreeLimit.fit(X_train, y_train)


# 점수 출력 : 가지치기를 한 결정트리모델 사용
print("Trian set score2 : {:.2f}".format(dTreeLimit.score(X_train, y_train)))
print("Trian set score2 : {:.2f}".format(dTreeLimit.score(X_test, y_test)))


# 트리 생성하여 문서로 저장 : 가지치기를 한 결정트리모델 사용
export_graphviz(dTreeLimit, # 결정트리를 그릴 적합한 의사결정트리 모델
                out_file="3.Dicision_Tree.dot", # 저장할 문서 파일의 이름
                class_names=["malignant","benign"], # 분류할 2가지 그룹에 대한 각각의 이름
                feature_names=cancer.feature_names, # 변수들의 이름 설정
                impurity=False, filled=True)


# 트리 정보 인코딩
(graph,) = pydot.graph_from_dot_file('3.Dicision_Tree.dot', encoding='utf8')


# Dot 파일을 Png 이미지로 저장
graph.write_png('3.Dicision_Tree.png')