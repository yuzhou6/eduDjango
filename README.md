# eduDjango

## 一、项目介绍

### 1.1 项目简介

基于 Django 搭建一个具有标准在线教育网站功能的项目。

演示地址：[http://lucatedu.applinzi.com/](http://lucatedu.applinzi.com/)

## 二、项目截图

### 2.1 项目截图

后台部分：

![01](http://ww1.sinaimg.cn/mw690/005EFdvdgy1fcxyj4vm4qj311i0httam)

![02](http://ww1.sinaimg.cn/mw690/005EFdvdgy1fcxyl367p0j311j0hugmf)

![](http://ww1.sinaimg.cn/mw690/005EFdvdgy1fcxymnef65j311s0hutal)

![](http://ww1.sinaimg.cn/mw690/005EFdvdgy1fcxyolc3hjj311t0hsabq)

![](http://ww1.sinaimg.cn/mw690/005EFdvdgy1fcxyrr5nz0j311j0hpwgf)

![](http://ww1.sinaimg.cn/mw690/005EFdvdgy1fcxyp6s4zfj311h0hq408)

![](http://ww1.sinaimg.cn/mw690/005EFdvdgy1fcxypfyuz3j311f0hqjta)

![](http://ww1.sinaimg.cn/mw690/005EFdvdgy1fcxypq4fakj311d0howok)

![](http://ww1.sinaimg.cn/mw690/005EFdvdgy1fcxypwea9xj31190hftav)

![](http://ww1.sinaimg.cn/mw690/005EFdvdgy1fcxyq0ymj5j30z80hkta1)

![](http://ww1.sinaimg.cn/mw690/005EFdvdgy1fcxyq69vtzj31050hojud)

![](http://ww1.sinaimg.cn/mw690/005EFdvdgy1fcxyqbor6uj311m0hnwgo)

## 三、项目部署

### 3.1 部署在新浪 SAE 上

项目地址：[http://lucatedu.applinzi.com/](http://lucatedu.applinzi.com/)

在项目根目录下，创建配置文件 `config.yaml`，编写如下内容：

```
#--config.yaml--#
name: eduDjango
version: 1

libraries:
- name: "django"
  version: "1.9.8"
- name: 'PIL'
  version: "1.1.7"

handlers:
- url: /static
  static_dir: static
- media: /media
  static_dir: media
```
创建文件 `index.wsgi`，编写如下内容：

```
import sae
from mxonline import wsgi

application = sae.create_wsgi_app(wsgi.application)
```
接着按照新浪 SAE 官方文档，建好仓库后，`push` 到相应仓库即可。

如有问题，欢迎留言。
