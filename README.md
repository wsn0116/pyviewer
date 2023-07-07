# pyviewer

特定ディレクトリに日付別に格納された画像をブラウザで見れます。

## 開発環境

Python 3.10.6  
Django 4.2.2  
SQLite

## 想定ディレクトリ構成
```
OUTPUT_DIR/
　├ images/（画像）
　│　├ yyyy-mm-dd/
　│　├ yyyy-mm-dd/
　│　└ yyyy-mm-dd/
  └ trashes/（ごみ箱）
```

## 使い方 (Windows & Powershell)

### 1. Python 3 をインストール
https://www.python.org/downloads/

### 2. venv 構築～有効化
```
mkdir venv
python -m venv ./venv
./venv/Scripts/Activate.ps1
```

### 3. django, django-environ をインストール
```
pip install django
pip install django-environ
```

### 4. 環境設定
./mysite/.env.sample を ./mysite/.env としてコピーし、画像参照先のディレクトリを書き換えます。

### 5. DB マイグレーション
```
cd mysite
python manage.py migrate
```

### 6. 管理ユーザー作成
```
python manage.py createsuperuser
```

### 7. 実行
```
python manage.py runserver 8080
```

### 8. 完成

#### 8-1. 画像ビューワを使う
ブラウザから http://localhost:8080/viewer/ で見れるはずです。6 で作成したユーザー情報で認証してください。

#### 8-2. ディレクトリに名前をつける
ブラウザから http://localhost:8080/admin/ にアクセスし、Theme テーブルにレコードを登録するとディレクトリに名前をつけられます。  
directory カラムにディレクトリ（yyyy-mm-dd）、theme カラムに名称を設定してください。
