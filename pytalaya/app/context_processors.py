
def current_team(request):
    '''Current team available on templates.'''
    return {'team': request.session.get('team', None)}
