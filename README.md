
# PDF Co-Viewer Application

A web application that allows an admin to present PDF slides remotely, synchronizing page views across multiple viewers in real-time. Ideal for online presentations, remote teaching, or collaborative document reviews.

---

---

## Features

- **Real-Time Synchronization:** Admin controls the PDF slides, and all viewers see the changes instantly.
- **Web-Based Interface:** No installation required for users; accessible via any modern web browser.
- **Responsive Design:** Works on desktops, tablets, and mobile devices.
- **Scalable Backend:** Built with Flask and Flask-SocketIO to handle multiple concurrent connections.

---

## Technologies Used

- **Frontend:**
  - HTML5, CSS3, JavaScript
  - [PDF.js] for rendering PDF documents
  - [Socket.IO Client] for real-time communication

- **Backend:**
  - [Python 3.7+]
  - [Flask] 
  - [Flask-SocketIO]
  - [Eventlet]
---

## Prerequisites

- **Python 3.7 or higher**
- **pip**
- **Virtual Environment** 

---

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/sethanimesh/pdf_viewer.git
   cd pdf-co-viewer
   ```

2. **Create a Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```


4. **Place Your PDF File**

   - Place the PDF file you wish to present in `static/pdfs/`.
   - Update the `url` variable in `static/script.js` to point to your PDF file.

---

## Running the Application

1. **Activate the Virtual Environment (if not already active)**

   ```bash
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

2. **Run the Flask Application**

   ```bash
   python app.py
   ```

   - The application should be running at `http://localhost:5000`.

---

## Usage

### Admin Interface

- **Access the Admin Page**

  Open your web browser and navigate to:

  ```
  http://localhost:5000/admin
  ```

- **Controls**

  - **Previous Button:** Navigate to the previous slide.
  - **Next Button:** Navigate to the next slide.
  - **Page Indicator:** Displays the current page number and total pages.

- **Functionality**

  - Any page change by the admin is broadcast to all connected viewers in real-time.

### Viewer Interface

- **Access the Viewer Page**

  Open your web browser and navigate to:

  ```
  http://localhost:5000/
  ```

- **Functionality**

  - Viewers will see the PDF slides synchronized with the admin's controls.
  - No navigation controls are provided to ensure synchronization.

---
