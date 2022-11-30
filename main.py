import streamlit as st

# Input --> Webpage(streamlit) ...

def Customer():
    
    st.header("Customer Information")
    st.sidebar.subheader("Customer Info")
    
    global customer_Name
    customer_Name = st.text_input("Enter customer name: ")

    global customer_Address
    customer_Address = st.text_input("Enter customer address: ")

    global customer_Phone_Number
    customer_Phone_Number = st.text_input("Enter customer phone number")

    global customer_Data
    customer_Data = [customer_Name, customer_Address, customer_Phone_Number]

    if(st.button("Submit")):
        st.success(customer_Data)

def Product():

    st.header("Product Information")
    st.sidebar.subheader("Product Info")

    global product_Name
    product_Name = st.text_input("Enter product name: ")

    global product_Amount
    product_Amount = st.slider("Amount: ", 1, 50)

    global product_Data
    product_Data = [product_Name, product_Amount]

def Payment():
    st.header("Payment Information")
    st.sidebar.subheader("Payament Info")

all_Pages = {
    "Customer": Customer,
    "Product": Product,
    "Payment": Payment,
}

st.sidebar.title("Python Website")
st.sidebar.header("Purchase Information")
selected_page = st.sidebar.selectbox("Select a page", all_Pages.keys())
all_Pages[selected_page]()











