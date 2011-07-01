import logging

from urllib2 import URLError
from urllib2 import Request, urlopen

from pyramid.renderers import get_renderer
from pyramid.exceptions import NotFound
from pyramid.httpexceptions import HTTPFound
from pyramid.session import UnencryptedCookieSessionFactoryConfig
from pyramid.view import view_config

logging.basicConfig()
log = logging.getLogger('views:')

# Since we don't have a schema we define something like that here.
# Don't be mislead by the name, this is not a proper pyramid schema.
# It is just a list of field names, some indicators and error messages.
schema = {
    'blog_post_url':
        {'required': True,
         'message': 'Source URL is a required field.'
        },
    'target_repo_url':
        {'required': True,
         'message': 'Target URL is a required field.'
        },
    'username':
        {'required': True,
         'message': 'User name is a required field.'
        },
    'password':
        {'required': True,
         'message': 'Password is a required field.'
        },
    'collection':
        {'required': True,
         'message': 'Collection is a required field.',
        },
    'Licence':
        {'required': True,
         'message': 'Licence is a required field.',
        },
}

@view_config(route_name='publish_blog',
             renderer='templates/publish_blog.pt')
def publish_blog_view(request):
    main = get_renderer('templates/main_template.pt').implementation()

    if request.params.get('submitted'):
        errors = {}
        
        # get a list of the posted parameter names (aka, field names)
        param_keys = request.params.keys()

        # figure out which fields are required 
        names_to_check = [field_name for field_name in schema.keys() if\
                         schema.get(field_name).get('required', False)]

        # check that we have all required fields 
        for field_name in names_to_check:
            value = request.params.get(field_name, None)
            if not value:
                errors.update(
                    {field_name: schema.get(field_name).get('message')}
                )

        # if we don't have all the data, prompt the user
        if errors:
            return {'main':main, 'messages': errors}
        
        # if we have the required data, process it
        result, errors = process_blog_post(request)

        # if it is successful, call the results view
        if result == 'success':
            return HTTPFound(location=request.route_url('results'))

        # else tell the user and start from scratch
        return {'main':main, 'messages': errors}

    return {'main':main, 'messages': None}

def process_blog_post(request):
    blog_post_url = request.params.get('blog_post_url')
    errors = {}
    try:
        req = Request(blog_post_url)
        response = urlopen(req)
        post = response.readlines()
    except URLError as e:
        if hasattr(e, 'reason'):
            errors['URLError'] = \
                    'We failed to reach a server. (Reason:%s)'%e.reason
        elif hasattr(e, 'code'):
            errors['URLError'] = \
                    'The server could not fulfill the request. (Error code:%s)'%e.code
    except ValueError as e:
        errors['ValueError'] = e

    if errors:
        return 'failure', errors

    return 'success', {}

@view_config(route_name='results',
             renderer='templates/results.pt')
def results_view(request):
    #request.session.flash('blog was successfully closed!')
    main = get_renderer('templates/main_template.pt').implementation()
    return {'main':main, }

@view_config(context='pyramid.exceptions.NotFound',
             renderer='templates/not_found.pt')
def notfound_view(self):
    main = get_renderer('templates/main_template.pt').implementation()
    return {'main':main, }

