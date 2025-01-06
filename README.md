# Fast API Hospital Project

**پروژه API بیمارستان با FastAPI**

## 📜 معرفی پروژه | Project Overview

این پروژه یک API است که با استفاده از **FastAPI** برای مدیریت اطلاعات بیمارستانی پیاده‌سازی شده است. هدف این پروژه ایجاد یک سیستم کارآمد برای مدیریت بیماران، پزشکان، پذیرش‌ها، آزمایش‌ها و سوابق پزشکی است.

This project is an API built with **FastAPI** for managing hospital data. The goal is to provide an efficient system for handling patients, doctors, admissions, tests, and medical records.

---

## 🛠 ویژگی‌ها | Features

- مدیریت اطلاعات بیماران، پزشکان، پذیرش‌ها و سوابق.
- پیاده‌سازی سیستم احراز هویت با JWT.
- قابلیت درج، ویرایش و حذف اطلاعات از پایگاه داده.
- استفاده از FastAPI و SQLAlchemy برای ارتباط با پایگاه داده.
- تست‌های مربوط به API با استفاده از pytest.

---

## 🚀 شروع کار | Getting Started

### پیش‌نیازها | Prerequisites

برای اجرای این پروژه به موارد زیر نیاز دارید:

- **Python 3.7+**
- **FastAPI**
- **SQLAlchemy**
- **Databases** (برای ارتباط با پایگاه داده)

### نصب | Installation

1. ابتدا به دایرکتوری پروژه بروید.
2. محیط مجازی ایجاد کنید:

    ```bash
    python -m venv venv
    ```

3. محیط مجازی را فعال کنید:

    **برای ویندوز:**

    ```bash
    venv\Scripts\activate
    ```

    **برای لینوکس/macOS:**

    ```bash
    source venv/bin/activate
    ```

4. وابستگی‌ها را نصب کنید:

    ```bash
    pip install -r requirements.txt
    ```


### راه‌اندازی پروژه | Running the Project

برای راه‌اندازی پروژه، دستور زیر را اجرا کنید:

```bash
uvicorn main:app --reload


###📋 ساختار پروژه | Project Structure

.
├── main.py              # فایل اصلی API
├── models.py            # مدل‌های پایگاه داده
├── schemas.py           # طرح‌های داده (Pydantic models)
├── database.py          # تنظیمات پایگاه داده
├── auth.py              # مدیریت احراز هویت
├── requirements.txt     # وابستگی‌های پروژه
├── tests/               # پوشه تست‌ها
│   ├── test_main.py     # تست‌های مربوط به API
└── README.md            # مستندات پروژه
