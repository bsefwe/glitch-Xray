

> 提醒： 滥用可能导致账户被BAN！！！ 
官网：https://glitch.com

## 概述

用于在 glitch中 部署 vless+websocket+tls，每次部署自动选择最新的 alpine linux 和 Xray core 。  
vless 性能更加优秀，占用资源更少。

* 使用[xray](https://github.com/XTLS/Xray-core)+caddy同时部署通过ws传输的vmess vless trojan shadowsocks socks等协议，并默认已配置好伪装网站。
* 支持tor网络，且可通过自定义网络配置文件启动xray和caddy来按需配置各种功能  
* 支持存储自定义文件,目录及账号密码均为UUID,客户端务必使用TLS连接  


 >  代理协议：vless 或 vmess 或 Trojan-go

    *地址：平台分配的域名链接

    *端口：443

    *默认UUID：

    *加密：none

    *传输协议：ws

    *伪装类型：none

    *路径：/$AUUID-vless // 默认vless使用/$AUUID-vless，vmess使用/$AUUID-vmess，Trojan使用/$AUUID-Trojan

    *底层传输安全：tls
