def filter_news(news_qs, filters: dict):
    if 'search' in filters:
        news_qs = news_qs.filter(title__icontains=filters["search"]) | news_qs.filter(text__icontains=filters["search"])

    if 'sort' in filters:
        news_qs = news_qs.order_by(f"-{filters['sort']}")

    return news_qs


def filter_comment(comments, news):
    comments = comments.filter(news=news)
    return comments
