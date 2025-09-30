from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q, F

from ..models import Question

import logging

logger = logging.getLogger("pybo")


def index(request):
    page = request.GET.get("page", "1")
    kw = request.GET.get("kw", "")
    sort_by = request.GET.get("sort", "-create_date")
    question_list = Question.objects.order_by(sort_by)

    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw)
            | Q(content__icontains=kw)
            | Q(answer__content__icontains=kw)
            | Q(author__username__icontains=kw)
            | Q(answer__author__username__icontains=kw)
        ).distinct()

    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)
    nav_list = [
        {"key": "voter", "name": "추천"},
        {"key": "subject", "name": "제목"},
        {"key": "author", "name": "글쓴이"},
        {"key": "view_count", "name": "조회수"},
        {"key": "create_date", "name": "작성일시"},
    ]
    context = {
        "question_list": page_obj,
        "nav_list": nav_list,
        "page": page,
        "kw": kw,
        "sort": sort_by,
    }
    return render(request, "pybo/question_list.html", context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    # 조회수 증가 (F 객체 사용으로 race condition 방지)
    Question.objects.filter(pk=question_id).update(view_count=F("view_count") + 1)

    # 업데이트된 객체 다시 조회
    question.refresh_from_db()

    context = {"question": question}
    return render(request, "pybo/question_detail.html", context)
