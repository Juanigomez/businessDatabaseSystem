# IMPORTS -->

# Python to Google Spreadsheets ...

import gspread

# Import streamlit (webpage) ...

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

    def input_Customer():

        sa = gspread.service_account(filename="myBusiness_credentials.json")
        sp = sa.open_by_key('15kWRPBdJrGbd5nmyN0bdK4OGFQkYeDwHQNl1vNp1rgI')

        spreadsheets = sa.openall()

        if spreadsheets:
            for spreadsheet in spreadsheets:
                print(f"Title: {spreadsheet.title}")
        else:
            print("No available spreadsheets")

        for worksheets in spreadsheet.worksheets():
            print(f"Worksheet: {worksheets.title}")

        global customers
        customers = spreadsheet.worksheet(title= "Customers")

        global index
        index = 0

        get_Customers = customers.col_values(2)
        count = int(len(get_Customers))

        all_Customers = customers.get(f"B6:B{count}")
        check_Customer = customer_Name
    
        if check_Customer != all_Customers[index][0]:

            for clients in all_Customers:
                while check_Customer != all_Customers[index][0]:
                    if index == int(count - 6):
                        break
                    else:
                        index += 1

        if check_Customer == all_Customers[index][0]:

            global current_Customer
            current_Customer = all_Customers[index][0]
            st.info("Existing customer, loading info ...")

            def get_Address():

                get_Adds = customers.col_values(3)
                count = int(len(get_Adds))

                all_Adds = customers.get(f"C6:C{count}")

                global current_Address
                current_Address = all_Adds[index][0]
                st.text(f"Address: {current_Address}")

            get_Address()

            def get_Phone_Number():

                get_Nmbs = customers.col_values(4)
                count = int(len(get_Nmbs))

                all_Nmbs = customers.get(f"D6:{count}")

                global current_Phone_Number
                current_Phone_Number = all_Nmbs[index][0]
                st.text(f"Phone number: {current_Phone_Number}")

            get_Phone_Number()

        else:

            def new_Customer():

                get_Customers = customers.col_values(2)

                count = int(len(get_Customers))
                row = int(count + 1)

                new_Client = check_Customer
                global current_Customer 
                current_Customer = new_Client

                customers.update_cell(row, 2, new_Client)

                new_Address = customer_Address
                global current_Address
                current_Address = new_Address

                customers.update_cell(row, 3, current_Address)

                new_Phone_Number = customer_Phone_Number
                global current_Phone_Number
                current_Phone_Number = new_Phone_Number

                customers.update_cell(row, 4, current_Phone_Number)

            new_Customer()

    if(st.button("Submit")):
        input_Customer()

def Product():

    st.header("Product Information")
    st.sidebar.subheader("Product Info")

    global product_Name
    product_Name = st.text_input("Enter product name: ")

    global product_Amount
    product_Amount = int(st.slider("Amount: ", 1, 50))

    global product_Data
    product_Data = [product_Name, product_Amount]

    def input_Product():

        sa = gspread.service_account(filename="myBusiness_credentials.json")
        sp = sa.open_by_key('15kWRPBdJrGbd5nmyN0bdK4OGFQkYeDwHQNl1vNp1rgI')

        spreadsheets = sa.openall()

        if spreadsheets:
            for spreadsheet in spreadsheets:
                print(f"Title: {spreadsheet.title}")
        else:
            print("No available spreadsheets")

        for worksheets in spreadsheet.worksheets():
            print(f"Worksheet: {worksheets.title}")

        global products
        products = spreadsheet.worksheet(title= "Products")

        index = 0

        get_Products = products.col_values(2)
        count = int(len(get_Products))

        all_Products = products.get(f"B6:B{count}")
        check_Product = product_Name

        if check_Product != all_Products[index][0]:

            for items in all_Products:
                while check_Product != all_Products[index][0]:
                    if index > int(count - 6):
                        break
                    else:
                        index += 1

        if check_Product == all_Products[index][0]:

            global current_Product
            current_Product = check_Product 

            def check_Stock():

                loc = int(index + 6)
                get_Stock = products.get(f"D{loc}", value_render_option='UNFORMATTED_VALUE')
                get_Amount = product_Amount

                global current_Stock
                current_Stock = int(get_Stock[0][0])

                global current_Amount
                current_Amount = get_Amount

                result = int(current_Stock - current_Amount)

                if result > 0:

                    products.update_cell(loc, 4, result)

                    def calculate_Price():

                        loc = int(index + 6)
                        get_Price = products.get(f"C{loc}", value_render_option='UNFORMATTED_VALUE')
                        st.text("")

                        global current_Price
                        current_Price = get_Price[0][0]
                        st.text(f"Precio {current_Product}: $ {current_Price}")

                        global net_Price
                        net_Price = int(current_Price * current_Amount)
                        st.success(f"Total: $ {net_Price}")

                    calculate_Price()

                else:

                    st.error(f"Not enough, only {current_Stock} available")

            check_Stock()

    if(st.button("Submit")):
        input_Product()

def Payment(): 

    st.header("Payment Information")
    st.sidebar.subheader("Payament Info")
 
    st.selectbox("Select payment method", ['efectivo', 'debito', 'credito'])
    st.slider("Cuotas", 1, 12)

all_Pages = {
    "Customer": Customer,
    "Product": Product,
    "Payment": Payment,
}

st.sidebar.title("Python Website")
st.sidebar.header("Purchase Information")
selected_page = st.sidebar.selectbox("Select a page", all_Pages.keys())
all_Pages[selected_page]()










