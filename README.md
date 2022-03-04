# Python API 基本研究
web services 用flask 
#### 1.先安裝虛擬環境
> pip install virtualenv
#### 2.建立虛擬環境方法
1. cmd移動到欲建立虛擬環境目錄
2. 建立虛擬環境
```
python -m venv venv
```
#### 3.clone lab code
> 安裝用到的套件
```
git clone https://gitlab.com/maxaiot/tools/apitoolforpython.git
cd apitoolforpython
pip install -r requirements.txt
```
#### 4.執行Web Services
python3 APIServer.py

#### 5.執行傳送API
開一個新的終端機
```
python SendAPI
```
#### 後記檢查函式庫相依性
```
pip list 
```
查看看有沒有版本函式庫相以的,將它移除
