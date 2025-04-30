# response_builder.py
# HTTP 응답을 생성합니다. / Build HTTP response

def build_http_response(status_code: int, content_type: str, body: bytes) -> bytes:
    """
    주어진 상태 코드, 컨텐츠 타입, 바디로 HTTP 응답을 생성합니다.
    Build an HTTP response from the given status code, content type, and body.
    """
    # 상태 코드에 따른 상태 메시지 매핑 / Map status code to status message
    status_messages = {
        200: "OK",
        400: "Bad Request",
        404: "Not Found",
        500: "Internal Server Error",
    }
    reason = status_messages.get(status_code, "OK")

    # 헤더 생성 / Build headers
    headers = [
        f"HTTP/1.1 {status_code} {reason}",
        f"Content-Type: {content_type}",
        f"Content-Length: {len(body)}",
        "Connection: close",
        "",  # 헤더 끝 표시 / End of headers
        ""   # 바디와 구분 / Separate from body
    ]
    
    # 최종 응답 조립 / Assemble the final response
    header_data = "\r\n".join(headers).encode('utf-8')
    response = header_data + body

    return response