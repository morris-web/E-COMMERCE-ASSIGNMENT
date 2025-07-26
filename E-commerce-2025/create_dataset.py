from faker import Faker 
import pandas as pd 
import numpy as np 
import random

random.seed(32)

faker = Faker()
num_of_customers = 6000
data = []

for i in range(num_of_customers):
    customer_id = faker.uuid4()
    gender = random.choice(["Male","Female"])
    ages = random.randint(18,65)
    country = faker.country()
    pages_visited = random.randint(1,20)
    session_date = faker.date_time_this_year()
    session_time = round(random.uniform(1.5,30.0),2)
    purchased = random.choice([0,1])
    customer_segment = random.choice(["Bargain Hunter", "Loyal", "Impulse Buyer", "Window Shopper"])
    product_clicked = faker.word()
    category_price_ranges = {
        "Electronics": (100, 500),
        "Clothing": (10, 100),
        "Books": (5, 50),
        "Home": (20, 200),
        "Beauty": (5, 80)
    }
    product_category = random.choice(list(category_price_ranges.keys()))
    if purchased:
        price = round(random.uniform(*category_price_ranges[product_category]), 2)
    else:
        price = 0

    # Extra features
    
    device_type = random.choice(["Mobile", "Desktop", "Tablet"])
    referral_source = random.choice(["Direct", "Search", "Social", "Email"])
    loyalty_score = random.randint(0, 100)
    repeat_customer = random.choice([0, 1])
    payment_method = random.choice(["Credit Card", "PayPal", "Bank Transfer", "Crypto"])
    cart_value = price + round(random.uniform(0, 200), 2) if purchased else 0
    discount_applied = random.choice([0, 1])
    customer_segment = random.choice(["Bargain Hunter", "Loyal", "Impulse Buyer", "Window Shopper"])

    data.append([
    customer_id, gender, ages, country, pages_visited, 
    payment_method, cart_value, discount_applied, customer_segment,
    purchased, product_clicked, loyalty_score, product_category, 
    price, session_date, session_time, device_type, 
    referral_source, repeat_customer
])


# Update DataFrame columns
columns = [
    'customer_id', 'gender', 'ages', 'country', 'pages_visited', 
    'payment_method', 'cart_value', 'discount_applied', 'customer_segment',
    'purchased', 'product_clicked', 'loyalty_score','product_category', 'price', 'session_date','session_time',
    'device_type', 'referral_source', 'repeat_customer'
    
]
df = pd.DataFrame(data, columns=columns)

df.to_csv("ecommerce_data_2k25.csv", index=False)
