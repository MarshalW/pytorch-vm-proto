# CUDA VM Proto

一个命令工具，可一健生成公有云（目前是阿里云）临时 vm，配置 gpu 和开发环境。

用于临时性的 `pytorch` 代码测试。

经济性好，使用竞价/抢占的付费方式，平均 1 小时小于 `¥0.4` (新加坡 nvidia t4/16GB)

## 准备镜像

设置阿里云环境变量，terraform 需要相关变量访问云端服务：

```bash
# ~/.zshrc
export ALICLOUD_ACCESS_KEY=xxxxx
export ALICLOUD_SECRET_KEY=xxxxx
# export ALICLOUD_REGION="cn-beijing"
```


复制项目：

```
git clone 
```