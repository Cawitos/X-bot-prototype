from playwright.sync_api import sync_playwright


def create_session():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        context = browser.new_context()

        page = context.new_page()

        print("👉 Inicia sesión manualmente en X...")
        page.goto("https://x.com/login")

        input("✅ Cuando hayas iniciado sesión presiona ENTER...")

        context.storage_state(path="session/storage.json")

        print("✅ Sesión guardada correctamente")

        browser.close()


if __name__ == "__main__":
    create_session()