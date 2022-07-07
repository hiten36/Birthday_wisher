import pandas as pd
import datetime
import smtplib
GMAIL_ID='hitenkhatri14@gmail.com'
GMAIL_PASSWORD='Hk36901470'
def sendmail(to,sub,msg):
    print(f'email to {to} with subject: {sub} and message: {msg}')
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(GMAIL_ID,GMAIL_PASSWORD)
    s.sendmail(GMAIL_ID,to,f'Subject: {sub}\n\n{msg}')
    s.quit()
if __name__ == '__main__':
    df=pd.read_excel('bday.xlsx')
    # print(df)
    today=datetime.datetime.now().strftime("%d-%m")
    yearnow=datetime.datetime.now().strftime("%y")
    print(today)
    # print(yearnow)
    wirteind=[]
    for index,item in df.iterrows():
        # print(index,item['birthday'])
        bday=item['birthday']
        # print(bday)
        if(today==bday and yearnow not in str(item['year'])):
            print('ye')
            sendmail(item['email'],"happy birthday",item['dialouge'])
            wirteind.append(index)
    print(wirteind)
    # for i in wirteind:
    #     yr=df.loc[i,'year']
    #     df.loc[i,'year']=str(yr)+', '+str(yearnow)
    #     print(df.loc[i,'year'])
    # df.to_excel('bday.xlsx',index=False)