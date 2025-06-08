# Renters Hub

## Overview
Renters Hub is a centralized web platform developed to simplify the process of finding rental properties in Malawi. It connects property owners with potential tenants, offering verified listings, real-time updates, and a user-friendly interface to reduce inefficiencies and misinformation commonly found on platforms like Facebook, WhatsApp groups, and word of mouth.

## Key Features
- **Verified Listings**: Ensures that every property listed has been reviewed for accuracy.
- **Real-Time Property Updates**: Keeps listing data current, reducing chances of misinformation.
- **Search & Filter Functionality**: Allows users to easily search for properties based on location, type, price range, and other parameters.
- **User Authentication**: Only registered users can post listings, improving trust and reducing spam.
- **Responsive Design**: Works well on both desktop and mobile devices using Bootstrap.

## ## Tech Stack
- **Backend**: Django
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite (for development)

## Getting Started

### Prerequisites
- Python 3.8+
- Git
- Virtual Environment

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Eddie992/renters_hub.git
cd renters-hub
```

2. **Set up virtual environment**
```bash
python -m venv env
.\env\Scripts\activate  # For Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the server**
```bash
python manage.py migrate
python manage.py runserver
```

## Project Background
Malawi lacks a centralized rental property platform. Most people rely on fragmented sources such as Facebook Marketplace and WhatsApp agents. Renters Hub aims to fill this gap by offering a reliable, easy-to-use, and scalable alternative.

## License
This project is open source and available under the MIT License.