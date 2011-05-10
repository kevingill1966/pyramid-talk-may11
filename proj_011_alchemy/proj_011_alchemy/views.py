from proj_011_alchemy.models import DBSession
from proj_011_alchemy.models import MyModel

def my_view(request):
    dbsession = DBSession()
    root = dbsession.query(MyModel).filter(MyModel.name==u'root').first()
    return {'root':root, 'project':'proj_011_alchemy'}
