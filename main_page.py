#streamlit run main_page.py で起動

#やること
#受け取ったデータを保存してエクセルにまとめる

import streamlit as st
from PIL import Image
import datetime

st.title('Inaman')
st.caption('東京都足立区千住寿町')

st.text('当マンションへ入居ご希望の方は以下のフォームからご連絡ください。')
#画像
image = Image.open('./data/yamakawa.png')
st.image(image, width=150)

with st.form(key='profile_form'):

   #テキストポックス
   room = st.multiselect("部屋タイプ（複数選択可）", ("1K", "2K", "1LDK"))
   floor = st.multiselect("階数（複数選択可）", ("1階", "2階", "3階", "4階"))
   name = st.text_input('お客様のお名前')
   email = st.text_input('メールアドレス')
   start_date = st.date_input(
      '入居希望日',
      datetime.date(2022,10,1))

   #ボタン 押された場合はTrueが帰ってくる
   submit_btn = st.form_submit_button('送信')
   cancel_btn = st.form_submit_button('キャンセル')

   if submit_btn:
      st.text(f'リクエストを受領いたしました。\nお客様のメールアドレスにご連絡いたします。')
