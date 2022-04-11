#_*_ encoding: utf-8 *_*
from captcha.fields import CaptchaField
from django import forms
from django.forms import ModelForm

from app_four import models


class LoginForm(forms.Form):
    username = forms.CharField(label='姓名', max_length=10)
    password = forms.CharField(label='密碼', widget=forms.PasswordInput())


class DateInput(forms.DateInput):
    input_type = 'date'


class DiaryForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = models.Diary4
        fields = ['budget', 'weight', 'note', 'ddate']
        widgets = {
            'ddate': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super(DiaryForm, self).__init__(*args, **kwargs)
        self.fields['budget'].label = '今日花費(元)'
        self.fields['weight'].label = '今日體重(KG)'
        self.fields['note'].label = '心情留言'
        self.fields['ddate'].label = '日期'
        self.fields['captcha'].label = '確定你不是機器人'
    