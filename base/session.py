def get_session_id(request):
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key