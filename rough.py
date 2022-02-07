
def random_generator():
    gen_data = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(10))
    return gen_data

def slug_generator():
        code = random_generator()
        if Todo.objects.filter(slug = code).exists():
            new_code = slug_generator()
            return new_code
        return code

print(slug_generator())