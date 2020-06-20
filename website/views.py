from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def add(request):
    from random import randint

    num_1 = randint(0,10)
    num_2 = randint(0,10)

    if request.method == 'POST':
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']

# Error handling for no form fill out
        if not answer:
            my_answer = "You forgot to answer"
            color = 'warning'
            return render(request, 'add.html', {
                'my_answer':my_answer,
                'color': color,
                'answer':answer,
                'num_1':num_1,
                'num_2':num_2,
                })

        correct_awnser = int(old_num_1) + int(old_num_2)
        if int(answer) == correct_awnser:
            my_answer = 'Correct! Answer = ' + answer
            color = 'success'
        else:
            my_answer = 'Incorrect! The correct answer = ' + str(correct_awnser)
            color = 'danger'

        return render(request, 'add.html', {
        'answer':answer,
        'my_answer':my_answer,
        'num_1':num_1,
        'num_2':num_2,
        'color':color,
        })

    return render(request, 'add.html', {
        'num_1':num_1,
        'num_2':num_2,
        })

def subtract(request):
    from random import randint

    num_1 = randint(0,10)
    num_2 = randint(0,10)

    if request.method == 'POST':
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']

# Error handling for no form fill out
        if not answer:
            my_answer = "You forgot to answer"
            color = 'warning'
            return render(request, 'subtract.html', {
                'my_answer':my_answer,
                'color': color,
                'answer':answer,
                'num_1':num_1,
                'num_2':num_2,
                })

        correct_awnser = int(old_num_1) - int(old_num_2)
        if int(answer) == correct_awnser:
            my_answer = 'Correct! Answer = ' + answer
        else:
            my_answer = 'Incorrect! The correct answer = ' + str(correct_awnser)

        return render(request, 'subtract.html', {
        'answer':answer,
        'my_answer':my_answer,
        'num_1':num_1,
        'num_2':num_2,
        })

    return render(request, 'subtract.html', {
        'num_1':num_1,
        'num_2':num_2,
        })
    return render(request, 'subtract.html', {})

def multiply(request):
    from random import randint

    num_1 = randint(0,10)
    num_2 = randint(0,10)

    if request.method == 'POST':
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']

# Error handling for no form fill out
        if not answer:
            my_answer = "You forgot to answer"
            color = 'warning'
            return render(request, 'multiply.html', {
                'my_answer':my_answer,
                'color': color,
                'answer':answer,
                'num_1':num_1,
                'num_2':num_2,
                })

        correct_awnser = int(old_num_1) * int(old_num_2)
        if int(answer) == correct_awnser:
            my_answer = 'Correct! Answer = ' + answer
        else:
            my_answer = 'Incorrect! The correct answer = ' + str(correct_awnser)

        return render(request, 'multiply.html', {
        'answer':answer,
        'my_answer':my_answer,
        'num_1':num_1,
        'num_2':num_2,
        })

    return render(request, 'multiply.html', {
        'num_1':num_1,
        'num_2':num_2,
        })
    return render(request, 'multiply.html', {})

def divide(request):
    from random import randint

    num_1 = randint(0,10)
    num_2 = randint(1,10)

    if request.method == 'POST':
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']

# Error handling for no form fill out
        if not answer:
            my_answer = "You forgot to answer"
            color = 'warning'
            return render(request, 'divide.html', {
                'my_answer':my_answer,
                'color':color,
                'answer':answer,
                'num_1':num_1,
                'num_2':num_2,
                })

        correct_awnser = float(old_num_1) / float(old_num_2)
        if float(answer) == correct_awnser:
            my_answer = 'Correct! Answer = ' + answer
        else:
            my_answer = 'Incorrect! The correct answer = ' + str(correct_awnser)

        return render(request, 'divide.html', {
        'answer':answer,
        'my_answer':my_answer,
        'num_1':num_1,
        'num_2':num_2,
        })

    return render(request, 'divide.html', {
        'num_1':num_1,
        'num_2':num_2,
        })
    return render(request, 'divide.html', {})
