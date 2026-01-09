# Account Management API Documentation

This document provides detailed information about the Account Management APIs for the Line In backend.

**Base URL:** `/api/v1/account/`

---

## 1. Dashboard Overview
Returns a summary of the user's account including profile, recent orders, default address, and wallet balance.

- **URL:** `/api/v1/account/`
- **Method:** `GET`
- **Auth Required:** Yes
- **Response:**
  ```json
  {
    "profile": {
      "user": {
        "id": 2,
        "avatar": "http://127.0.0.1:8000/media/avatars/user_2.jpg",
        "username": "thamjid",
        "full_name": "Thamjid M",
        "email": "thamjid@example.com",
        "phone": "0527627117",
        "gender": "M",
        "is_active": true
      },
      "nickname": "TJ",
      "date_of_birth": "2001-06-18",
      "country": "UAE",
      "bio": "Linen enthusiast",
      "interests": [
        { "id": 1, "name": "Mens Shirts", "slug": "mens-shirts" }
      ],
      "wallet_balance": "100.00"
    },
    "recent_orders": [...],
    "default_address": {...},
    "wallet_balance": "100.00",
    "referral_code": "LINEIN-000002"
  }
  ```

---

## 2. Profile Management
Retrieve or update secondary profile details.

- **URL:** `/api/v1/account/profile/`
- **Method:** `GET` / `PATCH`
- **Auth Required:** Yes
- **Fields (Update):**
  - `nickname` (string)
  - `date_of_birth` (date: YYYY-MM-DD)
  - `country` (string)
  - `bio` (text)
  - `interest_ids` (array of integers) - IDs of product categories

---

## 3. Address Management
Manage multiple delivery addresses.

- **URL:** `/api/v1/account/addresses/`
- **Method:** `GET` (List) / `POST` (Create)
- **Auth Required:** Yes
- **Fields (Create/Update):**
  - `address_type` (string: "home", "office", "other")
  - `full_name` (string)
  - `phone_number` (string)
  - `street_address` (text)
  - `city` (string)
  - `state` (string)
  - `country` (string)
  - `zip_code` (string)
  - `is_default` (boolean)

- **Detail URL:** `/api/v1/account/addresses/{id}/`
- **Methods:** `GET`, `PUT`, `PATCH`, `DELETE`

---

## 4. Order History
List all orders placed by the user.

- **URL:** `/api/v1/account/orders/`
- **Method:** `GET`
- **Auth Required:** Yes

---

## 5. My Reviews
List all product reviews/comments written by the user.

- **URL:** `/api/v1/account/reviews/`
- **Method:** `GET`
- **Auth Required:** Yes

---

## 6. Personal Offers
List available discount codes and promotions for the user.

- **URL:** `/api/v1/account/offers/`
- **Method:** `GET`
- **Auth Required:** Yes

---

## 7. Security (Authentication App)
While managed in the authentication app, these are relevant for the account section:

- **Update Info:** `PATCH /api/v1/auth/profile-update/` (Update core fields like email, phone, name)
- **Update Avatar:** `POST /api/v1/auth/avatar-update/`
- **Change Password:** `POST /api/v1/auth/password-reset/` (or dedicated endpoint if available)
- **Delete Account:** `POST /api/v1/auth/delete-account/` (Requires implementation or logic to set `is_active=False`)
