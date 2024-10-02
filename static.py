# -*- coding: utf-8 -*-
"""Untitled89.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cRdIvbARwkvr6d1mZUjggvNQj1dgvgPq
"""

import requests
from bs4 import BeautifulSoup
import re

def scrape_and_clean(url):
    try:
        # Fetch the webpage content
        response = requests.get(url)
        response.raise_for_status()  # Ensure the request was successful
        soup = BeautifulSoup(response.content, 'lxml')

        # Remove unwanted sections (headers, footers, nav bars, images, etc.)
        for tag in ['head', 'footer', 'nav', 'img']:
            for element in soup.find_all(tag):
                element.decompose()

        # Remove elements by class or id typically associated with ads, sidebars, etc.
        for class_or_id in [
            'ad', 'ads', 'advertisement', 'sponsored', 'promo', 'promotion',
            'banner', 'banner-ad', 'marketing', 'popup', 'popup-ad', 'sidebar',
            'side', 'widget', 'related', 'suggestions', 'recommendation', 'similar',
            'trending', 'popular', 'recent-posts', 'comments', 'comment-section',
            'respond', 'discussion', 'reply', 'feedback', 'social', 'share', 'like',
            'follow', 'twitter', 'facebook', 'instagram'
        ]:
            for element in soup.find_all(class_=re.compile(class_or_id), id=re.compile(class_or_id)):
                element.decompose()

        # Extract the main body content
        body = soup.find('body')
        if body is None:
            body = soup  # Fallback to entire content if no body tag is found

        text = body.get_text(separator='\n')

        # Clean the text
        text = text.lower()  # Convert to lowercase
        text = re.sub(r'\s+', ' ', text)  # Normalize whitespace
        text = re.sub(r'[^a-zA-Z0-9\s\.\,\;\:\!\?]', '', text)  # Remove special characters, except common punctuations

        # Phrases to remove
        phrases_to_remove = [
            'marketing',
            'advertisement',
            'contact',
            'cookie'
        ]

        # Filter out lines with unwanted phrases
        filtered_lines = []
        for line in text.splitlines():
            if not any(phrase in line for phrase in phrases_to_remove):
                filtered_lines.append(line)

        cleaned_text = '\n'.join(filtered_lines)

        return cleaned_text.strip()

    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return ""

def main(urls):
    for url in urls:
        print(f"Scraping {url}...")
        content = scrape_and_clean(url)
        if content:
            # Extract the last part of the URL to use as the output file name
            output_file = url.split('/')[-1].split('?')[0] + '.txt'
            with open(output_file, 'w') as f:
                f.write(content)
            print(f"Scraping completed. Content saved to {output_file}")
        else:
            print(f"No content found for {url}. Skipping file creation.")

if __name__ == "__main__":
    urls = [
        "https://docs.ros.org/en/jazzy/Tutorials/Intermediate.html"
    ]
    main(urls)

import requests
from bs4 import BeautifulSoup
import re

def scrape_and_clean(url):
    try:
        # Fetch the webpage content
        response = requests.get(url)
        response.raise_for_status()  # Ensure the request was successful
        soup = BeautifulSoup(response.content, 'lxml')

        # Remove unwanted sections (headers, footers, nav bars, images, etc.)
        for tag in ['head', 'footer', 'nav', 'img']:
            for element in soup.find_all(tag):
                element.decompose()

        # Remove elements by class or id typically associated with ads, sidebars, etc.
        for class_or_id in [
            'ad', 'ads', 'advertisement', 'sponsored', 'promo', 'promotion',
            'banner', 'banner-ad', 'marketing', 'popup', 'popup-ad', 'sidebar',
            'side', 'widget', 'related', 'suggestions', 'recommendation', 'similar',
            'trending', 'popular', 'recent-posts', 'comments', 'comment-section',
            'respond', 'discussion', 'reply', 'feedback', 'social', 'share', 'like',
            'follow', 'twitter', 'facebook', 'instagram'
        ]:
            for element in soup.find_all(class_=re.compile(class_or_id), id=re.compile(class_or_id)):
                element.decompose()

        # Extract the main body content
        body = soup.find('body')
        if body is None:
            body = soup  # Fallback to entire content if no body tag is found

        text = body.get_text(separator='\n')

        # Clean the text
        text = text.lower()  # Convert to lowercase
        text = re.sub(r'\s+', ' ', text)  # Normalize whitespace
        text = re.sub(r'[^a-zA-Z0-9\s\.\,\;\:\!\?]', '', text)  # Remove special characters, except common punctuations

        # Phrases to remove
        phrases_to_remove = [
            'marketing',
            'advertisement',
            'contact',
            'cookie'
        ]

        # Filter out lines with unwanted phrases
        filtered_lines = []
        for line in text.splitlines():
            if not any(phrase in line for phrase in phrases_to_remove):
                filtered_lines.append(line)

        cleaned_text = '\n'.join(filtered_lines)

        return cleaned_text.strip()

    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return ""

def main(urls):
    failed_urls = []  # List to store URLs that failed to produce content
    for url in urls:
        print(f"Scraping {url}...")
        content = scrape_and_clean(url)
        if content:
            # Extract the last part of the URL to use as the output file name
            output_file = url.split('/')[-1].split('?')[0] + '.txt'
            with open(output_file, 'w') as f:
                f.write(content)
            print(f"Scraping completed. Content saved to {output_file}")
        else:
            print(f"No content found for {url}.")
            failed_urls.append(url)  # Add to failed URLs list

    # Print out all URLs that failed
    if failed_urls:
        print("\nThe following URLs did not produce any content:")
        for failed_url in failed_urls:
            print(failed_url)

if __name__ == "__main__":
    urls = [
        "https://docs.ros.org/en/jazzy/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Nodes/Understanding-ROS2-Nodes.html",
        "https://docs.ros.org/en/jazzy/Concepts/Advanced/About-Build-System.html",
        "https://docs.ros.org/en/jazzy/How-To-Guides/Releasing/Releasing-a-Package.html#releasing-a-package",
        "https://docs.ros.org/en/jazzy/Installation/Windows-Install-Binary.html",
        "https://docs.ros.org/en/jazzy/Releases/Beta1-Overview.html",
        "https://docs.ros.org/en/jazzy/Tutorials/Intermediate/Tf2/Writing-A-Tf2-Static-Broadcaster-Cpp.html",
        "http://docs.ros.org/en/jazzy/p/rclcpp_components/generated/index.html",
        "https://docs.ros.org/en/jazzy/Tutorials/Beginner-CLI-Tools/Launching-Multiple-Nodes/Launching-Multiple-Nodes.html",
        "https://docs.ros.org/en/jazzy/How-To-Guides/Ament-CMake-Python-Documentation.html",
        "https://docs.ros.org/en/galactic/How-To-Guides/Releasing/Releasing-a-Package.html",
        "https://docs.ros.org/en/foxy/Installation.html",
        "https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Topic-Statistics.html",
        "https://docs.ros.org/en/jazzy/The-ROS2-Project/Contributing.html#setting-up-your-development-environment",
        "https://docs.ros.org/en/jazzy/Installation/DDS-Implementations/Install-Connext-Security-Plugins.html",
        "https://docs.ros.org/en/eloquent/Related-Projects.html",
        "https://docs.ros.org/en/jazzy/Installation/DDS-Implementations.html#id1",
        "https://design.ros2.org/articles/ros_on_dds.html",
        "https://docs.ros.org/en/foxy/How-To-Guides/RQt-Source-Install.html",
        "https://docs.ros.org/en/foxy/Releases.html",
        "https://docs.ros.org/en/jazzy/Related-Projects.html#further-community-projects"
    ]
    main(urls)