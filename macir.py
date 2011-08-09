from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

import iterableStringProperty
import iterableString
import os

class Point(db.Model):
    """Database object to store points"""
    id = iterableStringProperty.iterableStringProperty()
    point = db.GeoPtProperty()        
    

class MainPage(webapp.RequestHandler):
    """Class for / url"""

    def get(self):
        """Method for get requests"""
        points = Point.all().order("-id")

        #Use templates/index.html as the template file
        template = os.path.join(os.path.dirname(__file__), 'templates/index.html')
        self.response.out.write(template.render(template, locals()))


class Put(webapp.RequestHandler):
    """Class to put new coordinates on database"""

    def getLast(self):
        """Returns the last point on database"""
        last = Point.all().order("-id").get()
        return last

    def putPoint(self,p):
        """
        Puts a db.GeoPt object to database with a generated id
        Returns id
        """
        #Initialize a new Point
        point = Point()
        point.point = p
        point.id = self.getLast().id.next() #next() method comes from iterableString class
        
        #Save it on db
        point.put()

        return point.id

    def get(self):
        """Method to handle get requests"""

        #Get latitude & longitude from request
        la = self.request.get("la")
        lo = self.request.get("lo")

        #Initialize a new GeoPt object with that values
        point = db.GeoPt(la,lo)

        #Write it on db, get the id
        id = self.putPoint(point)

        #Simply write it to page
        self.response.out.write(id)


application = webapp.WSGIApplication([
        ('/', MainPage),
        ('/put',Put),
        
        ], debug=True)


def main():
    run_wsgi_app(application)


if __name__ == '__main__':
    main()
