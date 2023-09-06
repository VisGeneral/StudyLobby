from flask import Blueprint, send_file, render_template, request, flash, jsonify, redirect, url_for,send_from_directory
from flask_login import login_required, current_user
from flask_wtf import FlaskForm
import random
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
import base64
def base64Encoding(input):
  dataBase64 = base64.b64encode(input)
  dataBase64P = dataBase64.decode("UTF-8")
  return dataBase64P
def base64Decoding(input):
    return base64.decodebytes(input.encode("ascii"))
def generateRandomAesKey():
  return get_random_bytes(32)
def aesEcbEncryptToBase64(encryptionKey, plaintext):
  cipher = AES.new(encryptionKey, AES.MODE_ECB)
  ciphertext = cipher.encrypt(pad(plaintext.encode("ascii"), AES.block_size))
  ciphertextBase64 = base64Encoding(ciphertext)
  return ciphertextBase64
def aesEcbDecryptFromBase64(decryptionKey, ciphertextDecryptionBase64):
  ciphertext = base64Decoding(ciphertextDecryptionBase64)
  cipher = AES.new(decryptionKey, AES.MODE_ECB)
  decryptedtext = unpad(cipher.decrypt(ciphertext), AES.block_size)
  decryptedtextP = decryptedtext.decode("UTF-8")
  return decryptedtextP
encryptionKey = generateRandomAesKey()
encryptionKeyBase64 = base64Encoding(encryptionKey)
decryptionKeyBase64 = encryptionKeyBase64
decryptionKey = base64Decoding(decryptionKeyBase64)
from datetime import datetime
from . import db
import requests
from bs4 import BeautifulSoup
import smtplib
import re
answer="0"
secret_key=b'5345435343456454'
cipher = AES.new(secret_key,AES.MODE_ECB)
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
answer = "None"
global list1
list1 = []
views = Blueprint('views', __name__)
import json
@views.route('/app')
@login_required
def app():
    return render_template('StudyLobbyApp.html')
@views.route('/terms-of-service')
@login_required
def termsofservice():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if "iphone" in user_agent:
        return render_template('mobile/terms-of-service.html')
    elif "android" in user_agent:
        return render_template('mobile/terms-of-service.html')
    else:
        return render_template('terms-of-service.html')
@views.route('/privacy-policy')
@login_required
def privacypolicy():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if "iphone" in user_agent:
        return render_template('mobile/privacypolicy.html')
    elif "android" in user_agent:
        return render_template('mobile/privacypolicy.html')
    else:
        return render_template('privacypolicy.html')
@views.route('/cookie-policy')
@login_required
def cookiepolicy():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if "iphone" in user_agent:
        return render_template('mobile/cookiepolicy.html')
    elif "android" in user_agent:
        return render_template('mobile/cookiepolicy.html')
    else:
        return render_template('cookiepolicy.html')
@views.route('/')
@login_required
def homepage():
    achievements={}
    achievements_completed={}
    if current_user.is_authenticated:
        f = open('mysite/website/static/leaderboard.txt', 'r')
        for line in f:
            wr = open('mysite/website/static/leaderboard.txt', 'a')
            if line.startswith("{'"+current_user.first_name+"'"+": "):
                line.replace("}", "")
                replacestr="{'"+current_user.first_name+"': "
                line=line.replace(replacestr, "")
                line=line.replace("}","")
                userxp=int(line)
                if userxp >= 100:
                  xp_100=100
                  achievements_completed["Earn 100 xp"]= f'100/100'
                else:
                  xp_100=userxp
                  achievements["Earn 100 xp"]= f'{userxp}/100'

                if userxp >= 250:
                  xp_250=250
                  achievements_completed["Earn 250 xp"]= f'250/250'
                else:
                  xp_250=userxp
                  achievements["Earn 250 xp"]= f'{userxp}/250'

                if userxp >= 500:
                  xp_500=500
                  achievements_completed["Earn 500 xp"]= f'500/500'
                else:
                  xp_500=userxp
                  achievements["Earn 500 xp"]= f'{userxp}/500'

                if userxp >= 750:
                  xp_750=750
                  achievements_completed["Earn 750 xp"]= f'750/750'
                else:
                  xp_750=userxp
                  achievements["Earn 750 xp"]= f'{userxp}/750'

                if userxp >= 1000:
                  xp_1000=1000
                  achievements_completed["Earn 1000 xp"]= f'1000/1000'
                else:
                  xp_1000=userxp
                  achievements["Earn 1000 xp"]= f'{userxp}/1000'

                if userxp >= 1250:
                  xp_1250=1250
                  achievements_completed["Earn 1250 xp"]= f'1250/1250'
                else:
                  xp_1250=userxp
                  achievements["Earn 1250 xp"]= f'{userxp}/1250'

                if userxp >= 1500:
                  xp_1500=1500
                  achievements_completed["Earn 1500 xp"]= f'1500/1500'
                else:
                  xp_1500=userxp
                  achievements["Earn 1500 xp"]= f'{userxp}/1500'

                if userxp >= 2000:
                  xp_2000=2000
                  achievements_completed["Earn 2000 xp"]= f'2000/2000'
                else:
                  xp_2000=userxp
                  achievements["Earn 2000 xp"]= f'{userxp}/2000'

                if userxp >= 2500:
                  xp_2500=2500
                  achievements_completed["Earn 2500 xp"]= f'2500/2500'
                else:
                  xp_2500=userxp
                  achievements["Earn 2500 xp"]= f'{userxp}/2500'

                if userxp >= 5000:
                  xp_5000=5000
                  achievements_completed["Earn 5000 xp"]= f'5000/5000'
                else:
                  xp_5000=userxp
                  achievements["Earn 5000 xp"]= f'{userxp}/5000'

                if userxp >= 10000:
                  xp_10000=10000
                  achievements_completed["Earn 10000 xp"]= f'10000/10000'
                else:
                  xp_10000=userxp
                  achievements["Earn 10000 xp"]= f'{userxp}/10000'

                if userxp >= 25000:
                  xp_25000=25000
                  achievements_completed["Earn 25000 xp"]= f'25000/25000'
                else:
                  xp_25000=userxp
                  achievements["Earn 25000 xp"]= f'{userxp}/25000'

                if userxp >= 50000:
                  xp_50000=50000
                  achievements_completed["Earn 50000 xp"]= f'50000/50000'
                else:
                  xp_50000=userxp
                  achievements["Earn 50000 xp"]= f'{userxp}/50000'

                if userxp >= 75000:
                  xp_75000=75000
                  achievements_completed["Earn 75000 xp"]= f'75000/75000'
                else:
                  xp_75000=userxp
                  achievements["Earn 75000 xp"]= f'{userxp}/75000'

                if userxp >= 100000:
                  xp_100000=100000
                  achievements_completed["Earn 100000 xp"]= f'100000/100000'
                else:
                  xp_100000=userxp
                  achievements["Earn 100000 xp"]= f'{userxp}/100000'

                if userxp >= 125000:
                  xp_125000=125000
                  achievements_completed["Earn 125000 xp"]= f'125000/125000'
                else:
                  xp_125000=userxp
                  achievements["Earn 125000 xp"]= f'{userxp}/125000'

                if userxp >= 150000:
                  xp_150000=150000
                  achievements_completed["Earn 150000 xp"]= f'150000/150000'
                else:
                  xp_150000=userxp
                  achievements["Earn 150000 xp"]= f'{userxp}/150000'

                if userxp >= 175000:
                  xp_175000=175000
                  achievements_completed["Earn 175000 xp"]= f'175000/175000'
                else:
                  xp_175000=userxp
                  achievements["Earn 175000 xp"]= f'{userxp}/175000'

                if userxp >= 200000:
                  xp_200000=200000
                  achievements_completed["Earn 200000 xp"]= f'200000/200000'
                else:
                  xp_200000=userxp
                  achievements["Earn 200000 xp"]= f'{userxp}/200000'

                if userxp >= 250000:
                  xp_250000=250000
                  achievements_completed["Earn 250000 xp"]= f'250000/250000'
                else:
                  xp_250000=userxp
                  achievements["Earn 250000 xp"]= f'{userxp}/250000'

                if userxp >= 500000:
                  xp_500000=500000
                  achievements_completed["Earn 500000 xp"]= f'500000/500000'
                else:
                  xp_500000=userxp
                  achievements["Earn 500000 xp"]= f'{userxp}/500000'

                if userxp >= 750000:
                  xp_750000=750000
                  achievements_completed["Earn 750000 xp"]= f'750000/750000'
                else:
                  xp_750000=userxp
                  achievements["Earn 750000 xp"]= f'{userxp}/750000'

                if userxp >= 1000000:
                  xp_1000000=1000000
                  achievements_completed["Earn 1000000 xp"]= f'1000000/1000000'
                else:
                  xp_1000000=userxp
                  achievements["Earn 1000000 xp"]= f'{userxp}/1000000'
        user_agent = request.headers.get('User-Agent')
        user_agent = user_agent.lower()
        if "iphone" in user_agent:
            return render_template('mobile/StudyLobbyHome.html', achievements=achievements, achievements_completed=achievements_completed)
        elif "android" in user_agent:
            return render_template('mobile/StudyLobbyHome.html', achievements=achievements, achievements_completed=achievements_completed)
        else:
            return render_template('StudyLobbyHome.html', achievements=achievements, achievements_completed=achievements_completed)
    else:
        user_agent = request.headers.get('User-Agent')
        user_agent = user_agent.lower()
        if "iphone" in user_agent:
            return render_template('mobile/StudyLobbyHome.html')
        elif "android" in user_agent:
            return render_template('mobile/StudyLobbyHome.html')
        else:
            return render_template('StudyLobbyHome.html')
@views.route('/explore')
@login_required
def explore():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if "iphone" in user_agent:
        return render_template('mobile/StudyLobbyExplore.html')
    elif "android" in user_agent:
        return render_template('mobile/StudyLobbyExplore.html')
    else:
        return render_template('StudyLobbyExplore.html')
@views.route('/tutor')
@login_required
def tutor():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if "iphone" in user_agent:
        return render_template('mobile/StudyLobbyTutor.html')
    elif "android" in user_agent:
        return render_template('mobile/StudyLobbyTutor.html')
    else:
        return render_template('StudyLobbyTutor.html')
@views.route('/tutor', methods=['POST'])
@login_required
def tutor1():
    email = request.form['text']
    name = request.form['text1']
    try:
        message = "Message: "+{request.form['text2']}
    except:
        message="Message: None"
    subject = request.form['subject']
    grade = request.form['grade']
    if subject == "Math":
        if grade == "K":
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2002890kzheng@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'Kz2002890'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2004780sheck@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            answera="success"
            answerb="Success!"
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            else:
                return render_template('StudyLobbyTutor.html', answera=answera, answerb=answerb)
        if grade == "1st":
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2002890kzheng@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2004780sheck@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            answera="success"
            answerb="Success!"
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            else:
                return render_template('StudyLobbyTutor.html', answera=answera, answerb=answerb)
        if grade == "2nd":
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2002890kzheng@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2004780sheck@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            answera="success"
            answerb="Success!"
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            else:
                return render_template('StudyLobbyTutor.html', answera=answera, answerb=answerb)
        if grade == "3rd":
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2002890kzheng@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2004780sheck@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            answera="success"
            answerb="Success!"
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            else:
                return render_template('StudyLobbyTutor.html', answera=answera, answerb=answerb)
        if grade == "4th":
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2002890kzheng@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2004780sheck@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            answera="success"
            answerb="Success!"
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            else:
                return render_template('StudyLobbyTutor.html', answera=answera, answerb=answerb)
        if grade == "5th":
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2002890kzheng@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2004780sheck@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            answera="success"
            answerb="Success!"
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            else:
                return render_template('StudyLobbyTutor.html', answera=answera, answerb=answerb)
        if grade == "6th":
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2002890kzheng@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2004780sheck@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            answera="success"
            answerb="Success!"
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            else:
                return render_template('StudyLobbyTutor.html', answera=answera, answerb=answerb)
        if grade == "7th":
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2002890kzheng@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2004780sheck@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            answera="success"
            answerb="Success!"
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            else:
                return render_template('StudyLobbyTutor.html', answera=answera, answerb=answerb)
        if grade == "8th":
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2002890kzheng@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2004780sheck@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            answera="success"
            answerb="Success!"
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            else:
                return render_template('StudyLobbyTutor.html', answera=answera, answerb=answerb)
        if grade == "9th":
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2002890kzheng@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2004780sheck@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            answera="success"
            answerb="Success!"
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            else:
                return render_template('StudyLobbyTutor.html', answera=answera, answerb=answerb)
        else:
            answera="danger"
            answerb="Incorrect!"
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            else:
                return render_template('StudyLobbyTutor.html', answera=answera, answerb=answerb)
    if subject == "Physics":
        if grade == "K":
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2002890kzheng@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2004780sheck@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            answera="success"
            answerb="Success!"
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            else:
                return render_template('StudyLobbyTutor.html', answera=answera, answerb=answerb)
        if grade == "1st":
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2002890kzheng@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2004780sheck@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            answera="success"
            answerb="Success!"
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            else:
                return render_template('StudyLobbyTutor.html', answera=answera, answerb=answerb)
        if grade == "2nd":
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2002890kzheng@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2004780sheck@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            answera="success"
            answerb="Success!"
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            else:
                return render_template('StudyLobbyTutor.html', answera=answera, answerb=answerb)
        if grade == "3rd":
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2002890kzheng@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2004780sheck@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            answera="success"
            answerb="Success!"
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            else:
                return render_template('StudyLobbyTutor.html', answera=answera, answerb=answerb)
        if grade == "4th":
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2002890kzheng@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2004780sheck@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            answera="success"
            answerb="Success!"
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            else:
                return render_template('StudyLobbyTutor.html', answera=answera, answerb=answerb)
        if grade == "5th":
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2002890kzheng@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2004780sheck@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            answera="success"
            answerb="Success!"
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            else:
                return render_template('StudyLobbyTutor.html', answera=answera, answerb=answerb)
        if grade == "6th":
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2002890kzheng@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2004780sheck@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            answera="success"
            answerb="Success!"
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            else:
                return render_template('StudyLobbyTutor.html', answera=answera, answerb=answerb)
        if grade == "7th":
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2002890kzheng@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2004780sheck@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            answera="success"
            answerb="Success!"
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            else:
                return render_template('StudyLobbyTutor.html', answera=answera, answerb=answerb)
        if grade == "8th":
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2002890kzheng@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2004780sheck@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            answera="success"
            answerb="Success!"
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            else:
                return render_template('StudyLobbyTutor.html', answera=answera, answerb=answerb)
        if grade == "9th":
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2002890kzheng@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2004780sheck@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            answera="success"
            answerb="Success!"
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            else:
                return render_template('StudyLobbyTutor.html', answera=answera, answerb=answerb)
        else:
            answera="danger"
            answerb="Incorrect"
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            else:
                return render_template('StudyLobbyTutor.html', answera=answera, answerb=answerb)
    if subject == "ELA":
        if grade == "K":
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2002890kzheng@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2004780sheck@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            answera="success"
            answerb="Success!"
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            else:
                return render_template('StudyLobbyTutor.html', answera=answera, answerb=answerb)
        if grade == "1st":
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2002890kzheng@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2004780sheck@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            answera="success"
            answerb="Success!"
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            else:
                return render_template('StudyLobbyTutor.html', answera=answera, answerb=answerb)
        if grade == "2nd":
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2002890kzheng@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2004780sheck@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            answera="success"
            answerb="Success!"
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            else:
                return render_template('StudyLobbyTutor.html', answera=answera, answerb=answerb)
        if grade == "3rd":
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2002890kzheng@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2004780sheck@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            answera="success"
            answerb="Success!"
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            else:
                return render_template('StudyLobbyTutor.html', answera=answera, answerb=answerb)
        if grade == "4th":
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2002890kzheng@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2004780sheck@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            answera="success"
            answerb="Success!"
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            else:
                return render_template('StudyLobbyTutor.html', answera=answera, answerb=answerb)
        if grade == "5th":
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2002890kzheng@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2004780sheck@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            answera="success"
            answerb="Success!"
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            else:
                return render_template('StudyLobbyTutor.html', answera=answera, answerb=answerb)
        if grade == "6th":
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2002890kzheng@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2004780sheck@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            answera="success"
            answerb="Success!"
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            else:
                return render_template('StudyLobbyTutor.html', answera=answera, answerb=answerb)
        if grade == "7th":
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2002890kzheng@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2004780sheck@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            answera="success"
            answerb="Success!"
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            else:
                return render_template('StudyLobbyTutor.html', answera=answera, answerb=answerb)
        if grade == "8th":
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2002890kzheng@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2004780sheck@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            answera="success"
            answerb="Success!"
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            else:
                return render_template('StudyLobbyTutor.html', answera=answera, answerb=answerb)
        if grade == "9th":
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2002890kzheng@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            SUBJECT = 'Tutor Request'
            fromaddr = 'playtimekzplays@gmail.com'
            toaddrs  = '2004780sheck@vineland.org'
            username = 'playtimekzplays@gmail.com'
            password = 'reaewfhmjxkzqsak'
            msg1 = f" {name} ({email}) Is requesting a tutor for {subject} ({grade}) {message}"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            msg = MIMEText(msg1)
            msg['Subject'] = SUBJECT
            msg['To'] = toaddrs
            msg['From'] = fromaddr
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            answera="success"
            answerb="Success!"
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            else:
                return render_template('StudyLobbyTutor.html', answera=answera, answerb=answerb)
        else:
            answera="danger"
            answerb="Incorrect"
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyTutor.html', answera=answera, answerb=answerb)
            else:
                return render_template('StudyLobbyTutor.html', answera=answera, answerb=answerb)
@views.route('/leaderboard')
@login_required
def leaderboard():
    user=current_user
    if user.is_authenticated:
        leaderboard={}
        f = open('mysite/website/static/leaderboard.txt', 'r')
        leaderboard1 = [line.replace('\n','') for line in f.readlines()]
        for i in leaderboard1:
            leaderboard.update(eval(i))
        user_agent = request.headers.get('User-Agent')
        user_agent = user_agent.lower()
        if "iphone" in user_agent:
            return render_template('mobile/StudyLobbyLeaderboard.html',leaderboard=leaderboard)
        elif "android" in user_agent:
            return render_template('mobile/StudyLobbyLeaderboard.html',leaderboard=leaderboard)
        else:
            return render_template('StudyLobbyLeaderboard.html',leaderboard=leaderboard)
    else:
        return redirect("https://studylobby.pythonanywhere.com/login")
@views.route('/lessons')
@login_required
def lessons():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if "iphone" in user_agent:
        return render_template('mobile/StudyLobby.html')
    elif "android" in user_agent:
        return render_template('mobile/StudyLobby.html')
    else:
        return render_template('StudyLobby.html')
@views.route('/lessons', methods=['POST'])
@login_required
def lessons1():
    status = request.form['status']
    if status == "math":
        return redirect("https://studylobby.pythonanywhere.com/math")
    if status == "ela":
        return redirect("https://studylobby.pythonanywhere.com/ela")
    if status == "history":
        return redirect("https://studylobby.pythonanywhere.com/history")
    if status == "science":
        return redirect("https://studylobby.pythonanywhere.com/science")
    if status == "special":
        return redirect("https://studylobby.pythonanywhere.com/others")
@views.route('/minigames')
@login_required
def minigames():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if "iphone" in user_agent:
        return render_template('mobile/StudyLobbyMinigames.html')
    elif "android" in user_agent:
        return render_template('mobile/StudyLobbyMinigames.html')
    else:
        return render_template('StudyLobbyMinigames.html')
@views.route('/minigames', methods=['POST'])
@login_required
def minigames1():
    status = request.form['status']
    if status == "tower2defense":
        return redirect("https://studylobby.pythonanywhere.com/tower2defense")
@views.route('/tower2defense')
@login_required
def tower2defense():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if "iphone" in user_agent:
        return render_template('mobile/StudyLobbytower2defense.html')
    elif "android" in user_agent:
        return render_template('mobile/StudyLobbytower2defense.html')
    else:
        return render_template('StudyLobbytower2defense.html')
@views.route('/tower2defense', methods=['POST'])
@login_required
def tower2defense1():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if "iphone" in user_agent:
        return render_template('mobile/StudyLobbytower2defenseStart.html')
    elif "android" in user_agent:
        return render_template('mobile/StudyLobbytower2defenseStart.html')
    else:
        return render_template('StudyLobbytower2defenseStart.html')
@views.route('/others')
@login_required
def othersstudylobby():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if "iphone" in user_agent:
        return render_template('mobile/StudyLobbyOthers.html')
    elif "android" in user_agent:
        return render_template('mobile/StudyLobbyOthers.html')
    else:
        return render_template('StudyLobbyOthers.html')
@views.route('/others', methods=['POST'])
@login_required
def othersstudylobby1():
    status = request.form['status']
    if status == "russian":
        return redirect("https://studylobby.pythonanywhere.com/russian")
@views.route('/russian')
@login_required
def russian():
    questions = {'1a'  : 'Is this a vowel?: а',
                 '2a'   : 'Is this a vowel?: э',
                 '3a' : 'Is this a vowel?: ы',
                 '4a' : 'Is this a vowel?: у',
                 '5a'   : 'Is this a vowel?: о',
                 '6a'   : 'Is this a vowel?: я',
                 '7a' : 'Is this a vowel?: е',
                 '8a' : 'Is this a vowel?: ё',
                 '9a'   : 'Is this a vowel?: ю',
                 '10a'   : 'Is this a vowel?: и',
                 '11a'   : 'Is this a vowel?: б',
                 '12a' : 'Is this a vowel?: в',
                 '13a' : 'Is this a vowel?: г',
                 '14a'   : 'Is this a vowel?: д',
                 '15a'   : 'Is this a vowel?: ж',
                 '16a' : 'Is this a vowel?: з',
                 '17a' : 'Is this a vowel?: к',
                 '18a'   : 'Is this a vowel?: л',
                 '19a'   : 'Is this a vowel?: м',
                 '20a'   : 'Is this a vowel?: н',
                 '21a' : 'Is this a vowel?: п',
                 '22a' : 'Is this a vowel?: р',
                 '23a'   : 'Is this a vowel?: с',
                 '24a'   : 'Is this a vowel?: т',
                 '25a' : 'Is this a vowel?: ф',
                 '26a' : 'Is this a vowel?: х',
                 '27a'   : 'Is this a vowel?: ц',
                 '28a'   : 'Is this a vowel?: ч',
                 '29a'   : 'Is this a vowel?: ш',
                 '30a' : 'Is this a vowel?: щ',
                 '31a' : 'Is this a vowel?: й',
                 '32a'   : 'Is this a vowel?: ь',
                 '33a'   : 'Is this a vowel?: ъ',
                 '1b' : 'yes',
                 '2b' : 'yes',
                 '3b'   : 'yes',
                 '4b' : 'yes',
                 '5b' : 'yes',
                 '6b' : 'yes',
                 '7b'   : 'yes',
                 '8b' : 'yes',
                 '9b' : 'yes',
                 '10b' : 'yes',
                 '11b' : 'no',
                 '12b'   : 'no',
                 '13b' : 'no',
                 '14b' : 'no',
                 '15b' : 'no',
                 '16b'   : 'no',
                 '17b' : 'no',
                 '18b' : 'no',
                 '19b' : 'no',
                 '20b' : 'no',
                 '21b'   : 'no',
                 '22b' : 'no',
                 '23b' : 'no',
                 '24b' : 'no',
                 '25b'   : 'no',
                 '26b' : 'no',
                 '27b' : 'no',
                 '28b' : 'no',
                 '29b' : 'no',
                 '30b'   : 'no',
                 '31b' : 'no',
                 '32b' : 'no',
                 '33b' : 'no',
                 '34a' : 'What gender is a word that ends in a consonant? type both if your answer is both feminine and masculine.',
                 '34b' : 'masculine',
                 '35a' : 'What gender is a word that ends in й? type both if your answer is both feminine and masculine.',
                 '35b' : 'masculine',
                 '36a' : 'What gender is a word that ends in ь? type both if your answer is both feminine and masculine.',
                 '36b' : 'masculine',
                 '37a' : 'What gender is a word that ends in тель? type both if your answer is both feminine and masculine.',
                 '37b' : 'masculine',
                 '38a' : 'What gender is a word that ends in а? type both if your answer is both feminine and masculine.',
                 '38b' : 'feminine',
                 '39a' : 'What gender is a word that ends in я? type both if your answer is both feminine and masculine.',
                 '39b' : 'feminine',
                 '40a' : 'What gender is a word that ends in ия? type both if your answer is both feminine and masculine.',
                 '40b' : 'feminine',
                 '41a' : 'What gender is a word that ends in ь? type both if your answer is both feminine and masculine.',
                 '41b' : 'feminine',
                 '42a' : 'What gender is a word that ends in ость? type both if your answer is both feminine and masculine.',
                 '42b' : 'feminine',
                 '43a' : 'What gender is a word that ends in о? type both if your answer is both feminine and masculine.',
                 '43b' : 'neuter',
                 '44a' : 'What gender is a word that ends in е? type both if your answer is both feminine and masculine.',
                 '44b' : 'neuter',
                 '45a' : 'What gender is a word that ends in ие? type both if your answer is both feminine and masculine.',
                 '45b' : 'neuter',
                 '46a' : 'What gender is a word that ends in мя? type both if your answer is both feminine and masculine.',
                 '46b' : 'neuter',
                 '47a' : 'How do you convert a word ending with a consonant to plural?',
                 '47b' : 'add ы to the end',
                 '48a' : 'How do you convert a word ending with й to plural? (if the gender is masculine)',
                 '48b' : 'replace й with и',
                 '49a' : 'How do you convert a word ending with ь to plural? (if the gender is masculine)',
                 '49b' : 'replace ь with и',
                 '50a' : 'How do you convert a word ending with а to plural? (if the gender is masculine)',
                 '50b' : 'replace а with ы',
                 '51a' : 'How do you convert a word ending with я to plural? (if the gender is feminine)',
                 '51b' : 'replace я with и',
                 '52a' : 'How do you convert a word ending with ия to plural? (if the gender is feminine)',
                 '52b' : 'replace ия with ии',
                 '53a' : 'How do you convert a word ending with ь to plural? (if the gender is feminine)',
                 '53b' : 'replace ь with и',
                 '54a' : 'How do you convert a word ending with о to plural? (if the gender is feminine)',
                 '54b' : 'replace о with а',
                 '55a' : 'How do you convert a word ending with е to plural? (if the gender is neuter)',
                 '55b' : 'replace е with я',
                 '56a' : 'How do you convert a word ending with ие to plural? (if the gender is neuter)',
                 '56b' : 'replace ие with ия',
                 '57a' : 'How do you convert a word ending with мя to plural? (if the gender is neuter)',
                 '57b' : 'replace мя with ена',
                 '58a' : 'How do you convert a singular word ending in a consonant to the acusative singular form? (if the gender is masculine animate)',
                 '58b' : 'add а to the end',
                 '59a' : 'How do you convert a singular word ending in й to the acusative singular form? (if the gender is masculine animate)',
                 '59b' : 'replace й with я',
                 '60a' : 'How do you convert a singular word ending in ь to the acusative singular form? (if the gender is masculine animate)',
                 '60b' : 'replace ь with я',
                 '61a' : 'How do you convert a singular word to the acusative singular form? (if the gender is masculine inanimate)',
                 '61b' : 'it stays the same',
                 '62a' : 'How do you convert a singular word ending in а to the acusative singular form? (if the gender is feminine)',
                 '62b' : 'replace а with а',
                 '63a' : 'How do you convert a singular word ending in у to the acusative singular form? (if the gender is feminine)',
                 '63b' : 'replace у with я',
                 '64a' : 'How do you convert a singular word ending in ь to the acusative singular form? (if the gender is feminine)',
                 '64b' : 'replace ь with ь',
                 '65a' : 'How do you convert a singular word to the acusative singular form? (if the gender is neuter)',
                 '65b' : 'it stays the same',
                 '66a' : 'How do you convert a singular word ending in a consonant to the acusative plural form? (if the gender is masculine animate)',
                 '66b' : 'add ов to the end',
                 '67a' : 'How do you convert a singular word ending in й to the acusative plural form? (if the gender is masculine animate)',
                 '67b' : 'replace й mith ев',
                 '68a' : 'How do you convert a singular word to the acusative plural form? (if the gender is masculine animate)',
                 '68b' : 'replace ь with ей',
                 '69a' : 'How do you convert a singular word ending in а to the acusative plural form? (if the gender is masculine inanimate)',
                 '69b' : 'it stays the same',
                 '70a' : 'How do you convert a singular word ending in я to the acusative plural form? (if the gender is feminine animate)',
                 '70b' : 'replace а with nothing',
                 '71a' : 'How do you convert a singular word ending in ия to the acusative plural form? (if the gender is feminine animate)',
                 '71b' : 'replace я with ь',
                 '72a' : 'How do you convert a singular word ending in ь to the acusative plural form? (if the gender is feminine animate)',
                 '72b' : 'replace ия with ий',
                 '73a' : 'How do you convert a singular word to the acusative plural form? (if the gender is feminine animate)',
                 '73b' : 'replace ь with ей',
                 '74a' : 'How do you convert a singular word to the acusative plural form? (if the gender is feminine inanimate)',
                 '74b' : 'it stays the same',
                 '75a' : 'How do you convert a singular word to the acusative plural form? (if the gender is neuter)',
                 '75b' : 'it stays the same',
                 '76a' : 'Translate с помощью мамы to English',
                 '76b' : "with mom's help",
                 '77a' : 'Translate По словам президента, сахар не станет дороже в этом году. to Russian',
                 '77b' : 'according to the president, sugar will not become more expensive this year',
                 '78a' : 'Translate лидер оппозиции to English',
                 '78b' : 'opposition leader',
                 '79a' : 'Translate Сколько партий участвовало в выборах? to English',
                 '79b' : 'how many parties participated in the elections',
                 '80a' : 'Translate Парламент принимает законы. to Russian',
                 '80b' : 'the parliment passes laws',
                 '81a' : 'Translate Лидер оппозиции критикует действия министра. to Russian',
                 '81b' : "The leader of the opposition criticizes the minister's actions",
                 '82a' : 'Translate мнение нашей партии to Russian',
                 '82b' : 'the opinion of our party',
                 '83a' : 'Translate Я хочу голосовать против всех. to Russian',
                 '83b' : 'i want to vote against everyone',
                 '84a' : 'Translate По словам министра, войны не будет. to Russian',
                 '84b' : 'according to the minister, there will be no war',
                 '85a' : 'Translate Россия является самой большой по территории страной в мире to Russian',
                 '85b' : 'russia is the largest country in the world by territory',
                 '86a' : 'Translate выборы президента to Russian',
                 '86b' : 'presidential election',
                 '87a' : 'Translate По словам министра, законы у нас хорошие. to Russian',
                 '87b' : 'according to the minister, the laws we have are good',
                 '88a' : 'Translate У этой страны большая территория и маленькое население. to Russian',
                 '88b' : 'This country has a large territory and a small population',
                 '89a' : 'Translate решение президента to Russian',
                 '89b' : "president's decision",
                 '90a' : 'Translate Кто принимает законы в Германии? to Russian',
                 '90b' : 'who passes laws in germany',
                 '91a' : 'Translate Они всегда вместе принимают решения. to Russian',
                 '91b' : 'they always make decisions together',
                 '92a' : 'Translate Мы не голосовали на выборах в прошлом году. to Russian',
                 '92b' : "we didn't vote in an election last year",
                 '93a' : 'Translate По словам президента, сахар не станет дороже в этом году. to Russian',
                 '93b' : 'according to the president, sugar will not become more expensive this year',
                 '94a' : 'Translate Лидер оппозиции критикует действия министра. to Russian',
                 '94b' : 'the leader of the opposition criticizes the actions of the minister',
                 '95a' : 'Translate мнение нашей партии to Russian',
                 '95b' : 'the opinion of our party',
                 '96a' : 'Translate Россия является самой большой по территории страной в мире. to Russian',
                 '96b' : 'russia is the largest country in the world by territory',
                 '97a' : 'Translate громкий голос to Russian',
                 '97b' : 'a loud voice',
                 '98a' : 'What is the missing word? Где она видит _?',
                 '98b' : 'утку',
                 '99a' : 'Translate Моя сестра готовит рис и суп. to Russian',
                 '99b' : 'my sister is cooking rice and soup',
                 '100a' : 'Translate Ты идёшь или нет? to Russian',
                 '100b' : 'are you going or not',
                 '101a' : 'Translate Здесь можно жить? to Russian',
                 '101b' : 'can one live here',
                 '102a' : 'Translate Я ем салат и хлеб. to Russian',
                 '102b' : 'i am eating salad and bread',
                 '103a' : 'Translate Я хочу приготовить суп на обед. to Russian',
                 '103b' : 'i want to cook soup for lunch',
                 '104a' : 'Translate Нам надо помыть посуду. to Russian',
                 '104b' : 'We need to wash the dishes',
                 '105a' : 'Translate её младший брат to Russian',
                 '105b' : 'her younger brother',
                 '106a' : 'Translate У вас есть детская музыка? to Russian',
                 '106b' : "Do you have children's music?",
                 '107a' : 'Translate Мы готовим суши. to Russian',
                 '107b' : 'we are making sushi',
                 '108a' : 'Translate Можете помыть ножи и вилки? to Russian',
                 '108b' : 'can you wash the knives and forks',
                 '109a' : 'Translate Тарелка стоит далеко от меня. to Russian',
                 '109b' : 'the plate is far away from me',
                 '110a' : 'Translate хорошая неделя to Russian',
                 '110b' : 'a good week',
                 '111a' : 'Translate Мой брат любит и есть, и готовить. to Russian',
                 '111b' : 'my brother loves both to eat and to cook.',
                 '112a' : 'Translate Они любят есть на работе. to Russian',
                 '112b' : 'they love to eat at work',
                 '113a' : 'Translate Я хочу знать всё. to Russian',
                 '113b' : 'i want to know everything',
                 '114a' : 'Translate Я хочу собаку. to Russian',
                 '114b' : 'i want a dog',
                 '115a' : 'Translate Нет, музыка не громкая. to Russian',
                 '115b' : 'no, the music is not loud',
                 '116a' : 'Translate Пусть он готовит ужин. to Russian',
                 '116b' : 'let him cook dinner',
                 '117a' : 'Translate Я умею писать. to Russian',
                 '117b' : 'i know how to write',
                 '118a' : 'Translate Здесь можно жить? to Russian',
                 '118b' : 'can one live here',
                 '119a' : 'Translate Она хочет кофе. to Russian',
                 '119b' : 'she wants coffeee',
                 '120a' : 'Translate хороший композитор to Russian',
                 '120b' : 'a good composer',
                 '121a' : 'Translate Она читает всё. to Russian',
                 '121b' : 'she reads everything',
                 '122a' : 'Translate Мальчик, где твой старший брат? to Russian',
                 '122b' : 'boy, where is your older brother',
                 '123a' : 'Translate Что вы едите? to Russian',
                 '123b' : 'what are you eating',
                 '124a' : 'Translate Мы вас видим. to Russian',
                 '124b' : 'we see you',
                 '125a' : 'Translate Ты сейчас читаешь. to Russian',
                 '125b' : 'you are now reading'
                 }
    number = (random.randint(1, 125))
    answernum = (f'{number}b')
    questionnum = (f'{number}a')
    question = (questions.get(questionnum))
    answercorrect = (questions.get(answernum))
    answera="info"
    answerb="Your Result Will Be Here"
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if "iphone" in user_agent:
        return render_template('mobile/StudyLobbyRussian.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
    elif "android" in user_agent:
        return render_template('mobile/StudyLobbyRussian.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
    else:
        return render_template('StudyLobbyRussian.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
@views.route('/russian', methods=['POST'])
@login_required
def russianpost():
    questions = {'1a'  : 'Is this a vowel?: а',
                 '2a'   : 'Is this a vowel?: э',
                 '3a' : 'Is this a vowel?: ы',
                 '4a' : 'Is this a vowel?: у',
                 '5a'   : 'Is this a vowel?: о',
                 '6a'   : 'Is this a vowel?: я',
                 '7a' : 'Is this a vowel?: е',
                 '8a' : 'Is this a vowel?: ё',
                 '9a'   : 'Is this a vowel?: ю',
                 '10a'   : 'Is this a vowel?: и',
                 '11a'   : 'Is this a vowel?: б',
                 '12a' : 'Is this a vowel?: в',
                 '13a' : 'Is this a vowel?: г',
                 '14a'   : 'Is this a vowel?: д',
                 '15a'   : 'Is this a vowel?: ж',
                 '16a' : 'Is this a vowel?: з',
                 '17a' : 'Is this a vowel?: к',
                 '18a'   : 'Is this a vowel?: л',
                 '19a'   : 'Is this a vowel?: м',
                 '20a'   : 'Is this a vowel?: н',
                 '21a' : 'Is this a vowel?: п',
                 '22a' : 'Is this a vowel?: р',
                 '23a'   : 'Is this a vowel?: с',
                 '24a'   : 'Is this a vowel?: т',
                 '25a' : 'Is this a vowel?: ф',
                 '26a' : 'Is this a vowel?: х',
                 '27a'   : 'Is this a vowel?: ц',
                 '28a'   : 'Is this a vowel?: ч',
                 '29a'   : 'Is this a vowel?: ш',
                 '30a' : 'Is this a vowel?: щ',
                 '31a' : 'Is this a vowel?: й',
                 '32a'   : 'Is this a vowel?: ь',
                 '33a'   : 'Is this a vowel?: ъ',
                 '1b' : 'yes',
                 '2b' : 'yes',
                 '3b'   : 'yes',
                 '4b' : 'yes',
                 '5b' : 'yes',
                 '6b' : 'yes',
                 '7b'   : 'yes',
                 '8b' : 'yes',
                 '9b' : 'yes',
                 '10b' : 'yes',
                 '11b' : 'no',
                 '12b'   : 'no',
                 '13b' : 'no',
                 '14b' : 'no',
                 '15b' : 'no',
                 '16b'   : 'no',
                 '17b' : 'no',
                 '18b' : 'no',
                 '19b' : 'no',
                 '20b' : 'no',
                 '21b'   : 'no',
                 '22b' : 'no',
                 '23b' : 'no',
                 '24b' : 'no',
                 '25b'   : 'no',
                 '26b' : 'no',
                 '27b' : 'no',
                 '28b' : 'no',
                 '29b' : 'no',
                 '30b'   : 'no',
                 '31b' : 'no',
                 '32b' : 'no',
                 '33b' : 'no',
                 '34a' : 'What gender is a word that ends in a consonant? type both if your answer is both feminine and masculine.',
                 '34b' : 'masculine',
                 '35a' : 'What gender is a word that ends in й? type both if your answer is both feminine and masculine.',
                 '35b' : 'masculine',
                 '36a' : 'What gender is a word that ends in ь? type both if your answer is both feminine and masculine.',
                 '36b' : 'masculine',
                 '37a' : 'What gender is a word that ends in тель? type both if your answer is both feminine and masculine.',
                 '37b' : 'masculine',
                 '38a' : 'What gender is a word that ends in а? type both if your answer is both feminine and masculine.',
                 '38b' : 'feminine',
                 '39a' : 'What gender is a word that ends in я? type both if your answer is both feminine and masculine.',
                 '39b' : 'feminine',
                 '40a' : 'What gender is a word that ends in ия? type both if your answer is both feminine and masculine.',
                 '40b' : 'feminine',
                 '41a' : 'What gender is a word that ends in ь? type both if your answer is both feminine and masculine.',
                 '41b' : 'feminine',
                 '42a' : 'What gender is a word that ends in ость? type both if your answer is both feminine and masculine.',
                 '42b' : 'feminine',
                 '43a' : 'What gender is a word that ends in о? type both if your answer is both feminine and masculine.',
                 '43b' : 'neuter',
                 '44a' : 'What gender is a word that ends in е? type both if your answer is both feminine and masculine.',
                 '44b' : 'neuter',
                 '45a' : 'What gender is a word that ends in ие? type both if your answer is both feminine and masculine.',
                 '45b' : 'neuter',
                 '46a' : 'What gender is a word that ends in мя? type both if your answer is both feminine and masculine.',
                 '46b' : 'neuter',
                 '47a' : 'How do you convert a word ending with a consonant to plural?',
                 '47b' : 'add ы to the end',
                 '48a' : 'How do you convert a word ending with й to plural? (if the gender is masculine)',
                 '48b' : 'replace й with и',
                 '49a' : 'How do you convert a word ending with ь to plural? (if the gender is masculine)',
                 '49b' : 'replace ь with и',
                 '50a' : 'How do you convert a word ending with а to plural? (if the gender is masculine)',
                 '50b' : 'replace а with ы',
                 '51a' : 'How do you convert a word ending with я to plural? (if the gender is feminine)',
                 '51b' : 'replace я with и',
                 '52a' : 'How do you convert a word ending with ия to plural? (if the gender is feminine)',
                 '52b' : 'replace ия with ии',
                 '53a' : 'How do you convert a word ending with ь to plural? (if the gender is feminine)',
                 '53b' : 'replace ь with и',
                 '54a' : 'How do you convert a word ending with о to plural? (if the gender is feminine)',
                 '54b' : 'replace о with а',
                 '55a' : 'How do you convert a word ending with е to plural? (if the gender is neuter)',
                 '55b' : 'replace е with я',
                 '56a' : 'How do you convert a word ending with ие to plural? (if the gender is neuter)',
                 '56b' : 'replace ие with ия',
                 '57a' : 'How do you convert a word ending with мя to plural? (if the gender is neuter)',
                 '57b' : 'replace мя with ена',
                 '58a' : 'How do you convert a singular word ending in a consonant to the acusative singular form? (if the gender is masculine animate)',
                 '58b' : 'add а to the end',
                 '59a' : 'How do you convert a singular word ending in й to the acusative singular form? (if the gender is masculine animate)',
                 '59b' : 'replace й with я',
                 '60a' : 'How do you convert a singular word ending in ь to the acusative singular form? (if the gender is masculine animate)',
                 '60b' : 'replace ь with я',
                 '61a' : 'How do you convert a singular word to the acusative singular form? (if the gender is masculine inanimate)',
                 '61b' : 'it stays the same',
                 '62a' : 'How do you convert a singular word ending in а to the acusative singular form? (if the gender is feminine)',
                 '62b' : 'replace а with а',
                 '63a' : 'How do you convert a singular word ending in у to the acusative singular form? (if the gender is feminine)',
                 '63b' : 'replace у with я',
                 '64a' : 'How do you convert a singular word ending in ь to the acusative singular form? (if the gender is feminine)',
                 '64b' : 'replace ь with ь',
                 '65a' : 'How do you convert a singular word to the acusative singular form? (if the gender is neuter)',
                 '65b' : 'it stays the same',
                 '66a' : 'How do you convert a singular word ending in a consonant to the acusative plural form? (if the gender is masculine animate)',
                 '66b' : 'add ов to the end',
                 '67a' : 'How do you convert a singular word ending in й to the acusative plural form? (if the gender is masculine animate)',
                 '67b' : 'replace й mith ев',
                 '68a' : 'How do you convert a singular word to the acusative plural form? (if the gender is masculine animate)',
                 '68b' : 'replace ь with ей',
                 '69a' : 'How do you convert a singular word ending in а to the acusative plural form? (if the gender is masculine inanimate)',
                 '69b' : 'it stays the same',
                 '70a' : 'How do you convert a singular word ending in я to the acusative plural form? (if the gender is feminine animate)',
                 '70b' : 'replace а with nothing',
                 '71a' : 'How do you convert a singular word ending in ия to the acusative plural form? (if the gender is feminine animate)',
                 '71b' : 'replace я with ь',
                 '72a' : 'How do you convert a singular word ending in ь to the acusative plural form? (if the gender is feminine animate)',
                 '72b' : 'replace ия with ий',
                 '73a' : 'How do you convert a singular word to the acusative plural form? (if the gender is feminine animate)',
                 '73b' : 'replace ь with ей',
                 '74a' : 'How do you convert a singular word to the acusative plural form? (if the gender is feminine inanimate)',
                 '74b' : 'it stays the same',
                 '75a' : 'How do you convert a singular word to the acusative plural form? (if the gender is neuter)',
                 '75b' : 'it stays the same',
                 '76a' : 'Translate с помощью мамы to English',
                 '76b' : "with mom's help",
                 '77a' : 'Translate По словам президента, сахар не станет дороже в этом году. to Russian',
                 '77b' : 'according to the president, sugar will not become more expensive this year',
                 '78a' : 'Translate лидер оппозиции to English',
                 '78b' : 'opposition leader',
                 '79a' : 'Translate Сколько партий участвовало в выборах? to English',
                 '79b' : 'how many parties participated in the elections',
                 '80a' : 'Translate Парламент принимает законы. to Russian',
                 '80b' : 'the parliment passes laws',
                 '81a' : 'Translate Лидер оппозиции критикует действия министра. to Russian',
                 '81b' : "The leader of the opposition criticizes the minister's actions",
                 '82a' : 'Translate мнение нашей партии to Russian',
                 '82b' : 'the opinion of our party',
                 '83a' : 'Translate Я хочу голосовать против всех. to Russian',
                 '83b' : 'i want to vote against everyone',
                 '84a' : 'Translate По словам министра, войны не будет. to Russian',
                 '84b' : 'according to the minister, there will be no war',
                 '85a' : 'Translate Россия является самой большой по территории страной в мире to Russian',
                 '85b' : 'russia is the largest country in the world by territory',
                 '86a' : 'Translate выборы президента to Russian',
                 '86b' : 'presidential election',
                 '87a' : 'Translate По словам министра, законы у нас хорошие. to Russian',
                 '87b' : 'according to the minister, the laws we have are good',
                 '88a' : 'Translate У этой страны большая территория и маленькое население. to Russian',
                 '88b' : 'This country has a large territory and a small population',
                 '89a' : 'Translate решение президента to Russian',
                 '89b' : "president's decision",
                 '90a' : 'Translate Кто принимает законы в Германии? to Russian',
                 '90b' : 'who passes laws in germany',
                 '91a' : 'Translate Они всегда вместе принимают решения. to Russian',
                 '91b' : 'they always make decisions together',
                 '92a' : 'Translate Мы не голосовали на выборах в прошлом году. to Russian',
                 '92b' : "we didn't vote in an election last year",
                 '93a' : 'Translate По словам президента, сахар не станет дороже в этом году. to Russian',
                 '93b' : 'according to the president, sugar will not become more expensive this year',
                 '94a' : 'Translate Лидер оппозиции критикует действия министра. to Russian',
                 '94b' : 'the leader of the opposition criticizes the actions of the minister',
                 '95a' : 'Translate мнение нашей партии to Russian',
                 '95b' : 'the opinion of our party',
                 '96a' : 'Translate Россия является самой большой по территории страной в мире. to Russian',
                 '96b' : 'russia is the largest country in the world by territory',
                 '97a' : 'Translate громкий голос to Russian',
                 '97b' : 'a loud voice',
                 '98a' : 'What is the missing word? Где она видит _?',
                 '98b' : 'утку',
                 '99a' : 'Translate Моя сестра готовит рис и суп. to Russian',
                 '99b' : 'my sister is cooking rice and soup',
                 '100a' : 'Translate Ты идёшь или нет? to Russian',
                 '100b' : 'are you going or not',
                 '101a' : 'Translate Здесь можно жить? to Russian',
                 '101b' : 'can one live here',
                 '102a' : 'Translate Я ем салат и хлеб. to Russian',
                 '102b' : 'i am eating salad and bread',
                 '103a' : 'Translate Я хочу приготовить суп на обед. to Russian',
                 '103b' : 'i want to cook soup for lunch',
                 '104a' : 'Translate Нам надо помыть посуду. to Russian',
                 '104b' : 'We need to wash the dishes',
                 '105a' : 'Translate её младший брат to Russian',
                 '105b' : 'her younger brother',
                 '106a' : 'Translate У вас есть детская музыка? to Russian',
                 '106b' : "Do you have children's music?",
                 '107a' : 'Translate Мы готовим суши. to Russian',
                 '107b' : 'we are making sushi',
                 '108a' : 'Translate Можете помыть ножи и вилки? to Russian',
                 '108b' : 'can you wash the knives and forks',
                 '109a' : 'Translate Тарелка стоит далеко от меня. to Russian',
                 '109b' : 'the plate is far away from me',
                 '110a' : 'Translate хорошая неделя to Russian',
                 '110b' : 'a good week',
                 '111a' : 'Translate Мой брат любит и есть, и готовить. to Russian',
                 '111b' : 'my brother loves both to eat and to cook.',
                 '112a' : 'Translate Они любят есть на работе. to Russian',
                 '112b' : 'they love to eat at work',
                 '113a' : 'Translate Я хочу знать всё. to Russian',
                 '113b' : 'i want to know everything',
                 '114a' : 'Translate Я хочу собаку. to Russian',
                 '114b' : 'i want a dog',
                 '115a' : 'Translate Нет, музыка не громкая. to Russian',
                 '115b' : 'no, the music is not loud',
                 '116a' : 'Translate Пусть он готовит ужин. to Russian',
                 '116b' : 'let him cook dinner',
                 '117a' : 'Translate Я умею писать. to Russian',
                 '117b' : 'i know how to write',
                 '118a' : 'Translate Здесь можно жить? to Russian',
                 '118b' : 'can one live here',
                 '119a' : 'Translate Она хочет кофе. to Russian',
                 '119b' : 'she wants coffeee',
                 '120a' : 'Translate хороший композитор to Russian',
                 '120b' : 'a good composer',
                 '121a' : 'Translate Она читает всё. to Russian',
                 '121b' : 'she reads everything',
                 '122a' : 'Translate Мальчик, где твой старший брат? to Russian',
                 '122b' : 'boy, where is your older brother',
                 '123a' : 'Translate Что вы едите? to Russian',
                 '123b' : 'what are you eating',
                 '124a' : 'Translate Мы вас видим. to Russian',
                 '124b' : 'we see you',
                 '125a' : 'Translate Ты сейчас читаешь. to Russian',
                 '125b' : 'you are now reading'}
    answercorrect=aesEcbDecryptFromBase64(decryptionKey, request.form['answer1'])
    answer=request.form['answer']
    answer1=answercorrect
    if answer == answercorrect:
        if current_user.is_authenticated:
            number = (random.randint(1, 5))
            answernum = (f'{number}b')
            questionnum = (f'{number}a')
            question = (questions.get(questionnum))
            answercorrect = (questions.get(answernum))
            answera="success"
            answerb="Correct!"
            f = open('mysite/website/static/leaderboard.txt', 'r')
            for line in f:
                wr = open('mysite/website/static/leaderboard.txt', 'a')
                if line.startswith("{'"+current_user.first_name+"'"+": "):
                    line1=line
                    line.replace("}", "")
                    replacestr="{'"+current_user.first_name+"': "
                    line=line.replace(replacestr, "")
                    line=line.replace("}","")
                    line=int(line)
                    line=line+random.randint(10, 15)
                    line="{'"+current_user.first_name+"': "+str(line)+"}"
                    with open('mysite/website/static/leaderboard.txt', 'r') as file :
                      filedata = file.read()
                    filedata = filedata.replace(line1, line+"\n")
                    with open('mysite/website/static/leaderboard.txt', 'w') as file:
                      file.write(filedata)
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            else:
                return render_template('StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
        else:
            number = (random.randint(1, 5))
            answernum = (f'{number}b')
            questionnum = (f'{number}a')
            question = (questions.get(questionnum))
            answercorrect = (questions.get(answernum))
            answera="success"
            answerb="Correct!"
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            else:
                return render_template('StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
    else:
        number = (random.randint(1, 5))
        answernum = (f'{number}b')
        questionnum = (f'{number}a')
        question = (questions.get(questionnum))
        answercorrect = (questions.get(answernum))
        answera="danger"
        answerb=f"Incorrect, The correct answer was {answer1}"
        user_agent = request.headers.get('User-Agent')
        user_agent = user_agent.lower()
        if "iphone" in user_agent:
            return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
        elif "android" in user_agent:
            return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
        else:
            return render_template('StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
@views.route('/math')
@login_required
def mathstudylobby():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if "iphone" in user_agent:
        return render_template('mobile/StudyLobbyMath.html')
    elif "android" in user_agent:
        return render_template('mobile/StudyLobbyMath.html')
    else:
        return render_template('StudyLobbyMath.html')
@views.route('/math', methods=['POST'])
@login_required
def mathstudylobby1():
    status = request.form['status']
    if status == "1st":
        return redirect("https://studylobby.pythonanywhere.com/1/math")
    if status == "2nd":
        return redirect("https://studylobby.pythonanywhere.com/2/math")
    if status == "3rd":
        return redirect("https://studylobby.pythonanywhere.com/3/math")
    if status == "4th":
        return redirect("https://studylobby.pythonanywhere.com/4/math")
    if status == "5th":
        return redirect("https://studylobby.pythonanywhere.com/5/math")
    if status == "6th":
        return redirect("https://studylobby.pythonanywhere.com/6/math")
    if status == "7th":
        return redirect("https://studylobby.pythonanywhere.com/7/math")
    if status == "8th":
        return redirect("https://studylobby.pythonanywhere.com/8/math")
    if status == "9th":
        return redirect("https://studylobby.pythonanywhere.com/9/math")
    if status == "10th":
        return redirect("https://studylobby.pythonanywhere.com/10/math")
    if status == "11th":
        return redirect("https://studylobby.pythonanywhere.com/11/math")
    if status == "12th":
        return redirect("https://studylobby.pythonanywhere.com/12/math")
@views.route('/ela')
@login_required
def elastudylobby():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if "iphone" in user_agent:
        return render_template('mobile/StudyLobbyMath.html')
    elif "android" in user_agent:
        return render_template('mobile/StudyLobbyMath.html')
    else:
        return render_template('StudyLobbyMath.html')
@views.route('/ela', methods=['POST'])
@login_required
def elastudylobby1():
    status = request.form['status']
    if status == "1st":
        return redirect("https://studylobby.pythonanywhere.com/1/ela")
    if status == "2nd":
        return redirect("https://studylobby.pythonanywhere.com/2/ela")
    if status == "3rd":
        return redirect("https://studylobby.pythonanywhere.com/3/ela")
    if status == "4th":
        return redirect("https://studylobby.pythonanywhere.com/4/ela")
    if status == "5th":
        return redirect("https://studylobby.pythonanywhere.com/5/ela")
    if status == "6th":
        return redirect("https://studylobby.pythonanywhere.com/6/ela")
    if status == "7th":
        return redirect("https://studylobby.pythonanywhere.com/7/ela")
    if status == "8th":
        return redirect("https://studylobby.pythonanywhere.com/8/ela")
    if status == "9th":
        return redirect("https://studylobby.pythonanywhere.com/9/ela")
    if status == "10th":
        return redirect("https://studylobby.pythonanywhere.com/10/ela")
    if status == "11th":
        return redirect("https://studylobby.pythonanywhere.com/11/ela")
    if status == "12th":
        return redirect("https://studylobby.pythonanywhere.com/12/ela")
@views.route('/history')
@login_required
def historystudylobby():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if "iphone" in user_agent:
        return render_template('mobile/StudyLobbyMath.html')
    elif "android" in user_agent:
        return render_template('mobile/StudyLobbyMath.html')
    else:
        return render_template('StudyLobbyMath.html')
@views.route('/history', methods=['POST'])
@login_required
def historystudylobby1():
    status = request.form['status']
    if status == "1st":
        return redirect("https://studylobby.pythonanywhere.com/1/history")
    if status == "2nd":
        return redirect("https://studylobby.pythonanywhere.com/2/history")
    if status == "3rd":
        return redirect("https://studylobby.pythonanywhere.com/3/history")
    if status == "4th":
        return redirect("https://studylobby.pythonanywhere.com/4/history")
    if status == "5th":
        return redirect("https://studylobby.pythonanywhere.com/5/history")
    if status == "6th":
        return redirect("https://studylobby.pythonanywhere.com/6/history")
    if status == "7th":
        return redirect("https://studylobby.pythonanywhere.com/7/history")
    if status == "8th":
        return redirect("https://studylobby.pythonanywhere.com/8/history")
    if status == "9th":
        return redirect("https://studylobby.pythonanywhere.com/9/history")
    if status == "10th":
        return redirect("https://studylobby.pythonanywhere.com/10/history")
    if status == "11th":
        return redirect("https://studylobby.pythonanywhere.com/11/history")
    if status == "12th":
        return redirect("https://studylobby.pythonanywhere.com/12/history")
@views.route('/science')
@login_required
def sciencestudylobby():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if "iphone" in user_agent:
        return render_template('mobile/StudyLobbyMath.html')
    elif "android" in user_agent:
        return render_template('mobile/StudyLobbyMath.html')
    else:
        return render_template('StudyLobbyMath.html')
@views.route('/science', methods=['POST'])
@login_required
def sciencestudylobby1():
    status = request.form['status']
    if status == "1st":
        return redirect("https://studylobby.pythonanywhere.com/1/science")
    if status == "2nd":
        return redirect("https://studylobby.pythonanywhere.com/2/science")
    if status == "3rd":
        return redirect("https://studylobby.pythonanywhere.com/3/science")
    if status == "4th":
        return redirect("https://studylobby.pythonanywhere.com/4/science")
    if status == "5th":
        return redirect("https://studylobby.pythonanywhere.com/5/science")
    if status == "6th":
        return redirect("https://studylobby.pythonanywhere.com/6/science")
    if status == "7th":
        return redirect("https://studylobby.pythonanywhere.com/7/science")
    if status == "8th":
        return redirect("https://studylobby.pythonanywhere.com/8/science")
    if status == "9th":
        return redirect("https://studylobby.pythonanywhere.com/9/science")
    if status == "10th":
        return redirect("https://studylobby.pythonanywhere.com/10/science")
    if status == "11th":
        return redirect("https://studylobby.pythonanywhere.com/11/science")
    if status == "12th":
        return redirect("https://studylobby.pythonanywhere.com/12/science")
@views.route('/1/ela')
@login_required
def studylobbyela1():
  user_agent = request.headers.get('User-Agent')
  user_agent = user_agent.lower()
  if "iphone" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  elif "android" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  else:
      return render_template('StudyLobbyComingSoon.html')
@views.route('/2/ela')
@login_required
def studylobbyela2():
  user_agent = request.headers.get('User-Agent')
  user_agent = user_agent.lower()
  if "iphone" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  elif "android" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  else:
      return render_template('StudyLobbyComingSoon.html')
@views.route('/3/ela')
@login_required
def studylobbyela3():
  user_agent = request.headers.get('User-Agent')
  user_agent = user_agent.lower()
  if "iphone" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  elif "android" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  else:
      return render_template('StudyLobbyComingSoon.html')
@views.route('/4/ela')
@login_required
def studylobbyela4():
  user_agent = request.headers.get('User-Agent')
  user_agent = user_agent.lower()
  if "iphone" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  elif "android" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  else:
      return render_template('StudyLobbyComingSoon.html')
@views.route('/5/ela')
@login_required
def studylobbyela5():
  user_agent = request.headers.get('User-Agent')
  user_agent = user_agent.lower()
  if "iphone" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  elif "android" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  else:
      return render_template('StudyLobbyComingSoon.html')
@views.route('/6/ela')
@login_required
def studylobbyela6():
  user_agent = request.headers.get('User-Agent')
  user_agent = user_agent.lower()
  if "iphone" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  elif "android" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  else:
      return render_template('StudyLobbyComingSoon.html')
@views.route('/7/ela')
@login_required
def studylobbyela7():
  user_agent = request.headers.get('User-Agent')
  user_agent = user_agent.lower()
  if "iphone" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  elif "android" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  else:
      return render_template('StudyLobbyComingSoon.html')
@views.route('/8/ela')
@login_required
def studylobbyela8():
  user_agent = request.headers.get('User-Agent')
  user_agent = user_agent.lower()
  if "iphone" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  elif "android" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  else:
      return render_template('StudyLobbyComingSoon.html')
@views.route('/9/ela')
@login_required
def studylobbyela9():
  user_agent = request.headers.get('User-Agent')
  user_agent = user_agent.lower()
  if "iphone" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  elif "android" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  else:
      return render_template('StudyLobbyComingSoon.html')
@views.route('/10/ela')
@login_required
def studylobbyela10():
  user_agent = request.headers.get('User-Agent')
  user_agent = user_agent.lower()
  if "iphone" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  elif "android" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  else:
      return render_template('StudyLobbyComingSoon.html')
@views.route('/11/ela')
@login_required
def studylobbyela11():
  user_agent = request.headers.get('User-Agent')
  user_agent = user_agent.lower()
  if "iphone" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  elif "android" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  else:
      return render_template('StudyLobbyComingSoon.html')
@views.route('/12/ela')
@login_required
def studylobbyela12():
  user_agent = request.headers.get('User-Agent')
  user_agent = user_agent.lower()
  if "iphone" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  elif "android" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  else:
      return render_template('StudyLobbyComingSoon.html')
@views.route('/1/science')
@login_required
def studylobbyscience1():
  user_agent = request.headers.get('User-Agent')
  user_agent = user_agent.lower()
  if "iphone" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  elif "android" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  else:
      return render_template('StudyLobbyComingSoon.html')
@views.route('/2/science')
@login_required
def studylobbyscience2():
  user_agent = request.headers.get('User-Agent')
  user_agent = user_agent.lower()
  if "iphone" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  elif "android" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  else:
      return render_template('StudyLobbyComingSoon.html')
@views.route('/3/science')
@login_required
def studylobbyscience3():
  user_agent = request.headers.get('User-Agent')
  user_agent = user_agent.lower()
  if "iphone" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  elif "android" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  else:
      return render_template('StudyLobbyComingSoon.html')
@views.route('/4/science')
@login_required
def studylobbyscience4():
  user_agent = request.headers.get('User-Agent')
  user_agent = user_agent.lower()
  if "iphone" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  elif "android" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  else:
      return render_template('StudyLobbyComingSoon.html')
@views.route('/5/science')
@login_required
def studylobbyscience5():
  user_agent = request.headers.get('User-Agent')
  user_agent = user_agent.lower()
  if "iphone" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  elif "android" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  else:
      return render_template('StudyLobbyComingSoon.html')
@views.route('/6/science')
@login_required
def studylobbyscience6():
  user_agent = request.headers.get('User-Agent')
  user_agent = user_agent.lower()
  if "iphone" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  elif "android" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  else:
      return render_template('StudyLobbyComingSoon.html')
@views.route('/7/science')
@login_required
def studylobbyscience7():
  user_agent = request.headers.get('User-Agent')
  user_agent = user_agent.lower()
  if "iphone" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  elif "android" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  else:
      return render_template('StudyLobbyComingSoon.html')
@views.route('/8/science')
@login_required
def studylobbyscience8():
  user_agent = request.headers.get('User-Agent')
  user_agent = user_agent.lower()
  if "iphone" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  elif "android" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  else:
      return render_template('StudyLobbyComingSoon.html')
@views.route('/9/science')
@login_required
def studylobbyscience9():
  user_agent = request.headers.get('User-Agent')
  user_agent = user_agent.lower()
  if "iphone" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  elif "android" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  else:
      return render_template('StudyLobbyComingSoon.html')
@views.route('/10/science')
@login_required
def studylobbyscience10():
  user_agent = request.headers.get('User-Agent')
  user_agent = user_agent.lower()
  if "iphone" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  elif "android" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  else:
      return render_template('StudyLobbyComingSoon.html')
@views.route('/11/science')
@login_required
def studylobbyscience11():
  user_agent = request.headers.get('User-Agent')
  user_agent = user_agent.lower()
  if "iphone" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  elif "android" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  else:
      return render_template('StudyLobbyComingSoon.html')
@views.route('/12/science')
@login_required
def studylobbyscience12():
  user_agent = request.headers.get('User-Agent')
  user_agent = user_agent.lower()
  if "iphone" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  elif "android" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  else:
      return render_template('StudyLobbyComingSoon.html')
@views.route('/1/history')
@login_required
def studylobbyhistory1():
  user_agent = request.headers.get('User-Agent')
  user_agent = user_agent.lower()
  if "iphone" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  elif "android" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  else:
      return render_template('StudyLobbyComingSoon.html')
@views.route('/2/history')
@login_required
def studylobbyhistory2():
  user_agent = request.headers.get('User-Agent')
  user_agent = user_agent.lower()
  if "iphone" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  elif "android" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  else:
      return render_template('StudyLobbyComingSoon.html')
@views.route('/3/history')
@login_required
def studylobbyhistory3():
  user_agent = request.headers.get('User-Agent')
  user_agent = user_agent.lower()
  if "iphone" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  elif "android" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  else:
      return render_template('StudyLobbyComingSoon.html')
@views.route('/4/history')
@login_required
def studylobbyhistory4():
  user_agent = request.headers.get('User-Agent')
  user_agent = user_agent.lower()
  if "iphone" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  elif "android" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  else:
      return render_template('StudyLobbyComingSoon.html')
@views.route('/5/history')
@login_required
def studylobbyhistory5():
  user_agent = request.headers.get('User-Agent')
  user_agent = user_agent.lower()
  if "iphone" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  elif "android" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  else:
      return render_template('StudyLobbyComingSoon.html')
@views.route('/6/history')
@login_required
def studylobbyhistory6():
  user_agent = request.headers.get('User-Agent')
  user_agent = user_agent.lower()
  if "iphone" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  elif "android" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  else:
      return render_template('StudyLobbyComingSoon.html')
@views.route('/7/history')
@login_required
def studylobbyhistory7():
  user_agent = request.headers.get('User-Agent')
  user_agent = user_agent.lower()
  if "iphone" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  elif "android" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  else:
      return render_template('StudyLobbyComingSoon.html')
@views.route('/8/history')
@login_required
def studylobbyhistory8():
  user_agent = request.headers.get('User-Agent')
  user_agent = user_agent.lower()
  if "iphone" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  elif "android" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  else:
      return render_template('StudyLobbyComingSoon.html')
@views.route('/9/history')
@login_required
def studylobbyhistory9():
  user_agent = request.headers.get('User-Agent')
  user_agent = user_agent.lower()
  if "iphone" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  elif "android" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  else:
      return render_template('StudyLobbyComingSoon.html')
@views.route('/10/history')
@login_required
def studylobbyhistory10():
  user_agent = request.headers.get('User-Agent')
  user_agent = user_agent.lower()
  if "iphone" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  elif "android" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  else:
      return render_template('StudyLobbyComingSoon.html')
@views.route('/11/history')
@login_required
def studylobbyhistory11():
  user_agent = request.headers.get('User-Agent')
  user_agent = user_agent.lower()
  if "iphone" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  elif "android" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  else:
      return render_template('StudyLobbyComingSoon.html')
@views.route('/12/history')
@login_required
def studylobbyhistory12():
  user_agent = request.headers.get('User-Agent')
  user_agent = user_agent.lower()
  if "iphone" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  elif "android" in user_agent:
      return render_template('mobile/StudyLobbyComingSoon.html')
  else:
      return render_template('StudyLobbyComingSoon.html')
@views.route('/chatbot')
@login_required
def chatbotstudylobby():
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if "iphone" in user_agent:
        return render_template('mobile/StudyLobbyChatbot.html')
    elif "android" in user_agent:
        return render_template('mobile/StudyLobbyChatbot.html')
    else:
        return render_template('StudyLobbyChatbot.html')
    'return render_template("StudyLobbyChatbot.html", list_chat=list1)'
'''
@views.route('/chatbot', methods=['POST'])
def chatbotstudylobby1():
    text = request.form['search']
    list1.append(text)
    if len(list1) > 9:
      del list1[0]
    response = chatbot.get_response(text)
    list1.append(response)
    if len(list1) > 9:
      del list1[0]
    return render_template("StudyLobbyChatbot.html", list_chat=list1)
'''
@views.route('/changelogs')
@login_required
def changelogs():
    changeloglist=[
        "October 20, 2022 (12:56 PM):Added the leaderboard button to the navbar",
        "October 20, 2022 (7:32 PM): Fixed the X button on certain pages and fixed the submit button on 7th grade Math from sending you to the Tutoring page.",
        "October 20, 2022 (11:46 PM): Added Math Lessons for 9th, 10th, and 11th graders.",
        "October 21, 2022 (7:32 PM): Removed the X button on every page as the Navbar proved to be more effective",
        "October 21, 2022 (6:47 PM): Updated the NavBar so that it has a title above every icon.",
        "October 21, 2022 (7:04 PM): Fixed lessons not giving xp",
        "October 21, 2022 (7:06 PM): Fixed Infinite XP glitch",
        "October 21, 2022 (7:10 PM): Prevented Resubmition request upon lesson refresh",
        "October 21, 2022 (7:24 PM): Fixed NavBar on Mobile Devices",
        "October 21, 2022 (7:32 PM): Prevented NavBar from overlapping other elements",
        "October 21, 2022 (8:44 PM): Changed fonts on lesson selection to Open Sans SemiBold.",
        "October 21, 2022 (11:23 PM): Added Math Lessons for 1st, 2nd, 3rd, 4th, 5th, 6th, 7th, 8th, and 12th graders.",
        "October 22, 2022 (12:04 PM): Fixed drawing section on lessons overlapping other elements for both web and mobile.",
        'October 22, 2022 (12:07 PM): Fixed the message "Repl waking up" on Chatbot.',
        'October 22, 2022 (4:01 PM): Add Russian lessons.',
        'October 22, 2022 (5:59 PM): Added a home button to every page in the NavBar.',
        'October 22, 2022 (6:20 PM): Added achievements to the homepage',
        'October 22, 2022 (6:50 PM): Fixed items on the navbar being too big for some users',
        'October 23, 2022 (12:11 PM): Added signout, login, and sign up buttons to the homepage',
        'October 23, 2022 (12:49 PM): Fixed the navbar in the leaderboard page for mobile',
        'October 23, 2022 (1:06 PM): Added a scrollbar to the leaderboards page for both web and mobile',
        'October 23, 2022 (2:19 PM): Added a terms of service and privacy policy page onto the login and signup pages. Alse added an option to login with google.',
        'October 23, 2022 (6:21 PM): Added a cookie policy page to the login and signup page along with a cookie policy banner.',
        'October 23, 2022 (7:59 PM): Encoded and decoded the answers to lessons. This prevents users from cheating.',
        'October 23, 2022 (3:48 PM): Moved completed achivements to the bottom of the achievements board.',
        'October 23, 2022 (5:04 PM): Made logging in madatory in order to use the site. This is for the safety for this site and our staff.',
        'October 23, 2022 (5:37 PM): Fixed the button to Tower2Defense in Minigames.',
        "October 23, 2022 (5:59 PM): Added a feature where when you create an account with google, you will be able to choose a password. This prevents users from not knowing their passwords when they aren't logging in with google.",
        "October 23, 2022 (7:57 PM): Changed the chatbot to coming soon. This is due to the low efficiency of the chatbot."
        ]
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if "iphone" in user_agent:
        return render_template('mobile/changelogs.html', changelogs=changeloglist)
    elif "android" in user_agent:
        return render_template('mobile/changelogs.html', changelogs=changeloglist)
    else:
        return render_template('changelogs.html', changelogs=changeloglist)
@views.route('/11/math')
@login_required
def studylobbymath11():
    questions = {'1a'  : 'Factor 3x²+10x-8',
                 '2a'   : 'simplify 5^1/3×7^4/3',
                 '3a' : 'You buy a used truck for $17,000. It depricates at the rate of 19% per year. Find the value of the truck for 1 year.',
                 '4a' : 'P(x≤96) Find the indicated probability for X',
                 '5a'   : 'P(x≤106)',
                 '1b' : '(3x-2)(x+4)',
                 '2b' : '7 ⁵⁄₃',
                 '3b'   : '13,177',
                 '4b' : '98.21',
                 '5b'  : '99.9' }
    number = (random.randint(1, 5))
    answernum = (f'{number}b')
    questionnum = (f'{number}a')
    question = (questions.get(questionnum))
    answercorrect = (questions.get(answernum))
    answera="info"
    answerb="Your Result Will Be Here"
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if "iphone" in user_agent:
        return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
    elif "android" in user_agent:
        return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
    else:
        return render_template('StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
@views.route('/11/math', methods=['POST'])
@login_required
def studylobbymath11post():
    questions = {'1a'  : 'Factor 3x²+10x-8',
                 '2a'   : 'simplify 5^1/3×7^4/3',
                 '3a' : 'You buy a used truck for $17,000. It depricates at the rate of 19% per year. Find the value of the truck for 1 year.',
                 '4a' : 'P(x≤96) Find the indicated probability for X',
                 '5a'   : 'P(x≤106)',
                 '1b' : '(3x-2)(x+4)',
                 '2b' : '7 ⁵⁄₃',
                 '3b'   : '13,177',
                 '4b' : '98.21',
                 '5b'  : '99.9' }
    answercorrect=aesEcbDecryptFromBase64(decryptionKey, request.form['answer1'])
    answer=request.form['answer']
    answer1=answercorrect
    if answer == answercorrect:
        if current_user.is_authenticated:
            number = (random.randint(1, 5))
            answernum = (f'{number}b')
            questionnum = (f'{number}a')
            question = (questions.get(questionnum))
            answercorrect = (questions.get(answernum))
            answera="success"
            answerb="Correct!"
            f = open('mysite/website/static/leaderboard.txt', 'r')
            for line in f:
                wr = open('mysite/website/static/leaderboard.txt', 'a')
                if line.startswith("{'"+current_user.first_name+"'"+": "):
                    line1=line
                    line.replace("}", "")
                    replacestr="{'"+current_user.first_name+"': "
                    line=line.replace(replacestr, "")
                    line=line.replace("}","")
                    line=int(line)
                    line=line+random.randint(10, 15)
                    line="{'"+current_user.first_name+"': "+str(line)+"}"
                    with open('mysite/website/static/leaderboard.txt', 'r') as file :
                      filedata = file.read()
                    filedata = filedata.replace(line1, line+"\n")
                    with open('mysite/website/static/leaderboard.txt', 'w') as file:
                      file.write(filedata)
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            else:
                return render_template('StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
        else:
            number = (random.randint(1, 5))
            answernum = (f'{number}b')
            questionnum = (f'{number}a')
            question = (questions.get(questionnum))
            answercorrect = (questions.get(answernum))
            answera="success"
            answerb="Correct!"
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            else:
                return render_template('StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
    else:
        number = (random.randint(1, 5))
        answernum = (f'{number}b')
        questionnum = (f'{number}a')
        question = (questions.get(questionnum))
        answercorrect = (questions.get(answernum))
        answera="danger"
        answerb=f"Incorrect, The correct answer was {answer1}"
        user_agent = request.headers.get('User-Agent')
        user_agent = user_agent.lower()
        if "iphone" in user_agent:
            return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
        elif "android" in user_agent:
            return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
        else:
            return render_template('StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
@views.route('/8/math')
@login_required
def studylobbymath8():
    questions = {'1a'  : '2x-4 | x=-2',
                 '2a'   : '-10+2.5y | y=2',
                 '3a' : '-24÷6×3',
                 '4a' : '6+15÷3×2-5²',
                 '5a'   : '-3+2.5y | y=0.2',
                 '1b' : '-8',
                 '2b' : '-5',
                 '3b'   : '-12',
                 '4b' : '-9',
                 '5b'  : '-2.5' }
    number = (random.randint(1, 5))
    answernum = (f'{number}b')
    questionnum = (f'{number}a')
    question = (questions.get(questionnum))
    answercorrect = (questions.get(answernum))
    answera="info"
    answerb="Your Result Will Be Here"
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if "iphone" in user_agent:
        return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
    elif "android" in user_agent:
        return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
    else:
        return render_template('StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
@views.route('/8/math', methods=['POST'])
@login_required
def studylobbymath8post():
    questions = {'1a'  : '2x-4 | x=-2',
                 '2a'   : '-10+2.5y | y=2',
                 '3a' : '-24÷6×3',
                 '4a' : '6+15÷3×2-5²',
                 '5a'   : '-3+2.5y | y=0.2',
                 '1b' : '-8',
                 '2b' : '-5',
                 '3b'   : '-12',
                 '4b' : '-9',
                 '5b'  : '-2.5' }
    answercorrect=aesEcbDecryptFromBase64(decryptionKey, request.form['answer1'])
    answer=request.form['answer']
    answer1=answercorrect
    if answer == answercorrect:
        if current_user.is_authenticated:
            number = (random.randint(1, 5))
            answernum = (f'{number}b')
            questionnum = (f'{number}a')
            question = (questions.get(questionnum))
            answercorrect = (questions.get(answernum))
            answera="success"
            answerb="Correct!"
            f = open('mysite/website/static/leaderboard.txt', 'r')
            for line in f:
                wr = open('mysite/website/static/leaderboard.txt', 'a')
                if line.startswith("{'"+current_user.first_name+"'"+": "):
                    line1=line
                    line.replace("}", "")
                    replacestr="{'"+current_user.first_name+"': "
                    line=line.replace(replacestr, "")
                    line=line.replace("}","")
                    line=int(line)
                    line=line+random.randint(10, 15)
                    line="{'"+current_user.first_name+"': "+str(line)+"}"
                    with open('mysite/website/static/leaderboard.txt', 'r') as file :
                      filedata = file.read()
                    filedata = filedata.replace(line1, line+"\n")
                    with open('mysite/website/static/leaderboard.txt', 'w') as file:
                      file.write(filedata)
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            else:
                return render_template('StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
        else:
            number = (random.randint(1, 5))
            answernum = (f'{number}b')
            questionnum = (f'{number}a')
            question = (questions.get(questionnum))
            answercorrect = (questions.get(answernum))
            answera="success"
            answerb="Correct!"
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            else:
                return render_template('StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
    else:
        number = (random.randint(1, 5))
        answernum = (f'{number}b')
        questionnum = (f'{number}a')
        question = (questions.get(questionnum))
        answercorrect = (questions.get(answernum))
        answera="danger"
        answerb=f"Incorrect, The correct answer was {answer1}"
        user_agent = request.headers.get('User-Agent')
        user_agent = user_agent.lower()
        if "iphone" in user_agent:
            return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
        elif "android" in user_agent:
            return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
        else:
            return render_template('StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
@views.route('/10/math')
@login_required
def studylobbymath10():
    questions = {'1a'  : 'If m∠ABD=48° and m∠DBC=78°, find m∠ABC.',
                 '2a'   : 'If m∠DBC = 74° and m∠ABC=197°, find m∠ABD.',
                 '3a' : 'If m∠DEF = (7x+4)°, m∠DEG=(5x+11)°, and m∠GEF=23°, find x',
                 '4a' : 'If m∠JKM=43°, m∠MKL=(8x-20)°, and m∠JKL=(10x-11)°, find x',
                 '5a'   : 'If ∠DEF is a straight angle, m∠DEG=(23x-3)°, and m∠GEF=(12x+8)°, find x',
                 '1b' : '126',
                 '2b' : '45',
                 '3b'   : '10',
                 '4b' : '17',
                 '5b'  : '5' }
    number = (random.randint(1, 5))
    answernum = (f'{number}b')
    questionnum = (f'{number}a')
    question = (questions.get(questionnum))
    answercorrect = (questions.get(answernum))
    answera="info"
    answerb="Your Result Will Be Here"
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if "iphone" in user_agent:
        return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
    elif "android" in user_agent:
        return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
    else:
        return render_template('StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
@views.route('/10/math', methods=['POST'])
@login_required
def studylobbymath10post():
    questions = {'1a'  : 'If m∠ABD=48° and m∠DBC=78°, find m∠ABC.',
                 '2a'   : 'If m∠DBC = 74° and m∠ABC=197°, find m∠ABD.',
                 '3a' : 'If m∠DEF = (7x+4)°, m∠DEG=(5x+11)°, and m∠GEF=23°, find x',
                 '4a' : 'If m∠JKM=43°, m∠MKL=(8x-20)°, and m∠JKL=(10x-11)°, find x',
                 '5a'   : 'If ∠DEF is a straight angle, m∠DEG=(23x-3)°, and m∠GEF=(12x+8)°, find x',
                 '1b' : '126',
                 '2b' : '45',
                 '3b'   : '10',
                 '4b' : '17',
                 '5b'  : '5' }
    answercorrect=aesEcbDecryptFromBase64(decryptionKey, request.form['answer1'])
    answer=request.form['answer']
    answer1=answercorrect
    if answer == answercorrect:
        if current_user.is_authenticated:
            number = (random.randint(1, 5))
            answernum = (f'{number}b')
            questionnum = (f'{number}a')
            question = (questions.get(questionnum))
            answercorrect = (questions.get(answernum))
            answera="success"
            answerb="Correct!"
            f = open('mysite/website/static/leaderboard.txt', 'r')
            for line in f:
                wr = open('mysite/website/static/leaderboard.txt', 'a')
                if line.startswith("{'"+current_user.first_name+"'"+": "):
                    line1=line
                    line.replace("}", "")
                    replacestr="{'"+current_user.first_name+"': "
                    line=line.replace(replacestr, "")
                    line=line.replace("}","")
                    line=int(line)
                    line=line+random.randint(10, 15)
                    line="{'"+current_user.first_name+"': "+str(line)+"}"
                    with open('mysite/website/static/leaderboard.txt', 'r') as file :
                      filedata = file.read()
                    filedata = filedata.replace(line1, line+"\n")
                    with open('mysite/website/static/leaderboard.txt', 'w') as file:
                      file.write(filedata)
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            else:
                return render_template('StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
        else:
            number = (random.randint(1, 5))
            answernum = (f'{number}b')
            questionnum = (f'{number}a')
            question = (questions.get(questionnum))
            answercorrect = (questions.get(answernum))
            answera="success"
            answerb="Correct!"
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            else:
                return render_template('StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
    else:
        number = (random.randint(1, 5))
        answernum = (f'{number}b')
        questionnum = (f'{number}a')
        question = (questions.get(questionnum))
        answercorrect = (questions.get(answernum))
        answera="danger"
        answerb=f"Incorrect, The correct answer was {answer1}"
        user_agent = request.headers.get('User-Agent')
        user_agent = user_agent.lower()
        if "iphone" in user_agent:
            return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
        elif "android" in user_agent:
            return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
        else:
            return render_template('StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
@views.route('/1/math')
@login_required
def studylobbymath1():
    questions = {'1a': '6+9=', '1b': '15', '2a': '28-23=', '2b': '5', '3a': '14+14=', '3b': '28', '4a': '8-2=', '4b': '6', '5a': '6+22=', '5b': '28', '6a': '19-16=', '6b': '3', '7a': '17+9=', '7b': '26', '8a': '4-25=', '8b': '-21', '9a': '20+18=', '9b': '38', '10a': '0-10=', '10b': '-10'}
    number = (random.randint(1, 5))
    answernum = (f'{number}b')
    questionnum = (f'{number}a')
    question = (questions.get(questionnum))
    answercorrect = (questions.get(answernum))
    answera="info"
    answerb="Your Result Will Be Here"
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if "iphone" in user_agent:
        return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
    elif "android" in user_agent:
        return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
    else:
        return render_template('StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
@views.route('/1/math', methods=['POST'])
@login_required
def studylobbymath1post():
    questions = {'1a': '6+9=', '1b': '15', '2a': '28-23=', '2b': '5', '3a': '14+14=', '3b': '28', '4a': '8-2=', '4b': '6', '5a': '6+22=', '5b': '28', '6a': '19-16=', '6b': '3', '7a': '17+9=', '7b': '26', '8a': '4-25=', '8b': '-21', '9a': '20+18=', '9b': '38', '10a': '0-10=', '10b': '-10'}
    answercorrect=aesEcbDecryptFromBase64(decryptionKey, request.form['answer1'])
    answer=request.form['answer']
    answer1=answercorrect
    if answer == answercorrect:
        if current_user.is_authenticated:
            number = (random.randint(1, 5))
            answernum = (f'{number}b')
            questionnum = (f'{number}a')
            question = (questions.get(questionnum))
            answercorrect = (questions.get(answernum))
            answera="success"
            answerb="Correct!"
            f = open('mysite/website/static/leaderboard.txt', 'r')
            for line in f:
                wr = open('mysite/website/static/leaderboard.txt', 'a')
                if line.startswith("{'"+current_user.first_name+"'"+": "):
                    line1=line
                    line.replace("}", "")
                    replacestr="{'"+current_user.first_name+"': "
                    line=line.replace(replacestr, "")
                    line=line.replace("}","")
                    line=int(line)
                    line=line+random.randint(10, 15)
                    line="{'"+current_user.first_name+"': "+str(line)+"}"
                    with open('mysite/website/static/leaderboard.txt', 'r') as file :
                      filedata = file.read()
                    filedata = filedata.replace(line1, line+"\n")
                    with open('mysite/website/static/leaderboard.txt', 'w') as file:
                      file.write(filedata)
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            else:
                return render_template('StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
        else:
            number = (random.randint(1, 5))
            answernum = (f'{number}b')
            questionnum = (f'{number}a')
            question = (questions.get(questionnum))
            answercorrect = (questions.get(answernum))
            answera="success"
            answerb="Correct!"
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            else:
                return render_template('StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
    else:
        number = (random.randint(1, 5))
        answernum = (f'{number}b')
        questionnum = (f'{number}a')
        question = (questions.get(questionnum))
        answercorrect = (questions.get(answernum))
        answera="danger"
        answerb=f"Incorrect, The correct answer was {answer1}"
        user_agent = request.headers.get('User-Agent')
        user_agent = user_agent.lower()
        if "iphone" in user_agent:
            return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
        elif "android" in user_agent:
            return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
        else:
            return render_template('StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
@views.route('/2/math')
@login_required
def studylobbymath2():
    questions = {'1a': '76+23=', '1b': '99', '2a': '10-86=', '2b': '-76', '3a': '12+83=', '3b': '95', '4a': '64-40=', '4b': '24', '5a': '3+91=', '5b': '94', '6a': '50-99=', '6b': '-49', '7a': '90+3=', '7b': '93', '8a': '65-53=', '8b': '12', '9a': '62+71=', '9b': '133', '10a': '33-45=', '10b': '-12'}
    number = (random.randint(1, 5))
    answernum = (f'{number}b')
    questionnum = (f'{number}a')
    question = (questions.get(questionnum))
    answercorrect = (questions.get(answernum))
    answera="info"
    answerb="Your Result Will Be Here"
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if "iphone" in user_agent:
        return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
    elif "android" in user_agent:
        return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
    else:
        return render_template('StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
@views.route('/2/math', methods=['POST'])
@login_required
def studylobbymath2post():
    questions = {'1a': '76+23=', '1b': '99', '2a': '10-86=', '2b': '-76', '3a': '12+83=', '3b': '95', '4a': '64-40=', '4b': '24', '5a': '3+91=', '5b': '94', '6a': '50-99=', '6b': '-49', '7a': '90+3=', '7b': '93', '8a': '65-53=', '8b': '12', '9a': '62+71=', '9b': '133', '10a': '33-45=', '10b': '-12'}
    answercorrect=aesEcbDecryptFromBase64(decryptionKey, request.form['answer1'])
    answer=request.form['answer']
    answer1=answercorrect
    if answer == answercorrect:
        if current_user.is_authenticated:
            number = (random.randint(1, 5))
            answernum = (f'{number}b')
            questionnum = (f'{number}a')
            question = (questions.get(questionnum))
            answercorrect = (questions.get(answernum))
            answera="success"
            answerb="Correct!"
            f = open('mysite/website/static/leaderboard.txt', 'r')
            for line in f:
                wr = open('mysite/website/static/leaderboard.txt', 'a')
                if line.startswith("{'"+current_user.first_name+"'"+": "):
                    line1=line
                    line.replace("}", "")
                    replacestr="{'"+current_user.first_name+"': "
                    line=line.replace(replacestr, "")
                    line=line.replace("}","")
                    line=int(line)
                    line=line+random.randint(10, 15)
                    line="{'"+current_user.first_name+"': "+str(line)+"}"
                    with open('mysite/website/static/leaderboard.txt', 'r') as file :
                      filedata = file.read()
                    filedata = filedata.replace(line1, line+"\n")
                    with open('mysite/website/static/leaderboard.txt', 'w') as file:
                      file.write(filedata)
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            else:
                return render_template('StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
        else:
            number = (random.randint(1, 5))
            answernum = (f'{number}b')
            questionnum = (f'{number}a')
            question = (questions.get(questionnum))
            answercorrect = (questions.get(answernum))
            answera="success"
            answerb="Correct!"
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            else:
                return render_template('StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
    else:
        number = (random.randint(1, 5))
        answernum = (f'{number}b')
        questionnum = (f'{number}a')
        question = (questions.get(questionnum))
        answercorrect = (questions.get(answernum))
        answera="danger"
        answerb=f"Incorrect, The correct answer was {answer1}"
        user_agent = request.headers.get('User-Agent')
        user_agent = user_agent.lower()
        if "iphone" in user_agent:
            return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
        elif "android" in user_agent:
            return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
        else:
            return render_template('StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
@views.route('/3/math')
@login_required
def studylobbymath3():
    questions = {'1a': '6×10=', '1b': '60', '2a': '1÷5=', '2b': '0.2', '3a': '10×2=', '3b': '20', '4a': 'Round to the tens place: 7÷11=', '4b': '0.6', '5a': '6×6=', '5b': '36', '6a': 'Round to the tens place: 8÷12=', '6b': '0.6', '7a': '4×12=', '7b': '48', '8a': 'Round to the tens place: 2÷12=', '8b': '0.2', '9a': '11×11=', '9b': '121', '10a': 'Round to the tens place: 5÷12=', '10b': '0.4'}
    number = (random.randint(1, 5))
    answernum = (f'{number}b')
    questionnum = (f'{number}a')
    question = (questions.get(questionnum))
    answercorrect = (questions.get(answernum))
    answera="info"
    answerb="Your Result Will Be Here"
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if "iphone" in user_agent:
        return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
    elif "android" in user_agent:
        return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
    else:
        return render_template('StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
@views.route('/3/math', methods=['POST'])
@login_required
def studylobbymath3post():
    questions = {'1a': '6×10=', '1b': '60', '2a': '1÷5=', '2b': '0.2', '3a': '10×2=', '3b': '20', '4a': 'Round to the tens place: 7÷11=', '4b': '0.6', '5a': '6×6=', '5b': '36', '6a': 'Round to the tens place: 8÷12=', '6b': '0.6', '7a': '4×12=', '7b': '48', '8a': 'Round to the tens place: 2÷12=', '8b': '0.2', '9a': '11×11=', '9b': '121', '10a': 'Round to the tens place: 5÷12=', '10b': '0.4'}
    answercorrect=aesEcbDecryptFromBase64(decryptionKey, request.form['answer1'])
    answer=request.form['answer']
    answer1=answercorrect
    if answer == answercorrect:
        if current_user.is_authenticated:
            number = (random.randint(1, 5))
            answernum = (f'{number}b')
            questionnum = (f'{number}a')
            question = (questions.get(questionnum))
            answercorrect = (questions.get(answernum))
            answera="success"
            answerb="Correct!"
            f = open('mysite/website/static/leaderboard.txt', 'r')
            for line in f:
                wr = open('mysite/website/static/leaderboard.txt', 'a')
                if line.startswith("{'"+current_user.first_name+"'"+": "):
                    line1=line
                    line.replace("}", "")
                    replacestr="{'"+current_user.first_name+"': "
                    line=line.replace(replacestr, "")
                    line=line.replace("}","")
                    line=int(line)
                    line=line+random.randint(10, 15)
                    line="{'"+current_user.first_name+"': "+str(line)+"}"
                    with open('mysite/website/static/leaderboard.txt', 'r') as file :
                      filedata = file.read()
                    filedata = filedata.replace(line1, line+"\n")
                    with open('mysite/website/static/leaderboard.txt', 'w') as file:
                      file.write(filedata)
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            else:
                return render_template('StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
        else:
            number = (random.randint(1, 5))
            answernum = (f'{number}b')
            questionnum = (f'{number}a')
            question = (questions.get(questionnum))
            answercorrect = (questions.get(answernum))
            answera="success"
            answerb="Correct!"
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            else:
                return render_template('StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
    else:
        number = (random.randint(1, 5))
        answernum = (f'{number}b')
        questionnum = (f'{number}a')
        question = (questions.get(questionnum))
        answercorrect = (questions.get(answernum))
        answera="danger"
        answerb=f"Incorrect, The correct answer was {answer1}"
        user_agent = request.headers.get('User-Agent')
        user_agent = user_agent.lower()
        if "iphone" in user_agent:
            return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
        elif "android" in user_agent:
            return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
        else:
            return render_template('StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
@views.route('/4/math')
@login_required
def studylobbymath4():
    questions={'1a': 'Ashley and four friends went trick or treating. Each of them got ⅘ of a bag of treats. How many bags of treats did they have in total?', '1b': '4', '2a': 'There are 8 water bottles and each bottle is ¾ filled with water. If we pour all the water together, how many water bottles can be filled up?', '2b': '6', '3a': '⁶⁄₁₀-⁵⁄₁₀', '3b':'1/10', '4a': '⅔+⅓', '4b': '1', '5a': 'Simplify your answer: ⁷⁄₁₀-³⁄₁₀', '5b': '2/5'}
    number = (random.randint(1, 5))
    answernum = (f'{number}b')
    questionnum = (f'{number}a')
    question = (questions.get(questionnum))
    answercorrect = (questions.get(answernum))
    answera="info"
    answerb="Your Result Will Be Here"
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if "iphone" in user_agent:
        return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
    elif "android" in user_agent:
        return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
    else:
        return render_template('StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
@views.route('/4/math', methods=['POST'])
@login_required
def studylobbymath4post():
    questions={'1a': 'Ashley and four friends went trick or treating. Each of them got ⅘ of a bag of treats. How many bags of treats did they have in total?', '1b': '4', '2a': 'There are 8 water bottles and each bottle is ¾ filled with water. If we pour all the water together, how many water bottles can be filled up?', '2b': '6', '3a': '⁶⁄₁₀-⁵⁄₁₀', '3b':'1/10', '4a': '⅔+⅓', '4b': '1', '5a': 'Simplify your answer: ⁷⁄₁₀-³⁄₁₀', '5b': '2/5'}
    answercorrect=aesEcbDecryptFromBase64(decryptionKey, request.form['answer1'])
    answer=request.form['answer']
    answer1=answercorrect
    if answer == answercorrect:
        if current_user.is_authenticated:
            number = (random.randint(1, 5))
            answernum = (f'{number}b')
            questionnum = (f'{number}a')
            question = (questions.get(questionnum))
            answercorrect = (questions.get(answernum))
            answera="success"
            answerb="Correct!"
            f = open('mysite/website/static/leaderboard.txt', 'r')
            for line in f:
                wr = open('mysite/website/static/leaderboard.txt', 'a')
                if line.startswith("{'"+current_user.first_name+"'"+": "):
                    line1=line
                    line.replace("}", "")
                    replacestr="{'"+current_user.first_name+"': "
                    line=line.replace(replacestr, "")
                    line=line.replace("}","")
                    line=int(line)
                    line=line+random.randint(10, 15)
                    line="{'"+current_user.first_name+"': "+str(line)+"}"
                    with open('mysite/website/static/leaderboard.txt', 'r') as file :
                      filedata = file.read()
                    filedata = filedata.replace(line1, line+"\n")
                    with open('mysite/website/static/leaderboard.txt', 'w') as file:
                      file.write(filedata)
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            else:
                return render_template('StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
        else:
            number = (random.randint(1, 5))
            answernum = (f'{number}b')
            questionnum = (f'{number}a')
            question = (questions.get(questionnum))
            answercorrect = (questions.get(answernum))
            answera="success"
            answerb="Correct!"
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            else:
                return render_template('StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
    else:
        number = (random.randint(1, 5))
        answernum = (f'{number}b')
        questionnum = (f'{number}a')
        question = (questions.get(questionnum))
        answercorrect = (questions.get(answernum))
        answera="danger"
        answerb=f"Incorrect, The correct answer was {answer1}"
        user_agent = request.headers.get('User-Agent')
        user_agent = user_agent.lower()
        if "iphone" in user_agent:
            return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
        elif "android" in user_agent:
            return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
        else:
            return render_template('StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
@views.route('/5/math')
@login_required
def studylobbymath5():
    questions={'1a': '3.14×10', '1b': '31.4', '2a': '37.5×2', '2b': '75', '3a': '10.1×5', '3b':'50.5', '4a': '4.2×5', '4b': '21', '5a': '2.64×3', '5b': '7.92'}
    number = (random.randint(1, 5))
    answernum = (f'{number}b')
    questionnum = (f'{number}a')
    question = (questions.get(questionnum))
    answercorrect = (questions.get(answernum))
    answera="info"
    answerb="Your Result Will Be Here"
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if "iphone" in user_agent:
        return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
    elif "android" in user_agent:
        return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
    else:
        return render_template('StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
@views.route('/5/math', methods=['POST'])
@login_required
def studylobbymath5post():
    questions={'1a': '3.14×10', '1b': '31.4', '2a': '37.5×2', '2b': '75', '3a': '10.1×5', '3b':'50.5', '4a': '4.2×5', '4b': '21', '5a': '2.64×3', '5b': '7.92'}
    answercorrect=aesEcbDecryptFromBase64(decryptionKey, request.form['answer1'])
    answer=request.form['answer']
    answer1=answercorrect
    if answer == answercorrect:
        if current_user.is_authenticated:
            number = (random.randint(1, 5))
            answernum = (f'{number}b')
            questionnum = (f'{number}a')
            question = (questions.get(questionnum))
            answercorrect = (questions.get(answernum))
            answera="success"
            answerb="Correct!"
            f = open('mysite/website/static/leaderboard.txt', 'r')
            for line in f:
                wr = open('mysite/website/static/leaderboard.txt', 'a')
                if line.startswith("{'"+current_user.first_name+"'"+": "):
                    line1=line
                    line.replace("}", "")
                    replacestr="{'"+current_user.first_name+"': "
                    line=line.replace(replacestr, "")
                    line=line.replace("}","")
                    line=int(line)
                    line=line+random.randint(10, 15)
                    line="{'"+current_user.first_name+"': "+str(line)+"}"
                    with open('mysite/website/static/leaderboard.txt', 'r') as file :
                      filedata = file.read()
                    filedata = filedata.replace(line1, line+"\n")
                    with open('mysite/website/static/leaderboard.txt', 'w') as file:
                      file.write(filedata)
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            else:
                return render_template('StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
        else:
            number = (random.randint(1, 5))
            answernum = (f'{number}b')
            questionnum = (f'{number}a')
            question = (questions.get(questionnum))
            answercorrect = (questions.get(answernum))
            answera="success"
            answerb="Correct!"
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            else:
                return render_template('StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
    else:
        number = (random.randint(1, 5))
        answernum = (f'{number}b')
        questionnum = (f'{number}a')
        question = (questions.get(questionnum))
        answercorrect = (questions.get(answernum))
        answera="danger"
        answerb=f"Incorrect, The correct answer was {answer1}"
        user_agent = request.headers.get('User-Agent')
        user_agent = user_agent.lower()
        if "iphone" in user_agent:
            return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
        elif "android" in user_agent:
            return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
        else:
            return render_template('StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
@views.route('/6/math')
@login_required
def studylobbymath6():
    questions={'1a': 'a+5 | a=2', '1b': '7', '2a': 'b+3 | b=7', '2b': '10', '3a': 'c+4 | c=1', '3b':'5', '4a': 'd+6 | d=3', '4b': '9', '5a': 'e+7 | e=5', '5b': '12'}
    number = (random.randint(1, 5))
    answernum = (f'{number}b')
    questionnum = (f'{number}a')
    question = (questions.get(questionnum))
    answercorrect = (questions.get(answernum))
    answera="info"
    answerb="Your Result Will Be Here"
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if "iphone" in user_agent:
        return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
    elif "android" in user_agent:
        return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
    else:
        return render_template('StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
@views.route('/6/math', methods=['POST'])
@login_required
def studylobbymath6post():
    questions={'1a': 'a+5 | a=2', '1b': '7', '2a': 'b+3 | b=7', '2b': '10', '3a': 'c+4 | c=1', '3b':'5', '4a': 'd+6 | d=3', '4b': '9', '5a': 'e+7 | e=5', '5b': '12'}
    answercorrect=aesEcbDecryptFromBase64(decryptionKey, request.form['answer1'])
    answer=request.form['answer']
    answer1=answercorrect
    if answer == answercorrect:
        if current_user.is_authenticated:
            number = (random.randint(1, 5))
            answernum = (f'{number}b')
            questionnum = (f'{number}a')
            question = (questions.get(questionnum))
            answercorrect = (questions.get(answernum))
            answera="success"
            answerb="Correct!"
            f = open('mysite/website/static/leaderboard.txt', 'r')
            for line in f:
                wr = open('mysite/website/static/leaderboard.txt', 'a')
                if line.startswith("{'"+current_user.first_name+"'"+": "):
                    line1=line
                    line.replace("}", "")
                    replacestr="{'"+current_user.first_name+"': "
                    line=line.replace(replacestr, "")
                    line=line.replace("}","")
                    line=int(line)
                    line=line+random.randint(10, 15)
                    line="{'"+current_user.first_name+"': "+str(line)+"}"
                    with open('mysite/website/static/leaderboard.txt', 'r') as file :
                      filedata = file.read()
                    filedata = filedata.replace(line1, line+"\n")
                    with open('mysite/website/static/leaderboard.txt', 'w') as file:
                      file.write(filedata)
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            else:
                return render_template('StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
        else:
            number = (random.randint(1, 5))
            answernum = (f'{number}b')
            questionnum = (f'{number}a')
            question = (questions.get(questionnum))
            answercorrect = (questions.get(answernum))
            answera="success"
            answerb="Correct!"
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            else:
                return render_template('StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
    else:
        number = (random.randint(1, 5))
        answernum = (f'{number}b')
        questionnum = (f'{number}a')
        question = (questions.get(questionnum))
        answercorrect = (questions.get(answernum))
        answera="danger"
        answerb=f"Incorrect, The correct answer was {answer1}"
        user_agent = request.headers.get('User-Agent')
        user_agent = user_agent.lower()
        if "iphone" in user_agent:
            return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
        elif "android" in user_agent:
            return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
        else:
            return render_template('StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
@views.route('/7/math')
@login_required
def studylobbymath7():
    questions={'1a': '½×⁵⁄₄=', '1b': '⅝', '2a': '¼×⁵⁄₃=', '2b': '5/12', '3a': 'Leave as an improper fraction: ¹⁰⁄₃×¹¹⁄₆=', '3b':'55/9', '4a': '⅙×⁸⁄₁₁=', '4b': '4/33', '5a': 'Leave as an improper fraction: ¹¹⁄₂÷½=', '5b': '¹¹⁄₄'}
    number = (random.randint(1, 5))
    answernum = (f'{number}b')
    questionnum = (f'{number}a')
    question = (questions.get(questionnum))
    answercorrect = (questions.get(answernum))
    answera="info"
    answerb="Your Result Will Be Here"
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if "iphone" in user_agent:
        return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
    elif "android" in user_agent:
        return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
    else:
        return render_template('StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
@views.route('/7/math', methods=['POST'])
@login_required
def studylobbymath7post():
    questions={'1a': '½×⁵⁄₄=', '1b': '⅝', '2a': '¼×⁵⁄₃=', '2b': '5/12', '3a': 'Leave as an improper fraction: ¹⁰⁄₃×¹¹⁄₆=', '3b':'55/9', '4a': '⅙×⁸⁄₁₁=', '4b': '4/33', '5a': 'Leave as an improper fraction: ¹¹⁄₂÷½=', '5b': '¹¹⁄₄'}
    answercorrect=aesEcbDecryptFromBase64(decryptionKey, request.form['answer1'])
    answer=request.form['answer']
    answer1=answercorrect
    if answer == answercorrect:
        if current_user.is_authenticated:
            number = (random.randint(1, 5))
            answernum = (f'{number}b')
            questionnum = (f'{number}a')
            question = (questions.get(questionnum))
            answercorrect = (questions.get(answernum))
            answera="success"
            answerb="Correct!"
            f = open('mysite/website/static/leaderboard.txt', 'r')
            for line in f:
                wr = open('mysite/website/static/leaderboard.txt', 'a')
                if line.startswith("{'"+current_user.first_name+"'"+": "):
                    line1=line
                    line.replace("}", "")
                    replacestr="{'"+current_user.first_name+"': "
                    line=line.replace(replacestr, "")
                    line=line.replace("}","")
                    line=int(line)
                    line=line+random.randint(10, 15)
                    line="{'"+current_user.first_name+"': "+str(line)+"}"
                    with open('mysite/website/static/leaderboard.txt', 'r') as file :
                      filedata = file.read()
                    filedata = filedata.replace(line1, line+"\n")
                    with open('mysite/website/static/leaderboard.txt', 'w') as file:
                      file.write(filedata)
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            else:
                return render_template('StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
        else:
            number = (random.randint(1, 5))
            answernum = (f'{number}b')
            questionnum = (f'{number}a')
            question = (questions.get(questionnum))
            answercorrect = (questions.get(answernum))
            answera="success"
            answerb="Correct!"
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            else:
                return render_template('StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
    else:
        number = (random.randint(1, 5))
        answernum = (f'{number}b')
        questionnum = (f'{number}a')
        question = (questions.get(questionnum))
        answercorrect = (questions.get(answernum))
        answera="danger"
        answerb=f"Incorrect, The correct answer was {answer1}"
        user_agent = request.headers.get('User-Agent')
        user_agent = user_agent.lower()
        if "iphone" in user_agent:
            return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
        elif "android" in user_agent:
            return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
        else:
            return render_template('StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
@views.route('/9/math')
@login_required
def studylobbymath9():
    questions = {'1a'  : 'Simplify: 2(x-9)+6(-x+2)+4x',
                 '2a'   : 'Evaluate xyz if x=3,y=2, and z=1',
                 '3a' : 'Evaluate −3a−(2b+4) if a=−8 and b=−7',
                 '4a' : "Claire’s bakery sells croissants, muffins, and donuts. The expression 3.5c+4m+2.5d gives the cost (in dollars) of c croissants, m muffins, and d donuts. Will is having a party and needs to order 10 croissants, 6 muffins, and 12 donuts. What is the total cost of Will’s order? (Don't include the dollar sign)",
                 '5a'   : "Jack and Diane own a company that sells scooters. The amount they pay the employees on their sales team (in dollars) is 15x+25y. In this expression, x represents the number of hours worked and y represents the number of sales made. How much would an employee make if they work for 5 hours and sell 4 scooters? (Don't include the dollar sign))",
                 '1b' : '-6',
                 '2b' : '6',
                 '3b'   : '34',
                 '4b' : '89',
                 '5b'  : '175' }
    number = (random.randint(1, 5))
    answernum = (f'{number}b')
    questionnum = (f'{number}a')
    question = (questions.get(questionnum))
    answercorrect = (questions.get(answernum))
    answera="info"
    answerb="Your Result Will Be Here"
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if "iphone" in user_agent:
        return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
    elif "android" in user_agent:
        return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
    else:
        return render_template('StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
@views.route('/9/math', methods=['POST'])
@login_required
def studylobbymath9post():
    questions = {'1a'  : 'Simplify to solve for X: 2(x-9)+6(-x+2)+4x',
                 '2a'   : 'Evaluate xyz if x=3,y=2, and z=1',
                 '3a' : 'Evaluate −3a−(2b+4) if a=−8 and b=−7',
                 '4a' : "Claire’s bakery sells croissants, muffins, and donuts. The expression 3.5c+4m+2.5d gives the cost (in dollars) of c croissants, m muffins, and d donuts. Will is having a party and needs to order 10 croissants, 6 muffins, and 12 donuts. What is the total cost of Will’s order? (Don't include the dollar sign)",
                 '5a'   : "Jack and Diane own a company that sells scooters. The amount they pay the employees on their sales team (in dollars) is 15x+25y. In this expression, x represents the number of hours worked and y represents the number of sales made. How much would an employee make if they work for 5 hours and sell 4 scooters? (Don't include the dollar sign))",
                 '1b' : '-6',
                 '2b' : '6',
                 '3b'   : '34',
                 '4b' : '89',
                 '5b'  : '175' }
    answercorrect=aesEcbDecryptFromBase64(decryptionKey, request.form['answer1'])
    answer=request.form['answer']
    answer1=answercorrect
    if answer == answercorrect:
        if current_user.is_authenticated:
            number = (random.randint(1, 5))
            answernum = (f'{number}b')
            questionnum = (f'{number}a')
            question = (questions.get(questionnum))
            answercorrect = (questions.get(answernum))
            answera="success"
            answerb="Correct!"
            f = open('mysite/website/static/leaderboard.txt', 'r')
            for line in f:
                wr = open('mysite/website/static/leaderboard.txt', 'a')
                if line.startswith("{'"+current_user.first_name+"'"+": "):
                    line1=line
                    line.replace("}", "")
                    replacestr="{'"+current_user.first_name+"': "
                    line=line.replace(replacestr, "")
                    line=line.replace("}","")
                    line=int(line)
                    line=line+random.randint(10, 15)
                    line="{'"+current_user.first_name+"': "+str(line)+"}"
                    with open('mysite/website/static/leaderboard.txt', 'r') as file :
                      filedata = file.read()
                    filedata = filedata.replace(line1, line+"\n")
                    with open('mysite/website/static/leaderboard.txt', 'w') as file:
                      file.write(filedata)
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            else:
                return render_template('StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
        else:
            number = (random.randint(1, 5))
            answernum = (f'{number}b')
            questionnum = (f'{number}a')
            question = (questions.get(questionnum))
            answercorrect = (questions.get(answernum))
            answera="success"
            answerb="Correct!"
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            else:
                return render_template('StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
    else:
        number = (random.randint(1, 5))
        answernum = (f'{number}b')
        questionnum = (f'{number}a')
        question = (questions.get(questionnum))
        answercorrect = (questions.get(answernum))
        answera="danger"
        answerb=f"Incorrect, The correct answer was {answer1}"
        user_agent = request.headers.get('User-Agent')
        user_agent = user_agent.lower()
        if "iphone" in user_agent:
            return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
        elif "android" in user_agent:
            return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
        else:
            return render_template('StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
@views.route('/12/math')
@login_required
def studylobbymath12():
    questions = {'1a'  : "A conic section is represented by the following equation: −4x²+15y²+343=0    What type of conic section does this equation represent? (Don't include caps)",
                 '2a'   : 'What is the minimal value of 2x²+16x−7 over all real numbers?',
                 '3a' : 'Consider the function f(x)=x²−x Find the maximum of the function on the interval [0,1].',
                 '1b' : 'hyperbola',
                 '2b' : '-39',
                 '3b'   : '0'}
    number = (random.randint(1, 3))
    answernum = (f'{number}b')
    questionnum = (f'{number}a')
    question = (questions.get(questionnum))
    answercorrect = (questions.get(answernum))
    answera="info"
    answerb="Your Result Will Be Here"
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if "iphone" in user_agent:
        return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
    elif "android" in user_agent:
        return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
    else:
        return render_template('StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
@views.route('/12/math', methods=['POST'])
@login_required
def studylobbymath12post():
    questions = {'1a'  : "A conic section is represented by the following equation: −4x²+15y²+343=0    What type of conic section does this equation represent? (Don't include caps)",
                 '2a'   : 'What is the minimal value of 2x²+16x−7 over all real numbers?',
                 '3a' : 'Consider the function f(x)=x²−x Find the maximum of the function on the interval [0,1].',
                 '1b' : 'hyperbola',
                 '2b' : '-39',
                 '3b'   : '0'}
    answercorrect=aesEcbDecryptFromBase64(decryptionKey, request.form['answer1'])
    answer=request.form['answer']
    answer1=answercorrect
    if answer == answercorrect:
        if current_user.is_authenticated:
            number = (random.randint(1, 5))
            answernum = (f'{number}b')
            questionnum = (f'{number}a')
            question = (questions.get(questionnum))
            answercorrect = (questions.get(answernum))
            answera="success"
            answerb="Correct!"
            f = open('mysite/website/static/leaderboard.txt', 'r')
            for line in f:
                wr = open('mysite/website/static/leaderboard.txt', 'a')
                if line.startswith("{'"+current_user.first_name+"'"+": "):
                    line1=line
                    line.replace("}", "")
                    replacestr="{'"+current_user.first_name+"': "
                    line=line.replace(replacestr, "")
                    line=line.replace("}","")
                    line=int(line)
                    line=line+random.randint(10, 15)
                    line="{'"+current_user.first_name+"': "+str(line)+"}"
                    with open('mysite/website/static/leaderboard.txt', 'r') as file :
                      filedata = file.read()
                    filedata = filedata.replace(line1, line+"\n")
                    with open('mysite/website/static/leaderboard.txt', 'w') as file:
                      file.write(filedata)
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            else:
                return render_template('StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
        else:
            number = (random.randint(1, 5))
            answernum = (f'{number}b')
            questionnum = (f'{number}a')
            question = (questions.get(questionnum))
            answercorrect = (questions.get(answernum))
            answera="success"
            answerb="Correct!"
            user_agent = request.headers.get('User-Agent')
            user_agent = user_agent.lower()
            if "iphone" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            elif "android" in user_agent:
                return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
            else:
                return render_template('StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
    else:
        number = (random.randint(1, 5))
        answernum = (f'{number}b')
        questionnum = (f'{number}a')
        question = (questions.get(questionnum))
        answercorrect = (questions.get(answernum))
        answera="danger"
        answerb=f"Incorrect, The correct answer was {answer1}"
        user_agent = request.headers.get('User-Agent')
        user_agent = user_agent.lower()
        if "iphone" in user_agent:
            return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
        elif "android" in user_agent:
            return render_template('mobile/StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)
        else:
            return render_template('StudyLobbyMathStart.html', question=question, answer=aesEcbEncryptToBase64(encryptionKey, answercorrect), answera=answera,answerb=answerb)