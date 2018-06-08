from django.shortcuts import render

def index(request):
    # 1. common app내에 templates/common/iondex.html파일 생성
    # 2. 해당 파일에서 /blog로의 링크, /polls/로의 링크(a태그)enro todtjd
    # 3. installed_apps에 common을 추가
    # 4. config.urls에서 이 view를 바로 연결 (include 사용 x)
    return render(request, 'common/index.html')