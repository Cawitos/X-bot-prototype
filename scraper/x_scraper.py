from playwright.sync_api import sync_playwright
from utils.text_filter import match_exact
import time


def open_replies(page):
    try:
        btn = page.locator("text=Leer")
        if btn.count() > 0:
            btn.first.click()
            page.wait_for_timeout(3000)
    except:
        pass


def auto_scroll(page, max_scroll):

    last_height = 0

    for _ in range(max_scroll):
        page.mouse.wheel(0, 4000)
        time.sleep(2)

        new_height = page.evaluate("document.body.scrollHeight")

        if new_height == last_height:
            break

        last_height = new_height


def extract_replies(page, targets):

    results = []

    articles = page.locator("article").all()

    for article in articles:
        try:
            username = article.locator("a[role='link']").first.inner_text()
            comment = article.locator("div[data-testid='tweetText']").inner_text()
            time_data = article.locator("time").first.inner_text()

            if match_exact(comment, targets):
                results.append(f"{username} | {comment} // {time_data}")

        except:
            continue

    return results


def get_replies(post_url, targets, max_scroll=10):

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        context = browser.new_context(
            storage_state="session/storage.json"
        )

        page = context.new_page()

        page.goto(post_url)
        page.wait_for_timeout(4000)

        open_replies(page)
        auto_scroll(page, max_scroll)

        replies = extract_replies(page, targets)

        browser.close()

        return replies