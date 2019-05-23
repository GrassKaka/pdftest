# coding=utf-8
import threading
import time

import numpy as np
import logging
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit


logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - [%(levelname)s] : %(message)s')

# characteristicImpedance = 50
# dielectricConstant = 2.56
#
#
# coupleCoefficient_dB = 2.9
#
# evenImpedance_dB = characteristicImpedance * \
#                 np.sqrt((1+np.power(10, -coupleCoefficient_dB/20))/(1-np.power(10, -coupleCoefficient_dB/20)))
#
# oddImpedance_dB = characteristicImpedance * \
#                 np.sqrt((1-np.power(10, -coupleCoefficient_dB/20))/(1+np.power(10, -coupleCoefficient_dB/20)))
#
# logging.debug(evenImpedance_dB)
# logging.debug(oddImpedance_dB)
#
#
# coupleCoefficient_V = np.power(10, -coupleCoefficient_dB/20.0)
# logging.debug(coupleCoefficient_V)
#
# evenImpedance_V = characteristicImpedance * \
#                   (np.sqrt((1+coupleCoefficient_V)/(1-coupleCoefficient_V)))
#
# oddImpedance_V = characteristicImpedance * \
#                  (np.sqrt((1-coupleCoefficient_V)/(1+coupleCoefficient_V)))
#
# # logging.debug('evenImpedance_V: ' + str(evenImpedance_V))
# # logging.debug(oddImpedance_V)
# # print(np.sqrt(2.56)*63.5)
#
#
# xs =np.array([3, 6, 10, 15, 20])
# ys = np.array([3.5255, 2.2239, 1.6140, 1.3016, 1.1578])
#
# plt.plot(xs, ys)
#
# plt.show()

# def func(x, a, b, c):
#     return 1.0* a * np.exp(-1.0* b * x) + c*1.0
#
# popt, pcov = curve_fit(func, xs, ys)
# # print(type(popt[0]))
# #
# plt.plot(xs, func(xs, *popt), 'r-', label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))
# #
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()
# plt.show()


# print(5.005 * np.exp(-0.252* 50))

# import time
# from datetime import datetime
#
# # 将当前时间转换为datetime对象格式
# logging.debug(datetime.fromtimestamp(time.time()))
# logging.debug(datetime.now())
#
# # 将Unix时间戳后的3600s转换为datetime对象格式
# logging.debug(datetime.fromtimestamp(3600))

# print('start')
# def haha():
#     time.sleep(4)
#     print('wake up')
#
# threadObj = threading.Thread(target=haha)
# threadObj.start()
# time.sleep(5)
# print('end')

# import subprocess
# for i in range(5):
#     miniObj = subprocess.Popen('D:\Program Files (x86)\minipad2\minipad2.exe')
#     print(miniObj.poll())


# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
#
# message = MIMEText('我想你了！', 'plain', 'utf-8')
# message['From'] = 'rpzheng220807@163.com'
# message['To'] = '330610808@qq.com'
# subject = 'Long time no see!'
# message['Subject'] = Header(subject, 'utf-8')
#
#
# smtpObj = smtplib.SMTP('smtp.163.com', 25)
# logging.debug(type(smtpObj))
# # logging.debug(smtpObj.set_debuglevel(1))
# logging.debug(smtpObj.ehlo())
# logging.debug(smtpObj.starttls())
# # pass_word = input('Enter password: ')
# # logging.debug(smtpObj.login('rpzheng220807@163.com', pass_word))
# logging.debug(smtpObj.login('rpzheng220807@163.com', 'zrp220807'))
# logging.debug(smtpObj.sendmail('rpzheng220807@163.com', '330610808@qq.com', message.as_string()))
# smtpObj.quit()


import imapclient

imapObj = imapclient.IMAPClient('imap.163.com', ssl=True)
logging.debug(imapObj)
logging.debug(imapObj.login('rpzheng110606@163.com', 'zrp220807'))

import pprint

pprint.pprint(imapObj.list_folders())

logging.debug(imapObj.select_folder('INBOX', readonly=True))
# time.sleep(3)
# logging.debug('hahaha')
mail_UIDS = imapObj.search()

rfc_message = imapObj.fetch(mail_UIDS[1], 'BODY[]')
# pprint.pprint(rfc_message)

import  pyzmail

real_message = pyzmail.PyzMessage.factory(rfc_message[1558577238][b'BODY[]'])

logging.debug(real_message.get_subject())
logging.debug(real_message.get_addresses('from'))


if real_message.html_part != None:
    logging.debug('Have html!')
    logging.debug(real_message.html_part.get_payload().decode(real_message.html_part.charset))
    if real_message.text_part != None:
        logging.debug('Have text!')
        logging.debug(real_message.text_part.get_payload().decode(real_message.text_part.charset))
else:
    logging.debug('Both No!')

imapObj.logout()