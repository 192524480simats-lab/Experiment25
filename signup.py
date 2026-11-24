def signup(username, password):
    if not username:
        return "Username is required"

    if len(password) < 6:
        return "Password must contain at least 6 characters"

    return "Signup successful!"


print(signup("steffi", "hello123"))
print(signup("", "hello123"))
print(signup("steffi", "123"))