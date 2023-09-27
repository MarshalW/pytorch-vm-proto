#!/bin/bash

set -e

# domain=witmob.com
# sub_domain=chat

source ./env.sh

# 关闭服务
cd terraform/alicloud
terraform destroy -auto-approve
echo "Server has distroyed."

# 查找已存在的记录
response=$(curl -s -X POST https://dnsapi.cn/Record.List -d \
    "login_token=$DNSPOD_LOGIN_TOKEN&format=json&domain=$domain&sub_domain=$sub_domain&record_type=A&offset=0&length=10")

if echo $response | grep -q records; then
    echo "Has records ${sub_domain}.${domain}"
    record_ids=$(echo $response | jq -r .records[].id)
    # 删除已经存在的记录
    echo $record_ids | xargs -n 1 -I % curl -X POST https://dnsapi.cn/Record.Remove -d \
        "login_token=$DNSPOD_LOGIN_TOKEN&format=json&domain=$domain&record_id=%"
    echo

    echo "Record ${sub_domain}.${domain} has deleted."
fi


