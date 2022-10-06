import streamlit as st
import pandas as pd

st.set_page_config(page_title='Bakery Sales',page_icon = ':bar_chart:',layout='wide')



header = st.container()
dataset = st.container()
charts = st.container()

with header:
    st.title('BAKERY SALES ANALYSIS')
    st.text('''This project is focused on the analysis of sales record from 2019 to 2020.
The aim of the project is create new prespectives into the bakery buiness and 
provide recommendations to develop the buiness.''')


with dataset:
    st.header('SALES RECORD')
    st.text('''This table shows the total sales record of the bakery including the orders of customers.
This table can be filtered using the sidebar of the left, you can check the sales in a particular year and 
month. For example you can check the sales on Jan(01), 2020.''')
    
    df_1 = pd.read_csv('data/bakery_sales.csv')
    bakery_data = df_1.fillna(0)
    bakery_data = bakery_data.drop('place',axis=1)
   
    
    st.sidebar.header('Please filter here')
    month = st.sidebar.multiselect(
        'Select the month:',
        options=bakery_data['month'].unique(),
        default=bakery_data['month'].unique())

    year = st.sidebar.multiselect(
        'Select the year:',
        options=bakery_data['year'].unique(),
        default=bakery_data['year'].unique())
    
    
    
    df_selection = bakery_data.query(
        'month == @month & year == @year')

    st.dataframe(df_selection)
    
    st.text('''In this table, I filled the N/A values with 0. I did this to ease our mathmatical 
calulation and this is better alternative to dropping the columns with N/A values. 
If you try to drop the columns with N/A values then the whole dataset becomes empty.''')



with charts:
    st.title('ANALYSIS OF SALES')
    st.text('''This section shows sections of the broken down data.''')
    sel_col, disp_col = st.columns(2)
    
    total_sales = sel_col.selectbox('Sales on days',options=['monday','tuesday','wednesday','thursday','friday','saturday','sunday'],index=0)
    if total_sales == 'monday':
        y = bakery_data.loc[bakery_data['day of week']=='Mon']['total'].values
        z = pd.DataFrame(y)
        st.write(z)
        
    elif total_sales == "tuesday":
        y = bakery_data.loc[bakery_data['day of week']=='Tues']['total'].values
        z = pd.DataFrame(y)
        st.write(z)
        
    elif total_sales == "wednesday":
         y = bakery_data.loc[bakery_data['day of week']=='Wed']['total'].values
         z = pd.DataFrame(y)
         st.write(z)
    
    elif total_sales == "thursday":
        y = bakery_data.loc[bakery_data['day of week']=='Thur']['total'].values
        z = pd.DataFrame(y)
        st.write(z)
    
    elif total_sales == "friday":
        y = bakery_data.loc[bakery_data['day of week']=='Fri']['total'].values
        z = pd.DataFrame(y)
        st.write(z)
        
    elif total_sales == "saturday":
         y = bakery_data.loc[bakery_data['day of week']=='Sat']['total'].values
         z = pd.DataFrame(y)
         st.write(z)
         
    elif total_sales == "sunday":
         y = bakery_data.loc[bakery_data['day of week']=='Sun']['total'].values
         z = pd.DataFrame(y)
         st.write(z)
         
    st.text('''The table above shows all the sales according to days so for monday we can see all 
the sales you have done on monday, tuesday, wednesday, thursday, friday, saturday 
and sunday.''')
    
    st.text('Summary of sales record')
    st.write(bakery_data)
    #st.text('''The table above shows a summary of our data, which includes the number of rows and columns
#The mean values, the maximum and minimum values in each column and so on.''')
    st.text('Total sales by days.')
    sum_of_total = bakery_data.groupby('day of week')['total'].sum()
    sum_of_total = sum_of_total.drop(sum_of_total.index[0])
    st.write(sum_of_total)
    st.text('''The table above shows the sum of total sales made according to days.''')
    
    st.header('''CHARTS OF ANALYSIS''')
    st.text('''The first chart shows the busiest days, where we analyse the influx of customers.''')
    st.subheader('''BUSIEST DAYS OF THE WEEK''')
    days_of_week = bakery_data['day of week'].value_counts()
    tab5,tab6 = st.tabs(['bar chart','data'])
    tab5.bar_chart(days_of_week)
    tab6.write(days_of_week)
    st.text('''The chart above shows the days on which the bakery has the most customers.
From the table it is observable that the sunday is the busiest day followed by
saturday and so on. We can attribute to this high rate of influx to the fact
both days are on the weekend, so people have the oppotunity to go to the 
bakery.''')
    
    st.subheader('''TOTAL SALES BY DAYS''') 
    total_sales_by_days =bakery_data.groupby('day of week')['total'].sum()
    print(total_sales_by_days) 
    tab7,tab8 = st.tabs(['bar chart','data'])
    tab7.bar_chart(total_sales_by_days)
    tab8.write(total_sales_by_days)
    st.text('''In the chart above a patterned can be observed which shows that the days 
with the most sales is also the days with the highest number of customers''')
    
    x = bakery_data.columns
    products = x.drop(['datetime','day of week','total','date','time','am_pm','month','day','year'])

    sum_of_sales = bakery_data.groupby('day of week')[products].sum()

    st.subheader("""SUM OF SALES BY PRODUCTS""")
    st.write("""On this table we are looking at the, the products that sold the most according to days. 
             For example we can observe that the days with the most sale on the previous table is sunday, 
             But in this table we are looking at the quesion 'if sunday is the days with most sales, what did people buy on sunday?.
             and from the table we can see that the product with the most sales on sunday is angbutter.'""")
        
    st.write(sum_of_sales)
    tab1, tab2 = st.tabs(["📈 Bar chart", "Line chart"])

    tab1.subheader("A tab with bar chart of sales by days")
    tab1.bar_chart(sum_of_sales)

    tab2.subheader("A tab with Line chart of sales by days")
    tab2.area_chart(sum_of_sales)
    
    
    st.subheader('TOTAL SALES OF PRODUCTS')
    col1, col2 = st.columns(2)
    sum_of_products = bakery_data[products].sum()
    col1.write(sum_of_products)
    ang = 4800 * 3229
    plain =  3500 * 1028
    jam = 249 * 1500
    ameri = 4000 * 513
    croissant = 1049 * 3500
    coffe_latter = 4500 * 214
    tira = 945 * 4800
    cacao = 4000 * 264
    pain = 726 * 3500
    almond = 235 * 4000
    milk = 4500 * 160
    gate = 210 * 4000
    pan = 394 * 4500
    chesse = 92 * 5000
    lemon = 38 * 4500
    orange = 4500 * 566
    wiener = 2500 * 476
    valina = 241 * 4500
    berry = 55 * 4500
    tira = 7 * 4500
    meri = 49 * 4000
    y = [ang,plain,jam,ameri,croissant,coffe_latter,
         tira,cacao,pain,almond,milk,gate,pan,chesse,
         lemon,orange,wiener,valina,berry,tira,
         meri]
    total_sale_of_products = pd.DataFrame(y,index=['ang','plain','jam','ameri','croissant','coffe_latter',
         'tira','cacao','pain','almond','milk','gate','pan','chesse',
         'lemon','orange','wiener','valina','berry','tira',
         'meri'],columns=['$ total sold'])
    col2.write(total_sale_of_products)
    col1.text('''The table on the left shows the total 
number of products sold''')
    col2.text('''The table on the right shoes the total 
sum for each of the products.''')
    
    
    
    
    st.subheader('''chart of total number of products sold''')
    tab3,tab4 = st.tabs(["📈 Bar chart", "Line chart"])

    tab3.bar_chart(sum_of_products)
    tab4.area_chart(sum_of_products)
    
    st.subheader('''chart of total sum for each of the products''')
    tab9,tab10 = st.tabs(["📈 Bar chart", "Line chart"])

    tab9.bar_chart(total_sale_of_products)
    tab10.area_chart(total_sale_of_products)
    
    
#conlusion
    st.header('''CONCLUSION''')
    st.markdown('''From the representation above we can draw the various conclusions:''')
    st.markdown('''1. The day with the highest influx of customers is Sunday.''')
    st.markdown('''2. The day with the lowest influx of customers is Tuesday.''')
    st.markdown('''3. The day with the highest number of sales is sunday''')
    st.markdown('''4. The days with the lowest sales is Tuesday.''')
    st.markdown('''5. The most purchased product is Angbutter.''')
    st.markdown('''6. The least purchased products is mad gralic and croque monsuier.''')
    
#Recommendation
    st.header('''RECOMMENDATION''')
    st.markdown('''To improve the business sales these are the recommendations:''')
    st.markdown('''1. Include promo packages on Tuesday to increase influx of customers.''')
    st.markdown('''2. Remove mad gralic and croque monsuier from the food menu. It is not
bringing profit to the busniess and the cost of production of those items is expensive.''')
    st.markdown('''3. Create varities of angbutter, just as you have varities of crossaint creating 
varities of angbutter invvites more coustomers.''')

hide_st_style = '''
<style>
#MainMenu {visibility:hidden:}
footer{visibility:hidden;}
header{visibility:hidden;}
</style>'''
st.markdown(hide_st_style, unsafe_allow_html=True)