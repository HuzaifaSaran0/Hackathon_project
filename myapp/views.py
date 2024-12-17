from django.shortcuts import render

import requests
from bs4 import BeautifulSoup

# DEFAULT_IMAGE = "https://cdn.vectorstock.com/i/500p/65/30/default-image-icon-missing-picture-page-vector-40546530.jpg"


def home(request):
    return render(request, 'home.html')  # Make sure this line is indented properly


def login(request):
    return render(request, 'login.html')  # Make sure this line is indented properly


def signup(request):
    return render(request, 'signup.html')  # Make sure this line is indented properly

def about(request):
    return render(request, 'about.html')


# List of blog websites to scrape
BLOG_SITES = [
    "https://agrieducation.pk/agriculture-in-pakistan-blog/",
    "https://shrinkthatfootprint.com/agriculture-blogs/",
    "https://www.farmers.gov/blog"
]

DEFAULT_IMAGE = "https://cdn.vectorstock.com/i/500p/65/30/default-image-icon-missing-picture-page-vector-40546530.jpg"

# Valid image extensions
VALID_IMAGE_EXTENSIONS = ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'webp']

def blog_list(request):
    # Get the current site index from query parameters or default to 0
    site_index = request.GET.get('site_index', 0)  # Default to the first site
    site_index = int(site_index)  # Ensure it is an integer
    url = BLOG_SITES[site_index]  # Select the current site URL
    
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})  # Add User-Agent for better handling
    blogs = []

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        for article in soup.find_all('article'):  # Adjust tags based on the site's structure
            title_tag = article.find('h2')
            img_tag = article.find('img')
            link_tag = title_tag.find('a') if title_tag else None
            
            # Validate image format or use default image
            if img_tag and 'src' in img_tag.attrs:
                image_url = img_tag['src']
                if not any(image_url.lower().endswith(ext) for ext in VALID_IMAGE_EXTENSIONS):
                    image_url = DEFAULT_IMAGE
            else:
                image_url = DEFAULT_IMAGE

            blogs.append({
                'title': title_tag.text.strip() if title_tag else "No Title",
                'image': image_url,
                'link': link_tag['href'] if link_tag else "#"
            })
    else:
        print(f"Failed to fetch articles from {url}. Status code: {response.status_code}")

    # Determine if there are previous and next sites
    has_next = site_index < len(BLOG_SITES) - 1
    has_previous = site_index > 0
    next_index = site_index + 1 if has_next else None
    previous_index = site_index - 1 if has_previous else None

    # Pass data to the template
    return render(request, 'blogs.html', {
        'blogs': blogs,
        'has_next': has_next,
        'has_previous': has_previous,
        'next_index': next_index,
        'previous_index': previous_index
    })