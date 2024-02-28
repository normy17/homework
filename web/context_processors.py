from web.models import Settings


def custom_context(request):
    color = Settings.objects.first().color
    font_size = Settings.objects.first().font_size
    font_color = Settings.objects.first().font_color
    return {
        'color': color,
        'font_size': font_size,
        'font_color': font_color
    }