# **Star WarDrobe**

## **Project Overview**

Welcome to **Star WarDrobe**, an e-commerce platform offering exclusive Star Wars merchandise, including toys, clothing, and action figures. This project was created as part of a Django Full-Stack Development course, adhering to agile methodologies.

Star WarDrobe combines advanced functionality with a Star Wars-inspired design, delivering a unique shopping experience for fans of the galaxy far, far away.

![Screenshot of how the app looks on different screen sizes](docs/images/responsive-screens.png)

---

## Table Of Contents:
1. [User Stories](#user-stories)
2. [Features](#features)
3. [Future Features](#future-features)
4. [Bugs and Fixes](#bugs-and-fixes)
5. [Technologies Used](#technologies-used)
6. [Testing](#testing)
7. [Deployment](#deployment)
8. [Credits](#credits)

---

## **User Stories**

User stories define the functionality and features of the Star WarDrobe from the end-users' perspective:

- As a Developer, I want to set up Django and install the supporting libraries, so that I am ready to start development.
- As a User, I want to have a smooth browsing experience across devices, so that I can easily navigate the site on any screen size.
- As a User, I want to see a custom 404 error page, so that I have a better experience when encountering broken links.
- As a Marketer, I want to implement meta tags and descriptive titles for SEO, so that our site ranks better in search results.
- As a Developer, I want to deploy the site to Heroku early, so that I can start testing in a production-like environment.
- As a Developer, I want to finalize deployment, so that the site is live and functional for users.
- As a Customer, I want to browse products easily, so that I can find items to buy.
- As a Customer, I want to add products to a shopping cart, so that I can review and purchase them.
- As a Site Admin, I want to add meta tags and SEO-friendly content, so that the site ranks higher in search engines. 
- As a User, I want to register and log in to the site, so that I can save my shopping cart and make purchases. 
- As a Developer, I want to keep the secret keys secure, so that they are not exposed in the code repository.
- As a Customer, I want to add products to a wishlist, so that I can save items for future purchase.
- As a User, I want to easily navigate the site with a clear menu, so that I can find products and information faster.
- As a Developer, I want to write and run tests for my application, so that I can ensure it is bug-free and functional.
- As a Customer, I want to save my credit card details securely, so that I can make faster purchases in the future.
- As a Customer, I want to sign up for a newsletter, so that I can get updates about new products.
- As a Customer, I want to see links to social media pages, so that I can follow the brand online.
- As a Customer, I want to checkout and complete the purchase, so that I can pay for the items in my cart.

---

## **Features**

### **1. Core Features**
- **User Authentication**:  
  Users can register, log in, log out, and manage their profiles.
  ![Registration and login](docs/images/register.png)
- **Product Management**:  
  Products are categorized into toys, clothing, and action figures. Admin users can add, edit, and delete products.
  ![Product Management](docs/images/product_management.png)
- **Shopping Bag**:  
  Users can add items to their bag, adjust quantities, and view the total price.
  ![Shoping Bag](docs/images/bag.png)
- **Checkout System**:  
  Integrated with Stripe for secure payments, allowing users to place orders and receive confirmation emails.
  ![Place Order](docs/images/payment.png)

### **2. Design and Theming**
- **Star Wars-Themed Design**:  
  The site uses a black and gold color scheme with space-themed backgrounds, and a "galactic" look.  
- **Custom 404 Page**:  
  A Star Wars-inspired 404 error page with fun references to the galaxy far, far away.  

### **3. Marketing Features**
- **Newsletter Signup**:  
  Users can subscribe to receive updates about new products and offers.
  ![Newsletter Signup](docs/images/newsletter.png)
  ![Newsletter Subscribed](docs/images/newsletter_1.png)
- **Social Media Integration**:  
  Links to a mockup Star WarDrobe Facebook page for digital marketing. 
  ![Facebook Link](docs/images/fb.png) 
  ![Facebook Mockup](docs/images/fbpage.png)
- **SEO Optimization**:  
  Includes metadata, keywords, and Open Graph tags for better discoverability.  

### **4. Agile Methodology**
- **Epics and User Stories**:  
  The project was built using an agile approach, with epics and user stories created to guide development.  
- **Kanban Board**:  
  Tasks were tracked on a Trello board to ensure efficient project management.
  ![Kanban Board](docs/images/kanban.png)

---

## **Future Features**

### 1. **Social Login Options**
- **Facebook and Googlw Integration**:
  Integrate Facebook and Google login via allauth

---

## **Bugs and Fixes**

### **Resolved Bugs**
1. **Duplicate Index URL Error**:  
   Fixed a conflict in URL patterns.

2. **Static Files Issue on Heroku**:  
   Resolved by configuring Whitenoise for static file management and ensuring correct static file paths.

3. **Search Bar Misalignment**:  
   Adjusted the Bootstrap grid system to fix alignment issues in the search bar on mobile devices.

4. **File Structure**:
   Fixed file structure by moving folders 1 directory up.

### **Known Issues**

1. **Accessibility Compliance**:  
   The site has not been fully tested for accessibility compliance.

---

## **Technologies Used**

### **Backend**
- **[Python](https://www.python.org/):** Programming language used for backend development.
- **[Django](https://www.djangoproject.com/):** Python-based web framework.
- **[SQLite](https://www.sqlite.org/):** Database used (for development).
- **[PostgreSQL](https://www.postgresql.org/):** Database used (for production).

### **Frontend**
- **[HTML](https://en.wikipedia.org/wiki/HTML):** Markup language for creating web pages.
- **[CSS](https://en.wikipedia.org/wiki/CSS):** Style sheet language for designing web pages.
- **[Bootstrap](https://getbootstrap.com/):** CSS framework for responsive design.
- **[JavaScript](https://en.wikipedia.org/wiki/JavaScript):** Programming language for interactive web elements.(jQuery and custom scripts)

### **Other Tools and Libraries**
- **[AWS](https://aws.amazon.com/):**: Cloud storage service used for managing media files.
- **[Stripe](https://stripe.com/ie):**: Payment gateway for processing transactions.
- **[Mailchimp](https://mailchimp.com/):** Email marketing platform for managing newsletters, email campaigns, and subscriber lists.
- **[Django-Allauth](https://docs.allauth.org/en/latest/):**: Authentication application for user registration, login,
     and account management.
- **[Whitenoise](https://whitenoise.readthedocs.io/en/stable/django.html):**: Simplifies serving static files in production.
- **[FontAwesome](https://fontawesome.com/):**: For icons.
- **[Google-Fonts](https://fonts.google.com/):**: For custom typography.
- **[GitHub](https://github.com/):** Version control and collaboration platform.
- **[Heroku](https://www.heroku.com/):** Platform as a service (PaaS) used for deploying the application.
- **[Gunicorn](https://gunicorn.org/):** WSGI HTTP server used for deploying Django applications.

---

## **Testing**

### PEP8 Testing Screenshots

### **Note :** Much of the code was left as it is because it got broken
![CI Python Linter](docs/images/pep8_1.png)
![CI Python Linter](docs/images/pep8_2.png)
![CI Python Linter](docs/images/pep8_3.png)
![CI Python Linter](docs/images/pep8_4.png)
![CI Python Linter](docs/images/pep8_5.png)

### Lighthouse Testing Screenshots

![Lighthouse Mobile Test](docs/images/lighthouse_mobile.png)
![Lighthouse Desktop Test](docs/images/lighthouse_desktop.png)

### Manual Testing

| Feature                  | Test Performed                                                                                  | Result  |
|--------------------------|-------------------------------------------------------------------------------------------------|---------|
| **User Registration**    | Users can register a new account and receive an email confirmation for activation.              | Pass    |
| **User Login**           | Registered users can log in to access their profile and dashboard.                              | Pass    |
| **Profile Update**       | Users can update their delivery details and contact information in their profile.               | Pass    |
| **View Products**        | Users can view all products with details like name, price, description, and image.              | Pass    |
| **Add to Cart**          | Users can add products to the shopping cart and view updated totals.                            | Pass    |
| **Remove from Cart**     | Users can remove items from the shopping cart, and totals update accordingly.                   | Pass    |
| **Checkout**             | Users can enter delivery details, view order summaries, and complete purchases via Stripe.      | Pass    |
| **Order History**        | Users can view past orders with details like order number, date, and total cost.                | Pass    |
| **Search Functionality** | Users can search for products using keywords or filter products by category.                    | Pass    |
| **Newsletter Signup**    | Users can enter their email address and successfully subscribe to the newsletter.               | Pass    |
| **Social Media Links**   | Users can access the store’s Facebook page through a link in the footer.                        | Pass    |
| **Responsiveness**       | The app layout adjusts correctly for desktop, tablet, and mobile screen sizes.                  | Pass    |

### Automated Testing

Automated tests were created using Django's test framework:

- **Views Testing:** Confirm that the correct templates are rendered and HTTP responses are as expected.
- **Models Testing:** Validate that models behave as expected, including default values and field constraints.

---

## **Installation Instructions**

1. Clone the repository:  
   ```bash
   git clone https://github.com/Salewitcher/star-wardrobe.git
   cd star-wardrobe

## Deployment

The app was deployed to Heroku using the following steps:

1. **Create Repository on GitHub:**
   - Set up a new repository using the Django template and clone it locally.

2. **Install Dependencies:**
   - Install required dependencies including Django, Pillow, and others listed in `requirements.txt`.

3. **Create Heroku App:**
   - Log in to Heroku, create a new app, and connect it to the GitHub repository.

4. **Set Environment Variables:**
   - Configure environment variables for sensitive data such as `SECRET_KEY` and `DATABASE_URL`.

5. **Deploy to Heroku:**
   - Deploy the app from the `main` branch of your GitHub repository.

6. **Migrate Database:**
   - Run database migrations on Heroku to set up the database schema.

7. **Collect Static Files:**
   - Use `python manage.py collectstatic` to collect static files for deployment.

## **Credits**

### **Content**
- Product descriptions inspired by Star Wars lore, focusing on themes, characters, and iconic elements from the franchise.  

### **Fonts**
- Google Fonts for custom typography, enhancing the Star Wars-inspired design.  


## **Acknowledgments**

- **Code Institute**: For the Django e-commerce course and guidance.  
- **OpenAI ChatGPT**: For brainstorming ideas and resolving technical issues.
- **Matt Bodden**: For mentorship, guidance, and providing valuable feedback throughout the project development process.

## **Code References**

- **Stripe Integration**: Based on the Boutique Ado walkthrough provided by Code Institute.  
- **Star Wars Theming**: Inspired by various online design tutorials and resources.  
