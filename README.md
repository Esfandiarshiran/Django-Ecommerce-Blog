# Django-Ecommerce-Blog
## Ecommerce With Full Features And A Modern Blog
 
This package is under development, and the good news is that the project is maturing. However, Django developers can develop this web application as well as deploy it, which means that you will be able to deploy and sell your downloadable (digital) products, including source code, software, pictures, themes, books, etc.
 
There are three aspects to this article.
 
#### First, you will be familiar with the features.
#### Second, you will get hints to improve it.
#### Third, you will know about the weaknesses.
 
# Features:
 
## 1-Home page:

On the home page, you have access to almost all parts of the web site.
It is worth noting that, as a backend developer, I prefer to have just a slider bar and hot items on the home page. But you can add extra components like recommended products, news, and so on based on your preferences.
In addition, users can search for the product's title, product descriptions, and product tags just in the search field.

![home](https://raw.githubusercontent.com/Esfandiarshiran/Django-Ecommerce-Blog/master/Git-Pic/home.png)



 
## 2-Account  (E_Commerce_Account)

This is an amazing account app, simple and practical. You can use it in your projects. There are almost all the essential features, like:
Forget password, reset password, simple captcha, log in with the user registration email and registration form.



Note: if you are not logged in , you will see the "Register" and "Login" buttons in the top corner right of the page.

## 3- About us  (ECommerce_About_us)

The admin or owner is able to add a description of their company. In addition, it is possible to add team members with introduction text.

![about](https://raw.githubusercontent.com/Esfandiarshiran/Django-Ecommerce-Blog/master/Git-Pic/about.png)

## 4- contact  (ECommerce_contact)

Like on other websites, in this part, users can send messages to the website owner. All messages will be stored in the database.

![contact](https://raw.githubusercontent.com/Esfandiarshiran/Django-Ecommerce-Blog/master/Git-Pic/contact.png)
## 5- Products and products category

All your products will be defined here. Additionally, there is an external table called "ProductGallery" which gives you the option to add more pictures to your product. 
Note that you can add home page sliders here.

![products_list](https://raw.githubusercontent.com/Esfandiarshiran/Django-Ecommerce-Blog/master/Git-Pic/products_list.png)    
![product_detail](https://raw.githubusercontent.com/Esfandiarshiran/Django-Ecommerce-Blog/master/Git-Pic/product_detail.png)   
## 6- Ecommerce Tag  (ECommerce_Tags)

All  tags for products are here. You can define them and then link your products to them in the products app. It needs to be considered that in this part, I did not use a third-party app like "Tagit".

## 7- Setting  (ECommerce_Setting)

In this section, the website owner should define all the general information about their website, including their address(email ,fax,phone,location,social media, etc.), website logo, website introduction, website title,Terms of service, etc. In other words, website admin does not have to manually add basic information to templates, Adding all of them are available through the admin panel.


## 8- Dashboard  (ECommerce_User_Dashboard)

Developers need to do more in this section, but the essential parts work very well already. Note that after logging in, users will see a nice dashboard here(They will be redirected to this page).
The user's wish list, orders, news, notifications, profile, and authentication have been defined here.

![dashboard](https://raw.githubusercontent.com/Esfandiarshiran/Django-Ecommerce-Blog/master/Git-Pic/dashboard.png)  

## 8- API  
Based on  "Django Rest Framework," developers have web APIs for all products and blog posts. You need to consider that both admin and users have access to these APIs as a GET method, but only admin is able to implement PUT, POST, and DELETE methods via APIs. Moreover, users can register and login via APIs, which means developers can use it in other projects with different platforms and technologies. The other factor is API documentation. In this case, I used swagger as the best one.
Note: Developers can define more APIs; everything is ready for them.

![api](https://raw.githubusercontent.com/Esfandiarshiran/Django-Ecommerce-Blog/master/Git-Pic/api.png)   

![products_api](https://raw.githubusercontent.com/Esfandiarshiran/Django-Ecommerce-Blog/master/Git-Pic/products_api.png)   

![post_api](https://raw.githubusercontent.com/Esfandiarshiran/Django-Ecommerce-Blog/master/Git-Pic/post_api.png)  

## 9- BLOG 

Now it is time to talk about "BLOG". When users hit the Blog button, located in the home page header, they encounter a modern blog.

Everyday, admin can add posts with tags to their blog. All posts have specific tags, pictures, comments, etc. The blog features a powerful search engine that searches  in all post titles, descriptions, and tags. 
Users can observe the three most popular posts on the home page in the e-commerce section. Also, on "the product list" page, the three newest posts were embedded. SEO experts know that this is one of the best ways to regularly update your e-shop home page. As an SEO-friendly option, just benefit it to be optimised for the Google search engine.

![blog_home](https://raw.githubusercontent.com/Esfandiarshiran/Django-Ecommerce-Blog/master/Git-Pic/blog_home.png)   

## 10- Site Map and RSS

ordinary features to introduce a website to Google's search engine in an efficient way.

![site_map](https://raw.githubusercontent.com/Esfandiarshiran/Django-Ecommerce-Blog/master/Git-Pic/site_map.png)  

## 11- Secure payment method, using "Stripe" as a third-party app.

Simply register on the Stripe website, then obtain your confidential information for linking the website to the payment gateway based on your personal information such as bank account, name, and so on. The question is, what do you need to obtain to connect? Let me tell you!

bank_account/stripe.api_key/stripe_total/description/data_key

The good news is that, as a last step, you just have to add the above information via the admin panel; there is no need to add it manually in the template.


# what can developers do to improve the project? 

## There are a lot of suggestions to improve efficiency and productivity for this package.
1-As you consider in this project, we are not able to add free products. The solution would not be tough. We should define a field (ex: "is free?") in the product model. Then, for each product, use if conditional to determine whether or not it is free; if it is free, we will pass it to the dashboard user to download; if not, we will send it to the user's basket(cart page).
 
2-For visiting numbers on product-detail page as well as numbers of products in the basket to show, we retrieve them continuously from the DB. Redis will come here to help us. With Redis, we can gradually store new numbers (or any other piece of information) in memory and then save them in the database after a while. Fewer requests to the database could improve the website productivity.
3-Some parts of the user dashboard are not complete.

4-Based on the Django documentation, the definitions of urls in templates could be more professional.

5- As a backend developer, I'm totally sure that frontend experts could make profound positive changes to make it  more user-friendly website. Don't hesitate to contribute.

6-I used the whole Bootstrap resource(CSS & JS) for making the user-dashboard, but you can find most of them in the main template. In other words, here we have some duplicates, and it makes the project too heavy. My suggestion is that developers can remove unnecessary ones and simply just refer them to the main resource.

7-Adding a Telegram bot or SMS text for each "buy/sell" transaction would be a good idea, sending a message or link to both parties.

8-SQLite3 has been used just for testing. It would be much better to use PostgreSQL for the project. You can simply add PostgreSQL into the setting file in the Database section.


# Disadvantages :

1-First of all, I have to admit it, the codes are not clean, and I am completely aware of the issue.

2-There are not enough comments for every piece of code. Unsurprisingly, some of them are not so readable for other developers.

3-As I mentioned previously, somewheres, it has had to be used with other technologies like Ajax, Redis, and so on to achieve the highest performance. To be exact, the fewer requests to the database, the better the performance.

Thanks  
Esfandiar Shiran
