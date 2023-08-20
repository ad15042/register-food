# ベースイメージ
FROM python:3

# コンソールのバッファを無効にする
ENV PYTHONUNBUFFERED 1



# 必要なライブラリをインストール
RUN apt update -y && \
    apt install -y curl && \
    apt install -y vim
    
RUN pip install --upgrade pip

# 必要なライブラリをインストール
COPY ./src/app/requirements.txt .
RUN pip install -r requirements.txt


# 作業用ディレクトリを作成
RUN mkdir /work
# ワークディレクトリを設定
WORKDIR /work

# ローカル環境のリソースを作業ディレクトリに移動させる。
ADD . /work/

