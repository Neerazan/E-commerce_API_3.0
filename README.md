# E-commerce API

A robust REST API built with Django Rest Framework for managing an e-commerce platform. This API handles product management, shopping carts, orders, user authentication, and more.

## Features

- Product catalog management
- Shopping cart functionality
- Order processing
- User authentication and authorization
- Like system for products
- Celery integration for background tasks
- Custom permissions and pagination
- Image handling for products
- Comprehensive test suite with pytest
- Performance testing with Locust

## Tech Stack

- Django & Django REST Framework
- PostgreSQL (Compatible with Neon DB)
- Celery for async tasks
- pytest for testing
- Locust for load testing

## Project Structure

```
├── core/                  # Core functionality and user management
├── store/                 # Main e-commerce functionality
├── likes/                 # Product liking system
├── tags/                  # Product tagging system
└── storefront/           # Project configuration
```

## Prerequisites

- Python 3.x
- PostgreSQL or Neon DB account
- pip or pipenv

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd your-repository
```

2. Create a virtual environment:
```bash
# Using pip
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Or using pipenv
pipenv install
pipenv shell
```

3. Install dependencies:
```bash
# Using pip
pip install -r requirements.txt

# Or using pipenv
pipenv install
```

4. Create a `.env` file based on `.env-example`:
```
DATABASE_URL=your-database-url
EMAIL_USER=your-email
EMAIL_PASSWORD=your-email-password
ALLOWED_HOSTS=localhost,127.0.0.1
DEBUG=True
SECRET_KEY=your-secret-key
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

## API Endpoints

### Products
- `GET /store/products/` - List all products
- `GET /store/products/{id}/` - Get product details
- `POST /store/products/` - Create a product
- `PUT /store/products/{id}/` - Update a product
- `DELETE /store/products/{id}/` - Delete a product

### Cart
- `GET /store/carts/{id}/` - Get cart details
- `POST /store/carts/` - Create a cart
- `POST /store/carts/{id}/items/` - Add item to cart
- `DELETE /store/carts/{id}/items/{id}/` - Remove item from cart

### Orders
- `GET /store/orders/` - List user's orders
- `POST /store/orders/` - Create an order
- `GET /store/orders/{id}/` - Get order details

## Testing

Run the test suite:
```bash
# Using pytest
pytest

# Run specific tests
pytest store/tests/test_collections.py
```

Run load tests:
```bash
locust -f locustfiles/browse_products.py
```

## Deployment

This project is configured for deployment on Vercel. Make sure to:

1. Set up your environment variables in Vercel
2. Configure your database URL (Neon DB recommended)
3. Deploy using the Vercel CLI or GitHub integration
