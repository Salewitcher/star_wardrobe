# **Star WarDrobe**

## **Project Overview**

Welcome to **Star WarDrobe**, an e-commerce platform offering exclusive Star Wars merchandise, including toys, clothing, and lightsabers. This project was created as part of a Django Full-Stack Development course, adhering to agile methodologies.

Star WarDrobe combines advanced functionality with a Star Wars-inspired design, delivering a unique shopping experience for fans of the galaxy far, far away.

---

## **Features**

### **1. Core Features**
- **User Authentication**:  
  Users can register, log in, log out, and manage their profiles.  
- **Product Management**:  
  Products are categorized into toys, clothing, and lightsabers. Admin users can add, edit, and delete products.  
- **Shopping Bag**:  
  Users can add items to their bag, adjust quantities, and view the total price.  
- **Checkout System**:  
  Integrated with Stripe for secure payments, allowing users to place orders and receive confirmation emails.  
- **User Profiles**:  
  Authenticated users can view their order history and save delivery information for faster future checkouts.

### **2. Design and Theming**
- **Star Wars-Themed Design**:  
  The site uses a black and gold color scheme with custom fonts, space-themed backgrounds, and a "galactic" look.  
- **Custom 404 Page**:  
  A Star Wars-inspired 404 error page with lightsaber animations and fun references to the galaxy far, far away.  

### **3. Marketing Features**
- **Newsletter Signup**:  
  Users can subscribe to receive updates about new products and offers.  
- **Social Media Integration**:  
  Links to a mockup Star WarDrobe Facebook page for digital marketing.  
- **SEO Optimization**:  
  Includes metadata, keywords, and Open Graph tags for better discoverability.  

### **4. Agile Methodology**
- **Epics and User Stories**:  
  The project was built using an agile approach, with epics and user stories created to guide development.  
- **Kanban Board**:  
  Tasks were tracked on a Trello board to ensure efficient project management.

---

## **Bugs and Fixes**

### **Resolved Bugs**
1. **Duplicate Index URL Error**:  
   Fixed a conflict in URL patterns by removing the redundant `index` path in `recipes/urls.py`.

2. **Static Files Issue on Heroku**:  
   Resolved by configuring Whitenoise for static file management and ensuring correct static file paths.

3. **Search Bar Misalignment**:  
   Adjusted the Bootstrap grid system to fix alignment issues in the search bar on mobile devices.

### **Known Issues**
1. **Newsletter Signup Form**:  
   The form currently does not have backend functionality for sending emails.

2. **Accessibility Compliance**:  
   The site has not been fully tested for accessibility compliance.

---

## **Technologies Used**

### **Backend**
- **Python 3.12**
- **Django 4.2**
- **SQLite** (for development)
- **PostgreSQL** (for production)

### **Frontend**
- **HTML5**, **CSS3**, **Bootstrap 4.6.2**
- **JavaScript** (jQuery and custom scripts)

### **Other Tools and Libraries**
- **Cloudinary**: For media storage.
- **Stripe**: For payment processing.
- **Django-Allauth**: For authentication.
- **Whitenoise**: For static file handling.
- **FontAwesome**: For icons.
- **Google Fonts**: For custom typography.

---

## **Testing**

### **Manual Testing**
1. **User Authentication Flows**:  
   Registration, login, and logout functionality tested successfully.
   
2. **Add-to-Bag and Checkout**:  
   Verified that users can add products, adjust quantities, and complete the checkout process.

3. **Admin Product Management**:  
   Tested CRUD operations for managing products.

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

## **Code References**

- **Stripe Integration**: Based on the Boutique Ado walkthrough provided by Code Institute.  
- **Star Wars Theming**: Inspired by various online design tutorials and resources.  
