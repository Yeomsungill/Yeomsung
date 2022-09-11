## flask 로드
from flask import Flask,render_template,request,redirect
import pandas as pd

# Class생성
app = Flask(__name__)

@app.route("/")
def index():
    # index.html 그래프를 그리기 위해서 필요한 변수 값
    # x_pos, y_pos 
    # 코로나 데이터를 로드
    # 일일확진자 파생변수
    # x축에는 등록일시
    # y축에는 일일확진자
    co = pd.read_csv("../csv/corona.csv")
    co.columns = ["인덱스","등록일시","사망자","확진자","게시글번호","기준일","기준시간","수정일시","누적의심자","누적확진률"]
    co.sort_values("등록일시", inplace = True)
    co["일일확진자"] = co["확진자"] - co["확진자"].shift().fillna(0)
    data = co.tail(50)
    
    _d_data = data["일일확진자"].tolist()
    _da_list = data["등록일시"].tolist()
    data1 = data.to_dict()
    cnt = len(data1)
    columns = data.columns
    c_cnt = len(columns)
    return render_template("index.html" , _x = _da_list, _y = _d_data, cnt = cnt, data1=data1,c_cnt=c_cnt,columns=columns)


@app.route("/index2")
def index2():
 
    co = pd.read_csv("../csv/corona.csv")
    co.columns = ["인덱스","등록일시","사망자","확진자","게시글번호","기준일","기준시간","수정일시","누적의심자","누적확진률"]
    co.sort_values("등록일시", inplace = True)
    
    co["일일사망자"] = co["사망자"].diff().fillna(0)
    data = co.tail(50)
    
    _dd_data = data["일일사망자"].tolist()
    _da_list = data["등록일시"].tolist()
    data1 = data.to_dict()
    cnt = len(data1)
    columns = data.columns
    c_cnt = len(columns)
    return render_template("index copy.html" , _x = _da_list, _y = _dd_data, cnt = cnt, data1=data1,c_cnt=c_cnt,columns=columns)




app.run(port=8080)