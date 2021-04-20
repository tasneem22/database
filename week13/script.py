import redis
import json

r = redis.Redis(
    host='redis-12951.c251.east-us-mz.azure.cloud.redislabs.com',
    port="12951",
    password='ducnyk-4vIfso-xynfyw')

print(r)

customers = "Customers"


def add_cust(customer_numb, first_name, last_name):
    d = {"first_name": first_name, "last_name": last_name}
    r.hset(customers, customer_numb, json.dumps(d))


orders = "Orders"


def add_ord(order_numb, customer_numb, order_date, order_total):
    d = {"customer_numb": customer_numb, "order_date": order_date, "order_total": order_total}
    r.hset(orders, order_numb, json.dumps(d))


# Add a player to the Redis sorted set against the score

customer_numb = 1
first_name = "Jane"
last_name = "Doe"

add_cust(customer_numb, first_name, last_name)

customer_numb = 2
first_name = "John"
last_name = "Doe"

add_cust(customer_numb, first_name, last_name)

customer_numb = 3
first_name = "Jane"
last_name = "Smith"

add_cust(customer_numb, first_name, last_name)

customer_numb = 4
first_name = "John"
last_name = "Smith"

add_cust(customer_numb, first_name, last_name)

customer_numb = 5
first_name = "Jane"
last_name = "Jones"

add_cust(customer_numb, first_name, last_name)

customer_numb = 6
first_name = "John"
last_name = "Jones"

add_cust(customer_numb, first_name, last_name)

# Print all the customers based on the score in descending order

print("Contents of the Redis  in descending order:")

print(r.hgetall(customers))

order_numb = 1001
customer_numb = 2
order_date = "10/10/09"
order_total = 250.85

add_ord(order_numb, customer_numb, order_date, order_total)

order_numb = 1002
customer_numb = 2
order_date = "2/21/10"
order_total = 125.89

add_ord(order_numb, customer_numb, order_date, order_total)

order_numb = 1003
customer_numb = 3
order_date = "11/15/09"
order_total = 1567.99

add_ord(order_numb, customer_numb, order_date, order_total)

order_numb = 1004
customer_numb = 4
order_date = "11/22/09"
order_total = 180.92

add_ord(order_numb, customer_numb, order_date, order_total)

order_numb = 1005
customer_numb = 4
order_date = "12/15/09"
order_total = 565.00

add_ord(order_numb, customer_numb, order_date, order_total)

order_numb = 1006
customer_numb = 6
order_date = "11/22/09"
order_total = 25.00

add_ord(order_numb, customer_numb, order_date, order_total)

order_numb = 1007
customer_numb = 6
order_date = "10/08/09"
order_total = 85.00

add_ord(order_numb, customer_numb, order_date, order_total)

order_numb = 1008
customer_numb = 6
order_date = "12/29/09"
order_total = 109.12

add_ord(order_numb, customer_numb, order_date, order_total)

print("Contents of the Redis in descending order:")

print(r.hgetall(customers))

profiles = "Profiles"


def add_profile(id_, login, name, Followers, Following, Posts):
    d = {"login": login, "name": name, "Followers": Followers, "Following": Following, "Posts": Posts}
    r.hset(profiles, id_, json.dumps(d))


posts = "Posts"


def add_post(id_, login, time, Content):
    d = {"login": login, "time": time, "Content": Content}
    r.hset(profiles, id_, json.dumps(d))


id_ = 1
login = "my_cool_username"
name = "John Back"
Followers = [2]
Following = [2]
Posts = [1]

add_profile(id_, login, name, Followers, Following, Posts)

id_ = 2
login = "my_uncool_username"
name = "John Black"
Followers = [1]
Following = [1]
Posts = []

add_profile(id_, login, name, Followers, Following, Posts)

id_ = 1
login = "my_uncool_username"
time = "11/22/09"
Content = ["WHYYYY"]

add_post(id_, login, time, Content)
