#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/27 0027
# @Author  : justin.郑 3907721@qq.com
# @File    : conf.py
# @Desc    : 系统信息管理

from flask import render_template, request, jsonify
from app.libs.redprint import Redprint
from app.libs.role import role_required
from app.models.conf import Conf
from app.models.base import db

api = Redprint('conf')
mdb = globals()['Conf']


@api.route('/index', methods=['POST', 'GET'])
@role_required()
def conf_index():
    if request.method == 'GET':
        find = mdb.query.filter_by(id=1).first()
        return render_template('admin/conf/index.html', find=find, menutitle='站点管理', navtitle='站点配置')

    if request.method == 'POST':
        form = request.form
        data = mdb().set_dicts(form)
        id = request.form.get('id')
        try:
            mdb.query.filter_by(id=id).update(data)
            db.session.commit()
        except Exception as e:
            return jsonify({'status': 400, 'message': e})
        return jsonify({'status': 200})



