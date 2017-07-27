# -*- coding: utf-8 -*-
__author__ = 'custer'
__date__ = '2017/7/26 11:13'
import xadmin
from .models import CourseOrg, CityDict, Teacher


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']

xadmin.site.register(CityDict, CityDictAdmin)


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'click_nums', 'fav_num', 'address', 'city', 'add_time']
    search_fields = ['name', 'desc', 'click_nums', 'fav_num', 'address', 'city']
    list_filter = ['name', 'desc', 'click_nums', 'fav_num', 'address', 'city', 'add_time']

xadmin.site.register(CourseOrg, CourseOrgAdmin)


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_num', 'add_time']
    search_fields = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_num']
    list_filter = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_num', 'add_time']

xadmin.site.register(Teacher, TeacherAdmin)
