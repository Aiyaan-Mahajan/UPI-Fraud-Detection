import streamlit as st
import pandas as pd
import numpy as np
import pickle
import datetime
from datetime import datetime as dt
import base64

# -------------------- LOAD MODEL --------------------
pickle_file_path = "upi_fraud_model.pkl"
loaded_model = pickle.load(open(pickle_file_path, "rb"))

# -------------------- CATEGORY LISTS --------------------
tt = ["Bill Payment", "Investment", "Other", "Purchase", "Refund", "Subscription"]

pg = ["Google Pay", "HDFC", "ICICI UPI", "IDFC UPI", "Other",
      "Paytm", "PhonePe", "Razor Pay"]

ts = ['Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa',
      'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka',
      'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya',
      'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim',
      'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh',
      'Uttarakhand', 'West Bengal']

mc = ['Donations and Devotion', 'Financial services and Taxes',
      'Home delivery', 'Investment', 'More Services', 'Other',
      'Purchases', 'Travel bookings', 'Utilities']

#yeh UI hai just for the ke of implementation banaya taki kuch dikhe bhi 
st.title("UPI Transaction Fraud Detector")

st.subheader("Check Single Transaction")

tran_date = st.date_input("Select Transaction Date", datetime.date.today())
month = tran_date.month
year = tran_date.year

tran_type = st.selectbox("Transaction Type", tt)
pmt_gateway = st.selectbox("Payment Gateway", pg)
tran_state = st.selectbox("Transaction State", ts)
merch_cat = st.selectbox("Merchant Category", mc)

amt = st.number_input("Transaction Amount", step=0.1)

st.write("OR")

st.subheader("Upload CSV File")
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

# yeh button ka code hai 
if st.button("Check Transaction(s)"):

    # -------------------- CSV CASE --------------------
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        df[['Month', 'Year']] = df['Date'].str.split('-', expand=True)[[1, 2]]
        df[['Month', 'Year']] = df[['Month', 'Year']].astype(int)
        df.drop(columns=['Date'], inplace=True)

        results = []

        for index, row in df.iterrows():

            tt_oh = [0]*len(tt)
            pg_oh = [0]*len(pg)
            ts_oh = [0]*len(ts)
            mc_oh = [0]*len(mc)

            tt_oh[tt.index(row['Transaction_Type'])] = 1
            pg_oh[pg.index(row['Payment_Gateway'])] = 1
            ts_oh[ts.index(row['Transaction_State'])] = 1
            mc_oh[mc.index(row['Merchant_Category'])] = 1

            input_data = [
                row['Amount'],
                row['Year'],
                row['Month']
            ] + tt_oh + pg_oh + ts_oh + mc_oh

            prediction = loaded_model.predict([input_data])[0]
            results.append(prediction)

        df['Fraud'] = results

        st.success("Transactions Checked!")
        st.write(df)

    # -------------------- SINGLE INPUT CASE --------------------
    else:
        tt_oh = [0]*len(tt)
        pg_oh = [0]*len(pg)
        ts_oh = [0]*len(ts)
        mc_oh = [0]*len(mc)

        tt_oh[tt.index(tran_type)] = 1
        pg_oh[pg.index(pmt_gateway)] = 1
        ts_oh[ts.index(tran_state)] = 1
        mc_oh[mc.index(merch_cat)] = 1

        input_data = [amt, year, month] + tt_oh + pg_oh + ts_oh + mc_oh

        result = loaded_model.predict([input_data])[0]

        st.success("Transaction Checked!")

        if result == 0:
            st.write("Not a fraudulent transaction.")
        else:
            st.write("Fraudulent transaction detected!")
