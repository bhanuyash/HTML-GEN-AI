import os
from htmlgen import AI_AGENT

def read_images_and_links(image_folder, links_file, template_file=None):
    images = [os.path.join(image_folder, img) for img in os.listdir(image_folder) if img.endswith(('png', 'jpg', 'jpeg', 'gif'))]
    with open(links_file, "r") as f:
        links = f.read().splitlines()
    template_html = ""
    if template_file:
        with open(template_file, "r") as f:
            template_html = f.read()
    return images, links, template_html

def main():
    ai_agent = AI_AGENT()

    image_folder = "/home/bhanupratap/HTML-Site-Gen-AI/Newsletter/Nesletter Test/Givenchy/images"
    links_file = "/home/bhanupratap/HTML-Site-Gen-AI/Newsletter/Nesletter Test/Givenchy/giv_us_vday_gift.txt"
    template_file = "/home/bhanupratap/HTML-Site-Gen-AI/Newsletter/Sample Files/Givenchy Mothers Day/index.html"  
    theme = "Valentine's Day"

    images, links, template_html = read_images_and_links(image_folder, links_file, template_file)

#   Generate HTML code based on a template
    if template_html:
        html_template_content = ai_agent.generate_html_from_template(template_html, images, links,theme)
        with open("output_template.html", "w") as f:
            f.write(html_template_content)

if __name__ == "__main__":
    main()




   

