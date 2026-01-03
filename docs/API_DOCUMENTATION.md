# Line In Backend API Documentation

**Project:** Line In Backend  
**API Version:** v1  
**Base URL:** `http://localhost:8000/api/v1/`  
**Authentication:** JWT (JSON Web Tokens)

---

## Table of Contents

1. [Authentication Endpoints](#authentication-endpoints)
2. [Products Endpoints](#products-endpoints)
3. [Bookings Endpoints](#bookings-endpoints)
4. [Cart Endpoints](#cart-endpoints)
5. [Contacts Endpoints](#contacts-endpoints)
6. [Health Check](#health-check)

---

## Authentication Endpoints

### 1. Register User
- **URL:** `/api/v1/auth/register/`
- **Method:** `POST`
- **Authentication:** Not Required
- **Description:** Register a new user account

**Request Body:**
```json
{
  "username": "string (required, unique)",
  "email": "string (required, valid email, unique)",
  "full_name": "string (required)",
  "phone": "string (optional)",
  "password": "string (required, min length 8)",
  "password2": "string (required, must match password)",
  "avatar": "file (optional, image file)"
}
```

**Response (201 - Created):**
```json
{
  "user": {
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com",
    "full_name": "John Doe",
    "phone": "1234567890",
    "gender": "M/F",
    "avatar": "http://...image_url...",
    "is_active": true
  },
  "message": "User registered successfully. Please check your email for login credentials."
}
```

**Error Responses:**
- `400 Bad Request` - Validation errors (duplicate email/username, password mismatch, etc.)

---

### 2. Check Username/Email Availability
- **URL:** `/api/v1/auth/user-check/`
- **Method:** `GET`
- **Authentication:** Not Required
- **Description:** Check if username or email already exists

**Query Parameters:**
```
username=string (optional)
email=string (optional)
```

**Response (200 - OK):**
```json
{
  "status": true  // true if user exists, false if not found
}
```

---

### 3. Login User
- **URL:** `/api/v1/auth/login/`
- **Method:** `POST`
- **Authentication:** Not Required
- **Description:** Login with username/email and password

**Request Body:**
```json
{
  "username": "string (username or email, required)",
  "password": "string (required)"
}
```

**Response (200 - OK):**
```json
{
  "access": "jwt_access_token_string",
  "refresh": "jwt_refresh_token_string",
  "user": {
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com",
    "full_name": "John Doe",
    "phone": "1234567890",
    "gender": "M/F",
    "avatar": "http://...image_url...",
    "is_active": true
  }
}
```

**Error Responses:**
- `400 Bad Request` - Missing credentials
- `401 Unauthorized` - Invalid credentials

---

### 4. Refresh Access Token
- **URL:** `/api/v1/auth/token/refresh/`
- **Method:** `POST`
- **Authentication:** Not Required
- **Description:** Get a new access token using refresh token

**Request Body:**
```json
{
  "refresh": "jwt_refresh_token_string"
}
```

**Response (200 - OK):**
```json
{
  "access": "new_jwt_access_token_string"
}
```

---

### 5. Logout User
- **URL:** `/api/v1/auth/logout/`
- **Method:** `POST`
- **Authentication:** Required (JWT)
- **Description:** Logout the authenticated user

**Request Body:**
```json
{
  "refresh": "jwt_refresh_token_string"
}
```

**Response (200 - OK):**
```json
{
  "message": "Successfully logged out"
}
```

---

### 6. Get User Profile
- **URL:** `/api/v1/auth/profile/`
- **Method:** `GET`
- **Authentication:** Required (JWT)
- **Description:** Get authenticated user's profile information

**Response (200 - OK):**
```json
{
  "id": 1,
  "username": "john_doe",
  "email": "john@example.com",
  "full_name": "John Doe",
  "phone": "1234567890",
  "gender": "M/F",
  "avatar": "http://...image_url...",
  "is_active": true
}
```

---

### 7. Update User Profile
- **URL:** `/api/v1/auth/profile/update/`
- **Method:** `PUT` or `PATCH`
- **Authentication:** Required (JWT)
- **Description:** Update user profile information

**Request Body:**
```json
{
  "username": "string (optional)",
  "email": "string (optional)",
  "full_name": "string (optional)",
  "phone": "string (optional)",
  "gender": "string (optional, M/F)"
}
```

**Response (200 - OK):**
```json
{
  "id": 1,
  "username": "john_doe_updated",
  "email": "john.updated@example.com",
  "full_name": "John Doe Updated",
  "phone": "1234567890",
  "gender": "M",
  "avatar": "http://...image_url...",
  "is_active": true
}
```

---

### 8. Update User Avatar
- **URL:** `/api/v1/auth/profile/avatar/`
- **Method:** `POST` or `PATCH`
- **Authentication:** Required (JWT)
- **Description:** Update user avatar/profile picture

**Request Body (multipart/form-data):**
```
avatar: file (image file, required)
```

**Response (200 - OK):**
```json
{
  "id": 1,
  "username": "john_doe",
  "email": "john@example.com",
  "full_name": "John Doe",
  "phone": "1234567890",
  "gender": "M/F",
  "avatar": "http://...new_image_url...",
  "is_active": true
}
```

---

### 9. Forgot Password
- **URL:** `/api/v1/auth/forgot-password/`
- **Method:** `POST`
- **Authentication:** Not Required
- **Description:** Request password reset (sends email with token)

**Request Body:**
```json
{
  "username": "string (username or email, required)"
}
```

**Response (200 - OK):**
```json
{
  "message": "If an account exists with this email, a password reset link has been sent."
}
```

---

### 10. Reset Password
- **URL:** `/api/v1/auth/reset-password/`
- **Method:** `POST`
- **Authentication:** Not Required
- **Description:** Reset password using token from email

**Request Body:**
```json
{
  "username": "string (username or email, required)",
  "token": "string (token from email, required)",
  "new_password": "string (new password, min length 8, required)"
}
```

**Response (200 - OK):**
```json
{
  "message": "Password reset successfully"
}
```

**Error Responses:**
- `400 Bad Request` - Invalid token or username

---

### 11. Google Signup
- **URL:** `/api/v1/auth/google/signup/`
- **Method:** `POST`
- **Authentication:** Not Required
- **Description:** Register/Signup with Google OAuth2

**Request Body:**
```json
{
  "id_token": "string (Google ID token, required)"
}
```

**Response (201 - Created):**
```json
{
  "user": {
    "id": 1,
    "username": "user@example.com",
    "email": "user@example.com",
    "full_name": "User Name",
    "phone": "",
    "gender": "",
    "avatar": "http://...google_profile_picture...",
    "is_active": true
  },
  "access": "jwt_access_token_string",
  "refresh": "jwt_refresh_token_string"
}
```

---

### 12. Google Signin
- **URL:** `/api/v1/auth/google/signin/`
- **Method:** `POST`
- **Authentication:** Not Required
- **Description:** Login with Google OAuth2

**Request Body:**
```json
{
  "id_token": "string (Google ID token, required)"
}
```

**Response (200 - OK):**
```json
{
  "user": {
    "id": 1,
    "username": "user@example.com",
    "email": "user@example.com",
    "full_name": "User Name",
    "phone": "",
    "gender": "",
    "avatar": "http://...google_profile_picture...",
    "is_active": true
  },
  "access": "jwt_access_token_string",
  "refresh": "jwt_refresh_token_string"
}
```

---

## Products Endpoints

### 1. Get Featured Products
- **URL:** `/api/v1/products/featured/`
- **Method:** `GET`
- **Authentication:** Not Required
- **Description:** Get 4 most recently added featured products

**Response (200 - OK):**
```json
[
  {
    "id": 1,
    "name": "Product Name",
    "slug": "product-name",
    "description": "Product description",
    "price": 99.99,
    "image": "http://...image_url...",
    "min_people": 1,
    "max_people": 10,
    "rating": 4.5,
    "is_active": true,
    "created_at": "2024-01-03T10:00:00Z"
  }
]
```

---

### 2. Get Product List
- **URL:** `/api/v1/products/list/`
- **Method:** `GET`
- **Authentication:** Not Required
- **Description:** Get all active products (paginated)

**Query Parameters:**
```
page=integer (optional, default 1)
page_size=integer (optional, default 10)
```

**Response (200 - OK):**
```json
{
  "count": 50,
  "next": "http://...next_page_url...",
  "previous": null,
  "results": [
    {
      "id": 1,
      "name": "Product Name",
      "slug": "product-name",
      "price": 99.99,
      "image": "http://...image_url...",
      "min_people": 1,
      "max_people": 10,
      "is_active": true
    }
  ]
}
```

---

### 3. Get Product Details
- **URL:** `/api/v1/products/{slug}/detail/`
- **Method:** `GET`
- **Authentication:** Not Required
- **Description:** Get detailed information about a specific product

**Path Parameters:**
```
slug: string (product slug, required)
```

**Response (200 - OK):**
```json
{
  "id": 1,
  "name": "Product Name",
  "slug": "product-name",
  "description": "Detailed product description",
  "price": 99.99,
  "image": "http://...image_url...",
  "min_people": 1,
  "max_people": 10,
  "rating": 4.5,
  "is_active": true,
  "created_at": "2024-01-03T10:00:00Z"
}
```

---

### 4. Get Product Reviews
- **URL:** `/api/v1/products/{product_slug}/reviews/`
- **Method:** `GET`
- **Authentication:** Required (JWT)
- **Description:** Get all reviews/comments for a product (paginated)

**Path Parameters:**
```
product_slug: string (product slug, required)
```

**Query Parameters:**
```
page=integer (optional, default 1)
page_size=integer (optional, default 5)
```

**Response (200 - OK):**
```json
{
  "count": 10,
  "next": "http://...next_page_url...",
  "previous": null,
  "results": [
    {
      "id": 1,
      "author": "john_doe",
      "message": "Great product!",
      "rating": 5,
      "created_at": "2024-01-03T10:00:00Z"
    }
  ]
}
```

---

### 5. Create Product Review
- **URL:** `/api/v1/products/{product_slug}/reviews/`
- **Method:** `POST`
- **Authentication:** Required (JWT)
- **Description:** Create a new review/comment for a product

**Path Parameters:**
```
product_slug: string (product slug, required)
```

**Request Body:**
```json
{
  "message": "string (review text, required)",
  "rating": "integer (1-5, required)"
}
```

**Response (201 - Created):**
```json
{
  "id": 1,
  "author": "john_doe",
  "message": "Great product!",
  "rating": 5,
  "created_at": "2024-01-03T10:00:00Z"
}
```

---

### 6. Reply to Review
- **URL:** `/api/v1/products/reviews/{comment_id}/reply/`
- **Method:** `POST`
- **Authentication:** Required (JWT)
- **Description:** Reply to a product review/comment

**Path Parameters:**
```
comment_id: integer (comment ID, required)
```

**Request Body:**
```json
{
  "reply": "string (reply text, required)"
}
```

**Response (201 - Created):**
```json
{
  "detail": "Reply posted."
}
```

---

### 7. Get Advertisements
- **URL:** `/api/v1/products/advertisement/`
- **Method:** `GET`
- **Authentication:** Not Required
- **Description:** Get top 5 active advertisements

**Response (200 - OK):**
```json
[
  {
    "id": 1,
    "title": "Advertisement Title",
    "image": "http://...image_url...",
    "link": "http://...",
    "is_active": true
  }
]
```

---

### 8. Get Favorites List
- **URL:** `/api/v1/products/favorites/list-create/`
- **Method:** `GET`
- **Authentication:** Required (JWT)
- **Description:** Get user's favorite products (paginated)

**Query Parameters:**
```
page=integer (optional, default 1)
page_size=integer (optional, default 5)
```

**Response (200 - OK):**
```json
{
  "count": 5,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "product": {
        "id": 1,
        "name": "Product Name",
        "price": 99.99
      },
      "created_at": "2024-01-03T10:00:00Z"
    }
  ]
}
```

---

### 9. Add to Favorites
- **URL:** `/api/v1/products/favorites/list-create/`
- **Method:** `POST`
- **Authentication:** Required (JWT)
- **Description:** Add a product to user's favorites

**Request Body:**
```json
{
  "product_id": "integer (product ID, required)"
}
```

**Response (201 - Created):**
```json
{
  "id": 1,
  "product": {
    "id": 1,
    "name": "Product Name",
    "price": 99.99
  },
  "created_at": "2024-01-03T10:00:00Z"
}
```

---

### 10. Remove from Favorites
- **URL:** `/api/v1/products/favorites/delete/{product_id}/`
- **Method:** `DELETE`
- **Authentication:** Required (JWT)
- **Description:** Remove a product from user's favorites

**Path Parameters:**
```
product_id: integer (product ID, required)
```

**Response (204 - No Content):**
```
(Empty response)
```

---

## Bookings Endpoints

### 1. Create Booking
- **URL:** `/api/v1/bookings/create/`
- **Method:** `POST`
- **Authentication:** Not Required (but can be authenticated)
- **Description:** Create a new booking

**Request Body:**
```json
{
  "booking_date": "string (date in YYYY-MM-DD format, required)",
  "booking_time": "string (time in HH:MM format, optional)",
  "number_of_guests": "integer (required)",
  "special_requests": "string (optional)",
  "products": [
    {
      "product": "integer (product ID, required)",
      "quantity": "integer (required)"
    }
  ]
}
```

**Response (201 - Created):**
```json
{
  "message": "Your booking has been created successfully! A confirmation email has been sent.",
  "booking": {
    "id": 1,
    "booking_number": "BOOK-2024-001",
    "booking_date": "2024-01-15",
    "booking_time": "10:00",
    "number_of_guests": 4,
    "special_requests": "Window seat preferred",
    "status": "pending",
    "payment_status": "pending",
    "total_amount": 399.96,
    "created_at": "2024-01-03T10:00:00Z"
  }
}
```

**Error Responses:**
- `400 Bad Request` - Invalid booking data or product constraints

---

### 2. Get My Bookings
- **URL:** `/api/v1/bookings/my-bookings/`
- **Method:** `GET`
- **Authentication:** Required (JWT)
- **Description:** Get authenticated user's bookings (paginated)

**Query Parameters:**
```
page=integer (optional, default 1)
page_size=integer (optional, default 10)
```

**Response (200 - OK):**
```json
{
  "count": 5,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "booking_number": "BOOK-2024-001",
      "booking_date": "2024-01-15",
      "booking_time": "10:00",
      "number_of_guests": 4,
      "status": "confirmed",
      "payment_status": "paid",
      "total_amount": 399.96,
      "created_at": "2024-01-03T10:00:00Z"
    }
  ]
}
```

---

### 3. Get Booking Details
- **URL:** `/api/v1/bookings/{booking_number}/details/`
- **Method:** `GET`
- **Authentication:** Not Required
- **Description:** Get detailed information about a specific booking

**Path Parameters:**
```
booking_number: string (booking number, required)
```

**Response (200 - OK):**
```json
{
  "id": 1,
  "booking_number": "BOOK-2024-001",
  "user": {
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com"
  },
  "booking_date": "2024-01-15",
  "booking_time": "10:00",
  "number_of_guests": 4,
  "special_requests": "Window seat preferred",
  "status": "confirmed",
  "payment_status": "paid",
  "subtotal": 399.96,
  "tax": 40.00,
  "total_amount": 439.96,
  "payments": [
    {
      "id": 1,
      "amount": 439.96,
      "payment_method": "stripe",
      "payment_status": "paid",
      "transaction_id": "ch_1234567890",
      "payment_date": "2024-01-03T10:00:00Z"
    }
  ],
  "checkout_url": "http://...checkout_session_url...",
  "created_at": "2024-01-03T10:00:00Z",
  "updated_at": "2024-01-03T10:30:00Z"
}
```

---

### 4. Update Booking Status (Admin Only)
- **URL:** `/api/v1/bookings/{booking_number}/update-status/`
- **Method:** `PATCH`
- **Authentication:** Required (JWT, Admin Only)
- **Description:** Update booking status (admin only)

**Path Parameters:**
```
booking_number: string (booking number, required)
```

**Request Body:**
```json
{
  "status": "string (pending, confirmed, in_progress, completed, cancelled)",
  "admin_notes": "string (optional)"
}
```

**Response (200 - OK):**
```json
{
  "message": "Booking status updated successfully",
  "booking": {
    "id": 1,
    "booking_number": "BOOK-2024-001",
    "status": "confirmed",
    "admin_notes": "Additional notes",
    "total_amount": 439.96
  }
}
```

**Error Responses:**
- `403 Forbidden` - User is not an admin

---

### 5. Cancel Booking
- **URL:** `/api/v1/bookings/{booking_number}/cancel/`
- **Method:** `POST`
- **Authentication:** Not Required
- **Description:** Cancel a booking

**Path Parameters:**
```
booking_number: string (booking number, required)
```

**Request Body:**
```json
{
  "reason": "string (optional, cancellation reason)",
  "email": "string (required if not authenticated, guest email)"
}
```

**Response (200 - OK):**
```json
{
  "message": "Booking cancelled successfully",
  "booking_number": "BOOK-2024-001",
  "reason": "Changed plans"
}
```

**Error Responses:**
- `403 Forbidden` - Invalid email or no permission to cancel
- `400 Bad Request` - Cannot cancel completed/cancelled bookings

---

### 6. Create Payment (Manual)
- **URL:** `/api/v1/bookings/{booking_number}/payment/`
- **Method:** `POST`
- **Authentication:** Not Required
- **Description:** Create manual payment record for a booking

**Path Parameters:**
```
booking_number: string (booking number, required)
```

**Request Body:**
```json
{
  "amount": "decimal (required)",
  "payment_method": "string (cash, bank_transfer, stripe, etc., required)",
  "transaction_id": "string (optional)",
  "notes": "string (optional)"
}
```

**Response (201 - Created):**
```json
{
  "id": 1,
  "amount": 439.96,
  "payment_method": "bank_transfer",
  "payment_status": "pending",
  "transaction_id": "TXN-2024-001",
  "payment_date": "2024-01-03T10:00:00Z",
  "notes": "Payment notes"
}
```

---

### 7. Create Stripe Checkout Session
- **URL:** `/api/v1/bookings/{booking_number}/create-checkout-session/`
- **Method:** `POST`
- **Authentication:** Not Required
- **Description:** Create a Stripe checkout session for payment

**Path Parameters:**
```
booking_number: string (booking number, required)
```

**Response (200 - OK):**
```json
{
  "checkout_url": "https://checkout.stripe.com/pay/...",
  "session_id": "cs_live_...",
  "booking_number": "BOOK-2024-001"
}
```

---

### 8. Get Booking Payment Status
- **URL:** `/api/v1/bookings/{booking_number}/payment-status/`
- **Method:** `GET`
- **Authentication:** Not Required
- **Description:** Get payment status of a booking

**Path Parameters:**
```
booking_number: string (booking number, required)
```

**Response (200 - OK):**
```json
{
  "booking_number": "BOOK-2024-001",
  "payment_status": "paid",
  "total_amount": 439.96,
  "paid_amount": 439.96,
  "remaining_amount": 0,
  "payments": [
    {
      "id": 1,
      "amount": 439.96,
      "payment_method": "stripe",
      "payment_status": "paid",
      "transaction_id": "ch_1234567890",
      "payment_date": "2024-01-03T10:00:00Z"
    }
  ]
}
```

---

### 9. Verify Payment
- **URL:** `/api/v1/bookings/verify-payment/`
- **Method:** `POST`
- **Authentication:** Not Required
- **Description:** Verify a Stripe payment

**Request Body:**
```json
{
  "session_id": "string (Stripe session ID, required)"
}
```

**Response (200 - OK):**
```json
{
  "message": "Payment verified successfully",
  "booking_number": "BOOK-2024-001",
  "payment_status": "paid"
}
```

---

### 10. Stripe Webhook
- **URL:** `/api/v1/bookings/stripe-webhook/`
- **Method:** `POST`
- **Authentication:** Not Required
- **Description:** Handle Stripe webhook events (checkout.session.completed)

**Handled Events:**
- `checkout.session.completed` - Updates booking payment status to paid

---

## Cart Endpoints

### 1. Get Active Cart
- **URL:** `/api/v1/cart/get-my-cart/`
- **Method:** `GET`
- **Authentication:** Required (JWT)
- **Description:** Get user's active cart (creates if doesn't exist)

**Response (200 - OK):**
```json
{
  "id": 1,
  "user": 1,
  "status": "open",
  "cart_items": [
    {
      "id": 1,
      "product": {
        "id": 1,
        "name": "Product Name",
        "price": 99.99
      },
      "quantity": 2,
      "unit_price": 99.99,
      "booking_date": "2024-01-15",
      "booking_time": "10:00",
      "special_requests": "No requests",
      "created_at": "2024-01-03T10:00:00Z"
    }
  ],
  "subtotal": 199.98,
  "tax": 19.99,
  "total_amount": 219.97,
  "is_empty": false,
  "created_at": "2024-01-03T10:00:00Z"
}
```

---

### 2. Add to Cart
- **URL:** `/api/v1/cart/add-to-cart/`
- **Method:** `POST`
- **Authentication:** Required (JWT)
- **Description:** Add product to user's active cart

**Request Body:**
```json
{
  "product_id": "integer (product ID, required)",
  "quantity": "integer (required)",
  "booking_date": "string (date in YYYY-MM-DD format, required)",
  "booking_time": "string (time in HH:MM format, optional)",
  "special_requests": "string (optional)"
}
```

**Response (201 - Created):**
```json
{
  "message": "Item added to cart!!",
  "data": {
    "id": 1,
    "user": 1,
    "status": "open",
    "cart_items": [
      {
        "id": 1,
        "product": {
          "id": 1,
          "name": "Product Name",
          "price": 99.99
        },
        "quantity": 2,
        "unit_price": 99.99,
        "booking_date": "2024-01-15",
        "booking_time": "10:00"
      }
    ],
    "subtotal": 199.98,
    "tax": 19.99,
    "total_amount": 219.97
  }
}
```

---

### 3. Update Cart Item
- **URL:** `/api/v1/cart/items/{item_id}/`
- **Method:** `PUT` or `PATCH`
- **Authentication:** Required (JWT)
- **Description:** Update cart item quantity or details

**Path Parameters:**
```
item_id: integer (cart item ID, required)
```

**Request Body:**
```json
{
  "quantity": "integer (optional)",
  "booking_date": "string (optional)",
  "booking_time": "string (optional)",
  "special_requests": "string (optional)"
}
```

**Response (200 - OK):**
```json
{
  "id": 1,
  "product": {
    "id": 1,
    "name": "Product Name",
    "price": 99.99
  },
  "quantity": 3,
  "unit_price": 99.99,
  "booking_date": "2024-01-15",
  "booking_time": "10:00",
  "special_requests": "No requests"
}
```

---

### 4. Remove Item from Cart
- **URL:** `/api/v1/cart/items/{item_id}/remove/`
- **Method:** `DELETE`
- **Authentication:** Required (JWT)
- **Description:** Remove a specific item from cart

**Path Parameters:**
```
item_id: integer (cart item ID, required)
```

**Response (204 - No Content):**
```json
{
  "message": "Item removed from cart"
}
```

---

### 5. Clear Cart
- **URL:** `/api/v1/cart/clear-cart/`
- **Method:** `DELETE`
- **Authentication:** Required (JWT)
- **Description:** Clear all items from user's active cart

**Response (200 - OK):**
```json
{
  "message": "Cart cleared"
}
```

---

### 6. Checkout Cart
- **URL:** `/api/v1/cart/checkout/`
- **Method:** `POST`
- **Authentication:** Required (JWT)
- **Description:** Checkout cart and create order

**Request Body:**
```json
{
  "customer_name": "string (required)",
  "customer_email": "string (valid email, required)",
  "customer_phone": "string (required)",
  "special_instructions": "string (optional)"
}
```

**Response (201 - Created):**
```json
{
  "message": "Order created successfully!",
  "order": {
    "id": 1,
    "user": 1,
    "order_number": "ORD-2024-001",
    "cart": 1,
    "customer_name": "John Doe",
    "customer_email": "john@example.com",
    "customer_phone": "1234567890",
    "special_instructions": "Careful handling",
    "status": "pending",
    "subtotal": 199.98,
    "tax": 19.99,
    "total_amount": 219.97,
    "created_at": "2024-01-03T10:00:00Z"
  }
}
```

**Error Responses:**
- `404 Not Found` - No active cart found
- `400 Bad Request` - Cart is empty

---

### 7. Get Orders List
- **URL:** `/api/v1/cart/orders/`
- **Method:** `GET`
- **Authentication:** Required (JWT)
- **Description:** Get user's orders (paginated)

**Query Parameters:**
```
page=integer (optional, default 1)
page_size=integer (optional, default 10)
```

**Response (200 - OK):**
```json
{
  "count": 3,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "order_number": "ORD-2024-001",
      "customer_name": "John Doe",
      "status": "completed",
      "total_amount": 219.97,
      "created_at": "2024-01-03T10:00:00Z"
    }
  ]
}
```

---

### 8. Get Order Details
- **URL:** `/api/v1/cart/orders/{order_id}/`
- **Method:** `GET`
- **Authentication:** Required (JWT)
- **Description:** Get detailed information about a specific order

**Path Parameters:**
```
order_id: integer (order ID, required)
```

**Response (200 - OK):**
```json
{
  "id": 1,
  "order_number": "ORD-2024-001",
  "user": 1,
  "cart": 1,
  "customer_name": "John Doe",
  "customer_email": "john@example.com",
  "customer_phone": "1234567890",
  "special_instructions": "Careful handling",
  "status": "completed",
  "subtotal": 199.98,
  "tax": 19.99,
  "total_amount": 219.97,
  "order_items": [
    {
      "id": 1,
      "product": {
        "id": 1,
        "name": "Product Name"
      },
      "quantity": 2,
      "unit_price": 99.99
    }
  ],
  "created_at": "2024-01-03T10:00:00Z"
}
```

---

### 9. Complete Order Payment
- **URL:** `/api/v1/cart/orders/{order_id}/complete-payment/`
- **Method:** `POST`
- **Authentication:** Required (JWT)
- **Description:** Complete payment for an order

**Path Parameters:**
```
order_id: integer (order ID, required)
```

**Request Body:**
```json
{
  "payment_method": "string (stripe, cash, bank_transfer, etc., required)",
  "transaction_id": "string (optional)"
}
```

**Response (200 - OK):**
```json
{
  "message": "Payment processed successfully",
  "order": {
    "id": 1,
    "order_number": "ORD-2024-001",
    "status": "completed",
    "payment_status": "paid"
  }
}
```

---

### 10. Get Cart Details by ID
- **URL:** `/api/v1/cart/{cart_id}/detail/`
- **Method:** `GET`
- **Authentication:** Required (JWT)
- **Description:** Get detailed information about a specific cart

**Path Parameters:**
```
cart_id: integer (cart ID, required)
```

**Response (200 - OK):**
```json
{
  "id": 1,
  "user": 1,
  "status": "open",
  "cart_items": [
    {
      "id": 1,
      "product": {
        "id": 1,
        "name": "Product Name"
      },
      "quantity": 2,
      "unit_price": 99.99
    }
  ],
  "subtotal": 199.98,
  "tax": 19.99,
  "total_amount": 219.97
}
```

---

## Contacts Endpoints

### 1. Create Contact Message
- **URL:** `/api/v1/contacts/new/`
- **Method:** `POST`
- **Authentication:** Not Required
- **Description:** Send a contact/enquiry message

**Request Body:**
```json
{
  "name": "string (required)",
  "email": "string (valid email, required)",
  "subject": "string (required)",
  "message": "string (required)"
}
```

**Response (201 - Created):**
```json
{
  "message": "Your contact has been submitted successfully"
}
```

**Error Responses:**
- `400 Bad Request` - Missing or invalid fields

**Additional Info:**
- Sends email to admin with enquiry details
- Sends confirmation email to customer

---

## Health Check

### 1. Health Check
- **URL:** `/healthz/`
- **Method:** `GET`
- **Authentication:** Not Required
- **Description:** Check API health status

**Response (200 - OK):**
```json
{
  "status": "healthy"
}
```

---

### 2. Index/Home
- **URL:** `/`
- **Method:** `GET`
- **Authentication:** Not Required
- **Description:** Get API index/home information

**Response (200 - OK):**
```json
{
  "message": "Line In API v1",
  "version": "1.0"
}
```

---

## Authentication Header Format

For authenticated endpoints, include the JWT token in the Authorization header:

```
Authorization: Bearer {access_token}
```

Example:
```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

---

## Error Response Format

All error responses follow this format:

```json
{
  "error": "Error message",
  "details": {
    "field_name": ["error details"]
  }
}
```

Common HTTP Status Codes:
- `200 OK` - Success
- `201 Created` - Resource created successfully
- `204 No Content` - Success (no response body)
- `400 Bad Request` - Invalid request data
- `401 Unauthorized` - Missing or invalid authentication
- `403 Forbidden` - Permission denied
- `404 Not Found` - Resource not found
- `500 Internal Server Error` - Server error

---

## Pagination

Endpoints with pagination follow this format:

**Query Parameters:**
```
page=integer (page number, default 1)
page_size=integer (items per page, varies by endpoint)
```

**Response:**
```json
{
  "count": 100,
  "next": "http://...next_page_url...",
  "previous": "http://...previous_page_url...",
  "results": [
    { /* item objects */ }
  ]
}
```

---

## Rate Limiting

Currently, no rate limiting is implemented. Please use the API responsibly.

---

## Important Notes

1. **JWT Tokens:** Access tokens expire. Use the refresh token to get a new access token.
2. **Booking Numbers:** Used to uniquely identify bookings. Format: `BOOK-YYYY-XXXXX`
3. **Order Numbers:** Used to uniquely identify orders. Format: `ORD-YYYY-XXXXX`
4. **Stripe Integration:** Payment processing uses Stripe. Webhook integration handles automatic payment updates.
5. **Email Notifications:** Welcome email, booking confirmations, and contact responses are sent asynchronously using Celery.
6. **Google OAuth2:** ID tokens from Google authentication are required for Google signup/signin.

---

## Integration Guide for Frontend

### Step 1: Setup Headers
Always include the Authorization header for authenticated requests:
```javascript
const headers = {
  'Authorization': `Bearer ${accessToken}`,
  'Content-Type': 'application/json'
}
```

### Step 2: Authentication Flow
1. User registers via `/api/v1/auth/register/` or `/api/v1/auth/google/signup/`
2. User logs in via `/api/v1/auth/login/` or `/api/v1/auth/google/signin/`
3. Store `access` and `refresh` tokens from login response
4. Use `access` token for authenticated requests
5. When `access` token expires, use `refresh` token to get new `access` token

### Step 3: Handle Errors
Always check response status and handle errors gracefully:
```javascript
if (response.status === 401) {
  // Refresh token and retry
} else if (response.status === 400) {
  // Show validation errors to user
}
```

### Step 4: Cart & Checkout Flow
1. User adds products to cart via `/api/v1/cart/add-to-cart/`
2. User reviews cart via `/api/v1/cart/get-my-cart/`
3. User proceeds to checkout via `/api/v1/cart/checkout/`
4. For payment, either:
   - Use Stripe checkout session: `/api/v1/bookings/{booking_number}/create-checkout-session/`
   - Or create manual booking: `/api/v1/bookings/create/`

### Step 5: Booking Flow
1. Create booking via `/api/v1/bookings/create/`
2. Get booking details via `/api/v1/bookings/{booking_number}/details/`
3. Process payment via Stripe or manual method
4. Verify payment status via `/api/v1/bookings/{booking_number}/payment-status/`

---

**Last Updated:** January 3, 2026  
**API Version:** v1  
**Backend Framework:** Django REST Framework
