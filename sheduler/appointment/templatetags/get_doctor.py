# -*- coding: utf-8 -*-
from django import template
import re
from privacy.models import PrivacyGroup, PrivacyGroupMember

from achievement.models import SetItem, Achievement, AchievementToDo










register = template.Library()



@register.inclusion_tag('tags/get_doctor.html')
def get_doctor(doctor):
    pass