from django import forms


class AlcoholForm(forms.Form):
    # アルコール度数とmlの入力欄を5セット作成
    alcohol_percentage_1 = forms.DecimalField(label='アルコール度数 (%)', min_value=0)
    volume_ml_1 = forms.DecimalField(label='ボリューム (ml)', min_value=0)
    alcohol_percentage_2 = forms.DecimalField(label='アルコール度数 (%)', min_value=0)
    volume_ml_2 = forms.DecimalField(label='ボリューム (ml)', min_value=0)
    alcohol_percentage_3 = forms.DecimalField(label='アルコール度数 (%)', min_value=0)
    volume_ml_3 = forms.DecimalField(label='ボリューム (ml)', min_value=0)
    alcohol_percentage_4 = forms.DecimalField(label='アルコール度数 (%)', min_value=0)
    volume_ml_4 = forms.DecimalField(label='ボリューム (ml)', min_value=0)
    alcohol_percentage_5 = forms.DecimalField(label='アルコール度数 (%)', min_value=0)
    volume_ml_5 = forms.DecimalField(label='ボリューム (ml)', min_value=0)
