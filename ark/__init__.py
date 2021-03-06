# -*- coding: UTF-8 -*-
################################################################################
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
################################################################################
"""
**ark** 提供Guardian运行的核心机制与开发所需要的基础功能与工具，包含如下模块：

* ``are`` Guardian运行所依赖的基础库，包含一些常用的运维开发组件，并沉淀了我们的一些运维开发经验
* ``opal`` 操作抽象层,针对操作实体进行数据和操作的封装，屏蔽底层系统，为上层开发提供统一接口
* ``assemble`` 基于ark框架和一些开源组件实现的可直接使用的Guardian
"""
__version = '1.0.0'
__all = ['are', 'assemble', 'opal', 'component']
