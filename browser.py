import time

from DrissionPage import ChromiumPage, ChromiumOptions
from fake_useragent import UserAgent

from settings import *


def get_graph_request_headers(debug_port: int, url: str) -> dict or None:
    """
    连接到调试模式的 Chrome 浏览器，打开指定URL，
    监听路径包含 'graph' 的数据包，并返回其请求头。

    Args:
        debug_port: Chrome 调试端口，通常是 9222。
        url: 要打开的目标 URL。

    Returns:
        如果找到包含 'graph' 的数据包，则返回其请求头字典；
        否则返回 None。
    """
    global NOW_USER_AGENT
    global NOW_PROXIES
    try:
        options = ChromiumOptions()
        NOW_USER_AGENT = UserAgent().chrome
        NOW_PROXIES = random.choice(PROXIES)

        # if PROXIES:
        #     options.set_proxy(random.choice(PROXIES))
        #     print(f"已设置代理")

        # options.headless()
        # print("已启用无头模式")

        options.set_local_port(debug_port)
        page = ChromiumPage(addr_or_opts=options)
        print(f"成功连接到 Chrome 浏览器，端口：{debug_port}")

        page.set.headers({'User-Agent': NOW_USER_AGENT})
        print(f"已设置自定义 User-Agent: {NOW_USER_AGENT}")

        page.clear_cache()  # 清空所有缓存
        print("已清空浏览器缓存")
        time.sleep(1)  # 等待缓存清空完成

        # 启动网络请求监听
        # True 表示监听所有类型的请求
        page.listen.start(True)
        print("已启动网络请求监听...")

        # 访问目标 URL
        page.get(url)
        print(f"正在访问 URL: {url}")

        # 等待一段时间，让页面加载并发出请求
        time.sleep(5)  # 根据页面复杂度和请求发出时间调整此值

        # 获取所有监听到的数据包
        packets = page.listen.steps()

        target_headers = None
        for packet in packets:
            if 'graph' in packet.url:
                print(f"找到包含 'graph' 的数据包: {packet.url}, 方法: {packet.request.method}")
                if packet.request.method == 'POST' or packet.request.method == 'GET':  # 或者其他你期望的方法
                    target_headers = packet.request.headers
                    break

        # 停止监听
        page.listen.stop()
        print("已停止网络请求监听。")

        # 关闭浏览器连接
        # page.close()
        # print("已关闭浏览器连接。")

        return target_headers

    except Exception as e:
        print(f"发生错误: {e}")
        return None


# --- 使用示例 ---
if __name__ == "__main__":
    # 在运行此脚本之前，请确保您的 Chrome 浏览器已在调试模式下启动。
    # 启动命令示例（Windows）：
    # "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\ChromeDevProfile"
    # 请根据您的 Chrome 安装路径和希望的调试端口修改。
    # --user-data-dir 是可选的，用于为调试会话创建独立的配置文件，避免干扰主浏览器。

    debug_port_to_connect = 9222
    target_url = "https://www.kickstarter.com/projects/anatoliyomelchenko/the-survival-stove-head-accessory/comments"
    # target_url = "https://httpbin.org/user-agent"

    print(f"尝试连接到端口 {debug_port_to_connect} 的 Chrome 并访问 {target_url}...")
    headers = get_graph_request_headers(debug_port_to_connect, target_url)

    if headers:
        print("\n--- 找到的数据包请求头如下 ---")
        print(headers)
    else:
        print("\n未找到包含 'graph' 的数据包，或者发生错误。")
