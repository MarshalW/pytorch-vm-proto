# 记录生成镜像的命令

#### 本地
# 在本地执行，将docker-compose.yaml和Dockerfile 同步到 vm 上
./sync.sh


#### 服务器
# 更新系统
apt update && apt upgrade -y

# 安装驱动 535
ubuntu-drivers autoinstall
# apt install nvidia-driver-525 -y -qq

# 需要重启
reboot

# 测试驱动是否有效
nvidia-smi

# 安装 docker
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh

# 安装 nvidia container toolkit
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
  && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    tee /etc/apt/sources.list.d/nvidia-container-toolkit.list \
  && \
    apt-get update
apt-get install nvidia-container-toolkit -qq -y
systemctl restart docker

# 构建带 pytorch 的 docker 镜像并启动
docker compose up -d

# 测试容器是否可用
docker exec -it proto bash

