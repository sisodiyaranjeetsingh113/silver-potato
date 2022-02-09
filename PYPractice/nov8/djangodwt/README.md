# Online Barcode Reader with Django
The sample demonstrates how to create an online Barcode Reader with Django, [Dynamic Web TWAIN SDK](https://www.dynamsoft.com/web-twain/overview/) and [Dynamsoft Barcode Reader SDK](https://www.dynamsoft.com/barcode-reader/overview/).

## About Dynamic Web TWAIN
- [![](https://img.shields.io/badge/Download-Offline%20SDK-orange)](https://www.dynamsoft.com/web-twain/downloads)
- [![](https://img.shields.io/badge/Get-30--day%20FREE%20Trial%20License-blue)](https://www.dynamsoft.com/customer/license/trialLicense/?product=dwt)

## About Dynamsoft Barcode Reader
- [![](https://img.shields.io/badge/Download-Offline%20SDK-orange)](https://www.dynamsoft.com/barcode-reader/downloads)
- [![](https://img.shields.io/badge/Get-30--day%20FREE%20Trial%20License-blue)](https://www.dynamsoft.com/customer/license/trialLicense/?product=dbr)
- [![](https://img.shields.io/badge/Try-Online%20Demo-brightgreen)](https://demo.dynamsoft.com/dbr_wasm/barcode_reader_javascript.html)

## Python Development Environment

- Python 3.7.9

    ```bash
    python --version
    ```

- Django 3.2.7
    
    ```bash
    python -m pip install Django
    python -m django --version
    ```

## Usage
1. Download and install [Dynamic Web TWAIN](https://www.dynamsoft.com/web-twain/downloads).
2. Create folder `static/dwt` under the project root directory.
3. Copy and paste `Dynamic Web TWAIN SDK version/Resources` folder to `static/dwt/`.
4. Install Dynamsoft Barcode Reader
    
    ```bash
    pip install dbr
    ```
5. Set license keys for Dynamic Web TWAIN and Dynamsoft Barcode Reader.
    
    ```js
    Dynamsoft.DWT.ProductKey = 'DWT-KEY';
    ```
    
    ```python
    reader.init_license("DBR-KEY")
    ```

6. Run the project:

    ```bash
    python manage.py makemigrations
    python manage.py migrate --run-syncdb
    python manage.py runserver
    ``` 
    
7. visit `127.0.0.1:8000` in a web browser.

    ![load_multi_barcode](https://www.codepool.biz/wp-content/uploads/2015/07/load_multi_barcode.png)

    ![barcode_results](https://www.codepool.biz/wp-content/uploads/2015/07/barcode_results.png)

## Blog
[Reading Barcode from Scanned Documents](https://www.codepool.biz/read-barcode-from-documents.html)

