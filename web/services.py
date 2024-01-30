def filter_news(news_qs, filters: dict):
    if 'search' in filters:
        news_qs = news_qs.filter(title__icontains=filters["search"]) | news_qs.filter(text__icontains=filters["search"])

    return news_qs
