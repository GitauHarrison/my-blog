from app import create_app, db
from app.models import User, PersonalBlogPost, VagrantPost, VirtualenvwrapperPost, reCaptchaPost, richTextPost, ngrokPost, installDocker

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'PersonalBlogPost': PersonalBlogPost, 'VagrantPost': VagrantPost, 'VirtualenvwrapperPost': VirtualenvwrapperPost, \
         'reCaptchaPost': reCaptchaPost, 'richTextPost': richTextPost, 'ngrokPost': ngrokPost, 'installDocker': installDocker
    }