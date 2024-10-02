import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data Loading
def load_data():
    customers_df = pd.read_csv("data/olist_customers_dataset.csv")
    geolocation_df = pd.read_csv("data/olist_geolocation_dataset.csv")
    order_items_df = pd.read_csv("data/olist_order_items_dataset.csv")
    order_payment_df = pd.read_csv("data/olist_order_payments_dataset.csv")
    order_review_df = pd.read_csv("data/olist_order_reviews_dataset.csv")
    orders_df = pd.read_csv("data/olist_orders_dataset.csv")
    product_category_df = pd.read_csv("data/product_category_name_translation.csv")
    product_name_df = pd.read_csv("data/olist_products_dataset.csv")
    seller_df = pd.read_csv("data/olist_sellers_dataset.csv")
    
    return customers_df, order_items_df, order_payment_df, order_review_df, orders_df, product_category_df, product_name_df, seller_df

# Load Data
customers_df, order_items_df, order_payment_df, order_review_df, orders_df, product_category_df, product_name_df, seller_df = load_data()

# Sidebar
st.sidebar.title("E-Commerce Data Analysis")
page = st.sidebar.selectbox("Choose a Page", ["Creator","Company",  "Top Cities", "Top Sellers", "Top Products", "Product Rating","RFM Analysis"])

if page == "Creator":
    st.title("Data Creator")

    # Creator Information
    st.write("""
    **Name**: Ghani Fauzan  
    **Email**: ghanifauzan5@gmail.com  
    **Project**: E-Commerce Data Analysis by Olist
    """)

    # Profile Image
    st.image(
        "https://firebasestorage.googleapis.com/v0/b/bangkit-dashboard/o/production%2F2024-B2%2Fprofiles%2F35105d0d-6153-430e-b963-ec191b6805f6.jpeg?alt=media&token=4b3de331-09eb-4efa-aba3-b58c1ac2d808",
        width=150
    )

    # Project Description
    st.subheader("Project Description")
    st.write("""
    This project involves analyzing an e-commerce dataset provided by Olist. 
    The goal of this project is to answer key business questions, such as identifying the most profitable products and the most popular product categories.
    """)

    # Tools and Libraries Used
    st.subheader("Tools and Libraries Used")
    st.write("""
    - **Pandas**
    - **Matplotlib & Seaborn**
    - **Streamlit**
    """)


#Page: Company 
elif page == "Company":
    st.title("Data and Company Overview")

    # Company Description
    st.subheader("Company")
    st.write("""
    This company is an **e-commerce platform** offering a wide range of products across various categories, 
    including electronics, fashion, beauty, health, and more. 
    The company partners with thousands of sellers to provide products to millions of customers 
    nationwide, enabling them to easily shop online.
    """)

    st.write("""
    This dataset is generously provided by Olist, the largest department store in the Brazilian market. 
    Olist connects small businesses from all over Brazil to multiple sales channels, offering a seamless 
    experience through a single contract. Merchants can sell their products via Olist Store and ship them 
    directly to customers using Olist's logistics partners. You can learn more on our website: www.olist.com.
    After a customer purchases a product from Olist Store, the seller is notified to fulfill the order. Once the customer receives the product or by the estimated delivery date, they receive a satisfaction survey via email where they can rate their purchase experience and provide comments.
    """)

    # Dataset Description
    st.subheader("Dataset Description")

    st.write("""
    The dataset used in this project covers various aspects of the e-commerce platform, 
    such as customer data, products, sales, payments, and reviews. 
    Below is a description of each dataset:
    """)

    # Customers Data Description
    st.subheader("1. Customers Data")
    st.write("""
    **customers_dataset.csv**: This dataset contains information about the platform's customers. 
    Each row represents a customer with the following features:
    - `customer_id`: Unique ID for each customer.
    - `customer_unique_id`: Unique ID indicating a non-duplicated customer.
    - `customer_zip_code_prefix`: Customer's postal code.
    - `customer_city`: City where the customer resides.
    - `customer_state`: State where the customer resides.
    """)

    # Orders Data Description
    st.subheader("2. Orders Data")
    st.write("""
    **orders_dataset.csv**: This dataset contains information about the orders placed on the platform.
    - `order_id`: Unique ID for each order.
    - `customer_id`: Unique ID identifying the customer who placed the order.
    - `order_status`: Status of the order (delivered, returned, etc.).
    - `order_purchase_timestamp`: Timestamp when the order was placed.
    - `order_approved_at`: Timestamp when the order was approved.
    - `order_delivered_carrier_date`: Date the order was handed to the carrier.
    - `order_delivered_customer_date`: Date the order was delivered to the customer.
    - `order_estimated_delivery_date`: Estimated delivery date.
    """)

    # Order Items Data Description
    st.subheader("3. Order Items Data")
    st.write("""
    **order_items_dataset.csv**: This dataset contains details of the items in each order.
    - `order_id`: ID of the order.
    - `order_item_id`: ID of the item within the order.
    - `product_id`: ID of the ordered product.
    - `seller_id`: ID of the seller providing the product.
    - `shipping_limit_date`: Shipping deadline for the product.
    - `price`: Price of the product.
    - `freight_value`: Shipping cost.
    """)

    # Products Data Description
    st.subheader("4. Products Data")
    st.write("""
    **products_dataset.csv**: This dataset contains information about the products available on the platform.
    - `product_id`: Unique ID for the product.
    - `product_category_name`: Product category.
    - `product_name_length`: Length of the product name.
    - `product_description_length`: Length of the product description.
    - `product_photos_qty`: Number of product photos.
    - `product_weight_g`: Product weight in grams.
    - `product_length_cm`, `product_height_cm`, `product_width_cm`: Product dimensions.
    """)

    # Payments Data Description
    st.subheader("5. Payments Data")
    st.write("""
    **order_payments_dataset.csv**: This dataset contains information about customer payments.
    - `order_id`: Order ID.
    - `payment_sequential`: Sequential number of the payment within an order.
    - `payment_type`: Type of payment (credit card, voucher, bank transfer, etc.).
    - `payment_installments`: Number of installments chosen by the customer.
    - `payment_value`: Total payment value.
    """)

    # Reviews Data Description
    st.subheader("6. Reviews Data")
    st.write("""
    **order_reviews_dataset.csv**: This dataset contains information about customer reviews of purchased products.
    - `review_id`: Unique ID of the review.
    - `order_id`: ID of the order being reviewed.
    - `review_score`: Review score given by the customer (1-5).
    - `review_comment_title`: Title of the review.
    - `review_comment_message`: Content of the review.
    - `review_creation_date`: Date the review was created.
    - `review_answer_timestamp`: Date the review was answered.
    """)

    # Sellers Data Description
    st.subheader("7. Sellers Data")
    st.write("""
    **sellers_dataset.csv**: This dataset contains information about the sellers on the platform.
    - `seller_id`: Unique ID of the seller.
    - `seller_zip_code_prefix`: Seller's postal code.
    - `seller_city`: City where the seller operates.
    - `seller_state`: State where the seller operates.
    """)

    # Geolocation Data Description
    st.subheader("8. Geolocation Data")
    st.write("""
    **geolocation_dataset.csv**: This dataset contains geolocation information used for shipping.
    - `geolocation_zip_code_prefix`: Location postal code.
    - `geolocation_lat`: Latitude of the location.
    - `geolocation_lng`: Longitude of the location.
    - `geolocation_city`: City of the location.
    - `geolocation_state`: State of the location.
    """)

    st.write("This dataset enables a comprehensive analysis of customer behavior, seller performance, and logistics and payment processes.")


# Page: Top Products
elif page == "Top Products":
    st.title("Top Products Analysis")

    # Merge product_name_df and product_category_df
    products_df = pd.merge(
        left=product_name_df,
        right=product_category_df,
        how="left",
        left_on="product_category_name",
        right_on="product_category_name"
    )

    # Top Product Categories
    st.subheader("Top Product Categories")
    top_categories = products_df.groupby(by="product_category_name_english").product_id.nunique().sort_values(ascending=False).head()
    
    fig, ax = plt.subplots()
    sns.barplot(x=top_categories.values, y=top_categories.index, ax=ax)
    ax.set_title("Top 5 Most Popular Product")
    st.pyplot(fig)

# Page: Top Cities by Freight Value
elif page == "Top Cities":
    st.title("Top Cities by Freight Value")

    # Merge order_items and seller
    order_item_seller_df = pd.merge(
        left=order_items_df,
        right=seller_df,
        how="left",
        left_on="seller_id",
        right_on="seller_id"
    )

    # Top Cities by Freight Value
    top_freight_cities = order_item_seller_df.groupby(by="seller_city").agg({
        "price": "sum",
        "freight_value": "sum"
    }).sort_values(by='freight_value', ascending=False).head()

    st.subheader("Top Cities with Highest Freight Value")
    st.dataframe(top_freight_cities)

    # Visualization
    fig, ax = plt.subplots()
    sns.barplot(x=top_freight_cities.index, y=top_freight_cities['freight_value'], ax=ax)
    ax.set_title("Top 5 Cities by Freight Value")
    st.pyplot(fig)

# Page: Top Sellers by Sales
elif page == "Top Sellers":
    st.title("Top Sellers by Sales")

    # Top Sellers by Price
    top_sellers = order_items_df.groupby(by="seller_id").agg({
        'price': 'sum',
        "freight_value": "sum"
    }).sort_values(by='price', ascending=False).head()

    st.subheader("Top Sellers by Total Sales (Price)")
    st.dataframe(top_sellers)

    # Visualization
    fig, ax = plt.subplots()
    sns.barplot(x=top_sellers.index, y=top_sellers['price'], ax=ax)
    ax.set_title("Top 5 Sellers by Sales")
    st.pyplot(fig)

# Page: RFM Analysis
elif page == "RFM Analysis":
    st.title("RFM Analysis")

    # Merge data yang diperlukan untuk menghitung RFM
    customers_orders_df = pd.merge(customers_df, orders_df, on='customer_id')
    customers_payment_df = pd.merge(customers_orders_df, order_payment_df, on='order_id')

    # Pastikan kolom tanggal dalam format datetime
    customers_payment_df['order_purchase_timestamp'] = pd.to_datetime(customers_payment_df['order_purchase_timestamp'])

    # Hitung RFM
    rfm_df = customers_payment_df.groupby(by="customer_id", as_index=False).agg({
        "order_purchase_timestamp": "max",  
        "order_id": "nunique", 
        "payment_value": "sum"
    })
    rfm_df.columns = ["customer_id", "last_purchase", "frequency", "monetary"]

    # Recency
    recent_date = customers_payment_df["order_purchase_timestamp"].max()
    rfm_df["recency"] = rfm_df["last_purchase"].apply(lambda x: (recent_date - pd.to_datetime(x)).days)


    rfm_df.drop(columns=["last_purchase"], inplace=True)

    # Visualisasi RFM
    st.subheader("RFM Analysis Results")
    fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(20, 6))

    # Plot Recency
    sns.barplot(y="recency", x="customer_id", data=rfm_df.sort_values(by="recency", ascending=True).head(), ax=ax[0])
    ax[0].set_title("Top 5 Customers by Recency")
    ax[0].set_ylabel("Recency (Days)")
    ax[0].tick_params(axis='x', rotation=90)

    # Plot Frequency
    sns.barplot(y="frequency", x="customer_id", data=rfm_df.sort_values(by="frequency", ascending=False).head(), ax=ax[1])
    ax[1].set_title("Top 5 Customers by Frequency")
    ax[1].set_ylabel("Number of Orders")
    ax[1].tick_params(axis='x', rotation=90)

    # Plot Monetary
    sns.barplot(y="monetary", x="customer_id", data=rfm_df.sort_values(by="monetary", ascending=False).head(), ax=ax[2])
    ax[2].set_title("Top 5 Customers by Monetary")
    ax[2].set_ylabel("Total Payment Value (Monetary)")
    ax[2].tick_params(axis='x', rotation=90)

    st.pyplot(fig)

# Page: Product Rating
elif page == "Product Rating":
    st.title("Product Rating Analysis")

    # Rating Distribution
    rating_counts = order_review_df.groupby(by="review_score").review_id.nunique().sort_values(ascending=False)

    st.subheader("Distribution of Product Ratings")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=rating_counts.index, y=rating_counts.values, ax=ax)
    ax.set_title("Number of Reviews by Rating Score")
    ax.set_xlabel("Review Score")
    ax.set_ylabel("Number of Reviews")
    st.pyplot(fig)