import os

TEMPLATE_FILE = "admin/template.html"

# 1. THE TARGET FOLDERS
PREMIUM_SITES = {
    "Srinivas_Silk_Heritage": {
        "BUSINESS_NAME": "Srinivas Silk Heritage",
        "DESIGNATION": "Fashion",
        "ABOUT_TEXT": "Exclusive Assamese Silk & Mekhela Chador",
    },
    "The_Bean_Journal": {
        "BUSINESS_NAME": "The Bean Journal",
        "DESIGNATION": "Cafe",
        "ABOUT_TEXT": "Artisan Coffee & Continental Brews",
    },
    "The_Momos_Point": {
        "BUSINESS_NAME": "The Momos Point",
        "DESIGNATION": "Restaurant",
        "ABOUT_TEXT": "Best Momos in Town",
    },
    "Urban_Hardware_Pro": {
        "BUSINESS_NAME": "Urban Hardware Pro",
        "DESIGNATION": "Hardware",
        "ABOUT_TEXT": "Premium Fittings for Modern Homes",
    },
    "FreshBasket_Daily": {
        "BUSINESS_NAME": "FreshBasket Daily",
        "DESIGNATION": "Grocery",
        "ABOUT_TEXT": "Organic Fruits & Daily Essentials",
    },
    "Glow_and_Grace_Salon": {
        "BUSINESS_NAME": "Glow & Grace Salon",
        "DESIGNATION": "Service",
        "ABOUT_TEXT": "Luxury Spa & Bridal Makeup Studio",
    }
}

def update_portfolio():
    if not os.path.exists(TEMPLATE_FILE):
        print(f"❌ Error: {TEMPLATE_FILE} not found!")
        return

    with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
        base_html = f.read()

    for folder_name, site_data in PREMIUM_SITES.items():
        if not os.path.exists(folder_name):
            print(f"⚠️ Skipping {folder_name}: Folder does not exist.")
            continue

        html = base_html

        # --- DYNAMIC ASSET SCANNER ---
        # 1. Link the local profile picture
        image_url = "profile.jpg" if os.path.exists(os.path.join(folder_name, "profile.jpg")) else "https://via.placeholder.com/150?text=Logo"

        # 2. Scan the local 'g' folder for gallery images
        gallery_js_list = []
        g_folder = os.path.join(folder_name, "g")
        if os.path.exists(g_folder):
            for file in sorted(os.listdir(g_folder)):
                if file.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
                    gallery_js_list.append(f"'g/{file}'")
        
        gallery_js_str = "[" + ",".join(gallery_js_list) + "]"

        # --- THE PAYLOAD ---
        dummy_payload = {
            "PHONE": "9876543210",
            "WHATSAPP": "9876543210",
            "ADDRESS": "G.S. Road, Guwahati",
            "MAP_LINK": "https://www.google.com/maps/search/?api=1&query=Guwahati+Assam",
            "REVIEW_LINK": "https://www.google.com/maps",
            "BOOK_LINK": "9876543210",
            "EXPIRY_DATE": "2099-12-31", 
            "SALES_WA": "916001699400",
            "DEMO_BANNER_HTML": "",
            "IMAGE_URL": image_url,
            "GALLERY_FILES_JS": gallery_js_str,
            "QR_CODE_SECTION": """
            <div class="card" style="background:linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%); border:1px solid #f59e0b; text-align:center; padding:25px; margin-bottom:22px;">
                <div style="font-size:40px; margin-bottom:10px;">🛡️</div>
                <h3 style="color:#92400e; font-size:18px; margin-bottom:5px; text-transform:uppercase; letter-spacing:0.05em;">Official Verified Profile</h3>
                <p style="color:#b45309; font-size:13px; font-weight:600;">
                    This business is digitally verified & trusted by <a href="https://ne-connect.github.io/" style="color:#d97706; font-weight:800; text-decoration:none;">NE Connect</a>.
                </p>
            </div>
            """
        }

        # Merge data and inject into HTML
        dummy_payload.update(site_data)

        for key, val in dummy_payload.items():
            html = html.replace(f"{{{key}}}", str(val))

        html = html.replace("{PAGE_URL}", f"https://ne-connect.github.io/{folder_name}/")
        html = html.replace("{ROBOTS_META}", "index, follow")

        output_path = os.path.join(folder_name, "index.html")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(html)

        print(f"✅ Upgraded: {folder_name} (Loaded {len(gallery_js_list)} gallery images)")

if __name__ == "__main__":
    print("🚀 Firing Portfolio Updater...")
    update_portfolio()
    print("✨ All premium root folders updated with local images!")