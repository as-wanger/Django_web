#_*_ encoding: utf-8 *_*
from captcha.fields import CaptchaField
from django import forms

from app_five import models


class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile5
        fields = ['height', 'male', 'website']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['height'].label = '身高(cm)'
        self.fields['male'].label = '是男生嗎'
        self.fields['website'].label = '個人網站'


class LoginForm(forms.Form):
    username = forms.CharField(label='姓名', max_length=10)
    password = forms.CharField(label='密碼', widget=forms.PasswordInput())


class DateInput(forms.DateInput):
    input_type = 'date'


class DiaryForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = models.Diary5
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
        self.fields['captcha'].label = '機器人驗證'
    