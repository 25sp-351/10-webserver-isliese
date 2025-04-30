# utils.py
# 유틸리티 함수 모음 / Utility functions

def get_content_type(file_path: str) -> str:
    """
    파일 확장자에 따라 Content-Type을 반환합니다.
    Return the Content-Type based on the file extension.
    """
    # 파일 확장자에 따른 매핑 / Mapping file extensions to content types
    content_types = {
        ".html": "text/html",
        ".htm": "text/html",
        ".css": "text/css",
        ".js": "application/javascript",
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".gif": "image/gif",
        ".txt": "text/plain",
        ".pdf": "application/pdf",
        ".json": "application/json",
        ".ico": "image/x-icon",
    }

    # 파일 확장자 추출 / Extract file extension
    import os
    _, ext = os.path.splitext(file_path)

    # 소문자로 변환하여 매칭 / Match with lowercase extension
    return content_types.get(ext.lower(), "application/octet-stream")