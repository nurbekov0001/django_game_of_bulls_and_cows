from django.shortcuts import render

round={}
n=0

def index_view(request):
    return render(request, 'index.html')

def game(request):
    global n
    a=0
    b=0
    secret_nums =[1,2,3,4]
    if request.method == "GET":
        return render(request, 'game.html')
    elif request.method == "POST":
        n+=1
        actual_nums = request.POST.get('actual')
        try:
            actual_nums = list(map(int, actual_nums.split(' ')))
            if len(actual_nums) == 4:
                for i in actual_nums:
                    if i >= 11 or i <= 0 :
                        message = f"Вы неправильнно ввели число!    , должно быть мольше 0 и меньше 11"
                        round[n] = message
                        return render(request, 'game.html',{'message':message})    

                for i in range(3):
                    if actual_nums[i] in actual_nums[i+1:]:
                        message = f"они похожи"
                        round[n] = message
                        return render(request, 'game.html',{'message':message})    
    
                for i in range(4):
                    for j in range(4):
                        if secret_nums[i] == actual_nums[j]:
                            if i==j:
                                a+=1
                            else:
                                b+=1
                    message =f"You got {a} bulls , {b} cows"
                if a == 4 :
                    message = f'You got it right!'
                    round[n] = message
                    return render(request, 'game.html',{'message':message})
            elif  len(actual_nums) != 4:
                message =f'Вводите ровно 4 числа! не меньше и не больше!'
                round[n] = message
                return render(request, 'game.html',{'message':message})  
        except ValueError:
           message = "Водить можно только числа"   
    round[n] = message
    return render(request, 'game.html',{'message':message})
def story(request):
    print(round)
    return render(request, 'story.html', {'round': round})
