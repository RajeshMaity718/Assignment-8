import streamlit as st

# ==========================
# TASK 1 : Greeting App
# ==========================

st.title("Task 1 : Welcome to Streamlit")

name = st.text_input("Enter your name")

if st.button("Greet Me"):
    st.success(f"Hello, {name}!")

st.divider()

# ==========================
# TASK 2 : Price Calculator
# ==========================

st.title("Task 2 : Price Calculator")

product_price = st.number_input(
    "Enter Product Price",
    min_value=0.0,
    value=0.0
)

discount = st.slider(
    "Select Discount (%)",
    0,
    50,
    10
)

if st.button("Calculate Price"):

    final_price = product_price - (
        product_price * discount / 100
    )

    st.success(f"Final Price: ₹{final_price:.2f}")

    data = [
        ["Before Discount", product_price],
        ["After Discount", final_price]
    ]

    st.table(data)

st.divider()

# ==========================
# TASK 3 : Product Form
# ==========================

st.title("Task 3 : Product Form")

st.sidebar.header("Enter Product Details")

product_name = st.sidebar.text_input(
    "Product Name"
)

category = st.sidebar.selectbox(
    "Category",
    [
        "Electronics",
        "Accessories",
        "Clothing",
        "Books",
        "Food"
    ]
)

product_form_price = st.sidebar.number_input(
    "Price",
    min_value=0.0,
    value=0.0
)

if st.sidebar.button("Add Product"):

    st.success("Product Added Successfully!")

    st.subheader("Product Details")

    st.write("**Name:**", product_name)
    st.write("**Category:**", category)
    st.write("**Price:** ₹", product_form_price)

st.divider()

# ==========================
# TASK 4 : Sales Dashboard
# ==========================

st.title("Task 4 : Simple Sales Dashboard")

st.write("View monthly sales information.")

sales = {
    "January": 1200,
    "February": 1500,
    "March": 900,
    "April": 2000
}

selected_month = st.selectbox(
    "Select Month",
    list(sales.keys())
)

st.metric(
    label=f"{selected_month} Sales",
    value=f"₹{sales[selected_month]}"
)

st.subheader("Sales Chart")

st.bar_chart(sales)
