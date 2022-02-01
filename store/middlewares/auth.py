from django.shortcuts import redirect, reverse


def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print("Auth Middleware1")
        # print(dict(request.session))
        # for key, value in request.META.items():
        #     print(key, " = ", value)
        # print(len(dict(request.META)))
        # print(request.META['PATH_INFO'])

        request_url = request.META["PATH_INFO"]
        print("RRurl >> ", request_url)

        if not request.session.get("customer_id"):
            return redirect(f'/login/?request_url={request_url}')

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware

# def my_decorator(func):
#
#     def inner_func(text):
#
#         text = "Pre----" + text
#
#         rtext = func(text)
#
#         rtext = rtext + "----Post"
#
#         return rtext
#
#     return inner_func
#
#
# @my_decorator
# def my_func(text):
#     text = text.upper()
#
#     return text
#
#
# # my_func = my_decorator(my_func)
#
# result = my_func("Hello")
#
# print(result)




