# DynamicMart

DynamicMart is a powerful web application built with Django, hosted on the cloud. It provides users with dynamic product listings and seamless payment processing using the Stripe API. The application is connected to a MySQL database to manage product data efficiently.

## Features

- **Product Listings**: Browse a wide range of products dynamically displayed on the platform.
- **Payment Processing**: Securely purchase products using the integrated Stripe API.
- **Database Integration**: Utilizes a MySQL database to store and manage product information.
- **Cloud Hosting**: Hosted on the cloud for scalability and reliability.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/dynamicmart.git
   ```

2. Navigate to the project directory:

   ```bash
   cd dynamicmart
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the project directory.
   - Add the following environment variables:
     ```
     DATABASE_URL=mysql://username:password@hostname:port/database_name
     STRIPE_SECRET_KEY=your_stripe_secret_key
     ```

5. Run migrations:

   ```bash
   python manage.py migrate
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Access the application at `http://localhost:8000/` in your web browser.

## Usage

- Explore the product listings available on the platform.
- Add desired products to your cart and proceed to checkout.
- Complete the payment process securely using the integrated Stripe payment gateway.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please submit them to the [issue tracker](https://github.com/your_username/dynamicmart/issues).

## License

This project is licensed under the [MIT License](LICENSE).
