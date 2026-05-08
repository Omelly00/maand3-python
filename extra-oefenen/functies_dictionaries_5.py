def toon_website_info(website):
    for sleutel, waarde in website.items():
        print(sleutel, ",", waarde)

website = {
    "naam": "PiresVision",
    "type": "portfolio",
    "skills": "SEO en webdesign",
    "status": "in ontwikkeling"
}

toon_website_info(website)