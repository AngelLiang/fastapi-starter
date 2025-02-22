# 构建前端
# 使用Node.js作为基础镜像
# FROM node:18 AS build-stage

# WORKDIR /app

# ARG react_app_env=development
# ENV REACT_APP_ENV=${react_app_env}
# ENV NODE_OPTIONS=--openssl-legacy-provider

# COPY . .
# RUN cd frontend && yarn install && yarn run build:product


FROM python:3.11-slim-bullseye

# 清空所有现有的源列表，并添加阿里源
# RUN echo '' > /etc/apt/sources.list && \
#     rm -rf /etc/apt/sources.list.d/* && \
#     echo 'deb https://mirrors.aliyun.com/debian/ bullseye main non-free contrib' > /etc/apt/sources.list \
#     && echo 'deb https://mirrors.aliyun.com/debian/ bullseye-updates main non-free contrib' >> /etc/apt/sources.list
#     # && echo 'deb https://mirrors.aliyun.com/debian-security/ bullseye-security main' >> /etc/apt/sources.list \
#     # && echo 'deb-src https://mirrors.aliyun.com/debian-security/ bullseye-security main' >> /etc/apt/sources.list && \
#     # && echo 'deb https://mirrors.aliyun.com/debian/ bullseye-updates main non-free contrib' >> /etc/apt/sources.list  \
#     # && echo 'deb-src https://mirrors.aliyun.com/debian/ bullseye-updates main non-free contrib' >> /etc/apt/sources.list  \
#     # && echo 'deb https://mirrors.aliyun.com/debian/ bullseye-backports main non-free contrib' >> /etc/apt/sources.list \
#     # echo 'deb-src https://mirrors.aliyun.com/debian/ bullseye-backports main non-free contrib' >> /etc/apt/sources.list


# 设置环境变量
ENV LANG=en_US.UTF-8 LC_ALL=en_US.utf8
# 设置时区，否则存入到数据库的时间会不正确
RUN ln -s -f /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' > /etc/timezone

# 阻止 Python 生成.pyc文件、阻止段错误上启用 Python 回溯
ENV PYTHONPATH=${PYTHONPATH}:${PWD} PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PYTHONFAULTHANDLER=1

WORKDIR /code
RUN chown -R 1001:0 /code
# USER 1001

RUN apt-get update -y && apt-get install -y python3-dev default-libmysqlclient-dev build-essential pkg-config

COPY uv.lock /code
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv
RUN uv sync

COPY . .

# 从构建阶段复制构建后的文件到静态文件夹
# COPY --from=build-stage /app/frontend_vue/dist/index.html /code/apps/suno/templates/frontend_vue/index.html
# COPY --from=build-stage /app/frontend_vue/dist/assets /code/staticfiles

# 打开端口
EXPOSE 8000
# 启动服务器
CMD alembic upgrade head && uvicorn server.main:app --port 8000 --host 0.0.0.0 --proxy-headers --forwarded-allow-ips='*'
