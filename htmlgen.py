import json
import os
from openai import OpenAI

with open("keys.json", "r") as f:
    keys = json.load(f)

class AI_AGENT:
    def __init__(self):
        self.client = OpenAI(api_key=keys["open_ai_subscription_key"])

    def generate_html_from_content(self, images, links):
        prompt = self.construct_prompt(images, links)
        response = self.client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

    def generate_html_from_template(self, template_html, images, links,theme):
        prompt = self.construct_template_prompt(template_html, images, links,theme)
        response = self.client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

    def construct_prompt(self, images, links):
        prompt = "Create an HTML website with the following images and links:\n\n"
        for img in images:
            prompt += f"Image: {img}\n"
        for link in links:
            prompt += f"Link: {link}\n"
        prompt += "\nHTML:\n"
        return prompt

    def construct_template_prompt(self, template_html, images, links,theme):
        prompt = f"Using the following template HTML, create a new HTML website with the given images (make sure the to use the proper image names given in directory in HTML code) and links IN THE SAME STRUCTURE AS IN TEMPLATE for the {theme} theme:\n\nTemplate HTML:\n{template_html}\n\n"
        for img in images:
            prompt += f"Image: {os.path.basename(img)}\n"
        for link in links:
            prompt += f"Link: {link}\n"
        prompt += "\nNew HTML:\n"
        return prompt
