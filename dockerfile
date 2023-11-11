FROM nvidia/cuda:11.8.0-cudnn8-devel-ubuntu22.04

#docker-composeから引数を受け取る
ARG http_tmp
ARG https_tmp

#環境変数にプロキシの設定を追加
ENV http_proxy=$http_tmp
ENV https_proxy=$https_tmp

#タイムゾーンを東京に設定
ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

#apt関連の設定
RUN apt-get -y update && apt-get -y upgrade
RUN apt install -y nano screen tmux systemd init nginx python3 python3-pip

