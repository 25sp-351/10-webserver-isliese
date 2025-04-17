# handler_static.py
# /static 경로에 대한 파일 서빙 처리 / Handle serving files under /static

import os

def handle_static_request(path: str) -> tuple:
    """
    요청된 경로에 따라 static 파일을 읽어 반환합니다.
    Read the static file based on the requested path.
    
    반환: (status_code, content_type, body)
    Returns: (status_code, content_type, body)
    """
    # static 폴더 기준으로 절대 경로 생성 / Build absolute file path
    static_root = os.path.join(os.getcwd(), 'static')
    target_path = os.path.join(static_root, *path.split('/')[2:])  # '/static' 이후 경로

    # 보안 처리: static 폴더 바깥 접근 방지 / Security: prevent directory traversal
    if not os.path.abspath(target_path).startswith(static_root):
        return (400, "text/plain", b"Bad Request")

    if not os.path.isfile(target_path):
        # 파일이 존재하지 않는 경우 / If file does not exist
        return (404, "text/plain", b"File Not Found")

    try:
        # 파일 읽기 (바이너리 모드) / Read file in binary mode
        with open(target_path, 'rb') as f:
            body = f.read()

        # content-type 결정 / Determine content-type
        from utils import get_content_type
        content_type = get_content_type(target_path)

        return (200, content_type, body)

    except Exception as e:
        print(f"Error serving static file: {e}")
        return (500, "text/plain", b"Internal Server Error")