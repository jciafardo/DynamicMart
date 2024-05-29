# DynamicMart

DynamicMart is a powerful web application built with Django, hosted on the cloud. It provides users with dynamic product listings and seamless payment processing using the Stripe API. The application is connected to a MySQL database to manage product data efficiently.

## Features

- **Product Listings**: Browse a wide range of products dynamically displayed on the platform.
- **Payment Processing**: Securely purchase products using the integrated Stripe API.
- **Database Integration**: Utilizes a MySQL database to store and manage product information.
- **User Authentication**: Features a secure login system allowing users to login/out.

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
     
    ```plaintext
    STRIPE_PUBLIC_KEY=YourKeyHere
    STRIPE_SECRET_KEY=YourKeyHere
    SECRET_KEY=YourKeyHere
    DB_PWD=YourKeyHere
    DB_ENGINE=YourKeyHere
    DB_NAME=YourKeyHere
    DB_USER=YourKeyHere
    DB_HOST=YourKeyHere
    ```

6. Run migrations:

   ```bash
   python manage.py migrate
   ```

7. Start the development server:

   ```bash
   python manage.py runserver
   ```

8. Access the application at `http://localhost:8000/` in your web browser.

## Usage

- Explore the product listings available on the platform.
- Add desired products to your cart and proceed to checkout.
- Complete the payment process securely using the integrated Stripe payment gateway.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please submit them to the [issue tracker](https://github.com/your_username/dynamicmart/issues).

## License

This project is licensed under the [MIT License](LICENSE).
