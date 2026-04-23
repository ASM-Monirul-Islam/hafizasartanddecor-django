# 🎨 Hafiza's Art & Decor — E-Commerce Platform

A full-featured web-based e-commerce platform for handcrafted home decor products, built with Django. This platform replaces a manual order management process (previously handled via social media and phone calls) with a streamlined, scalable, and user-friendly online storefront.

---

## 📖 About

**Hafiza's Art & Decor** is a online store specializing in handcrafted home decor products. Every item is made on-demand by hand, making each piece unique.

This platform empowers customers to browse products, manage a cart, and place orders — all without needing to create an account. At the same time, the admin (seller) gets a dedicated panel to manage products, categories, and orders with real-time status updates and optional email notifications.

---

## 🌐 Live Demo

The platform is live at:

🔗 **[Hafiza's Art & Decor](https://hafizasartanddecor.pythonanywhere.com)**

---

## ✨ Features

### 🛍️ Customer
- Browse all products and view detailed product pages
- Add products to cart and manage quantities
- Place orders **without registration or login**
- Choose delivery method: **Inside Dhaka** or **Outside Dhaka** (delivery charges vary)
- Payment method: **Cash on Delivery only**
- Track order status using Order ID

### 🔧 Admin (Seller)
- Secure login panel (accessible via navbar logo or footer link)
- Add, update, and delete **product categories**
- Add, update, and delete **product listings** with images
- View and manage all incoming orders
- Update order statuses (Pending → Confirmed → Delivered, etc.)
- Receive **email notifications** for new orders *(optional, see setup)*
- Send **order confirmation emails** to customers *(optional, see setup)*

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 4.x, Python 3.11 |
| Frontend | HTML, CSS, JavaScript |
| Database | SQLite (default) / PostgreSQL |
| Image Handling | Pillow |
| Email | Django Email (SMTP) |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone <repo-url>
cd hafizas-art-and-decor
```

### 2. Create & Activate Virtual Environment

```bash
python -m venv venv
.\venv\Scripts\activate        # Windows
# source venv/bin/activate     # macOS/Linux
```

### 3. Install Dependencies

```bash
pip install django
python.exe -m pip install --upgrade pip
python -m pip install Pillow
```

Or install from requirements file (if available):

```bash
pip install -r requirements.txt
```

### 4. Run the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

---

## 🔑 Admin Access

To access the admin panel, click the **logo in the navbar** or the **"Admin Login"** link in the footer.

| Field | Value |
|---|---|
| Username | `admin` |
| Password | `admin123` |

---

## 📬 Email Notification System (Optional)

The platform includes an email notification system for:
- Notifying the admin when a new order is placed
- Sending order confirmation emails to customers when order status changes

> ⚠️ **Email credentials are intentionally hidden for privacy.** The email system is disabled by default and must be configured manually.

### Step 1 — Set Email Credentials

Open `hafizas_art_and_decor/settings.py` and fill in your Gmail (or SMTP) credentials:

```python
EMAIL_HOST_USER = 'youremail@example.com'
EMAIL_HOST_PASSWORD = '**** **** **** ****'  # Use an App Password, not your regular password
```

> 💡 For Gmail, generate an **App Password** from your Google Account security settings.

### Step 2 — Uncomment Email Calls in Views

#### `order/views.py` — Lines 49–53

Uncomment the following block to send emails when a new order is placed:

```python
try:
    send_new_order_mail(order.order_id, order.name, order.email, order.phone, order.shipping_method, order.address, order.total_price)
    send_user_order_mail(order.order_id, order.name, order.phone, order.email, order.shipping_method, order.total_price, order.address)
except Exception as e:
    print(e)
```

#### `admin_panel/views.py` — Lines 126, 143, 166

Uncomment the following line at each location to send confirmation emails on order status updates:

```python
send_confirmation_mail(order.order_id, order.email, order.name, order.order_status)
```

> ℹ️ If email credentials are not set, the platform will continue to function normally — only email notifications will be skipped.

---

## 📁 Project Structure

```
hafizas-art-and-decor/
├── accounts/           # Admin authentication
├── cart/               # Cart session management
├── order/              # Order placement and tracking
├── admin_panel/        # Admin dashboard (products, categories, orders)
├── homepage/           # Home page view
├── products/           # Product listing and detail views
├── base/               # Shared utilities (session, models, email helpers)
├── templates/          # All HTML templates
├── public/
│   ├── static/         # CSS, JS, and static assets
│   └── media/          # Uploaded product images
├── hafizas_art_and_decor/  # Project settings and URL config
├── manage.py
└── requirements.txt
```

---

## ⚙️ Configuration Notes

- **No stock management** — Products are handcrafted on-demand; inventory tracking is not required.
- **Payment** — Cash on Delivery only. No payment gateway integration.
- **Delivery charges** vary based on location: Inside Dhaka vs. Outside Dhaka.
- **Database** — SQLite is used by default. Can be switched to PostgreSQL in `settings.py`.

---

## 🌐 Browser Support

| Browser | Supported |
|---|---|
| Google Chrome | ✅ |
| Mozilla Firefox | ✅ |
| Microsoft Edge | ✅ |

---

## 📄 License

This project is for personal/educational use. All handcrafted product images and branding belong to **Hafiza's Art & Decor**.
