from pyramid.i18n import get_localizer, TranslationStringFactory


def add_renderer_globals(event):
    request = event['request']
    event['_'] = request.translate
    event['localizer'] = request.localizer

tsf = TranslationStringFactory('analytics')


def add_localizer(event):
    request = event.request

    language = request.POST.get('_LOCALE_', request.session.get('_LOCALE_', None))

    request.locale_name = language or request.locale_name

    localizer = get_localizer(request)

    def auto_translate(*args, **kwargs):
        return localizer.translate(tsf(*args, **kwargs))

    request.localizer = localizer
    request.translate = auto_translate
