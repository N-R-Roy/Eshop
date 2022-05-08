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

        if not request.session.get("customer_id"):
            request_url = request.META["PATH_INFO"]
            print("RRurl >> ", request_url)
            if request_url == "/check-out/":
                address = request.POST.get("address")
                mob_no = request.POST.get("mob_no")
                print("Addresssssssssssssss ------->", address)
                print("Mobbbbbbbbbbbbbbbbbbbbb ---->", mob_no)
                return redirect(f'/login/?request_url={request_url}&address={address}&mob_no={mob_no}')
            else:
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





# def div_num(num1, num2):
#     return num1 / num2
#
#
# def modify(func):
#
#     def nwfunnc(num1, num2):
#
#         if num2 == 0:
#             return "Division by zero is not possible"
#
#         num1 = num1 * 10
#
#         result = func(num1, num2)
#
#         return "Result is = %.3f" % result
#
#     return nwfunnc
#
#
# div_num = modify(div_num)
#
# print(div_num(5, 2))



