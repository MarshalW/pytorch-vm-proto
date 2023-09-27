#!/bin/bash

set -e

# domain=witmob.com
# sub_domain=proto

source ./env.sh

cd terraform/alicloud
terraform apply -auto-approve
echo "Server started."

public_ip=$(terraform -chdir=./ output -json | jq .public_ip.value -r)

# 测试用
# public_ip="47.245.126.191"

echo "Public ip: $public_ip, start set domain .."

# 查找已存在的记录
response=$(curl -s -X POST https://dnsapi.cn/Record.List -d \
    "login_token=$DNSPOD_LOGIN_TOKEN&format=json&domain=$domain&sub_domain=$sub_domain&record_type=A&offset=0&length=10")

if echo $response | grep -q records; then
    echo "Has records ${sub_domain}.${domain}"
    record_ids=$(echo $response | jq -r .records[].id)
    # 删除已经存在的记录
    echo $record_ids | xargs -n 1 -I % curl -X POST https://dnsapi.cn/Record.Remove -d \
        "login_token=$DNSPOD_LOGIN_TOKEN&format=json&domain=$domain&record_id=%"
fi

response=$(curl -s -X POST https://dnsapi.cn/Record.Create -d \
    "login_token=$DNSPOD_LOGIN_TOKEN&format=json&domain=$domain&sub_domain=$sub_domain&record_type=A&record_line=默认&value=$public_ip")

code=$(echo $response | jq -r .status.code)

if [[ $code -eq 1 ]]; then
    echo "Add $sub_domain ok."
else
    echo "Error: add $sub_domain"
fi

# 启动服务
# ssh root@$sub_domain.$domain -t "docker compose up -d"

# 删除以前的 ssh 记录
ssh-keygen -R $sub_domain.$domain
